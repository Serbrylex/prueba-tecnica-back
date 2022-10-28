from django.contrib.auth.models import User
import json

def my_user():
    form_data = {
        'username': 'Serbrylex',
        'email': 'sbryanmadridn@gmail.com',
        'password': 'hol123',
        'first_name': 'Sergio Bryan',
        'last_name': 'Madrid Nuñez'
    }	

    user = User.objects.get_or_create(**form_data)    


def read_and_fill():
    f = open('scripts/data.json')
    data = json.load(f)
    for x in data:
        print(x)
        x['stock'] = x['quantity']
        x.pop('quantity')
        prod = Product.objects.create(**x)
        prod.save()

def main():	
    my_user()
    read_and_fill()

# exec(open('Scripts/fill_data.py').read())