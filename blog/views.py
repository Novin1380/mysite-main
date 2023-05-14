from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone

# Create your views here.

def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by('-published_date')

    Post.status = True
    posts = Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by('-published_date')
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
    
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your comment didnt submiter')
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
    post.counted_views += 1
    post.save()
    if Post.objects.filter(pk=pid+1).exists():
            has_next=True
    else:
            has_next=False
    if Post.objects.filter(pk=pid-1).exists():
            has_previous=True
    else:
            has_previous=False
    next_pid=pid+1
    previous_pid=pid-1
    
    if not post.login_require:
        comments = Comment.objects.filter(post=post.id,approved=True)
        form = CommentForm()
        posts=get_object_or_404(Post,pk=pid,status=1)
        context={'post':posts,'pid':pid,'has_next':has_next,'has_previous':has_previous,'next_pid':next_pid,'previous_pid':previous_pid,'comments':comments,'form':form}
        return render(request,'blog/blog-single.html',context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))


def blog_search(request):
    #print(request.__dict__)
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        #print(request.GET.get('s'))
        # if s := request.GET.get('s'): #use this method only when your using python version 3.8 and above
        if request.GET.get('s'):
            s =  request.GET.get('s')
            posts = posts.filter(content__contains=s)
    
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def post_details(request,pid):
    posts = Post.objects.all()
    post = get_object_or_404(posts,pk=pid) 
    post.counted_views += 1
    post.save()
    if post.published_date <= timezone.now():
        post.status = True
    else :
        post.status = False
    next_post = post.get_next_by_id()
    if next_post:
        next_post_id=next_post.id
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

'''def next_post(request,pid):
    current_post = Post.objects.get(pk=pid)
    nextpost= Post.objects.filter(pid__gt=current_post.id).order_by('id').first()
    #next_post = get_object_or_404(pk=pid+1)
    context = {'posts':next_post,'current_post':current_post}
    print(next_post)
    if next_post is not None :
        return HttpResponseRedirect(reverse('blog/blog-single'))
    else :
        return HttpResponseRedirect(reverse('accounts:login'))'''
    
    
def test(request):
    return render(request,'test.html')

'''def post_list_view(request):
    post_list=Post.objects.all()
    paginator = paginator(post_list,1)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request,'blog/blog-single.html',context)'''

'''def next_prev(request ,pid):
    posts= Post.objects.filter(status=1).order_by("published_date")
    Posts = posts.objects.get(pid=id)
    nextpost = Posts -1
    #nextpost= Post.objects.filter(pid__gt=posts.id).order_by('id').first()
    prevpost= Post.objects.filter(pid__lt=pid).order_by('pid').last()
    context = {'posts':Posts , 'nextpost':nextpost , 'prevpost':prevpost }
    return render(request,'blog/blog-single.html',context)'''

'''def previous_post_view(request, pid):
    previous_post = Post.objects.filter(pid__lt=pid).order_by('pid').last()
    context= {'previous_post':previous_post}
    return render(request,'blog/blog-single.html',context)'''

    




