import base64
import json
import urllib.parse
import urllib.request

from components import WebCam


def capture():
    camera = WebCam()
    return camera.capture()


def get_alitoken(client_id, client_secret):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' \
           + client_id + '&client_secret=' + client_secret + ''
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    return json.loads(content.decode('utf-8'))['access_token'] if content else 'error'


def formatted_image(impath):
    f = open(impath, 'rb')
    img = base64.b64encode(f.read()).decode('utf-8')
    return img


def detection(request_url, params):
    req = urllib.request.Request(url=request_url, data=params)
    req.add_header('Content-Type', 'application/json')
    res = urllib.request.urlopen(req)
    return res.read()


def face_verify(client_id, client_secret, image1, image2):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
    params = json.dumps(
        [{"image": formatted_image(image1), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
         {"image": formatted_image(image2), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"}])
    access_token = get_alitoken(client_id, client_secret)
    request_url = request_url + "?access_token=" + access_token
    params = params.encode("utf-8")
    content = detection(request_url, params)
    if json.loads(content.decode('utf-8'))['result']:
        return json.loads(content.decode('utf-8'))['result']['score']
    else: return 0


def main():
    # TODO: replace with your own key/secret
    client_id = 'client_id'
    client_secret = 'client_secret'
    admin = "/home/pi/Desktop/Camera/webCam/host.jpg"
    user = capture()
    return True if face_verify(client_id, client_secret, admin, user) >= 0.8 else False


if __name__ == '__main__':
    print(main())
