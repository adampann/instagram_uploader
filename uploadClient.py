from instapy_cli import client
from postObject import post
import json
class agent:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password 
        
    def upload_to_instagram(self, post):
        with client(self.username, self.password) as cli:
            cli.upload(post.path, post.caption)


if __name__ == "__main__":
    with open('login.config') as json_data:
        data = json.load(json_data)
    username = data['username']
    password = data['password'] 
    
    print(username, password)
    instpost = post('pics/AAGxnz2x.jpg', 'test upload', True)
    print('post:', instpost)
    uploader = agent(username, password)
    print('attempt upload')
    uploader.upload_to_instagram(instpost)
    print('finished upload')
