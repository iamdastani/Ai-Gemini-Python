# Gemini 1.5 Pro Chatbot

# README

## Overview

This script allows you to send a voice call through the Bland AI API. The call contains a preset dialogue in Swahili for a customer service interaction promoting Tunda Shopping App.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. **Install Python:** Ensure that you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

2. **Install `requests` library:** If you don't have the `requests` library installed, you can install it using pip:

   ```bash
   pip install requests
   ```

## Usage

1. **API Key:** Replace `'YOUR_API'` in the `headers` dictionary with your actual Bland AI API key.

2. **Recipient's Phone Number:** Update the `phone_number` field in the `data` dictionary with the recipient's phone number.

3. **Run the Script:** Save the script to a `.py` file and run it using Python:

   ```bash
   python your_script_name.py
   ```

## Script Details

### Headers

```python
headers = {
   'Authorization': 'YOUR_API'
}
```

- Replace `'YOUR_API'` with your Bland AI API key.

### Data Payload

```python
data = {
  "phone_number": "+255744963858",  # Add the recipient's phone number
  "from": None,
  "task": "...",  # The full dialogue text
  "model": "enhanced",
  "language": "eng",
  "voice": "ravi",
  "voice_settings": {},
  "local_dialing": False,
  "max_duration": 12,
  "answered_by_enabled": False,
  "wait_for_greeting": False,
  "record": False,
  "amd": False,
  "interruption_threshold": 100,
  "temperature": None,
  "transfer_list": {},
  "metadata": {},
  "pronunciation_guide": [],
  "start_time": None,
  "request_data": {},
  "tools": [],
  "webhook": None
}
```

- **phone_number:** Replace with the recipient's phone number.
- **task:** Contains the dialogue to be delivered during the call.
- **model, language, voice, etc.:** Various settings for the API request. Modify if necessary based on your specific needs.

### API Request

```python
response = requests.post('https://api.bland.ai/v1/calls', json=data, headers=headers)
```

- Sends a POST request to the Bland AI API to initiate the call.

### Response Handling

```python
if response.status_code == 200:
    print("Call successfully initiated.")
else:
    print("Error:", response.status_code, response.text)
```

- Checks the response from the API and prints whether the call was successfully initiated or if there was an error.

## Additional Information

For more detailed information on the Bland AI API and its capabilities, please refer to the [Bland AI API documentation](https://api.bland.ai/docs).

## Contact

For any issues or questions, please contact support at [support@bland.ai](mailto:support@bland.ai).




Gemini 1.5 Pro is an advanced conversational AI model developed by Google GenerativeAI. This README provides instructions on how to use the chatbot script to interact with the model and initiate conversations.

Swahili Video Tutorial link:
https://twitter.com/iamdastani/status/1788880021760638992

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



