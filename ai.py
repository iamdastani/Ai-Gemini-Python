import google.generativeai as genai

genai.configure(api_key="")

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest"
)

msg = "parts"

messages = model.start_chat(history=[
    {"role" : "user", msg : [""]},
    {"role": "model" , msg :[""] }
])

while True:

    user_input = input("Dastani: ")
    user_rens = messages.send_message(user_input)
    print("Mwamba: " , messages.last.text)
    
