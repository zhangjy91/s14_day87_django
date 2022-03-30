from rest_framework.serializers import ModelSerializer

from app03.models import Fruit

class FruitSerializers(ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'
