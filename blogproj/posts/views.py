from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User 
from .models import Post
from .forms import PostForm

"""def Home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/home.html', {'posts': posts})

def Detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author_id = request.POST.get('author_id')
        
        author = Author.objects.get(id=author_id)
        Post.objects.create(title=title, author=author, content=content)
        return redirect('home')
    
    # ✅ GET request - yahan authors bhejo
    authors = Author.objects.all()
    return render(request, 'posts/create_form.html', {'authors': authors})

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author_id = request.POST.get('author_id')
        
        post.title = title
        post.content = content
        if author_id:
            post.author = Author.objects.get(id=author_id)
        post.save()
        return redirect('detail', post_id=post.id)
    
    # ✅ GET request - authors bhejo
    authors = Author.objects.all()
    return render(request, 'posts/edit_form.html', {'post': post, 'authors': authors})

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    return render(request, 'posts/delete_confirm.html', {'post': post})
    """

#-----------------------------------
# Class Base Views 
#------------------------------------
class PostListView(ListView): #all posts
    model=Post
    template_name='posts/home.html'
    context_object_name='posts'

    def get_queryset(self):
        queryset=Post.objects.all()
        #search ki querry
        search=self.request.GET.get('search') #search 
        if search:
            queryset=queryset.filter(title__icontains=search)
            #auther search 
        author_id = self.request.GET.get('author')
        if author_id:
            queryset = queryset.filter(author_id=author_id)    

        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = User.objects.all()
        return context

class PostDetailView(DetailView): #1 post
    model=Post
    template_name='posts/detail.html'
    context_object_name='post'

class PostCreateView(LoginRequiredMixin,CreateView): #creade post
    model=Post
    #fields=['title', 'content']
    form_class=PostForm
    template_name='posts/create_form.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form):  
        form.instance.author = self.request.user
        return super().form_valid(form)

    

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model=Post
    #fields=['title', 'content'] 
    form_class=PostForm
    template_name='posts/edit_form.html'
    success_url=reverse_lazy('home')

    def get_queryset(self):  
        if self.request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(author=self.request.user)

   

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    template_name='posts/delete_confirm.html'
    success_url=reverse_lazy('home') 

    def get_queryset(self):  
        if self.request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(author=self.request.user)   
