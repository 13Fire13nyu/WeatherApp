from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadTableForm
from .models import WeatherTable, UploadTable
import pandas as pd
import re

year_choice = []
for i in range(2010,2014):
    year_choice.append(str(i))
month_choice = ['Январь','Февраль',
                'Март','Апрель',
                'Май','Июнь',
                'Июль','Август',
                'Сентябрь','Октябрь',
                'Ноябрь','Декабрь']                
month_choice_num = ['01','02','03','04','05',
                    '06','07','08','09','10',
                    '11','12'] 

def index(request):
    return render(request, 'weather/index.html')
    
def table(request):
    excel = UploadTable.objects.all()

    data = WeatherTable.objects.all()
    obj = []
    data_choice=[]
    for i in range(WeatherTable.objects.all().count()):
        obj.append(WeatherTable.objects.get(id=i+1))
    print('DATA: ')
    for a in obj:
        print(a.date)
    print('CHOICE: ')
    '''
    for a in obj:
        res = re.findall(r'\d{2}.\d{2}.(\d{4})', a.date)
        if res == ['2010']:
            print(a.date)
            data_choice.append(a)
    #data = WeatherTable.objects.filter(date = ['2010'])
    '''
    if request.GET.get('Year_ch'):
        print('YES')
        answer_year=request.GET.get('Year_ch')
        print([str(answer_year)])
        '''
        if request.GET.get('Month_ch'):
            answer_month=request.GET.get('Month_ch')
            for a in obj:
                res1 = re.findall(r'\d{2}.\d{2}.(\d{4})', a.date)
                res2 = re.findall(r'\d{2}.(\d{2}).\d{4}', a.date)
                # Переделаем название месяца из численного в словесное
                for i in range(len(month_choice_num)):
                    if res2 == [month_choice_num[i]]:
                        res2 = month_choice[i]
                        print(res2)
                if res1 == [str(answer_year)] and res2 == [str(answer_month)]:
                    print('res == answer_month and answer_year')
                    print(a.date)
                    data_choice.append(a)
        else:
        '''
        for a in obj:
            res = re.findall(r'\d{2}.\d{2}.(\d{4})', a.date)
            print('RES = ',res)
            if res == [str(answer_year)]:
                print('res == answer')
                print(a.date)
                data_choice.append(a)
    else:
        data_choice = WeatherTable.objects.all()
    context = {
        'data': data_choice,
        'Year': year_choice,
        'Month': month_choice,
    }


    return render(request, 'weather/table.html', context)
    
def download(request):
    try:
        if request.method == 'POST':
            form = UploadTableForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            '''    
            obj = []
            for i in range(UploadTable.objects.all().count()):
                obj.append(WeatherTable.objects.get(id=i+1))
            print('DATA: ')
            for a in obj:
                print(a.date)
            '''
        else:
            form = UploadTableForm()
        except Exception:
            print('НЕ ВЫШЛО')
            return render(request, 'weather/download.html')
    return render(request, 'weather/download.html', {'form': form})
    