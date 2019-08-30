import os
import subprocess
import urllib3
from slack import RTMClient



@RTMClient.run_on(event="message")
def say_hello(**payload):
  data = payload['data']
  web_client = payload['web_client']

  if 'text' in data.keys() and 'Video' in data['text']:
    channel_id = data['channel']
    thread_ts = data['ts']
    user = data['user']


    subprocess.call("/home/pi/gif.sh", shell=True)

    response = web_client.files_upload(channels=channel_id,  file="gif.gif")


print("Waiting for internet")
http=urllib3.PoolManager(timeout=1.0)
while True:
        try:
            response = http.request("GET",'http://google.com',retries=False)
            break
        except urllib3.exceptions.NewConnectionError:
            pass

print("Connecting")
token = "INSERT YOUR API TOKEN HERE"

slack_token = token
rtm_client = RTMClient(token=slack_token)
print("Starting")
result = rtm_client.start()
print(result)
