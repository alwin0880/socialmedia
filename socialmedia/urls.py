"""socialmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from social import views
from django.conf import settings                      # run cheyumbo image display avan use these 2 (settings and static)lines of code
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('addpost/',views.AddpostView.as_view(),name='addpost'),
    path('home/',views.IndexView.as_view(),name='index'),
    path('register/',views.RegistrationView.as_view(),name='signup'),
    path('',views.Loginview.as_view(),name='signin'),
    path('post/<int:id>/',views.PostDetailsView.as_view(),name='postdetail'),
    path('post/<int:id>/add_comment/',views.addcomment_view,name='addcomment'),
    path('post/<int:id>/like/',views.like_view,name='like'),
    path('myprofile/',views.MyProfileView.as_view(),name='myprofile'),
    path("post/<int:id>/remove",views.remove_post,name='remove-post'),
    path('logout/',views.signout_view,name='logout'),
    path('search/',views.ExploreView.as_view(),name='explore'),
    path('update/<int:id>',views.ProfileUpdateView.as_view(),name='update'),
    # path("post/search/",views.SearchView.as_view(),name="search")
    path("searchbar/",views.searchbar,name="searchbar")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

