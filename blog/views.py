from django.shortcuts import render, get_object_or_404

from .models import Blog  # from the files models that we have in this folder, import the JOB one


def allblogs(request):
    # defining a 'blog_entries' variable : where "Blog.objects" is getting all the blog entries from the DB,
    # and will turn them in Python objects, to be available in the code, later . . .
    blogs = Blog.objects  #

    # . . . , or the 'blog_entries' can be passed forward when calling this 'allblogs' function , through a dictionary :
    return render(request, 'blog/allblogs.html', {'blogs': blogs})


def detail(request, blog_id):
    # a function that look to find a blog_id,
    # if it gets it, then it will go to DB and ask for all the details of it from DB(PostgreSQL),
    # if not , the function will return a '404 page'

    # first we will define a variable :
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})
