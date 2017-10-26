import threading
import paho.mqtt.client as mqtt

def publish_1(client,topic):
    message="on"
    print("publish data")
    client.publish(topic,message)
    publish_1(client,topic)


broker="test.mosquitto.org"
topic_pub='/temperature123'
topic_sub='outTopic'

def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic_sub)


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)
thread1=threading.Thread(target=publish_1,args=(client,topic_pub))
thread1.start()

client.loop_forever()
