
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.post_list, name='post_list'), # Home HTML
    path('post', views.post_info, name='post_info'), # 메인 페이지 HTML
    path('Chopsticks', views.Chopsticks, name='Chopsticks'), # 쇠젓가락 데이터 값 시각화 HTML
    path('VacuumChopsticks', views.VacuumChopsticks, name='VacuumChopsticks'), #진공 젓가락 데이터 값 시각화 HTML
    path('SEN0114', views.SEN0114, name='SEN0114'), # SEN0114 데이터 값 시각화 HTML
    path('FC_28', views.FC_28, name='FC_28'), # FC-28 데이터 값 시각화 HTML
    path('ChopGraph', views.ChopGraph, name='ChopGraph'), # 쇠젓가락 그래프 구현 HTML
    path('VacuumGraph', views.VacuumGraph, name='VacuumGraph'), # 진공 젓가락 그래프 구현 HTML
    path('SenGraph', views.SenGraph, name='SenGraph'), # SEN0114 그래프 구현 HTML
    path('FC_28Graph', views.Fc_28Graph, name='FC_28Graph'), # FC-28 그래프 구현 HTML
    path('export/xls/', views.export_users_xls, name='export_users_xls'), # 엑셀로 데이터 값 추출 경로
    path('api/result/', views.ResultAPIView.as_view(), name="result_api"),
    path('result/', views.result_detail, name='result_detail'),
    path('test/', views.test, name='test'),
   # path('humid_new', views.humid_new, name='humid_new') # pagenation을 위한 url 경로
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)