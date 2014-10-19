Ladies and Gentlemen,

If I were standing before you to host the Tony awards or maybe the Oscars, I
could be jumping about or dance around with a bunch of jokers and make an
absolute fool of myself. However, since this is none of that, all I can say is
that it is both a privilege and honor to be here, standing before you.

I could go on and on with this intro, but taking into consideration the fact
that we only have roughly about two hours to go, I'll save the speech for the
end. Let's get on with it. I'll just say that my name is Haris Ibrahim K V and
I come from South India. So if you want to ask something in between the
session, do call out my name and ask.

As you must have already gone through the abstract, you would know that this
tutorial is about learning Django. However instead of explaining a "Hello,
World" application, we are going to fetch, process and visualize Twitter data,
plugging in redis to implement a few use cases.


1. The origin of Django
-----------------------

Let me take you back for about a decade. It is the fall of year 2003. Mr.
Adrian Holovaty was sitting there at the Lawrence Journal-World newspaper
office in Kansas along with the new intern, Simon Willison. Both of them,
experienced wed developers during the time when PHP reigned supreme.

Apparently, the two of them were extremely fed up of having to maintain the
huge websites they developed in PHP. I wonder why. :smile:

However, during that time, both of them were in love with Python already and
they wanted to make web development happen in Python.


2. How does a website work?
--------------------------

Why are you learning Django in the first place? The answer is, unanimously,
*"To build a website!"*, right? Absolutely. However, what part of a website
does Django help you to make? Or if you just use Django, does that take care of
everything?

Whenever you host a website, think of any website that you know, there is a
computer sitting at some part of the world which serves that website for you,
on a plate or more often on your browser.

There are more than a few things that come into picture here. To keep a long
story short, first in the line of defense comes a web server. Things like
Apache, Nginx, etc are the candidates here. After this layer comes a WSGI
application. WSGI is a standard which lets Python application communicate with
web servers. Gunicorn is one of the popular ones here. After these two layers
comes our Django application!

To complete the entire picture, behind Django, comes the Database. Keep this
picture in mind and now let's move on.


3. MVC architecture
-------------------

During olden days, there was no structure as such for web applications. If you
have seen old php sites or even tried to build one in your college curriculum,
you know how messed up it becomes with your script in between your HTML and all
that.

Anyway, thankfully for us, the world has moved on and certain best practices
have been put into place. MVC is one of them. It stands for
Model-View-Controller. "Separation of concern" is what it enforces.

In very broad terms, Model is the part where the business logic of your
application lies. This means thinking through what all entities your website
requires such as User accounts, Friend's list, Categories, Pages, Photos, etc.

View is what your user sees. The HTML and what all goes into based on the
user's response are decided by the views.

Last but not the least, comes the controller. As the name suggests, it controls
your application's behaviour. This means deciding which function or part of
your code to execute based on the user's actions.

Capiche?


4. Starting off with Django
---------------------------

Now that we have finished our monologue and hopefully you have a better
understanding of how a website works, let's get into business, shall we?

It is time to start your project in Django. Now, before we jump into it, you
must understand how a Django project is structured. Bear with me on this one.
Listen carefully.

Two things: "project" and "app". Did you hear that? "PROJECT" and "APP".

From now on, whenever I say "project", think of it as the Umbrella which
everything comes under, got it? When I say "project", get the image of a huge
supermarket into your mind, okay? It will have an entrance, a reception, a
billing section, etc.

Whenever I say "app", get the image of different sections within a supermarket
into your mind. Like cutlery, cosmetics, stationery, etc.

So this is how a Django project is laid out. There is the "project" which
encompasses everything and then there are the apps to take care of specific
things within the project. Let's make a project!

```bash
$ django-admin.py startproject visualizer
```

There you go! Django has created the project skeleton for you. Let's explore
what we have here. You have something like:

