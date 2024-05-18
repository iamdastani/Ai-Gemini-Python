import requests

# Headers
headers = {
   'Authorization': 'YOUR_API'
}

# Data
data = {
  "phone_number": "+255744963858",  # Add the recipient's phone number
  "from": None,
  "task": "You: Mambo Vipi , Naitwa John ni huduma kwa wateja  kutoka tunda Shopping App, Nilikuwa nataka kushiriki habari njema nawe kuhusu jinsi ya kurahisisha maisha yako ya ununuzi.\n\n\nYou: Umewahi kusikia kuhusu Tunda Shopping? Siyo tu duka la matunda, bali ni soko kubwa mtandaoni ambapo unaweza kupata kila kitu unachohitaji, kutoka kwa bidhaa aina zote kama nguo, hadi vifaa vya elektroniki. Na unajua lililo zuri zaidi? Usafirishaji ni bure popote ulipo Tanzania! , Download app ya tunda Shopping sasa inapatikana Playstore na Appstore\n\n\nYou: Hakika kabisa! Tunda Shopping inashirikiana na wauzaji wengi waliothibitishwa ili kuhakikisha unapata bidhaa bora na za bei nafuu. Ukiwa na Tunda Shopping, unapata kila unachohitaji kwa , bila kupoteza muda na gharama za usafiri.\n\nCustomer: Ngoja nikwambie, hii ni habari njema sana! huna haja ya kwenda kuhangaika kununua bidhaa , download app ya tunda shopping ununue sasa !\n\nYou: Karibu sana! Ukiwa na maswali yoyote au unahitaji msaada, usisite kuniuliza.\n\nCustomer: Asante sana! Bila shaka utaingia Tunda Shopping leo leo.\n\nYou: Hakuna shida! Nakuhakikishia utafurahia manunuzi yako.\n\nCustomer: Asante, na wewe pia! Baadaye!\n\nYou: Baadaye!",
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
  "transfer_list": {
   
  },
  "metadata": {},
  "pronunciation_guide": [],
  "start_time": None,
  "request_data": {},
  "tools": [],
  "webhook": None
}

# API request 
response = requests.post('https://api.bland.ai/v1/calls', json=data, headers=headers)

# Check the response
if response.status_code == 200:
    print("Call successfully initiated.")
else:
    print("Error:", response.status_code, response.text)
