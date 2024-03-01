import tiktoken

def estimate_input_cost(model_name, token_count):
    # Mapping of model names to their cost per 1000 tokens
    model_costs = {
        "gpt-3.5-turbo-0613": 0.0015,
        "gpt-3.5-turbo-16k-0613": 0.003,
        "gpt-4-0613": 0.03,
        "gpt-4-32k-0613": 0.06
    }
    
    # Fetch the cost per 1000 tokens for the given model name
    cost_per_1000_tokens = model_costs.get(model_name, 0)  # Default to 0 if model_name is not found

    # Calculate and return the estimated cost
    estimated_cost = (token_count / 1000) * cost_per_1000_tokens
    return estimated_cost


def count_tokens(text, selected_model):
    encoding = tiktoken.encoding_for_model(selected_model)
    num_tokens = encoding.encode(text)
    return len(num_tokens)
