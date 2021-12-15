from django.shortcuts import render

posts = [
    {
        'author': 'Gimmione',
        'title': 'Blog Post 1',
        'content': 'Gimmione the first',
        'date_posted': 'December 12, 2021'
    },
      {
        'author': 'Gino Fettuccia',
        'title': 'Blog Post 2',
        'content': 'I am Gino',
        'date_posted': 'December 14, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
