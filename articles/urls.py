from django.urls  import path
from .import views

app_name = 'articles'

urlpatterns = [
	path(r'^$', views.article_list, name="list"),
	path(r'^create/$', views.article_create, name='create'),
	path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]
