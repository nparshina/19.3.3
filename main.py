import requests

#данные пользователя по ходу теста везде захардкожены, это можно улучшить

url = "https://petstore.swagger.io/v2"

new_user = {
  "id": 111111111,
  "username": "natalya-test0902",
  "firstName": "Firstname",
  "lastName": "Lastname",
  "email": "test@test.com",
  "password": "test0902",
  "phone": "123456789",
  "userStatus": 75924464
}

# Данные для создания нового пользователя

update_users_info = {
  "id": 111111111,
  "username": "natalya-test0902_UPDATE",
  "firstName": "Firstname_update",
  "lastName": "Lastname_update",
  "email": "test+update@test.com",
  "password": "test0902update",
  "phone": "123456789",
  "userStatus": 75924464
}

#данные для последующего обновления пользователя

headers = {'accept': 'application/json'}

#заголовок в переменную, для удобства передачи в get запросах

create_user = requests.post(f'{url}/user', json=new_user)
print(create_user.status_code)

#Создание нового пользователя

get_user = requests.get(f'{url}/user/natalya-test0902', headers=headers)
print(get_user.status_code)
print(get_user.text)

#Получение информации о новом пользователе, который создан

update_user = requests.put(f'{url}/user/natalya-test0902', json=update_users_info)
get_user = requests.get(f'{url}/user/natalya-test0902_UPDATE', headers=headers)
print(get_user.status_code)
print(get_user.text)

#Обновление информации о новом пользователе и получение обновленных данных

delete_user = requests.delete(f'{url}/user/natalya-test0902_UPDATE')
print(get_user.status_code)
get_user = requests.get(f'{url}/user/natalya-test0902_UPDATE', headers=headers)
print(get_user.text)

#удалим пользователя и проверим, что такого действительно нет
