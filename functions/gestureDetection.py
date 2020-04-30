import time
from json import JSONDecoder

import requests

from components import WebCam


def capture():
    camera = WebCam()
    return camera.capture()


def detection(dicts):
    possibility = 0
    gesture = ""
    for i in dicts:
        if dicts[i] > possibility:
            gesture = i
    return gesture


def main():
    # TODO: replace with your own key/secret
    url = "https://api-cn.faceplusplus.com/humanbodypp/v1/gesture"
    key = "key"
    secret = "secret"
    image_path0 = capture()
    data = {"api_key": key, "api_secret": secret}
    files = {"image_file": open(image_path0, "rb")}

    response = requests.post(url, data=data, files=files)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    results_dict = req_dict["hands"]

    if results_dict:
        gesture_detected = results_dict[0]["gesture"]
        return detection(gesture_detected)
    else:
        return "error"


if __name__ == "__main__":
    print(main())
