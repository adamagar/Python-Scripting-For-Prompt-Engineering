import tiktoken
import newspaper

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

def get_article_from_url(url):
    try:
        # Scrape the web page for content using newspaper
        article = newspaper.Article(url)
        # Download the article's content with a timeout of 10 seconds
        article.download()
        # Check if the download was successful before parsing the article
        if article.download_state == 2:
            article.parse()
            # Get the main text content of the article
            article_text = article.text
            return article_text
        else:
            print("Error: Unable to download article from URL:", url)
            return None
    except Exception as e:
        print("An error occurred while processing the URL:", url)
        print(str(e))
        return None
