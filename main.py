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

    profile = input("По какому параметру вы хоитте ощуствлять поиск страницы вк?\n 1-по id\n 2-по имени пользователя\n:")
    if profile == '1':
        owner_id = int(input("Введите id пользователя vk:"))
        username = None
    else:
        username= input("Введите имя пользователя vk:")
        owner_id = None
    token_y = #input("Введите токен с Полигона Яндекс.Диска:")
    folder_name = input("Введите имя папки для скачивания:")
    count_photo = int(input("Введите кол-во фотографий:"))
    vk_client = VkUser(token_vk, '5.131')
    photos = vk_client.get_photos(owner_id, username)
    photo_for_load = vk_client.get_max_size_photo(photos, count_photo)

    uploader = YaUploader(token_y)
    result = uploader.upload(photo_for_load, folder_name, count_photo)