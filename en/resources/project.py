from guizero import App, Box, Text, TextBox, Picture, PushButton
from PIL import Image

### This is the code for the user interface, including updating the text and resizing images ###

# This dictionary stores the dimensions for the displayed image
DISPLAY_IMAGE_SIZE = {
    'max_width': 300.0,
    'max_height': 300.0
}

# This function resizes an image that is bigger than either the max width or height to fit within them


def generate_display_picture(picture_path, display_image_size):
    picture = Image.open(picture_path)

    if picture.height > picture.width:
        scaled_width = picture.height / display_image_size['max_height']

        scaled_width = (scaled_width if picture.height < display_image_size[
            'max_height'] else 1 / scaled_width) * picture.width

        picture = picture.resize(
            (
                int(scaled_width),
                int(display_image_size['max_height'])
            )
        )
    else:

        scaled_height = picture.width / display_image_size['max_width']

        scaled_height = (scaled_height if picture.width < display_image_size[
            'max_width'] else 1 / scaled_height) * picture.height

        picture = picture.resize(
            (
                int(display_image_size['max_width']),
                int(scaled_height)
            )
        )

    return picture

# This function updates the wiki_text text box with contents passed to it in updated_text


def update_text_box(updated_text):

    global wiki_text

    wiki_text.enable()

    wiki_text.clear()

    wiki_text.append(updated_text)

    wiki_text.disable()


# Create the application
app = App(title='Amazing Image Identifier')

# Create an invisible box to hold the title — useful for setting up complex layouts
title_box = Box(app, width='fill', align='top')

# Create the title and centre it in the application
title = Text(title_box, text="Amazing Image Identifier")

# Create an invisible box to hold the image and article text
content_box = Box(app, width='fill', align='top')
# Create an invisible box to hold the image
picture_box = Box(content_box, align='left')
# Create the image and set it to the start.jpg file included in this directory
display_image = Picture(picture_box, image=generate_display_picture(
    'start.jpg', DISPLAY_IMAGE_SIZE))
# Create the text box for article text
wiki_text = TextBox(content_box, multiline=True, enabled=False, scrollbar=True,
                    text="Please choose an image to identify.", width='fill', height='fill')
# Create a box to hold the button
button_box = Box(app, width='fill', align='bottom')

### End user interface code ###


def update_picture():
    pic = app.select_file()
    display_image.image = generate_display_picture(pic, DISPLAY_IMAGE_SIZE)


# This line creates a button with the text 'Select picture' and tells it to run the update_picture function when clicked
# It has to come later than the other interface code, as it needs the update_picture function to be created first
button = PushButton(button_box, text='Select picture', command=update_picture)

# Display the whole interface — this has to come after the button, the last piece of the interface, is created
app.display()
