import profile
import xlwt
import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post,humiditysensor, sensor
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
import datetime
#from .forms import HumidForm

# Create your views here
from django.http.response import HttpResponseRedirect

# # Create your views here.
# def index(request)
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     # context에 모든 어린이 정보를 저장
#     return render(request, 'blog/post_list.html', context)
#     # context안에 있는 어린이 정보를 index.html로 전달

start_date = '2020-09-07 05:50'
end_date = '2020-11-21 01:50'

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts' : posts})


def post_info(request):
    return render(request, 'post_info.html')



def Chopsticks(request):
    date = request.GET.get('date')
    page = request.GET.get('page')  # 페이지 번호 알아오기
    # Sensor = sensor.objects.all()
    '''
    form을 이용해서 html 페이지에서 views.py로 값 전달
    date에 전달받은 날짜 값 저장 후 해당 날짜를 기준으로 값 검색
    '''
    if date is not None:
        target_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        HumiditySensor = humiditysensor.objects.filter(s_name="1", s_date__contains=target_date)
    else:
        HumiditySensor = humiditysensor.objects.filter(s_name="1", s_date__range=[start_date, end_date])
    # HumiditySensor = humiditysensor.objects.filter(s_name="1", s_date__range=[start_date, end_date])
    # HumiditySensor = humiditysensor.objects.filter(s_name="1", s_date__contains=target_date)

    # context = {'HumiditySensor' : HumiditySensor, 'Sensor' : Sensor}
    paginator = Paginator(HumiditySensor, 20000) # %개씩 잘라내기

    posts = paginator.get_page(page) #페이지 번호 인자로 넘겨주기
    # context = {'HumiditySensor': HumiditySensor, 'Sensor' : Sensor, 'posts' : posts}
    context = {'HumiditySensor': HumiditySensor, 'posts': posts}
    return render(request, 'Chopsticks.html', context)

def VacuumChopsticks(request):
    date = request.GET.get('date')
    page = request.GET.get('page')
    #Sensor = sensor.objects.all()

    if date is not None:
        target_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        HumiditySensor = humiditysensor.objects.filter(s_name="2", s_date__contains=target_date)

    else:
        HumiditySensor = humiditysensor.objects.filter(s_name="2", s_date__range=[start_date, end_date])

    paginator = Paginator(HumiditySensor, 20000)
    posts = paginator.get_page(page)
    # context = {'HumiditySensor' : HumiditySensor, 'Sensor' : Sensor}
    context = {'HumiditySensor': HumiditySensor, 'posts':posts}
    return render(request, 'FC_28.html', context)

def SEN0114(request):
    date = request.GET.get('date')
    page = request.GET.get('page')
    # Sensor = sensor.objects.all()
    if date is not None:
        target_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        HumiditySensor = humiditysensor.objects.filter(s_name="3", s_date__contains=target_date)

    else:
        HumiditySensor = humiditysensor.objects.filter(s_name="3", s_date__range=[start_date, end_date])

    paginator = Paginator(HumiditySensor, 20000)
    posts = paginator.get_page(page)
    # context = {'HumiditySensor' : HumiditySensor, 'Sensor' : Sensor}
    context = {'HumiditySensor': HumiditySensor, 'posts':posts}
    return render(request, 'SEN0114.html', context)

def FC_28(request):
    date = request.GET.get('date')
    page = request.GET.get('page')
    #Sensor = sensor.objects.all()

    if date is not None:
        target_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        HumiditySensor = humiditysensor.objects.filter(s_name="4", s_date__contains=target_date)
    else:
        HumiditySensor = humiditysensor.objects.filter(s_name="4", s_date__range=[start_date, end_date])

    paginator = Paginator(HumiditySensor, 20000)
    posts = paginator.get_page(page)
    context = {'HumiditySensor':HumiditySensor, 'posts':posts}

    # context = {'HumiditySensor' : HumiditySensor, 'Sensor' : Sensor}
    return render(request, 'FC_28.html', context)

