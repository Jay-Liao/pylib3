import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


def post_recognition_request(file_name):
    print(f"post_recognition_request({file_name})...")
    multipart_data = MultipartEncoder(
        fields={
            # a file upload field
            "file": (file_name, open(f"input/{file_name}", "rb")),
            # plain text fields
            "callback_url": "http://aaa.bbb",
            "model_names": "object,scene,general_object,general_scene,general_concept"
        })

    headers = {
        "Content-Type": multipart_data.content_type,
        "Accept": "application/json"
    }

    url = "http://test.com"
    response = requests.post(url=url,
                             headers=headers,
                             data=multipart_data)
    print(f"result: {response.text}")