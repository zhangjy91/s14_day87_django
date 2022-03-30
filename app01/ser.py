from rest_framework.serializers import ModelSerializer
from app01.models import Book

class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        # fields = "__all__"
        exclude = ('name',)


from rest_framework import serializers
from rest_framework.exceptions import ValidationError


def check_author(data):
    if data.startswith('sb'):
        raise ValidationError('作者不能以sb开头')
    else:
        return data


class BookSerializer(serializers.Serializer):
    nid = serializers.CharField(max_length=5, read_only=True)
    name = serializers.CharField(max_length=5)
    price = serializers.DecimalField(max_digits=5,decimal_places=2)
    author = serializers.CharField(max_length=5,validators=[check_author])


    def validate_price(self, data):
        if float(data) > 10:
            return data
        else:
            raise ValidationError('价格太低 ')


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.price = validated_data.get('price')
        instance.author = validated_data.get('author')
        instance.save()
        return instance

    def create(self, validated_data):
        instance = Book.objects.create(**validated_data)
        return instance