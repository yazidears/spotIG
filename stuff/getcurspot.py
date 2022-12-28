import requests
import time
import os
from pprint import pprint
import base64
from os import system, name
if os.path.exists("data/notplaying.datayzde"):
            os.remove("data/notplaying.datayzde")
SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'    
if os.path.exists("data/tkn.encryzde"):
    os.remove("data/tkn.encryzde")
os.system("python3 stuff/logspot.py")
notexists = True
while notexists:
    if os.path.exists("data/tkn.encryzde"):
        file = open("data/tkn.encryzde", "r")
        base64_message = str(file.read())
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        token = message
        notexists = False
    
ACCESS_TOKEN = str(token)
def get_current_track(access_token):

    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()
    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]
    link = json_resp['item']['external_urls']['spotify']
    artist_names = ', '.join([artist['name'] for artist in artists])
    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
    	"link": link
    }

    return current_track_info


def main():
    current_track_id = None
    current_track_info = get_current_track(ACCESS_TOKEN)
    if current_track_info['id'] != current_track_id:
        #pprint(current_track_info,indent=4)
        if os.path.exists("data/currently.yzde"):
            os.remove("data/currently.yzde")
        fle = open("data/currently.yzde", "x")
        fle.write(str(current_track_info))
        fle.close()
        current_track_id = current_track_info['id']

if __name__ == '__main__':
    main()