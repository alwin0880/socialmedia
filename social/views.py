from django.shortcuts import render,redirect

from social.forms import RegistrationForm,LoginForm,AddPostForm,ProfileUpdateForm,AddStoryForm
from django.views.generic import CreateView,TemplateView,FormView,ListView,DetailView,UpdateView
from social.models import MyUser,Posts,Comments,Storys
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
# from django.contrib import messages
from django.utils.decorators import method_decorator

# Create your views here.

def signin_reqired(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


@method_decorator(signin_reqired,name='dispatch')
class AddpostView(CreateView):
    template_name='addpost.html'
    model=Posts
    form_class=AddPostForm
    success_url=reverse_lazy('index')
    
    def form_valid(self, form):                     #database ke save cheyunnene mumbe form ke enthaghilum attribute add cheyanaghil form_valid enna methode over ride cheytha mathi
        form.instance.user=self.request.user
        # message-post added succesfully
        return super().form_valid(form)

    
@method_decorator(signin_reqired,name='dispatch')
class IndexView(ListView):
    template_name='home.html'
    model=Posts
    context_object_name='post'

    def get_queryset(self):              #query set le enthaghilum change cheyanaghil get_queryset enna method override cheytha mathi
        return Posts.objects.all().order_by("-post_date")    




@method_decorator(signin_reqired,name='dispatch')
class ExploreView(ListView):
    template_name='explore.html'
    model=Posts
    context_object_name='explore'

    def get_queryset(self):             
        return Posts.objects.all().exclude(user=self.request.user) 

@signin_reqired  
def searchbar(request):
    if request.method=='GET':
        search=request.GET.get("search")
        post=MyUser.objects.all().filter(username=search)
        return render(request,"searchbar.html",{"post":post})



class RegistrationView(CreateView):
    form_class=RegistrationForm
    model=MyUser
    template_name='register.html'
    success_url=reverse_lazy('signin')

class Loginview(FormView):
    form_class=LoginForm
    template_name='login.html'
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect('addpost')
            else:
                return render(request,self.template_name,{'form':form})

@method_decorator(signin_reqired,name='dispatch')
class PostDetailsView(DetailView):
    model=Posts
    template_name='postdetail.html'
    pk_url_kwarg='id'
    context_object_name='post'

@signin_reqired
def addcomment_view(request,*args,**kwargs):
    pid=kwargs.get('id')
    post=Posts.objects.get(id=pid)
    comment=request.POST.get('comments')
    Comments.objects.create(user=request.user,comment=comment,post=post)
    return redirect('index')

@signin_reqired
def like_view(request,*args,**kwargs):
    id=kwargs.get('id')
    pst=Posts.objects.get(id=id)
    pst.likes.add(request.user)
    pst.save()
    return redirect('index')



@method_decorator(signin_reqired,name='dispatch')
class MyProfileView(ListView):
    model=Posts
    template_name='profile.html'
    context_object_name='images'

    def get_queryset(self):
        return Posts.objects.filter(user=self.request.user)

@signin_reqired
def remove_post(request,*args,**kwargs):
    id=kwargs.get('id')
    Posts.objects.get(id=id).delete()
    return redirect('index')

@method_decorator(signin_reqired,name='dispatch')
class ProfileUpdateView(UpdateView):
    model=MyUser
    template_name="profile-update.html"
    form_class=ProfileUpdateForm
    pk_url_kwarg="id"
    success_url=reverse_lazy('myprofile')
    
    

@signin_reqired
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")
        



@method_decorator(signin_reqired,name='dispatch')
class AddStoryView(CreateView):
    template_name='addstory.html'
    model=Storys
    form_class=AddStoryForm
    success_url=reverse_lazy('index')
    
    def form_valid(self, form):                     
        form.instance.user=self.request.user
        # message-post added succesfully
        return super().form_valid(form)