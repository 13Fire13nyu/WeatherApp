from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import WeatherTable
from .resources import WeatherResource
from django.contrib import messages
from tablib import Databook
from django.db.models import DateTimeField, Q
import datetime as DT


year_choice = []
for i in range(2010,2014):
    year_choice.append(str(i))
    
month_choice = ['Январь','Февраль',
            'Март','Апрель',
            'Май','Июнь',
            'Июль','Август',
            'Сентябрь','Октябрь',
            'Ноябрь','Декабрь']
                    


def index(request):
    return render(request, 'weather/index.html')
    
def table(request):
    
    data = WeatherTable.objects.all().order_by('date_time')
    answer_year = None
    answer_month = None

    answer_year = request.GET.get('Year')
    answer_month = request.GET.get('Month')
                
    if answer_year != None:

        if answer_month!=None:
            
            for i in range(12):
                if month_choice[i] == request.GET.get('Month'):
                    answer_month = i+1
                    break
        #print('ANSWER_MONTH: ', answer_month)
            queryset = WeatherTable.objects.filter(
                                                    Q(date_time__year=answer_year),
                                                    Q(date_time__month=answer_month)
                                                    ).order_by('date_time')
        else:
            queryset = WeatherTable.objects.filter(date_time__year=answer_year).order_by('date_time')
    else:
        queryset = data

    context = {
        'data': queryset,
        'Year': year_choice,
        'Month': month_choice,
    }


    return render(request, 'weather/table.html', context)
    
def download(request):
    #WeatherTable.objects.all().delete() # Чтобы при необходимости удалить все данные из бд
    try:
        if request.method == 'POST':
            weather_resource = WeatherResource()
            databook = Databook()
            new_weather = request.FILES['document']
            
            if not new_weather.name.endswith('xlsx'):
                message.info('wrong format')
                return render(request,'weather/download.html')
            
            imported_data = databook.load(new_weather.read(),format = 'xlsx')
            for dataset in imported_data.sheets():
                data_list = []
                del dataset[0:3]
                for data in dataset:
                    value = WeatherTable()
                    d = DT.datetime.strptime(data[0],'%d.%m.%Y').date() #data[0]
                    t =  DT.datetime.strptime(data[1],'%H:%M').time()# data[1]
                    value.date_time = DT.datetime.combine(d,t)
                    value.t = data[2]
                    value.ran = data[3]
                    value.td = data[4]
                    value.atm_pres = data[5]
                    value.wind_dir = data[6]
                    value.wind_speed = data[7]
                    value.cloudiness = data[8]
                    value.h = data[9]
                    value.vv = data[10]
                    value.wconditions = data[11]
                    data_list.append(value)
                    #value.save()
                WeatherTable.objects.bulk_create(data_list) # Добавление данных в БД
            

    except Exception:
        print('Какая-то ошибка')
        

    return render(request,'weather/download.html')
    
