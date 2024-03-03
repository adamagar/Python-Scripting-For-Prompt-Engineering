import helpers
import llm
from prompt_templates import youtube_prompts

selected_model = "gpt-3.5-turbo"

youtube_url = "https://www.youtube.com/watch?v=gnCO6443kuk"

video_transcript = helpers.get_video_transcript(youtube_url, language='en')

prompt = youtube_prompts.youtube_to_points_summary.format(transcript=video_transcript)

response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)

print(response)