```bash
$ tree visualizer/
visualizer/
└── visualizer
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

The top level "visualizer" directory is just a container for your project.
Django does not care what you name it. But the visualizer that you see inside
is important as you will have to use that to reference whatever is inside. It
is a "Python Package".

The manage.py, as the name suggests, is what lets you manage the project. You
can pass various command line arguments to it in order to get more than a few
things done.

Inside the visualizer folder, the `__init__.py` file is what Python requires
to make your project a package.

The `settings.py` file is where you specify the DB connections, the path to
your static files directory and many other paths and settings which we will
talk about through the duration of this session.

`urls.py`, as you might have guessed has the urls defined. What part of your
Django code should execute when a certain URL is hit, will be defined there.
You can, at a very high level, think of it as an entry point into your
application when a request comes in.

Ready to run your Django code? Splendid. Make it so number one!

```bash
$ python manage.py runserver
```

Head over to http://127.0.0.1:8000/ and see the magic!

Let's move on soldier.


5. Creating your first Django app
---------------------------------

Remember the subsections in the supermarket? That's that we are going to create
now. Let's think about our project for a moment now. We are building something
that is going to fetch tweets from Twitter and showcase it using a graph. So
that's why I decided to call the project visualizer, because that's the main
thing it does.

If you think about it, we could visualize anything and it necessarily need not
be just twitter. Let's say our stretch goal is to visualize posts from a myriad
of social networking sites. Hence, the core visualization code that we are
going to use needs to be reusable no matter what the source is. This is a good
excuse for an app.

It is time for you to leave the analogy behind. Let me tell you how to think of
apps. First of all, think of it as a separation of concern. You have different
things that your project is going to do. Apps let you modularize your code.

In our case, broadly, we have two requirements:
 - To visualize whatever data is there.
 - To fetch posts from different services.

So either you could have two apps, one for each of these. Or you could split up
the "different services" into different apps one for each service. For the sake
of this tutorial, I am going with the "an app for a service" approach.

Thus, the two apps that I am going to have are:
 - visualize
 - twitter

Let's create them.

```bash
$ python manage.py startapp visualize
$ python manage.py startapp twitter
```

Voila! You have two new folders there within. Let's explore the innards of
these apps quickly before we move forward.

```
twitter
     ├── admin.py
     ├── __init__.py
     ├── models.py
     ├── tests.py
     └── views.py
