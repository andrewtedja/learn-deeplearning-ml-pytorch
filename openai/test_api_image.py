import os
import base64
from openai import OpenAI
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# load image, convert ke format base64
file_path = input("Enter the path to your image file: ")

image_path = file_path.strip()

with open(image_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

# MAIN API CUSTOMIZATION
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What's the main object in this image? Reply with just one lowercase word. If the object is classified as unsafe, reply with 'unsafe'."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    max_tokens=10
)

print("GPT-Image-1 response:", response.choices[0].message.content.strip())
