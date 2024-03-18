from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DeleteView
from flat.models import Post
from flat.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import response, FileResponse, HttpResponse


def posts(request):
    search_query=request.GET.get("search","")
    if search_query:
        posts=Post.objects.filter(title__icontains=search_query)
    else:
        posts =Post.objects.all().order_by("id")
    all_images=Post.objects.all()
    return render(request, "posts.html", {"posts": posts,"all_images":all_images})


# Create your views here.

def posts_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "posts_view.html", {"post": post})


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # we dont save   it , unless we will add something
            post.custom_user = request.user
            post.save()
            form.save_m2m()
            return redirect("posts")
        else:
            return HttpResponse("something is wrong")
    else:
        form = PostForm()
    return render(request, "create.html", {"form": form})


def edit_post(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    if request.user !=post.custom_user:
        return redirect(f"/posts/{post_id}/")
    if request.method=="GET":
        form=PostForm(instance=post)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
        return redirect("posts")
    return render(request, "edit_post.html", {"form":form,"post": post})

class PostDeleteView(DeleteView):
    model=Post
    success_url = "/posts/<int:post_id>/"
    template_name="delete_post.html"


# Create your views here.
