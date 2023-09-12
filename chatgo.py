import os
import openai
from skimage import io
from matplotlib import pyplot as plt
import cv2

openai.organization = "org-iGW7KAYcBIQALDzwvCjhqOVy"
openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message['content'])

response_img = openai.Image.create(
  prompt="请给出一张许天宇的肖像",
  n=2,
  size="1024x1024"
)

for i,img_data in enumerate(response_img['data']):
  img = io.imread(img_data['url'])
  cv2.imshow('reponse img {}'.format(i), img)

cv2.waitKey(0)


