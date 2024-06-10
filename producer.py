import json
import time
import requests
from concurrent.futures import ThreadPoolExecutor
from kafka import KakfaProducer
from confluent_kafka import Producer
from time import sleep

#Set up Kakfa producer
def serializer(message):
    return json.dumps(message)


#Kakfa Producer
producer = KafkaProducer(bootstrap_servers = ['localhost:9092'],value_serializer = serializer)

#API endpoints
# API endpoints
api_url_1 = 'https://randomuser.me/api/'
api_url_2 = 'https://randomuser.me/api/'


# Periodically fetch and publish data to Kafka
while True:
    response_1 = requests.get(api_url_1)

    if response_1.status_code == 200:
        data_1 = response_1.json()
        producer.produce('api1',key='key1',value = json.dumps(data_1))
    else:
        print(f'Failed to fetch data from 1st API {response_1.status_code}')

    response_2 = requests.get(api_url_2)

    if response_2.status_code == 200:
        data_2 = response_2.json()
        producer.produce('api2',key='key2',value = json.dumps(data_2))
    else:
        print(f'Failed to fetch data from 2nd API {response_2.status_code}')
    
    #Sleep for 600 seconds
    time.sleep(600)

    

