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

    owner_id = input("Введите id пользователя vk:")
    token_y = input("Введите токен с Полигона Яндекс.Диска:")
    vk_client = VkUser(token_vk, '5.131')
    photos = vk_client.get_photos(owner_id)
    photo_for_load = vk_client.get_max_size_photo(photos)
    uploader = YaUploader(token_y)
    result = uploader.upload(photo_for_load)