from PIL import Image, ImageDraw, ImageFont
import random
import os
import datetime
import qrcode

# Create a new blank image for the ID card
image = Image.new('RGB', (1000, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Load fonts
font_large = ImageFont.truetype('arial.ttf', size=60)
font_small = ImageFont.truetype('arial.ttf', size=45)

# Function to paste ID photo onto the ID card
def paste_id_photo(photo_path):
    try:
        photo = Image.open(photo_path)
        # Resize the photo to fit a specific area on the ID card
        photo = photo.resize((150, 150))
        image.paste(photo, (750, 250))  # Adjust coordinates based on your layout
    except IOError:
        print(f"Unable to load image: {photo_path}")

# User inputs and data collection
os.system("ID CARD Generator")
d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("%d-%m-%Y\t ID CARD Generator\t  %I:%M:%S %p")
print(reg_format_date)
print('\n\nAll Fields are Mandatory')
print('Avoid any kind of Spelling Mistakes')
print('Write Everything in uppercase letters')

# Company name
message = input('\nEnter Your Company Name: ')
company = message

# Draw company name on ID card
(x, y) = (50, 50)
draw.text((x, y), message, fill='rgb(0, 0, 0)', font=font_large)

# Generate and draw unique ID number
(x, y) = (600, 75)
idno = random.randint(10000000, 90000000)
message = f'ID {idno}'
draw.text((x, y), message, fill='rgb(0, 0, 0)', font=font_large)

# User details input and drawing
(x, y) = (50, 250)
message = input('Enter Your Full Name: ')
name = message
draw.text((x, y), message, fill='rgb(0, 0, 0)', font=font_small)

(x, y) = (50, 350)
message = input('Enter Your Gender: ')
draw.text((x, y), message, fill='rgb(0, 0, 0)', font=font_small)

(x, y) = (250, 350)
message = input('Enter Your Age: ')
draw.text((x, y), message, fill='rgb(0, 0, 0)', font=font_small)

(x, y) = (50, 450)
message = input('Enter Your Date Of Birth: ')
draw.text((x, y), message, fill='rgb(0, 0, 0)', font=font_small)

(x, y) = (50, 550)
message = input('Enter Your Blood Group: ')
draw.text((x, y), message, fill='rgb(255, 0, 0)', font=font_small)

(x, y) = (50, 650)
message = input('Enter Your Mobile Number: ')
temp = message
draw.text((x, y), message, fill='rgb(0, 0, 0)', font=font_small)

(x, y) = (50, 750)
message = input('Enter Your Address: ')
draw.text((x, y), message, fill='rgb(0, 0, 0)', font=font_small)

# Save the initial image with user's name
output_filename = f'{name}.png'
image.save(output_filename)

# Create QR code with company name and ID number
qr_img = qrcode.make(f'{company}{idno}')
qr_img.save(f'{idno}.bmp')

# Load and paste QR code onto ID card
id_card = Image.open(output_filename)
qr_code = Image.open(f'{idno}.bmp')
id_card.paste(qr_code, (800, 600))  # Adjust coordinates based on your layout

# Save the image after adding QR code
id_card.save(output_filename)

# Load and paste ID photo onto ID card
id_photo_path = input('Enter the path to your ID photo: ')
paste_id_photo(id_photo_path)

# Save the final ID card image
id_card = Image.open(output_filename)
id_card.paste(image, (0, 0))
id_card.save(output_filename)

print(f'\n\n\nYour ID Card has been successfully created in a PNG file: {output_filename}')
input('\n\nPress any key to close the program...')
