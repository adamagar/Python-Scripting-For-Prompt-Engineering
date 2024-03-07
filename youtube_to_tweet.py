import helpers
import llm
from prompt_templates import youtube_prompts

selected_model = "gpt-3.5-turbo"

youtube_url = "https://www.youtube.com/watch?v=_PV_SBFJS74"

video_transcript = helpers.get_video_transcript(youtube_url, language="tr")

prompt = youtube_prompts.tweet_from_youtube_prompt.format(transcript=video_transcript)

response = llm.llm_generate_text(prompt, "OpenAI", selected_model)

print(response)