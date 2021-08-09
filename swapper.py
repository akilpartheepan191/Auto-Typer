import keboard as k
import json
import time
file=open('swapper.json')
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
  send('swap')
  wait()
  send(file["swapper"])
  wait()
  for i in range(file["number of times"]):
    send(file["attack no."])
    wait()