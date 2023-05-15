# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from app.models import Student
# from app.serializers import StudentSerializer

# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view

# from django.http import Http404
# from rest_framework.views import APIView

# from rest_framework import mixins
# from rest_framework import generics

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# from rest_framework.reverse import reverse
# ---------------------------------------------------------------

from django.shortcuts import get_object_or_404
from app.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from app.models import Student
from rest_framework import status


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)



# ---------------------------------------------------------------




# function base api
# @api_view(['GET', 'POST'])
# def api_list(request):

#     if request.method == "GET":
#         apibar = Student.objects.all()
#         serializer = StudentSerializer(apibar, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def api_detail(request, pk): 
#         try:
#             apibar = Student.objects.get(pk=pk)
#         except apibar.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         if request.method == 'GET':
#             serializer = StudentSerializer(apibar)
#             return Response(serializer.data)

#         elif request.method == 'PUT':
#             serializer = StudentSerializer(apibar, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         elif request.method == 'DELETE':
#             apibar.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)


# function base api --------------------------------------------------------------
# csrf_exempt file ta hide kore pass kore for secureti parpase
# @csrf_exempt 
# def api_list(request):

#     if request.method == 'GET':
#         apivar = Student.objects.all()
#         serializer = StudentSerializer(apivar, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def api_detail(request, pk):
#     try:
#         detailvar = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return HttpResponse(status=404)
    
# #get data show korar jonno use kora hobe 
#     if request.method == 'GET':
#         serializer = StudentSerializer(detailvar)
#         return JsonResponse(serializer.data)
    
# # put data update er jonno use kora hbe
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(detailvar, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.error, status=400)
    
#     elif request.method == 'DELETE':
#         detailvar.delete()
#         return HttpResponse(status=400)


# Class base api CRUD
# class BlogList(APIView):
#     def get(self, request, format=None):
#         stud = Student.objects.all()
#         serializer = StudentSerializer(stud, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ApiDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk, format=None):
#         stud = self.get_object(pk)
#         serializer = StudentSerializer(stud)
#         return Response(serializer.data)
        
#     def put(self, request, pk, format=None):
#         stud = self.get_object(pk)
#         serializer = StudentSerializer(stud, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         stud = self.get_object(pk)
#         stud.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Api hyperlinked --------------------------------------------
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'student': reverse('student-list', request=request, format=format),
        
#     })


# Mixins CRUD
# class StudentList(generics.ListCreateAPIView,
#                   mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)
    
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView,
#                     mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
    
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# # authentication systam -------------------
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # authentication_classes = [TokenAuthenticated]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    


