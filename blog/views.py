from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
# Create your views here.
def post_list(request):
	posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def publish_list(request):
	latest_post = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'blog/post_list.html', {'latest_post':latest_post})

def post_detail(request, pk):
	post = get_object_or_404(Post, id = pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.publish_date = timezone.now()
			post.save()
			return redirect('post_detail',pk = post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html',{'form':form})

def post_edit(request, pk):
	post = get_object_or_404(Post, id=pk)
	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.save()
			return redirect('post_detail',pk = post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html',{'form':form})