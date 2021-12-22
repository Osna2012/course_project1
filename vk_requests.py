import requests
from pprint import pprint
from collections import OrderedDict
import json

#тестовый токен
#token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'

class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version    
        }

    def get_id(self,name):
        url = self.url + 'utils.resolveScreenName'
        photos_params = {
            'screen_name': name 
        }
        res = requests.get(url,params={**self.params, **photos_params}).json()['response']['object_id']
        return res

    def get_photos(self, owner_id):
    
        photos_url = self.url + 'photos.get'
        photos_params = {
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended':1
        }
        res = requests.get(photos_url, params={**self.params, **photos_params}).json()
        return res['response']["items"]


    def get_max_size_photo(self, photos, count_photo):
        #создаем объектам-фото дополнительное значение - размер
        size_photo = {} 
        for photo in photos:
            height = photo["sizes"][-1]['height']
            width = photo["sizes"][-1]['width']
            photo['size'] = height * width
            photo['type']=photo["sizes"][-1]['type']
            if photo["likes"]['count'] not in size_photo.keys():
                size_photo[photo["likes"]['count']] = {'size':photo['size'], 'url':photo["sizes"][-1]['url'],'type':photo['type']} 
            else:
                size_photo[str(photo["likes"]['count']) + "_" + str(photo['date'])] = {'size':photo['size'], 'url':photo["sizes"][-1]['url'],'type':photo['type']} 
             
        #сортировка словаря по значению size, от большего к меньшему
        sorted_dict = OrderedDict()
        sorted_keys = sorted(size_photo, key=lambda x: size_photo[x]['size'],reverse=True)     

        for key in sorted_keys: 
            sorted_dict[key] = size_photo[key]    

        #берем заданное кол-во значений отсортированого словаря
        max_size_photo = {}
        count = 0
        for key, value in sorted_dict.items():
            if count < count_photo:
                max_size_photo[key] = value
            count += 1
        
        res_list = []
        for key,value in max_size_photo.items():
            res_list.append({'file_name': f'{key}.jpg', 'size': value['type']})
        
        with open('info.json', 'w') as f:
            f.write(json.dumps(res_list))
        # with open('info.json') as f:
        #     print(f.read())       
    
        return max_size_photo




