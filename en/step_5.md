## Predict an image from your computer

Now that the model is loaded, you need to take the image provided by the users of your program and give it to the model to identify. Of course, the image will need to be prepared for the model first, as it will be expecting a very specific structure of image, to match the structure it was trained on.

--- task ---

First, create a variable that stores the size of image, in pixels, that the model expects. Since it was trained on square images, you only need to store a single number — the width and height are the same.

Near the end of `project.py`, find the `update_picture` function. In the gap between the end of the `update_picture` function and the line after it (`button = PushButton…`), add a few blank lines for space (just to make it easier to read the code), and add an `IMAGE_SIZE` variable and set it to 224. Remember to use upper case names for variables set by the programmer and not changed during the course of the program.

```python
IMAGE_SIZE = 224
```

--- /task ---

Now you need to create a function that will take the image path the user selects and return the model's prediction of what that image contains.

--- task ---

Add this code below the `IMAGE_SIZE` variable:

```python
def identify_image(image_path):
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(IMAGE_SIZE, IMAGE_SIZE))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    prediction_result = model.predict(image, batch_size=1)
    best_prediction = tf.keras.applications.imagenet_utils.decode_predictions(prediction_result, top=1)
    return best_prediction[0][0][1]
```

--- /task ---

To understand each step in this process, you can review [Testing your computer's vision](#), particularly the 'Load your model and image' and 'Use the model to predict an image' steps. In short: 

  * All the lines that start with `image` work to convert the image to the right format for the model.
  * The `prediction_result` line gets the model's prediction in the form of numbers that represent confidence in different guesses.
  * The `best_prediction` line takes those numbers and uses a tool provided by TensorFlow for models trained on the ImageNet dataset (as this one was) which takes the numerical values and selects the labels for the top predictions. In this case, you're only asking for the very top prediction, by setting `top=1`.

Now you need to have your function called when users choose a new picture. 

--- task ---

Add the following lines to the end of the `update_picture` function:

```python
prediction = identify_image(pic)
print(prediction)
```

--- /task ---

Now, when users select a picture, the prediction of what is in the picture will appear in the CLI.

--- save ---

--- task ---

Run the program again and try to select some of the pictures included in the project's directory, to see what predictions get printed out in the CLI.

--- /task ---

Note the first time you run the program it may take a while, as it needs to download the model before it can be used.
