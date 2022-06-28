import ssl, ast, json, sqlite3
import paho.mqtt.client as mqtt
conn = sqlite3.connect('Xakdb.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Xakaton(DeviceID TEXT, Time INT, IsWorking TEXT, IsWatering TEXT, geo1lat TEXT, geo1lon TEXT);')
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed", client, userdata, mid, granted_qos)
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected
        Connected = True
    else:
        print("Connection failed")
def on_message(client, userdata, message):
    print(f"Message received: {message.payload}")
    jsonstring = message.payload
    dict_str = jsonstring.decode("UTF-8")
    try:
        global jsondata
        jsondata = ast.literal_eval(dict_str)
        geo1lat = jsondata['current']['geo1']['lat']
        geo1lon = jsondata['current']['geo1']['lon']
        try:
            cursor.execute(f"INSERT INTO 'Xakaton' VALUES (\'{jsondata.get('thingId')}\', \'{jsondata.get('timeStamp')}\', \'{jsondata.get('isWorking')}\', \'{jsondata.get('isWatering')}\', \'{geo1lat}\', \'{geo1lon}\');")
            conn.commit()
        except:
            pass
    except ValueError:
        jsondata = json.loads(dict_str)
        geo1lat = jsondata['current']['geo1']['lat']
        geo1lon = jsondata['current']['geo1']['lon']
        try:
            cursor.execute(
                f"INSERT INTO 'Xakaton' VALUES (\'{jsondata.get('thingId')}\', \'{jsondata.get('timeStamp')}\', \'{jsondata.get('isWorking')}\', \'{jsondata.get('isWatering')}\', \'{geo1lat}\', \'{geo1lon}\');")
            conn.commit()
        except:
            pass
    file1 = open("var.txt", "w+")
    file1.write(str(jsondata))
broker_address = "mqtt.cloud.yandex.net"
port = 8883
user = "aresmv64htqk8lkmqr61"
password = "ICLinnocamp2022"
client = mqtt.Client("kazanka")
client.username_pw_set(user, password=password)
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.tls_set(r"rootCA.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True)
client.connect(broker_address, port=port)
client.subscribe("$devices/are9gnqohp4npug37mbs/events/raw")
client.subscribe("$devices/are1suqff6jhlala2bsh/events/raw")
client.subscribe("$devices/areg5dfne7179n4o24q2/events/raw")
client.loop_forever()