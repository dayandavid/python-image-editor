from PIL import Image

Image.MAX_IMAGE_PIXELS = None

# Open the image
image = Image.open('image.jpg')

#Get the current size
width, height = image.size

new_width = int(width*0.5)
new_height = int(height*0.5)


print("Resizing...")

# Resize the image
resized_image = image.resize((new_width, new_height))

# Save the resized image
resized_image.save('resized_image.jpg')