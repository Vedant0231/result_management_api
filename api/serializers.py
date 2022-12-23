from rest_framework import serializers
from .models import Student

"""serializer for student data"""
class StudentSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=20)
    city = serializers.CharField(max_length=20)
    std = serializers.IntegerField()
    result = serializers.CharField(max_length=20)
    checkby = serializers.CharField(max_length=20)


    """create function create to post data"""
    def create(self, validation_data):

        return Student.objects.create(**validation_data)

    """create function update to put data"""
    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.std = validated_data.get('std', instance.std)
        instance.result = validated_data.get('result', instance.result)
        instance.checkby = validated_data.get('checkby', instance.checkby)

        instance.save()

        return instance
