# -*- coding: utf-8 -*-
import hashlib
import hmac
import json
import time

import paho.mqtt.client as mqtt

options = {
    # TODO: replace with your own key/secret
    'productKey': 'product_key',
    'deviceName': 'device_name',
    'deviceSecret': 'device_secret',
    'regionId': 'cn-shanghai'
}

HOST = options['productKey'] + '.iot-as-mqtt.' + options['regionId'] + '.aliyuncs.com'
PORT = 1883
PUB_TOPIC = "/sys/" + options['productKey'] + "/" + options['deviceName'] + "/thing/event/property/post"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # client.subscribe("the/topic")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    setjson = json.loads(msg.payload)
    humi_stats = setjson['params']['humidifier']
    return humi_stats


def hmacsha1(key, msg):
    return hmac.new(key.encode(), msg.encode(), hashlib.sha1).hexdigest()


def getAliyunIoTClient():
    timestamp = str(int(time.time()))
    CLIENT_ID = "paho.py|securemode=3,signmethod=hmacsha1,timestamp=" + timestamp + "|"
    CONTENT_STR_FORMAT = "clientIdpaho.pydeviceName" + options['deviceName'] + "productKey" + options[
        'productKey'] + "timestamp" + timestamp
    # set username/password.
    USER_NAME = options['deviceName'] + "&" + options['productKey']
    PWD = hmacsha1(options['deviceSecret'], CONTENT_STR_FORMAT)
    client = mqtt.Client(client_id=CLIENT_ID, clean_session=False)
    client.username_pw_set(USER_NAME, PWD)
    return client


def main(weather_data, humi_stats):
    client = getAliyunIoTClient()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, 1883, 300)
    payload_json = {
        'id': int(time.time()),
        'params': {
            'temp': 25,
            'humi': 25,
            'Weather': weather_data,
            'humidifier': humi_stats
        },
        'method': "thing.event.property.post"
    }
    print('send data to iot server: ' + str(payload_json))
    client.publish(PUB_TOPIC, payload=str(payload_json), qos=1)
    client.loop_forever()


if __name__ == '__main__':
    main(0, 0)

'''
payload_json = {
        'id': int(time.time()),
        'params': {
            'temp': 25,
            'humi': 25,
            'Weather': 1,
            'humidifier': 0
        },
'''
