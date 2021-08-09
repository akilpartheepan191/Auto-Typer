import keboard as k
import json
import time
file=open('direct.json')
file=json.load(file)

k.send('alt+tab')
time.sleep(1)
def send(msg):
  k.write(msg)
  k.send('enter')
def wait():
  time.sleep(file["interval"])


while True:
  send(f'.route {file["route no."]}')
  wait()
  for i in range(file["no. of times"]):
    send(file["attack no."])
    wait()