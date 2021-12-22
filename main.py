from vk_requests import VkUser
from YaUploader import YaUploader
import requests
from pprint import pprint
from collections import OrderedDict
from progress.bar import IncrementalBar
import time

if __name__ == '__main__':
    with open('token_vk.txt', 'r') as file_object:
        token_vk = file_object.read().strip()
    
    vk_client = VkUser(token_vk, '5.131')
    profile = input("По какому параметру будет осуществляться поиск страницы вк?\n 1-по id\n 2-по username\n:")
    if profile == '2':
        username = input("Введите username пользователя vk:")
        owner_id = vk_client.get_id(username)
    elif profile == '1':
        owner_id = int(input("Введите id пользователя vk:"))  
        
    token_y = input("Введите токен с Полигона Яндекс.Диска:")
    folder_name = input("Введите имя папки для скачивания:")
    count_photo = int(input("Введите кол-во фотографий:"))
   
    photos = vk_client.get_photos(owner_id)
    photo_for_load = vk_client.get_max_size_photo(photos, count_photo)

    uploader = YaUploader(token_y)
    result = uploader.upload(photo_for_load, folder_name, count_photo)