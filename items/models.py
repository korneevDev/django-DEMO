from django.db import models

from rest_framework import serializers, viewsets
from rest_framework.routers import DefaultRouter

#Модель
class Tovar(models.Model):
    articul = models.CharField(max_length=10, primary_key=True) # "articul" VARCHAR(10) NOT NULL PRIMARY KEY,
    name = models.CharField(max_length=50)
    ed_inz = models.CharField(max_length=10)
    price = models.IntegerField(default=0) # "price" INTEGER NOT NULL,
    postavshic = models.CharField(max_length=100)
    proizvoditel = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    skidka = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    description = models.TextField()
    photo = models.CharField(max_length=50, default='picture.png')
#Сериализатор
class TovarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tovar
        fields = '__all__'
#Вьюсет
class TovarViewSet(viewsets.ModelViewSet):
    queryset = Tovar.objects.all()
    serializer_class = TovarSerializer
#Роутер
router = DefaultRouter()
router.register('', TovarViewSet)
urlpatterns = router.urls



