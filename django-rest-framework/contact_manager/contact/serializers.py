# Introduction to serializer
from rest_framework import serializers
from contact.models import Contact


# class ContactSerializer(serializers.Serializer):
#     id = IntegerField(label='ID', read_only=True)
#     name = CharField(allow_blank=True, max_length=100, required=False)
#     number = IntegerField(required=False)

#     def create(self, validated_data):
#         """
#         Create and return a new `Contact` instance, given the validated data.
#         """
#         return Contact.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Contact` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.title)
#         instance.number = validated_data.get('number', instance.code)
#         instance.save()
#         return instance


# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = ('id', 'name', 'number')

        

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