def ChopGraph(request):
    date = request.GET.get('date')
    page = request.GET.get('page')  # 페이지 번호 알아오기
    #Sensor = sensor.objects.all()

    '''
    if date is not None:
        target_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        HumiditySensor = humiditysensor.objects.filter(s_name="1", s_date__contains=target_date)

    else:
        HumiditySensor = humiditysensor.objects.filter(s_name="1", s_date__range=[start_date, end_date])
    
    

    paginator = Paginator(HumiditySensor, 17280)  # %개씩 잘라내기
    posts = paginator.get_page(page)  # 페이지 번호 인자로 넘겨주기

    data_list = []
    '''
    '''
    if date is not None:
        target_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        chop_date_list_qry = humiditysensor.objects.values_list('s_date', flat=True).filter(s_name_id=1, s_date__contains=target_date)
        chopsticksGraph = list(humiditysensor.objects.values_list('soil_humi', flat=True).filter(s_name_id=1, s_date__contains=target_date))
    else:
        chop_date_list_qry = humiditysensor.objects.values_list('s_date', flat=True).filter(s_name_id=1, s_date__range=[start_date, end_date])
        chopsticksGraph = list(humiditysensor.objects.values_list('soil_humi', flat=True).filter(s_name_id=1, s_date__range=[start_date, end_date]))
    '''
    chop_date_list_qry = humiditysensor.objects.values_list('s_date', flat=True).filter(s_name_id=1, s_date__range=[start_date, end_date], s_date__minute=30)

    #chop_date_list_qry = humiditysensor.objects.values_list('s_date', flat=True).filter(s_name_id=1, s_date__range=[start_date, end_date])
    date_list = []

    chopsticksGraph = list(humiditysensor.objects.values_list('soil_humi', flat=True).filter(s_name_id=1, s_date__range=[start_date, end_date], s_date__minute=30))
    VacuumGraph = list(humiditysensor.objects.values_list('soil_humi', flat=True).filter(s_name_id=2,
                                                                                             s_date__range=[start_date,
                                                                                                            end_date],
                                                                                             s_date__minute=30))
    SEN0114Graph = list(humiditysensor.objects.values_list('soil_humi', flat=True).filter(s_name_id=3,
                                                                                             s_date__range=[start_date,
                                                                                                            end_date],
                                                                                             s_date__minute=30))
    FC_28Graph = list(humiditysensor.objects.values_list('soil_humi', flat=True).filter(s_name_id=4,
                                                                                             s_date__range=[start_date,
                                                                                                            end_date],
                                                                                             s_date__minute=30))

    #chopsticksGraph = list(humiditysensor.objects.values_list('soil_humi', flat=True).filter(s_name_id=1, s_date__range=[start_date, end_date]))

    chopsticksGraph.append(0)
    chopsticksGraph.append(1000)

    for date in chop_date_list_qry:
        date_list.append(str(date.isoformat()))

    date_list = json.dumps(date_list)
    # context = {'HumiditySensor': HumiditySensor, 'posts':posts}
    return render(request, 'ChopGraph.html', {'date_list': date_list, 'chopsticksGraph': chopsticksGraph, 'VacuumGraph':VacuumGraph, 'SEN0114Graph':SEN0114Graph, 'FC_28Graph':FC_28Graph})

def VacuumGraph(request):
    #Sensor = sensor.objects.all()
    #HumiditySensor = humiditysensor.objects.filter(s_name="2")
    #context = {'HumiditySensor': HumiditySensor, 'Sensor' : Sensor}
    #date_list_qry = humiditysensor.objects.values_list('s_date', flat=True).filter(s_name_id=2)

    date_list_qry = humiditysensor.objects.values_list('s_date', flat=True).filter(s_name_id=2,
                                                                                   s_date__range=[start_date, end_date],
                                                                                   s_date__minute=30)
    date_list = []

    VacuumGraph= list(humiditysensor.objects.values_list('soil_humi', flat=True).filter(s_name_id=2,
                                                                                        s_date__range=[start_date,
                                                                                                       end_date],
                                                                                        s_date__minute=30))

   #VacuumGraph = list(humiditysensor.objects.values_list('soil_humi', flat=True).filter(s_name_id=2))
    VacuumGraph.append(0)
    VacuumGraph.append(1000)

    for date in date_list_qry:
        date_list.append(str(date.isoformat()))
    date_list = json.dumps(date_list)
    return render(request, 'VacuumGraph.html', {'date_list': date_list, 'VacuumGraph': VacuumGraph})

