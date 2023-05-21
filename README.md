## 0x00. AirBnB clone - The console

### Background Context
#### Welcome to the AirBnB clone project!

###### First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building a full web application: the AirBnB clone.  
This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help us to:

 - put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our future instances
 - create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
 - create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
 - create the first abstracted storage engine of the project: File storage.
 - create all unittests to validate all our classes and storage engine

##### What’s a command interpreter?

It's like a Shell, It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

 - Create a new object (ex: a new User or a new Place)
 - Retrieve an object from a file, a database etc…
 - Do operations on objects (count, compute stats, etc…)
 - Update attributes of an object
 - Destroy an object

### Learning Objectives
At the end of this projcect, you(we) are expected to be able to explain to anyone, **without the help pf Google:**  
  
##### GeneralHow to create a Python package
 - How to create a command interpreter in Python using the cmd module
 - What is Unit testing and how to implement it in a large project
 - How to serialize and deserialize a Class
 - How to write and read a JSON file
 - How to manage datetime
 - What is an UUID
 - What is \*args and how to use it
 - What is \*\*kwargs and how to use it
 - How to handle named arguments in a function

## More Info
#### Execution
Your shell should work like this in interactive mode:
  
	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$

But also in non-interactive mode:  

	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

## 0x01 AirBnB clone - Web Static

Now that we have a command interpreter for managing our AirBnB objects, it's time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

- Create simple HTML static pages
- Style guide
- Fake contents
- No Javascript
- No data loaded from anything

During this project, we will learn how to manipulate HTML and CSS languages.
HTML is the structure of our page, it should be the first thing to write. CSS is the styling of your page, the design.
I'll fix our HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

### Learning Objectives
At the end of this project, we are expected to be able to explain to anyone, **without the help of Google:**

#### General
- What is HTML
- How to create an HTML page
- What is a markup language
- What is the DOM
- What is an element / tag
- What is an attribute
- How does the browser load a webpage
- What is CSS
- How to add style to an element
- What is a class
- What is a selector
- How to compute CSS Specificity Value
- What are Box properties in CSS
