from .serializers import StudentSerializer , EmailSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from datetime import date
from django.db.models.functions import ExtractYear
from rest_framework.decorators import api_view ,permission_classes

from django.core.mail import send_mail

# Create your views here.

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        if Student.objects.filter(user=request.user).exists():
            return Response({'detail': 'Record already exists for current user'}, status=HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(studentName__icontains=name)
        return queryset
    



class EmailView(APIView):
    serializer_class = EmailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        message = serializer.data['message']
       
        send_mail(
            'Subject here',
            message,
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return Response({'message': 'Email sent successfully'})


@api_view(['GET'])
def students_under_age(request, age):
    queryset = Student.objects.annotate(age=ExtractYear(date.today()) - ExtractYear('DateOfBirth')).filter(age__lt=int(age))
    serializer = StudentSerializer(queryset, many=True)
    return Response(serializer.data)