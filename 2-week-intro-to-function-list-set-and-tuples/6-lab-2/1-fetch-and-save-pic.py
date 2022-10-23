# Download and chnage desktop wallpaper automatically

import requests
import json

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# pip install requests

# get the json
response = requests.get(api_url)
content = response.content.decode('UTF-8')

# print(response)
# print(type(content))
# print(content)

# convert string to json
dict_content = json.loads(content)

# print(dict_content)

# get the image url
img_url = dict_content['url']

# print(img_url)

# download the image

res = requests.get(img_url)
# print(res)

# save the image
with open('apod.png', 'wb') as image:
    image.write(res.content)

