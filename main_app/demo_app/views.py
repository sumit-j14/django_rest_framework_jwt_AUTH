from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


# Create your views here.
@api_view(['GET'])
def get_api(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response({'status': 'ready', 'payload': serializer.data})


# imitating data coming from frontend
@api_view(['POST'])
def post_api(request):
    data = request.data
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        print("valid ")
        serializer.save()
    else:
        print("invalid")
        return Response({'status': 'something went wrong', 'payload': data})
    return Response({'status': 'ready', 'payload': data})


# delete api filter by id
@api_view(['DELETE'])
def delete_api(request,id):
    try:
        # id = request.GET.get('id')
        student_to_delete = Student(id=id)
        student_to_delete.delete()
        return Response({'status': 203, 'message': 'deleted successfully'})
    except:
        return Response({'status': 403, 'message': 'delete unsuccessful error occured'})
