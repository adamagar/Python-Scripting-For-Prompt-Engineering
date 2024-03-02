import helpers
import llm
from prompt_templates import blogging, productivity_prompts, text_analysis, ideas

selected_model = "gpt-3.5-turbo"
input_text = ""

prompt = productivity_prompts.summarize_text_to_bullet_points.format(
    Minimum="5", Maximum="10", Text=input_text
)

token_count = helpers.count_tokens(prompt, selected_model)
estimated_costs = helpers.estimate_input_cost(selected_model, token_count)
print(f"Costs: {estimated_costs}")

# prompt = blogging.twitter_thread_generator_prompt.format(topic="prompt engineering tips")
# print(prompt)

response = llm.llm_generate_text(prompt, "OpenAI", selected_model)

print("Result:")
print(response)

num_tokens = helpers.count_tokens(prompt, "gpt-3.5-turbo")
print(f"Token count: {num_tokens}")