#url https://open.spotify.com/track/2WyNqDHLRJLzJuidCsO1Ey?si=73c4738c9c2647f1
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 
import download

#To access authorised Spotify data
client_id = '6bbbe4ed36e74435bb87f04904cb0d31'
client_secret = 'cfdc80fa279f4d8cbf2a24b161293910'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
#
# spotify object to access API
name = "Dua lipa" #chosen artist
result =sp.track("https://open.spotify.com/track/2WyNqDHLRJLzJuidCsO1Ey?si=73c4738c9c2647f1")
#result = sp.search(name) #search query
#result['tracks']['items'][0]['artists']
print (result['artists'][0]['name'], result['name'])

