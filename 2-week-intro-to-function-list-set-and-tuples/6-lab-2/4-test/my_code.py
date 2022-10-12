import requests

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

def get_res(url):
    return requests.get(url)

if __name__ == "__main__":
    # print(__name__)
    res = get_res(api_url)
    print(res)