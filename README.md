# Joeweb

Joeweb is an educational wsgi based python web framework
Its aim is to be simple enough to give everyone the ease of contributing to open source projects.
If you are willing to get your hands dirty, just join in

## how to contribute
- Read documents about wsgi
- Read simple bits of bottle [just the part you need to implement the feature you want]
- Then try to implement it.
- As much as you can, add tests. They should be simple. Remember, we are just learning
- And don't forget the comments, we need to know why you did what you did.
- You can always ask a question when you are stuck or file a bug.
- there are millions of bugs, and it is required of us to fix them the most we can.

## installation

    pip install git+https://github.com/Joetib/joeweb.git


### key tips:
    __slots__ are python's special class property that allows us to specify the variables it will have. Somehow it increases speed.

    request.Request keeps all the environ variables we need as a single class

    app.App is or base application class. It adds all the features together such as keep track of static variables and its __call__ function is the wsgi callable

    response.py holds various wsgi responses to abstract the details from the consumer. Such as handling file sending, plain text reponse, json, etc

    router.py holds the base class for managing registered paths and checking which ones they match
