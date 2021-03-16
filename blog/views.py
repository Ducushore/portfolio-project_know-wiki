from django.http import Http404
from .models import Blog  # from the 'models' file from this folder, import 'Blog' objects (instances of 'Blog' class)
from django.shortcuts import render, get_object_or_404


def allblogs(request):  # intead of 'def allblogs(request, blog_id):'
    # # In order to show customized HTML when Django returns a 404, you can create an HTML template named 404.html and
    # # place it in the top level of your template tree. This template will then be served when DEBUG is set to False :
    # try:  # NEW-15.MAR.2021
    #     blogs = Blog.objects.get(pk=blog_id)
    # except Blog.DoesNotExist:
    #     raise Http404("Blog does not exist")

    # defining a 'blog_entries' variable : where "Blog.objects" is getting all the blog entries from the DB,
    blogs = Blog.objects  # and will turn them in Python objects, to be available in the code, later . . .

    # . . . , or the 'blog_entries' can be passed forward when calling this 'allblogs' function , through a dictionary :
    return render(request, 'blog/allblogs.html', {'blogs': blogs})  # where 'blogs' is the list of blog entries


def detail(request, blog_id):
    # A function that is looking over to find a 'blog_id' within the url provided; if identified (e.g. 1, 2),
    # then it will go to DB(PostgreSQL) and will ask for all the details corresponding to that specific 'blog_id'.
    # If nothing available for that id, the function will return a '404 page'

    # First we will define a variable that will be loaded with all the details of a blog-entry:
    detail_blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'blog/detail.html', {'blog': detail_blog})
    # where 'detail_blog' is the list of the details of each blog-entry
