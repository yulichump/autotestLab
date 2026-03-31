import pytest
import requests
import json

def test_get_positive():
    url = "https://petstore.swagger.io/v2/user/login/?username=1&password=1"
    response = requests.get(url)
    print("result get = ", response.text)
    assert response.json()['code'] == 200

def test_post_positive():
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    request['category'] = {}
    request['category']['name'] = "pokemon"
    print(request)
    response = requests.post(url, json=request)
    print("result post = ", response.json())
    assert response.json()['code'] == 200

def test_post_negative():
    url = "https://petstore.swagger.io/v2/user"
    request = [{}]
    print(request)
    response = requests.post(url, json=request)
    print("result post = ", response.json())
    assert response.json()['code'] == 200 #ошибка 500 - тк отправляем неверный запрос (вместо объекта массив)

def test_delete_negative():
    url = "https://petstore.swagger.io/v2/user/1"
    response = requests.delete(url)
    assert response.status_code in [200, 204], \
        f"Удаление не удалось, статус: {response.status_code}"  #тк пользователей не существует, то при любом удалении приходит ошибка 404 ('пользователь не найден')
