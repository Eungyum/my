from django.shortcuts import render
from blog.models import Post

# Create your views here.
def root(request):
    posts = Post.objects.filter(is_index=True)
    context = {'posts':posts}
    return render(request, 'index-full.html', context)