from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import uuid
import random

default_args = {
    'owner':'sridhar',
    'start_date':days_ago(1)
}

def get_data():
    import requests
    res = requests.get('https://randomuser.me/api/')
    res = res.json()
    res = res['results'][0]
    return res

def format_data(res):
    data = {}
    data['id'] = str(uuid.uuid4())
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    location = res['location']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}"\
                    f"{location['city']} {location['state']} {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']
    print(data)
    return data

def stream_data():
    import json
    from kafka import KafkaProducer
    import time
    import logging


    producer = KafkaProducer(bootstrap_servers=['kafka:29092'], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 60: #1 min
            break
        try:
            res = get_data()
            res = format_data(res)
            producer.send('user_data',json.dumps(res).encode('utf-8'))
            time.sleep(random.randint(0,10))
        except Exception as e:
            logging.error(f'An error occured: {e} ')
            continue

with DAG('user_data_from_api',\
         default_args = default_args,
         schedule_interval = '@daily',
         catchup = False) as dag:
    
    streaming_task = PythonOperator(
        task_id = 'stream_data_from_api',
        python_callable = stream_data
    )