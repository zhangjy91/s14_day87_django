from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    name = serializers.CharField(source='title')
    price = serializers.CharField()
    pub_date = serializers.DateField(source='test')
    publish = serializers.CharField()
    # authors = serializers.CharField()
    authors = serializers.SerializerMethodField()

    def get_authors(self,instance):
        authors = instance.authors.all()
        ll = []
        for author in authors:
            ll.append({'name':author.name, 'age':author.age})

        return ll

