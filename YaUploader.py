import requests
from pprint import pprint
from progress.bar import IncrementalBar
import time


class YaUploader:
    def __init__(self,token_y: str):
        self.token_y = token_y

    def upload(self, photo_for_load, folder_name, count_photo):
        API_BASE_URL = "https://cloud-api.yandex.net/"

        headers = {
          'accept':"application/json",
          'authorization': f"OAuth {self.token_y}"
        }
        bar = IncrementalBar("Загрузка фото:", max = count_photo, suffix='Выполнено %(percent)d%%. До окончания процесса: %(remaining)s фото, %(eta_td)s времени')
        
        #проверка существования папки
        exist_folget = requests.get(API_BASE_URL + 'v1/disk/resources', params={'path':folder_name}, headers=headers) 
        try:
          exist_folget.json()['error']
        except:  
          return print(f"Папка с именем '{folder_name}' уже существует.")

        create_folder = requests.put(API_BASE_URL + 'v1/disk/resources', params={'path':folder_name}, headers=headers) 
   
        for key, value in photo_for_load.items():
            r = requests.get(API_BASE_URL + 'v1/disk/resources/upload', 
                          params={'path':f'{folder_name}/' + str(key)}, headers=headers)
      
            #проверка существование фото
            try:
              r.json()['href']  
            except:
              return print(f"Фото с именем '{key}' уже есть в папке и не может быть загружено повторно.")
            
            url = value['url']

            #ВАРИАНТ С ЗАГРУЗКОЙ ФОТОГРАФИЙ В ТЕКУЩЕЮ ПАПКУ НА КОМПЬЮТЕРЕ
            # r2 = requests.get(url).content

            # with open(str(key), 'wb') as photo:
            #     photo.write(r2)
            
            #requests.put(upload_url ,headers=headers, files={'file':open(str(key), 'rb')})

            #загрузка фотографий по url
            params = {"path": f'{folder_name}/{key}', "url": url, "overwrite": "true"}
            response = requests.post(API_BASE_URL + 'v1/disk/resources/upload', headers=headers, params=params)
          
            bar.next()
       
        bar.finish()  
        return print("Фото успешно загружены")  

    
 
 
    



