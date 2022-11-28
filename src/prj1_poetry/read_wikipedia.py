import requests

if __name__ == "__main__":
    url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
    with requests.get(url) as response:
        print(response.text)
        print(response.status_code)
        for data in response.json():
            print(data)
