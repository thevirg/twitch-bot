import socket
import datetime
import threading

import requests


class TwitchIRC:
    def __init__(self, username, channel, token):
        """
        IRC client with Twitch specific methods.
        Get your access token at www.twitchapps.com/tmi/
        """
        self.username = username
        self.token = token
        self.channel = '#' + channel
        self.host = 'irc.twitch.tv'
        self.port = 6667
        self.irc_sock = socket.socket()
        self.welcome()

    def welcome(self):
        """
        This function connects to twitch IRC in few steps:

        1. Connects to the server
        2. Sends a token
        3. Sends the username
        4. Joins a channel
        5. Requests extra tags (badges, emotes, etc)
        """
        self.irc_sock.connect((self.host, self.port))
        self.send_token()
        self.send_nick()
        self.join_channel()
        self.request_tags()

    def disconnect(self):
        self.irc_sock.close()
        
    def send(self, data):
        """
        This function converts data into bytes with UTF-8 encoding then socket.send()
        """
        self.irc_sock.send(bytes(data, 'UTF-8'))

    def send_pong(self):
        self.send("PONG :tmi.twitch.tv\r\n")

    def send_nick(self):
        self.send("NICK {}\r\n".format(self.username))

    def send_token(self):
        self.send("PASS {}\r\n".format(self.token))

    def join_channel(self):
        self.send("JOIN {}\r\n".format(self.channel))

    def part_channel(self):
        self.send("PART {}\r\n".format(self.channel))

    def send_message(self, message):
        self.send("PRIVMSG {} :{}\r\n".format(self.channel, message))
    
    def request_tags(self):
        #https://discuss.dev.twitch.tv/t/unable-to-register-for-irc-capabilities/27023
        self.send("CAP REQ :twitch.tv/tags\r\n")


class TwitchAPI:
    def __init__(self, client_id, channel, token=None):
        """
        Basic Twitch API calls using kraken v5
        
        client_id = client id from your bot application <string> https://glass.twitch.tv/console/apps
        channel = username of the channel authorized above <string>
        token = token for "user_read channel_editor" scopes <string> https://twitchapps.com/tokengen/
        """
        self.base_api = "https://api.twitch.tv/kraken/"
        self.client_id = client_id
        self.channel = channel
        self.token = token
        
        self.headers = {'Client-ID': self.client_id,
                        'Accept': 'application/vnd.twitchtv.v5+json'}
                        
        if self.token:
            self.headers['Authorization'] = f'OAuth {self.token}'
            
        self.user = {}
        self.channel_id = ''
        self.status = ''
        self.game = ''
        self.channel_info = {}
        
        self.connect()
        
    def connect(self):
        user = threading.Thread(target=self.get_user)
        info = threading.Thread(target=self.get_channel_by_id)
        
        user.start()
        user.join()
        
        self.channel_id = self.user.get('_id', '')
        
        info.start()
        
        info.join()
        self.status = self.fetch_status()
        self.game = self.fetch_game()

    def get_user(self):
        #https://dev.twitch.tv/docs/v5/#getting-a-client-id
        r = requests.get(self.base_api + 'user', headers=self.headers)
        
        if r.status_code == 200:
            self.user = r.json()
        return r.json()

    def get_channel_by_id(self):
        #https://dev.twitch.tv/docs/v5/reference/channels/#get-channel-by-id
        r = requests.get(self.base_api + "channels/" + self.channel_id, headers=self.headers)
        
        if r.status_code == 200:
            self.channel_info = r.json()
        return r.json()

    def fetch_status(self):
        return self.channel_info.get('status')

    def fetch_game(self):
        return self.channel_info.get('game')
    
    def update_game(self, game_title):
        post_data = {
            'channel': {
                'game': game_title
            }
        }
        
        response = requests.put(self.base_api + 'channels/' + self.channel_id, json=post_data, headers=self.headers)
        
        if response.status_code == 200:
            self.game = game_title
        return response

    def update_status(self, stream_title):
        post_data = {
            'channel': {
                'status': stream_title
            }
        }

        response = requests.put(self.base_api + 'channels/' + self.channel_id, json=post_data, headers=self.headers)

        if response.status_code == 200:
            self.status = stream_title
        return response
    
    def retrieve_followers(self, count=5):
        followers = list()

        if self.channel_id:
            response = requests.get(self.base_api + 'channels/' + self.channel_id + '/follows?limit=' + str(count), headers=self.headers)
        else:
            print('[Twitch API] retrieve_followers: channel ID is None.')
            return followers
        
        if response.status_code == 200:
            for block in response.json()["follows"]:
                followers.append(block["user"]["display_name"])
        else:
            print('[Twitch API] _retrieve_followers():', response.text)
            
        self.recent_followers = followers
        return followers
        
    def check_for_new_followers(self):
        latest_followers = self.retrieve_followers()
        new_followers = []
        
        for user in latest_followers:
            if user not in self.recent_followers:
                new_followers.append(user)
        
        self.recent_followers = latest_followers
        
        return new_followers
        
    def get_stream_by_user(self):
        #https://dev.twitch.tv/docs/v5/reference/streams/#get-stream-by-user
        response = requests.get(self.base_api + 'streams/' + self.channel_id, headers=self.headers)
        return response.json()
        
    def get_current_stream_startup_time(self):
        json = self.get_stream_by_user()
        if json.get('stream'):
            return json.get('stream').get('created_at')
        
    def get_uptime(self):
        #json format "2016-12-14T22:49:56Z"
        string = self.get_current_stream_startup_time()
        
        if string:
            then = datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%SZ')
            now = datetime.datetime.now()
            diff = now - then
            
            return diff
          
    def get_users(self, username):
        #https://dev.twitch.tv/docs/v5/reference/users/#get-users
        r = requests.get(self.base_api + 'users?login=' + username, headers=self.headers)
        return r.json()
