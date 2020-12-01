## Run the program

Now that you have the libraries you need installed, it's time to open the Python file you'll use to do this project. If you've never written Python on your computer before, you may need to install a programmer's text editor first.

--- collapse ---
---
title: Click here if you need to install a programmer's text editor
---
There are lots of different programmer's text editors, and they are usually free, so most programmers try a few before finding their favourite. As you become more experienced, you should try different editors to see if there's one you enjoy using more than the others. For now, though, try one of the following:

Use [Thonny](https://thonny.org/) if you do all your text-based programming in Python. It's got a lot of helpful features that work with Python to help you program correctly, and to investigate if your program isn't working as expected.

If you use a few different languages — for example, if you create web pages with HTML and CSS as well as Python applications — then [Visual Studio Code](https://code.visualstudio.com/) is a good choice. It offers less help for any particular language, but supports a lot of different languages.

--- /collapse ---

--- task ---

Open your text editor and use it to open the `project.py` file in the directory you're using.

--- /task ---

There's a lot of code already provided for you, but it's all to create the user interface of the application you'll build. First, run the program as it is to get an idea of how the application will work.

--- task ---

Go back to your CLI window and type the following command to run the program. Remember it, as you'll need to run the program several times.

### If you're using Windows

```
python project.py
```

Then press the Return key to run the program.

### If you're using macOS or Linux
```
python3 project.py
```

Then press the Return key to run the program.

--- /task ---

It may take a moment, but when your program runs you should see something like the image below.

![The application screen. A title at the top reads 'Amazing Image Identifier'. Below is divided vertically into two equal sections. On the left is a large red question mark on a white background. On the right is black text, also on a white background, which reads 'Please choose an image to identify.' At the bottom of the screen there is a 'Select picture' button, which is in the centre.](images/initial_application.png)

If you click on the **Select picture** button, you will be able to select an image, which should replace the question mark. Note the image has to be a `.jpg` or `.jpeg` file, as this is what this model will expect.

--- task ---

Once you've explored the application as it is, close the application by closing its window.

--- /task ---
