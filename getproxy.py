import os,sys

socks5 = os.system("curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt -o socks5.txt")
socks4 = os.system("curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt -o socks4.txt")
http = os.system("curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt -o http.txt")

try:
    print(socks5,socks4,http)
    print("Done.")
except:
    print("Error.")
