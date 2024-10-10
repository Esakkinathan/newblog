from typing import Any, Dict
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm,EditForm,CommentForm,CategoryForm
from .models import Post,Category,Comment
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']
    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        post_count = Post.objects.all().count()
        user_count = User.objects.all().count()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context['user_count'] = user_count
        context['post_count'] = post_count
        context['cat_menu'] = cat_menu
        return context
class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_detail.html"

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        stuffs = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuffs.total_likes()
        liked =False
        print(self.request.user.id)
        if stuffs.likes.filter(id=self.request.user.id).exists():
            liked = True
        else:
            liked = False
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    #fields = '__all__'
    #fields = ["title","author","body"]

class UpdatePostView(UpdateView):
    model=Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ["title","title_tag","body"]

class DeletePostView(DeleteView):
    model=Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCatergoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "add_category.html"

def CategoryView(request,cats):
    temp=cats.replace('-',' ')
    category_posts = Post.objects.filter(category=temp).order_by('-post_date')
    print(category_posts)
    return render(request,'category.html',{'cats':temp.title(),'category_posts':category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})

def LikeView(request,pk):
    liked = False
    #post = get_object_or_404(Post,id=request.POST.get('post_id'))
    post = get_object_or_404(Post, id=pk)
    #print(request.user.id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = True
    else:
        post.likes.add(request.user)
        liked = False
    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    post.save()
    return HttpResponseRedirect(reverse('article_detail', kwargs={'pk': pk}))
    #return HttpResponseRedirect(reverse('article_detail', kwargs={'pk': pk}))
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    def form_valid(self,form):
        form.instance.post_id= self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')
def add_comment(request):
    if request.method == "POST" :
        postname = request.POST['postname']
        cmtname = request.POST['commentname']
        cmtbody = request.POST['commentbody']
        cmtdata= Comment(post_id=postname,name_id=cmtname,body=cmtbody)
        cmtdata.save()
        return HttpResponseRedirect(reverse("article_detail",args=[str(postname)]))
def search_box(request):
    if request.method == "POST" :
        searched = request.POST['searched']
        print(searched)
        posts= Post.objects.filter(title__icontains=searched).order_by('-post_date')
        users= User.objects.filter(Q(first_name__icontains=searched) | Q(username__icontains=searched) | Q(last_name__icontains=searched) )
        return render(request,'search.html',{
            'searched':searched,
            'posts':posts,
            'users':users
            })
    return render(request,'search.html',{})

def delete_comment(request,id):
    com=Comment.objects.get(pk=id)
    if request.user.id == com.name.id :
        com.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    