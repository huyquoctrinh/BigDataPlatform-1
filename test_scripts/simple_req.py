import requests

url = "http://localhost:5000/upload"

payload = {'db': '8',
'id': '004',
'device': 'microwave',
'status': 'normal',
'tag': 'mimic-data'}
files=[
  ('audio_file',('coarse.reconstructed_wave_0.0.wav',open('/home/trnhq/huy/BigDataPlatform-1/coarse.reconstructed_wave_0.0.wav','rb'),'audio/wav'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
