# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import Student


# Create a model serializer
class StudentSerializer(serializers.ModelSerializer):
    # specify model and fields
    # these fields will be serialized
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error':'age cant be less than 18'})

        # else no exception is raised just pass data
        return data
