import helpers
import llm
import prompts

token_count = 1000

costs = helpers.estimate_input_cost("gpt-3.5-turbo-0613", token_count)

print(f"Costs: {costs}")

prompt = prompts.twitter_thread_generator_prompt.format(topic="prompt engineering tips")

print(prompt)

response = llm.llm_generate_text(prompt, "OpenAI", "gpt-3.5-turbo")

print(response)

num_tokens = helpers.count_tokens(prompt, "gpt-3.5-turbo")
print(f"Token count: {num_tokens}")