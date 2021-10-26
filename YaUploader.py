import requests
from pprint import pprint
from progress.bar import IncrementalBar
import time

class YaUploader:
    def __init__(self,token_y: str):
        self.token_y = token_y

    def upload(self, photo_for_load):
        API_BASE_URL = "https://cloud-api.yandex.net/"

        headers = {
          'accept':"application/json",
          'authorization': f"OAuth {self.token_y}"
        }
        bar = IncrementalBar("Загрузка фото:", max = 5, suffix='Выполнено %(percent)d%%. До окончания процесса: %(remaining)s фото, %(eta_td)s времени')
        for key, value in photo_for_load.items():
            r = requests.get(API_BASE_URL + 'v1/disk/resources/upload', 
                          params={'path':'photo_vk/' + str(key)}, headers=headers)
            try:
                upload_url = r.json()['href']
            except:
                return print(f"Фото с именем '{key}' уже есть на диске и не может быть загружено повторно.")
                
            url = value['url']
            r2 = requests.get(url).content

            with open(str(key), 'wb') as photo:
                photo.write(r2)
            
            r = requests.put(upload_url ,headers=headers, files={'file':open(str(key), 'rb')})
            bar.next()
       
        bar.finish()  
        return print("Фото успешно загружены")  

# if __name__ == '__main__':
#     token_y = 'AQAAAABYmXBzAADLW_DbQF67WUKVsrP_oMKVQaE'
#     uploader = YaUploader(token_y)
#     result = uploader.upload(photo_for_load)
    
 
 
    



