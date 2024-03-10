import requests

web = ('https://группа-вагнера.online')
result = requests.get(web)
print(result)
print('Код ответа на сервер:', result.status_code)


golub = f'{web}?page_id=5/'
result2024 = requests.post(golub, data = {})
print(result2024)