from django.db import models
from django.contrib.postgres.fields import ArrayField


USE_TZ = False

class Platform(models.Model):
    Name = models.TextField(null=False)

class Table(models.Model):
    name = models.TextField(null=False)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

class Category(models.Model):
    Platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    Parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, related_name='subcategory')
    Name = models.TextField(null=False)
    Description = models.TextField()
    XML_Value = models.TextField(null=False)
    Table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)

class Cell(models.Model):
    NUMBER = 1
    TEXT = 2
    MULTIPLE = 3
    DATE = 3
    BOOL = 4
    FEELD_TYPE_CHOICES = [
        (NUMBER, "Число"),
        (TEXT, "Текст"),
        (MULTIPLE, "Несколько значений"),
        (DATE,"Дата"),
        (BOOL, "Логическое")
    ]
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    cellName = models.TextField(null=False)
    info = models.TextField()
    xmlValue = models.TextField()
    dataType = models.IntegerField(choices=FEELD_TYPE_CHOICES)
    values = ArrayField(models.TextField())
    max_len = models.IntegerField()
    fieldForDisplay = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    valueForDisplay = models.TextField()
