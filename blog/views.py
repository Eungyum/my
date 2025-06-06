from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .models import Post, Comment
import json

# Create your views here.
def root(request):
    query = request.GET.get('q', '')
    
    if query:
        post_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
            # Q(category__name__icontains=query) | Q(tags__name__icontains=query)
        ).order_by('-created_at').distinct()
    else:
        post_list = Post.objects.all().order_by('-created_at')
    
    # 페이지네이션
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj': page_obj, 'query':query}
    
    return render(request, 'blog.html', context)

def detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    comments = post.comments.filter(is_visible=True).order_by('-created_at')
    context = {'post':post, 'comments':comments}
    return render(request, 'blog-detail.html', context)

def create_comment(request):
    if request.method == "POST":
        author = request.POST.get('author')
        author_email = request.POST.get('author_email')
        pw = request.POST.get('pw')
        content = request.POST.get('content')
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        Comment.objects.create(
            post=post,
            author = author,
            author_email = author_email,
            pw=pw,
            content=content,
            is_visible=True
        )
        return redirect('blog_detail', pk=post.id)
    
@csrf_exempt
def delete_comment(request):
    if request.method == "POST":
        comment_id = request.POST.get('comment_id')
        author_email = request.POST.get('author_email')
        pw = request.POST.get('pw')
        post_id = request.POST.get('post_id')

        comment = get_object_or_404(Comment, id=comment_id)

        if (author_email != comment.author_email) or (pw != comment.pw):
            messages.error(request, "이메일 또는 비밀번호가 일치하지 않습니다.")
            return redirect('blog_detail', pk=post_id)

        comment.is_visible = False
        comment.save()
        messages.success(request, "댓글이 성공적으로 삭제되었습니다.")
        return redirect('blog_detail', pk=post_id)

    return redirect('/')