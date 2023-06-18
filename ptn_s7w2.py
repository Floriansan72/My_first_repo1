# Folosim Simple Books API, descris aici :
# https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md
#
# Toata rezolvarea se va face într-o clasa numita Books API Client.
# Pentru testare se va crea un obiect din aceasta clasa și se vor apela metodele
# implementate.
#
# 1. Folosind endpoint-ul de authentication, genereaza un access token
# (fa asta in constructor, client name si email ar trebui sa fie atribute).
#
# 2. Adaugă o metoda prin care poți vedea toate comenzile.
#
# 3. Adaugă o metoda prin care poți vedea toate cărțile.
#
# 4. Adaugă o metoda prin care poți posta o comanda.
#
# 5. Adaugă o metoda prin care poți șterge o comanda.

import requests
from pprint import pprint
class Books_API_Client:
    def __init__(self, client_name, client_email):
        self.client_name = client_name
        self.client_email = client_email
        user = {
                  "clientName": self.client_name,
                  "clientEmail": self.client_email
                }
        while self.client_name == "":
            response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=user)
            #print(response.status_code)
            if response.status_code == 200 or 201:
                auth = response.json()['accessToken']
                with open(f'FILES/Auth.txt', 'w') as new_file:
                    new_file.writelines(f'{auth}')
        print("Te-ai logat cu succes pe site")

    def get_all_books(self):
            response = requests.get('https://simple-books-api.glitch.me/books')
            #print(response.status_code)
            response_books = response.json()
            pprint(response_books)

    def get_all_orders(self):
        with open(f'FILES/Auth.txt', 'r') as new_file:
            aut_token = new_file.read()
        Header = {
                   "Authorization": f'Bearer {aut_token}'
                 }
        response = requests.get('https://simple-books-api.glitch.me/orders', headers=Header)
        #print(response.status_code)
        print(response.json())

    def post_order(self, book_id, customer_name):
        with open(f'FILES/Auth.txt', 'r') as new_file:
            aut_token = new_file.read()
        Header = {
                   "Authorization": f'Bearer {aut_token}'
                  }
        Order = {
                  "bookId": book_id,
                  "customerName": customer_name
                }
        response = requests.post('https://simple-books-api.glitch.me/orders', headers=Header, json=Order)
        #print(response.status_code)
        print(response.json())
        order_id = response.json()['orderId']
        print(order_id)

    def delete_order(self, order_id):
        with open(f'FILES/Auth.txt', 'r') as new_file:
            aut_token = new_file.read()
        Header = {
                   "Authorization": f'Bearer {aut_token}'
                 }
        response = requests.delete(f'https://simple-books-api.glitch.me/orders/{order_id}', headers=Header)


client = Books_API_Client('Florian', 'florian4@yahoo.com')
#client.get_all_books()
client.get_all_orders()
#client.post_order(1, "Florian")
#client.delete_order('gULLiYejk28h2deUawSBl')


