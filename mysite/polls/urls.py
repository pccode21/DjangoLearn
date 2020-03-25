from django.urls import path
from . import views

app_name = 'polls'  # 添加 app_name以设置命名空间URL名称
urlpatterns = [
                path('', views.index, name='index'),
                path('<int:question_id>/', views.detail, name='detail'),
                path('<int:question_id>/results/', views.results, name='results'),
                path('<int:question_id>/vote/', views.vote, name='vote'),
]
