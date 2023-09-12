import openai
from skimage import io
import cv2


def redrawimage(img_path):
  openai.organization = "org-iGW7KAYcBIQALDzwvCjhqOVy"
  openai.api_key = "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"


  response_img = openai.Image.create_variation(
    image=io.imread(img_path),
    n=1,
    size="1024x1024"
  )

  for i,img_data in enumerate(response_img['data']):
    img = io.imread(img_data['url'])
    cv2.imshow('reponse img {}'.format(i), img)

  cv2.waitKey(0)

if __name__ == '__main__':
  img_path = r"D:\Rtest1.png"
  redrawimage(img_path)

