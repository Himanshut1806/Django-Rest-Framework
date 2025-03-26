from rest_framework import serializers
from .models import Person, Color

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id','color_name']

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer(read_only=True)
    color_info = serializers.SerializerMethodField()
    

    class Meta:
        model = Person 
        fields = '__all__'

    def get_color_info(self, obj): 
        if obj.color: 
            return {'color_name': obj.color.color_name}
        return None

    def validate(self, data):
        special_characters = "!@#$%^&*()_+,<>/"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError('Name cannot contain special characters')
        
        # if 'age' in data and data['age'] < 18: 
        #     raise serializers.ValidationError('Age should be greater than or equal to 18')
        return data

