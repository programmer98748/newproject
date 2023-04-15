from django.urls import path
from . import views
from website.account import authview
urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('collections/', views.collections, name='collections'),
    path('collections/<slug:slug>/', views.collectionsviews, name='collectionsviews'),
    path('collections/<slug:cate_slug>/<slug:prod_slug>/', views.productview, name='productview'),


    path('register/', authview.register, name='register'),
    path('login/', authview.loginpage, name='login'),
    path('logout/', authview.logoutpage, name='logout'),

]