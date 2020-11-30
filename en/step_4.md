## Load your model

The application has all the parts it needs, but it doesn't actually work yet. It just loads up an image and displays it — no machine learning, no information about the thing in the picture. Time to fix that!

First, you need to load a model to do your image identification. While you could collect and label tens of thousands of images, design a model, and train it like in [Teach a computer to read](#), that would take days of work. It's much faster to use a model that has already been trained to identify a wide variety of things. Luckily, TensorFlow contains several such models, so you can just load one of them: VGG16.

First, you need to import TensorFlow so you can use it in the program. On the very first lines of the file, you'll see a couple of existing `import` statements:

```python
from guizero import App, Box, Text, TextBox, Picture, PushButton
from PIL import Image
```

--- task ---

Below the existing import lines, add two more for libraries you'll need to get the machine learning elements of the project working: `tensorflow` and `numpy`:

```python
import tensorflow as tf
import numpy as np
```

--- /task ---

Notice that, while you import the libraries, you use the `as` keyword to give them shorter names, so you don't have to type as much later!

--- task ---

Just below the `import` statements at the top of the file, load the VGG16 model from the TensorFlow library into a variable called `model`.

```python
model = tf.keras.applications.VGG16()
```

--- /task ---

Load the model at the start of your program because it takes some time, and you need to load it before you create your user interface to avoid creating an empty window that might confuse your user. Since this can mean the program doesn't seem to do anything for a few seconds, you might want to print out a message like 'Preparing to start application' or 'Loading image identifier' before you start to load the model.

The `keras.applications` included in loading the model is because TensorFlow is a very large library and is broken up into sections. 'Keras' is one of those, 'applications' is a section of 'Keras', and VGG16 is in the 'applications' section.

--- save ---