```

We'll come to the `admin.py` in a minute.

You already know what `__init__` is.

The models.py is where we define our models. If you recall when I mentioned
about MVC earlier, the model is where you define the different "entities" that
you are going to use for your website. Like User accounts, Friend's list,
Categories, Pages, Photos, etc.

The `tests.py` is where you obviously write tests, something that we won't be
covering as a part of this tutorial.

Last but not the least, the `views.py` file. This is what will take care of what
the user sees when he requests a certain URL.


6. Customary "Hello, World" tutorial.
-------------------------------------

Now you know where the URLs go and where the views go. It is about time we did
our "Hello, World!"

In order for a request to be processed, we need to define a URL which the user
can hit and view that runs the Python code corresponding to that URL.

For the sake of the example, we are just going to print "Hello, World" on the
browser. Let's first write the "view" to do that. Open up your
`visualize/views.py`

You can see we are importing something called "Render", but we will use that
later. Let us import something called HttpResponse. Now let's write the view.
We'll call it "`entity_visualizer`".

Going in depth to what happens here would leave us with very little time, but
one thing that you should know is that every view, EVERY VIEW, should return an
Http Response. Django provides different functions to do it, but at the end of
the day, it should have a return statement which uses one of these functions.

Also, notice that for every view, a default parameter needs to be passed in
called "request". That will contain all the information regarding the incoming
request. The data passed in with it, the parameters, the user information,
whether it is a GET or a POST request, etc.

Now since we have the view, let's use it to define the URL as well. Open the up
the `visualizer/urls.py` file. Let's say, you want this "Hello, World" to show
up when you visit

"http://localhost:8000/visualize"

Then let's edit the `urls.py` file to make that happen.

First make sure you import the view from where it is.

Then define the URL.

Let's go visit the URL and viola! Hellooooo World!

Explore: Use "include" and have the URLs for each app within themselves.


7. Enter Templates.
-------------------

Well, in the `views.py`, we just returned a string as an HttpResponse object.
While you can feel extremely proud of cramming in your entire HTML file in the
place of that string, for the sake of sanity, we should have HTML files as a
separate concern.

This is where render comes in. Render uses the "request" parameter, a template
and a context. The "context" are the variables that you want pass from your
Python code into your templates so that they can be accessed there.

Where do you keep your templates? There are a couple of options out of which
the best one is to make a "templates" directory under each app where you keep
your HTML files.

So let's go ahead and create an HTML files within the templates directory under
the visualize app.

```
/visualize/templates/hello_world.html
```

Great! Now let's use "Render" to render it.

Now try visiting the same URL as earlier. You will get an error saying
"Template Does not Exist".

Remember when we explained the concept of "project" and "apps" earlier? Well,
Django uses the same concept for many of its core functions as well. Would you
like to see all the predefined apps that Django comes with?

Open up `visualizer/settings.py`.

Do you see the dictionary called "INSTALLED_APPS" defined? Whatever you see
over there are apps. And it is only natural that any app that we create needs
to be added there as well.

Added it? Splendid. Let's visit the URL once again, shall we?

There you go, as promised. :smile:

Just to get the hang of things, let's try passing in some variables into the
templates.

For the sake of knowing I am not pulling your leg, let's get the current date
and print it within the template each time we visit the URL. For that, we can
use the datetime library.

Get the current date.

Make it into a dictionary.

Pass it in along with render.


8. Defining the problem statement
---------------------------------

The problem statement is simple. Fetch the tweets related to a certain hashtag,
visualize the tweets/hr graph along with knowing the most popular tweet and how
many tweets we got in total. So what do we need? A form for the user to input
the hashtag, which is to be displayed at a separate URL. Also, the visualize
page that we already have.


9. A small intro to Redis
-------------------------

What is a SQL datastore and how is redis different by being a NoSQL datastore.


10. Thinking about models
-------------------------

Ah yes, the models. We have left this part out, one of the most important part
out until now. As we have alredy discussed what models are, this is the time to
decide on what our models will be. As you can see, we are fetching tweets and
we need to show the user the visualization, popular and count each time he
visits the "visualize" URL. So, instead of hitting the API each time when the
user wants it, we can save the information we need in a database. This is where
models step in.

How many of you know what an ORM is? 7 of you. Splendid. To make a long story
short as a programmer, it is hard to always think in terms of rows and columns
when you are writing Python code. So what the ORM (the Object Relational
Mapper) does it that, it maps the Relations to Classes in Python.

So when you are thinking "table name", it is Class Name in Python. When you
think of columns, they will be the respective attributes within the classes.
When you think of one row, it will be an instance of the corresponding Class.
When you are thinking a particular column of a row, it will the
instance.attribute name.

Without further ado, let's define our models. Since we are storing the tweet,
and we need to show the tweet text and we need the time to compute the
tweets/hr graph, we will define a table called Tweet with the fields, text,
created_at and author name.

Excellent. There is yet another important aspect that we have not introduced
until now. Now that you have created the model, how do you make sure it is
there in the database?

For that to happen, manage.py gives you another convenience command called
"syncdb". Let's try that out now.

```bash
$ python manage.py syncdb
```

Now you would have seen a lot of tables being created when you ran that even
though you have innocently defined only one. The answer to that mystery lies in
the `settings.py` file under `INSTALLED_APPS`.

As I told you before, Django itself comes with a few apps pre-installed and
those have their own models defined. When you ran the syncdb for the first
time, the tables corresponding to all those models got created.

Specify the superuser and let's move on.


11. Introducing the ORM functions
---------------------------------

Let's drop down to the shell and play around with the ORM.

```python
$ python manage.py shell
>>> import datetime
>>> date = "Wed Mar 03 22:23:57 +0000 2010"
>>> created_at = datetime.datetime.strptime(date,'%a %b %d %H:%M:%S +0000 %Y')
>>> Tweet.objects.create(hashtag = "#pyconireland", author = "Batman",
created_at = created_at, text = "Sometimes words are hard to find")
>>> Tweet.objects.all()
[<Tweet: Tweet object>]
>>> Tweet.objects.create(hashtag = "#pyconireland", author = "Superman",
created_at = created_at, text = "Greatest detective")
<Tweet: Tweet object>
>>> Tweet.objects.all()
[<Tweet: Tweet object>, <Tweet: Tweet object>]
>>> Tweet.objects.filter(author = "Batman")
[<Tweet: Tweet object>]
>>>
```

12. Receiving input from the user
---------------------------------
