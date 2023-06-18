# Folosim https://jsonplaceholder.typicode.com/guide/ Toate requesturile se vor
# face prima data in Postman (pentru verificare), iar apoi folosind
# libraria requests din Python.
#
# Structura datelor este următoarea:
# - fiecare post este deținut de un user, și poate avea mai multe comments
# - fiecare album este deținut de un user, și poate avea mai multe photos
# - fiecare todo este detinut de un user.
#
# 1. Alege un user din lista de useri predefiniti. Pentru acesta,
# fa requesturile necesare pentru a afișa următoarele informații:
# 	-> lista de posts
# 	-> lista de albume
# 	-> lista de todos
# Pentru a menține output-ul la un nivel acceptabil, afișează la fiecare
# dintre aceste liste doar informații despre primele 3 obiecte,
# iar apoi afiseaza "+x more posts/albums/todos", unde x este numărul de obiecte rămase.

import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'

# response = requests.get(f'{BASE_URL}/users/4/posts')
# print(f'Status code: {response.status_code}')
# if response.status_code == 200:
#     response_post = response.json()
#     for i in range(3):
#         post_id = response_post[i]['id']
#         post_title = response_post[i]['title']
#         post_body = response_post[i]['body']
#         print(f"id = {post_id}")
#         print(f"title: {post_title}")
#         print(f"body: {post_body}")
#
#     print(f" +{len(response_post)-3} more posts")

# response = requests.get(f'{BASE_URL}/users/4/albums')
# print(f'Status code: {response.status_code}')
# if response.status_code == 200:
#     response_post = response.json()
#     for i in range(3):
#         post_id = response_post[i]['id']
#         post_title = response_post[i]['title']
#         print(f"id = {post_id}")
#         print(f"title: {post_title}")
#
#     print(f" +{len(response_post)-3} more posts")

# response = requests.get(f'{BASE_URL}/users/4/todos')
# print(f'Status code: {response.status_code}')
# if response.status_code == 200:
#     response_post = response.json()
#     for i in range(3):
#         post_id = response_post[i]['id']
#         post_title = response_post[i]['title']
#         post_completed = response_post[i]['completed']
#         print(f"id = {post_id}")
#         print(f"title: {post_title}")
#         print(f"completed: {post_completed}")
#
#     print(f" +{len(response_post)-3} more posts")

#2. Alege un post, și afișează lista de comentarii.
# Alege un album, si afiseaza lista de photos.

# response = requests.get(f'{BASE_URL}/posts/53/comments')
# print(f'Status code: {response.status_code}')
# if response.status_code == 200:
#     response_post = response.json()
#     for i in range(3):
#          post_body = response_post[i]['body']
#          print(f"comments posts id_53 : {post_body}")
#
#     print(f" +{len(response_post) - 3} more comments")

# response = requests.get(f'{BASE_URL}/albums/53/photos')
# print(f'Status code: {response.status_code}')
# if response.status_code == 200:
#     response_post = response.json()
#     for i in range(3):
#           photos_url = response_post[i]['url']
#           print(f"photos_url{i} albums_53 : {photos_url}")
#
#     print(f" +{len(response_post) - 3} more photos")

#3. Creeaza un post nou (atentie, acesta NU va fi salvat, dar putem analiza
# răspunsul pentru a vedea cum ar arata în viitor dacă ar fi fost salvat).
# Încearcă să-l creezi cu si fără id. Ce observi?

# request_body = {
#     "title": "foo",
#     "body": "bar",
#     "id": 50
# }
# response = requests.post(f'{BASE_URL}/posts', data=request_body)
# print(f'Status code: {response.status_code}')
# if response.status_code == 200 or response.status_code == 201:
#     response_post = response.json()
#     print(response_post)

#4. Alege un post existent și realizează operațiunile de PUT si PATCH
# (atentie, modificările NU vor fi salvate, analizăm doar răspunsul).
# Ce observi ca este diferit între cele 2 metode?

# request_body1 = {
#     "title": "foo",
#     "body": "bar"
# }
#
# request_body2 = {
#
#     "titile": "foo"
# }
#
# response1 = requests.get(f'{BASE_URL}/posts/53')
# if response1.status_code == 200:
#     response_post = response1.json()
#     print(f"title: {response_post['title']}\n {'-' * 50}\n body: {response_post['body']}")
#
# print('_' * 50)
#
# response2 = requests.put(f'{BASE_URL}/posts/53', data = request_body1)
# if response2.status_code == 200 or response2.status_code == 201:
#     response_post = response2.json()
#     print(f"title: {response_post['title']}\n body:{response_post['body']}")
#
# print('_' * 50)
#
# response3 = requests.patch(f'{BASE_URL}/posts/53', data = request_body1)
# if response3.status_code == 200 or requests3.status == 201:
#     response_post = response3.json()
#     print(f"title: {response_post['title']}\n body:{response_post['body']}")
#
# print('_' * 50)

#5. Folosind query parameters, filtrează lista de todos pentru userul
# ales astfel incat sa afisezi doar todos care nu sunt completed.

# response = requests.get(f'{BASE_URL}/users/53/todos/?complete=false')
# if response.status_code == 200 or response.status_code == 201:
#     response_post = response.json()
#     if len(response_post) > 0:
#         for i in range(3):
#             post_id = response_post[i]['id']
#             post_title = response_post[i]['title']
#             post_completed = response_post[i]['completed']
#             print(f"id = {post_id}")
#             print(f"title: {post_title}")
#             print(f"completed: {post_completed}")
#             print(f" +{len(response_post)-3} more todos")
#     else:
#         print("Nu exista todos incomplete")

#6. Alege un album, și ia pozele din acesta în 2 moduri diferite
# (o data cu nested resource, o data folosind query params).
# Verifica dacă exista vreo diferenta intre cele 2 rezultate.

query_param = {
     'albumId': 0
}

response = requests.get(f'{BASE_URL}/photos', params = query_param)
if response.status_code == 200 or response.status_code == 201:
     response_post = response.json()
     if len(response_post) > 0:
        for i in range(3):
            url_photo = response_post[i]['url']
            print(f"photo : {url_photo}")
        print(f" +{len(response_post)-3} more photo")
     else:
        print(f"Nu exista photo in album {query_param['albumId']}")



