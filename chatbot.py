import openai
import llm

openai.api_key = llm.openai.api_key

# Initialize the list of messages
messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Start a chat
def continue_chat(user_message):
    global messages # Use the global messages list
    # Add the user's message to the list
    messages.append({"role": "user", "content": user_message})

    # Ensure the correct API call with required parameters
    try:
        response = openai.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",  # or whichever model you're intending to use
            
        )
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return ""

    # Assuming the response structure follows the example provided, adjust as necessary
    if response.choices and response.choices[0].message:
        response_text = response.choices[0].message.content
    else:
        response_text = "No response generated."

    # Print the AI's response for debugging
    print("AI:", response_text)

    return response_text

# Chat with the bot
while True:
    user_message = input("You: ")
    if user_message.lower() == "quit":
        break
    
    ai_response = continue_chat(user_message)
    print("AI: ", ai_response)