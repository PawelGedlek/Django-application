from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Movie, Comment
from .forms import CommentForm

def film_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    movies = Movie.objects.filter(after_premiere=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        movies = Movie.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'movies': movies
    }
    return render(request, 'films/film/list.html', context)


def film_detail(request, id, slug):
    movie = get_object_or_404(Movie, id=id, slug=slug, after_premiere=True)
    context = {
        'movie': movie
    }
    return render(request, 'films/film/detail.html', context)


from .models import Comment
from .forms import CommentForm

def index(request):
    comments = Comment.objects.order_by('-date_added')

    context = {'comments' : comments}

    return render(request, 'films/film/detail.html', context)

def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return redirect('index')

    else:
        form = CommentForm()

    context = {'form' : form}
    return render(request, 'films/sign.html', context)