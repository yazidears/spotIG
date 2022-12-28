import spotipy.util as util
import base64
import os
username = '31ok7li3ejk4gbasfet4pwturmou'
client_id ='5f97d340783d46a0bfbc4e00f69ad19a'
client_secret = '829b8daa882546f8bcd38d0e94223deb'
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-read-currently-playing'

token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)

if os.path.exists("data/tkn.encryzde"):
    os.remove("data/tkn.encryzde")
usr = open("data/tkn.encryzde", "x")
message = str(token)
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')
usr.write(base64_message)
usr.close()