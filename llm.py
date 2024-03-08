"""
This module provides functionalities to interact with different language models and services,
such as OpenAI's GPT and Whisper APIs, Cohere's language model, and more. It includes capabilities
to generate text based on prompts, transcribe audio files to text, and download podcast episodes
from RSS feeds. It also supports saving responses to JSON for persistence and further analysis.
"""
# Import necessary libraries
import json
import os
from urllib.parse import unquote
import cohere
import feedparser
from openai import OpenAI
import requests
from dotenv import load_dotenv
from prompt_templates import podcast_to_blog_prompts as prompts

# Load environment variables
load_dotenv()
openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
cohere_api_key = os.environ.get("COHERE_API_KEY")

# Function to generate text using specified LLM service
def llm_generate_text_with_save(prompt, service, model):
    """
    Generates text using a specified language model and service.
    The generated text is saved along with the prompt to a JSON file.
    """
    if service == "OpenAI":
        generated_text = openai_generate(prompt, model)
    elif service == "Cohere":
        generated_text = cohere_generate(prompt, model)
    else:
        raise ValueError(f"Service {service} is not supported.")

    save_to_json(prompt, generated_text)
    return generated_text

# Function to save prompt and response to a JSON file
def save_to_json(prompt, response):
    """
    Saves the prompt and its response to a JSON file using UTF-8 encoding.
    """
    data = {"prompt": prompt, "response": response}
    # Specify encoding as UTF-8
    with open("ai_prompts_responses.json", "a", encoding="utf-8") as f:
        json.dump(data, f)
        f.write("\n")


# Function to generate text using OpenAI
def openai_generate(user_prompt, selected_model):
    """
    Generates text using OpenAI's GPT model.
    """
    completion = openai.chat.completions.create(
        model=selected_model,
        messages=[{"role": "user", "content": user_prompt}]
    )
    return completion.choices[0].message.content

# Function to transcribe audio using OpenAI's Whisper API
def whisperapi_generate(file_path, selected_model="whisper-1"):
    """
    Transcribes audio to text using OpenAI's Whisper API.
    """
    with open(file_path, "rb") as audio_file:
        transcription_response = openai.audio.transcriptions.create(
            model=selected_model, file=audio_file, response_format="text",
        )
    return transcription_response['choices'][0]['text']

# Function to generate a blog outline from a transcript
def generate_blog_outline(transcript, temperature=0.5):
    """
    Generates a blog outline from a transcript using OpenAI.
    """
    system_prompt = prompts.PROMPT_1.format(transcript=transcript)
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo", temperature=temperature,
        messages=[{"role": "system", "content": system_prompt},
        {"role": "user", "content": transcript}]
    )
    return response.choices[0].message.content

# Function to download the latest podcast episode from an RSS feed
def download_podcast_from_rss(rss_url, save_folder):
    """
    Downloads the latest podcast episode from the provided RSS feed URL and saves it to
    the specified folder.

    Parameters:
    - rss_url (str): The URL of the podcast RSS feed.
    - save_folder (str): The local directory path where the podcast episode should be saved.

    Returns:
    - str or None: The full path to the downloaded podcast file if successful, None otherwise.
    """
    feed = feedparser.parse(rss_url)
    if not feed.entries:
        print("No entries found in the RSS feed.")
        return

    for entry in feed.entries:
        audio_url = None
        for link in entry.get('links', []):
            if link.get('type') == 'audio/x-m4a':
                audio_url = link.get('href')
                break

        if not audio_url:
            print("No suitable audio link found in this entry.")
            continue

        decoded_audio_url = unquote(audio_url)

        episode_title = entry.title.replace(" ", "_").replace("/", "_").replace("%", "_")
        file_name = f"{episode_title}.m4a"
        full_path = os.path.join(save_folder, file_name)

        print(f"Downloading podcast episode from {decoded_audio_url}...")

        # Adding a timeout parameter
        try:
            response = requests.get(decoded_audio_url, stream=True, timeout=10)
            with open(full_path, 'wb') as audio_file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        audio_file.write(chunk)
            print(f"Podcast episode downloaded and saved to {full_path}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download podcast episode: {e}")

        return full_path


# Cohere API function
def cohere_generate(user_prompt, selected_model):
    """
    Generates text using Cohere's language model.
    """
    co = cohere.Client(cohere_api_key)
    response = co.generate(
        model=selected_model, prompt=user_prompt, max_tokens=300,
        temperature=0.9, k=0, stop_sequences=[], return_likelihoods='NONE'
    )
    return response.generations[0].text
