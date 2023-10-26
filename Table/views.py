from django.shortcuts import render, HttpResponse
from .models import TableColumn, TableData, File
from django.db import migrations, models
from django.core import management
state = 1
# Create your views here.
def home(request):
        column_name = request.GET.get('name')
        global state
        if column_name == None:
            columns = TableColumn.objects.all()
            data = TableData.objects.all()
            files = File.objects.all()
            return render(request, 'Table.html', {'columns': columns, 'data': data, 'files': files})

        else:
            columns = TableColumn.objects.all()
            if state == 1:
                data = TableData.objects.filter(column=column_name).order_by('data')
                state = 0
            else:
                data = TableData.objects.filter(column=column_name).order_by('-data')
                state = 1
            files=[]
            for dat in data:
                files.append(dat.file)
            new_files =File.objects.all()
            for dat in new_files:
                if dat not in files:
                    files.append(dat)
            data = TableData.objects.all()
            return render(request, 'Table.html', {'columns': columns, 'data': data, 'files': files})


