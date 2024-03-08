"""
This module is the main script for the 'Podcast to Blog Post' project. It automates the process of
downloading podcast episodes from an RSS feed, transcribing them using a selected LLM
(like OpenAI's Whisper API), and then generating a structured blog post outline from the transcript.
It utilizes functionalities defined in external modules, including transcription and text generation
services.
"""
import os  # For operating system interactions, like checking directory existence
import llm  # Importing your custom module for handling podcasts and transcription

# Define the podcast RSS feed URL and the folder where downloaded episodes should be stored
PODCAST_FEED_URL = "https://anchor.fm/s/ee6f2324/podcast/rss"
DOWNLOAD_FOLDER = "/Users/barisemre/Desktop/Python-Scripting-For-Prompt-Engineering/assets/media"

# Ensure the download folder exists, create it if it doesn't
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Download the podcast episode and get the file path to the downloaded file
downloaded_file_path = llm.download_podcast_from_rss(PODCAST_FEED_URL, DOWNLOAD_FOLDER)
SELECTED_MODEL = "whisper-1"

# Check if a file was actually downloaded before proceeding with transcription
if downloaded_file_path:
    podcast_transcript = llm.whisperapi_generate(downloaded_file_path, SELECTED_MODEL)
    print(podcast_transcript)
else:
    print("No file was downloaded. Transcription skipped.")

# Generate a blog outline from the podcast transcript and print it
blog_outline = llm.generate_blog_outline(podcast_transcript)
print(blog_outline)