def SenGraph(request):
    #Sensor = sensor.objects.all()
    #HumiditySensor = humiditysensor.objects.filter(s_name="3")
    #context = {'HumiditySensor': HumiditySensor, 'Sensor' : Sensor}
    #date_list_qry = humiditysensor.objects.values_list('s_date', flat=True).filter(s_name_id=3)
    #date_list = []
    data_list = []

    date_list_qry = humiditysensor.objects.values_list('s_date', flat=True).filter(s_name_id=3,
                                                                                   s_date__range=[start_date, end_date],
                                                                                   s_date__minute=30)
    date_list = []

    SenGraph = list(humiditysensor.objects.values_list('soil_humi', flat=True).filter(s_name_id=3,
                                                                                        s_date__range=[start_date,
                                                                                                       end_date],
                                                                                        s_date__minute=30))

    #SenGraph = list(humiditysensor.objects.values_list('soil_humi', flat=True).filter(s_name_id=3))
    SenGraph.append(0)
    SenGraph.append(1000)
    for date in date_list_qry:
        date_list.append(str(date.isoformat()))
    date_list = json.dumps(date_list)
    return render(request, 'SenGraph.html', {'date_list': date_list, 'SenGraph': SenGraph})

def Fc_28Graph(request):
    #Sensor = sensor.objects.all()
    #start_date = '2020-09-17 05:30'
    #end_date = '2020-09-27 05:30'
    #HumiditySensor = humiditysensor.objects.filter(s_name="4")
    #context = {'HumiditySensor': HumiditySensor, 'Sensor' : Sensor}
    # date_list_qry = humiditysensor.objects.values_list('s_date', flat=True).filter(s_name_id=4, s_date__range=[start_date, end_date], s_date__hour = 5, s_date__minute = 30)
    date_list_qry = humiditysensor.objects.values_list('s_date', flat=True).filter(s_name_id=4,
                                                                                   s_date__range=[start_date, end_date],
                                                                                   s_date__minute=30)
    date_list = []

    Fc_28Graph = list(humiditysensor.objects.values_list('soil_humi', flat=True).filter(s_name_id=4, s_date__range=[start_date, end_date], s_date__minute=30))
    Fc_28Graph.append(0)
    Fc_28Graph.append(1000)
    #context = {'HumiditySensor': HumiditySensor}
    for date in date_list_qry:
        date_list.append(str(date.isoformat()))
    date_list = json.dumps(date_list)
    return render(request, 'FC_28Graph.html', {'date_list': date_list, 'Fc_28Graph': Fc_28Graph})


#Export Excel
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    columns = ['시간', '데이터 값', '센서' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = humiditysensor.objects.filter(s_name="1").values_list('s_date', 'soil_humi', 's_name')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

# textfield에서 특정 날짜 검색을 위한 함수
#def humid_new(request):
#    form = HumidForm()
#    return render(request, 'blog/Chopsticks.html', {'form':form})

def create(request):
    profile.photo = request.FILES['photo']



class ResultAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        data = request.session.get('result')
        return Response(data)


def result_detail(request):
    context = {}
    return render(request, 'ChopGraph.html', context)

def test(request):
    return render(request, 'test.html')
## 지정한 MEDIA 파일 사용 ##
# <!-- 1번 -->
# <img src="{{ profile.photo }}" >
# <!-- 2번 -->
# <img src="{{ profile.photo.url }}" >
# <!-- 3번 -->
# <img src="{{ profile.photo.path }}" >

## 해당 photo 가 존재하지 않는다면 이는 경로를 찾지 못하는 오류 예방
# {% if profile.photo %}
#     <img src="{{ profile.photo.url }}" >
# {% endif %}
