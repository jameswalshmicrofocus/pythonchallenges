from PIL import Image

target_image = Image.open('oxygen.png').convert('LA')
target_image.save('greyscale.png')