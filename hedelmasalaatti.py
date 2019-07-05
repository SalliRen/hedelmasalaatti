import boto3
from decimal import Decimal
import json
from boto3.dynamodb.conditions import Key, Attr
import boto

#create table

dynamodb_client = boto3.client('dynamodb')


table_name = 'hedelmasalaatti'
existing_tables = dynamodb_client.list_tables()['TableNames']

if table_name not in existing_tables:
    response = dynamodb_client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'item',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'price',
                'AttributeType': 'N',
            },
        ],
        KeySchema=[
            {
                'AttributeName': 'item',
                'KeyType': 'HASH',
            },
            {
                'AttributeName': 'price',
                'KeyType': 'RANGE',
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        },
        TableName=table_name,
    )


#put.item in table function

def put_item(i, y):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('hedelmasalaatti')
    table.put_item(
        Item={
            'item': i,
            'price': y
            }
        )



def intro():
    print("Tervetuloa heldelmäsalaatin tekoon!\n"
          "[1] Lisää tuote\n"
          "[2] Näytä kallein tuote\n"
          "[3] Näytä halvin tuote\n")
    response = input("syötä numero valintasi: ")

    if response == "1":
        def new_item():
            add_item = input("Syötä lisättävän tuotteen nimi: ")

            if add_item != "":
                new_price = input("Syötä tuotteen hinta: ")

                try:
                    val = Decimal(new_price)
                    put_item(add_item, val)
                    print("Tuote lisätty onnistuneesti! Haluatko\n"
                    "[1] lisätä uuden tuoteen\n"
                    "[2] palata alkuun?")
                    user_choice = input("Syötä numero:")

                    if user_choice == "1":
                        new_item()

                    elif user_choice == "2":
                        intro()

                    else:
                        print("En ymmärtänyt valintaasi! Syötä numero 1-2. Palataan alkunäyttöön")
                        intro()

                except ValueError:
                        print("Tuotteen hinta pitää olla numero")
                        new_item()

            else:
                print("Tuotteen nimi ei voi olla tyhjä\n")
                new_item()

        new_item()

    elif response == "2":

        def most_expensive():
            try:

            except ValueError:
                print("Lista on tyhjä!")
                intro()

        most_expensive()

    elif response == "3":
        def least_expensive():
            try:
                #min toiminto ei toimi

                basket = zip(item, price)
                print(min(basket, key=lambda x: x[1]))

                intro()

            except ValueError:
                print("Lista on tyhjä!")
                intro()

        least_expensive()

    else:
        print("Numeron täytyy olla 1-4 välillä!")
        intro()


intro()
