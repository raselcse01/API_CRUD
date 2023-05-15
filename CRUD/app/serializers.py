from rest_framework import serializers
from app.models import Student


# viewset er jonnno------------------
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'email', 'address']
        # fields = __file__ //all data send kore 


# model serializers------------------------
# model serializers hyperlink 2 ta ak sathe kora owner line ta hyperlink er and field e url nad owner add hoyece link er jonno
# class StudentSerializer(serializers.HyperlinkedModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     class Meta:
#         model = Student
#         fields = ['name', 'email', 'address', 'url', 'owner']
        # fields = __file__ //all data send kore 


# class base serializers------------------------
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     address = serializers.CharField(max_length=100)
#     # image = serializers.ImageField(upload_to='image')

#     def create(self, validated_data):       
#         return Student.objects.create(validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.address = validated_data.get('address', instance.address)
#         #instance.image = validated_data.get('image', instance.image)
#         instance.save()
#         return instance
    


# power shel value import commande-------------------
# python manage.py shell
# from app.models import Student
# from app.serializers import StudentSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

# serializer = StudentSerializer(a)
# serializer.data

# from app.serializers import StudentSerializer
# serializer = StudentSerializer()
# print(repr(serializer))