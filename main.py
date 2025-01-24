import face_recognition
from PIL import Image, ImageDraw

# Load an image
image_path = "test_image.jpg"
image = face_recognition.load_image_file(image_path)

# Find all face locations in the image
face_locations = face_recognition.face_locations(image)
print(f"Found {len(face_locations)} face(s) in the image.")

# Draw rectangles around the faces
pil_image = Image.fromarray(image)
draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left) in face_locations:
    draw.rectangle(((left, top), (right, bottom)), outline="red", width=3)

# Display the image with faces highlighted
pil_image.show()
