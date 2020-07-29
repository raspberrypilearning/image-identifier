## Install the libraries

Now that you have a CLI in the right directory, you can start running Python commands with the files in it. 

The command to install the libraries you need uses **pip**, a tool for fetching Python code written by other people from the internet and setting it up so you can use it in your projects. It's important to use pip to install libraries rather than just downloading them: some libraries need other libraries to work (these libraries are called their **dependencies**) and pip will automatically install those too.

Conveniently, pip can be given a list of all the librarys a project needs, and told to install them all at once. These are usually included in a file called `requirements.txt`, as they have been with the starter code provided here.

--- task ---

Run this command on your CLI to install the libraries you'll need. It may take a while to run, as it will have to download the libraries from the internet and some of them are quite large.

```bash
pip install requirements.txt 
```

--- /task ---

Now that you have the libraries you need installed, it's time to open the Python file you'll be using to do this project. If you've never written Python on your computer before, you may need to install a programmer's text editor first.

--- collapse ---
---
title: Click here if you need to install a programmer's text editor
---

--- /collapse ---

--- task ---

Open your text editor and use it to open the `project.py` file in the directory you've been working in.

--- /task ---

There's a lot of code already provided for you, but it's all for creating the user interface of the application you'll be building. First, run the program as it is to get an idea of how the application will work.

--- task ---

Go back to your CLI window and type the following command to run the program. Remember it, as you'll need to run the program several times.

### If you're using Windows or Linux

```
python project.py
```

Then press the return key to run the program.

### If you're using a Mac
```
python3 project.py
```

Then press the return key to run the program.

--- /task ---

It may take a moment, but when your program runs you should see something like the image below.

![The application screen. A title at the top reads 'Amazing Image Identifier'. The are below is divided vertically into two equal sections. On the left is a large red question mark on a white background. On the right is black text, also on a white background, which reads 'Please choose an image to identify.' At the bottom of the screen there is a 'Select picture' button, which is centred.](images/initial_application.png)

If you click on the 'Select picture' button, you will be able to select an image, which should replace the question mark. Note the image has to be a `.jpg` or `.jpeg` file, as this is what the model you'll be using will expect.

--- task ---

Once you've finished exploring the application as it is, close the application by closing its window.

--- /task ---