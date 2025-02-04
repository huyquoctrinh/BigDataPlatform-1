import time
import threading
import os 
from tqdm import tqdm
import requests
from concurrent.futures import ThreadPoolExecutor

LIST_RPT = []
def create_test_data(path):
    # list_payload = []
    # list_files = []
    list_data = []
    for device in os.listdir(path):
        device_path = os.path.join(path, device)
        # print(device_path)
        for idx in tqdm(os.listdir(device_path)):
            idx_path = os.path.join(device_path, idx)
            # print(idx_path)
            for status in os.listdir(idx_path):
                status_path = os.path.join(idx_path, status)
                # print(status_path)
                for file in os.listdir(status_path):
                    
                    file_path = os.path.join(status_path, file)
                    # print(file_path)
                    # list_files.append(('audio_file', (file, open(file_path, 'rb'), 'audio/wav')))
                    payload = {
                        'db': "-6dB",
                        'id': idx,
                        'device': device,
                        'status': status,
                        'tag': 'mimic-data'
                    }
                    list_data.append((payload, ('audio_file', (file, open(file_path, 'rb'), 'audio/wav'))))
                    # list_payload.append(payload)
    return list_data

def upload_file(data):
    payload, file = data
    files = [file]
    url = "http://localhost:5000/upload"
    headers = {}
    start = time.time()
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    end = time.time()
    LIST_RPT.append(end - start)
    print(end - start)
    # print(response.text)


data_path = "E:/bdp_data/test_data/-6_dB_pump/"
list_data = create_test_data(data_path)

print(len(list_data))

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(upload_file, list_data)

print("Average results:", sum(LIST_RPT)/len(LIST_RPT))

# url = "http://localhost:5000/upload"

# payload = {'db': '7',
# 'id': '003',
# 'device': 'microwave',
# 'status': 'normal',
# 'tag': 'mimic-data'}
# files=[
#   ('audio_file',('coarse.reconstructed_wave_0.14000.wav',open('/C:/Users/LG/Downloads/coarse.reconstructed_wave_0.14000.wav','rb'),'audio/wav'))
# ]
# headers = {}

# response = requests.request("POST", url, headers=headers, data=payload, files=files)

# print(response.text)

# def create_test_data(path):
