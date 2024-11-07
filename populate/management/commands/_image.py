import base64
import requests

from hackathon.models import Images

def fetch_random_image_base64():
    url = "https://random.imagecdn.app/v1/image?width=1280&height=720&category=dogs&format=json"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        image_url = data.get("url")

        if image_url:
            image_response = requests.get(image_url)

            if image_response.status_code == 200:
                return base64.b64encode(image_response.content).decode("utf-8")

    return None

def populate_images():
    if Images.objects.exists():
        return

    images_to_insert = []
    for _ in range(2):
        image_base64 = fetch_random_image_base64()
        if image_base64:
            image_instance = Images(photo_base64=image_base64)
            images_to_insert.append(image_instance)

    Images.objects.bulk_create(images_to_insert)