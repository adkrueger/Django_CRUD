from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .forms import PostForm
from .models import Post

# Home view for posts, displayed in a list
class IndexView(ListView):
    template_name = 'crud_app/index.html'
    context_object_name = 'post_list'
    
    def get_queryset(self):
        return Post.objects.all()

# Detail view (view post detail)
class PostDetailView(DetailView):
    model = Post
    template_name = 'crud_app/post-detail.html'

# New post view (create a new post)
def postview(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    
    form = PostForm()
    return render(request, 'crud_app/post.html', {'form': form})

# Edit a post        
def edit(request, pk, template_name='crud_app/edit.html'):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request, template_name, {'form': form})

# Delete a post
def delete(request, pk, template_name='crud_app/confirm_delete.html'):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    
    return render(request, template_name, {'object': post})
