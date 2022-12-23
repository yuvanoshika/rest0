from django.shortcuts import render,HttpResponse
from app1.models import Course
from app1.serializers import CourseSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request,'app1/index.html',({'msg':'this is index page'}))

@csrf_exempt
def courseinfo(request,id=None):
    if request.method == 'GET':
        if id is None:
            course = Course.objects.all()
            serializer = CourseSerializer(course,many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type = 'application/json')
        if id is not None:
            course = Course.objects.get(id=id)
            serializer = CourseSerializer(course)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
    if request.method == 'POST':
        json_data = request.body
        stream_data = BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        serializer = CourseSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Has been Inserted'}
            json_data = JSONRenderer().render(res)
        else:
            json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    if request.method == 'PUT':
        json_data = request.body
        stream_data = BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        id = python_data.get('id')
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            json_data = JSONRenderer().render({'msg':'Data Updated'})
        else:
            json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    if request.method == 'DELETE':
        json_data = request.body
        stream_data = BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        id = python_data.get('id')
        course = Course.objects.get(id=id)
        course.delete()
        json_data = JSONRenderer().render({'msg':'Data was Deleted'})
        return HttpResponse(json_data,'application/json')

