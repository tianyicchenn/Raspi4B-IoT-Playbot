import base64
import json
import urllib.parse
import urllib.request

import requests

from components import WebCam


def capture():
    camera = WebCam()
    return camera.capture()


def formatted_image(impath):
    f = open(impath, 'rb')
    img = base64.b64encode(f.read()).decode('utf-8')
    return img


def get_token(AK, SK):
    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials'
    host = url + '&client_id={}&client_secret={}'.format(AK, SK)
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    return json.loads(content.decode('utf-8'))['access_token'] if content else 'error'


def detection(image_path, header, request_url):
    data = formatted_image(image_path)
    response = requests.post(request_url, data=json.dumps({"image": data}), headers=header).text
    results = json.loads(response)
    if results.get("results"):
        return results.get("results")[0]["name"]
    else:
        return "error"


def main():
    request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/detection/PetCatsDetection'
    # TODO: replace with your own key/secret
    api_key = 'api_key'
    secret_key = 'secret_key'
    image_path = capture()
    access_token = get_token(api_key, secret_key)
    request_url = request_url + "?access_token=" + access_token
    header = {'Content-Type': 'application/json'}
    breed = detection(image_path, header, request_url)
    return breed


if __name__ == "__main__":
    breed = main()
    print(breed)

