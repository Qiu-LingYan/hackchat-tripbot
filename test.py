from json import dumps, loads
from time import sleep
import websocket,random
import ssl,threading,getrandomproxy
channel="lounge"
botnick="shabiice"
CRAZY_MODE=False
f=open("main.txt","r")
l=f.readlines()
f.close()
wsaddr="wss://hack.chat/chat-ws"
def mine_once():
    try:
        x=random.randint(10,100)
        y=random.sample(l,x)
        password=''.join(y).replace('\n','')
        botname=botnick+str(random.randint(1,999))
        i=getrandomproxy.get_random_proxy()
        ws=websocket.create_connection(wsaddr,sslopt={"cert_reqs": ssl.CERT_NONE},http_proxy_host=i["addr"][0], 
                http_proxy_port=i["addr"][1], 
                proxy_type=i["type"],
                timeout=5)
        ws.send(dumps({"cmd":"join","channel":channel,"nick":botname,"password":password}))
        while 1:
            data=loads(ws.recv())
            if data["cmd"]=="warn":
                ws.close()
            elif data["cmd"]=="onlineSet":
                aa=data["users"][-1]["trip"]
                bb=f"{password} {aa}"
                with open("result.txt","a+") as f:
                    f.write(bb+"\n")
                print(bb)
                ws.close()
            else:
                ws.close()
    except:
        pass
if __name__ == "__main__":
    print("Start after 3 seconds")
    sleep(3)
    while 1:
        for i in range(30):
            try:
                threading.Thread(target=mine_once).start()
            except:
                pass
            if not CRAZY_MODE:
                sleep(0.01)
