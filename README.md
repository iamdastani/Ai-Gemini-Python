# Gemini 1.5 Pro Chatbot

Gemini 1.5 Pro is an advanced conversational AI model developed by Google GenerativeAI. This README provides instructions on how to use the chatbot script to interact with the model and initiate conversations.

## Requirements
- Python 3.x
- Google GenerativeAI API key

## Installation
1. Clone or download the repository.
2. Install the required Python packages by running:
    ```
    pip install google-generativeai
    ```

## Usage
1. Import the necessary modules:
    ```python
    import google.generativeai as genai
    ```

2. Configure the GenerativeAI API key:
    ```python
    genai.configure(api_key="YOUR_API_KEY")
    ```

3. Initialize the GenerativeModel:
    ```python
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
    ```

4. Start the conversation:
    ```python
    messages = model.start_chat(history=[
        {"role": "user", "parts": [""]},
        {"role": "model", "parts": [""]}
    ])
    ```

5. Interact with the chatbot:
    ```python
    while True:
        user_input = input("User: ")
        user_response = messages.send_message(user_input)
        print("Bot: ", messages.last.text)
    ```

## Important Notes
- Replace `"YOUR_API_KEY"` with your actual API key obtained from Google GenerativeAI.
- Modify the conversation history structure as needed.
- Ensure a stable internet connection to interact with the GenerativeAI model.

