from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DeleteView, CreateView
from flat.models import Post
from flat.forms import PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.http import response, FileResponse, HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from users.models import CustomUser


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



@permission_required(perm="flat.add_post", raise_exception=True)
def create( request):
  if request.method == "POST":
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit=False)  # we dont save   it , unless we will add something
                post.custom_user = request.user
                post.save()
                form.save_m2m()
                return redirect("posts")
            else:
                return redirect("posts")
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
    success_url = "posts"
    template_name="delete_post.html"


# Create your views here.
