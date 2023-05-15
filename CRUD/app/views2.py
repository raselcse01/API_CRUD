
# from django.shortcuts import get_object_or_404
# from app.serializers import StudentSerializer
# from rest_framework import viewsets
# from rest_framework.response import Response
# from app.models import Student
# from rest_framework import status


# class StudentViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Student.objects.all()
#         serializer = StudentSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         queryset = Student.objects.all()
#         student = get_object_or_404(queryset, pk=pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#     def update(self, request, pk=None):
#         student = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

