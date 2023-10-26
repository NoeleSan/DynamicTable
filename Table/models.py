from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.
class TableColumn(models.Model):
    name = models.CharField(max_length=100)
    types = (
        ('Числовой','Числовой'),
        ('Строка','Строка'),
        ('Текст','Текст'),
        ('Дата','Дата'),
        ('Список','Список'),
    )
    type = models.CharField(max_length=20, choices=types, default='1')
    def __str__(self):
        return f"{self.name}({self.type})"
    class Meta:
        unique_together = ('name', 'type')

class File(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class TableData(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    column = models.ForeignKey(TableColumn, on_delete=models.CASCADE)
    data = models.TextField()

    def __str__(self):
        return f"{self.data} - {self.column.name}({self.column.type}) - {self.file.name}"
    
    class Meta:
        unique_together = ('column', 'file')
    
    def clean(self, *args, **kwargs):

        if self.column.type == 'Числовой' :
            if self.data.isdigit():
                super(TableData, self).clean(*args, **kwargs)
            else:
                raise ValidationError('Данные не являются числовыми')


        elif self.column.type == 'Строка' :
            print (len(self.data))
            if len(self.data) < 200 :
                super(TableData, self).clean(*args, **kwargs)
            else:
                raise ValidationError('Слишком большая строка')


        elif self.column.type == 'Дата' :
            pattern = r'^\d{4}-\d{2}-\d{2}$'
            if re.match(pattern, self.data):
                super(TableData, self).clean(*args, **kwargs)
            else:
                raise ValidationError('Данные не являются датой, попробуйте написать в виде гггг-мм-дд')


        elif self.column.type == 'Список' :
            pattern = r'^\([^)]*\)$'
            if re.match(pattern, self.data):
                super(TableData, self).clean(*args, **kwargs)
            else:
                raise ValidationError('Данные не являются списком, попробуйте написать в виде (1, 2, 3)')