from PIL import Image


def optimize():
    # Open the image file
    img = Image.open('cursos.jpg')

    # Reduce the quality of the image and save as a new file
    img.save('compressed.jpg', optimize=True, quality=70)
