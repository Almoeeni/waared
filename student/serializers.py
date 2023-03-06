from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Student
        fields = ['studentID', 'user_id' ,'studentNumber', 'studentName', 'facultyName', 'DateOfBirth']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return ret
    
    def to_internal_value(self, data):
        data_copy = data.copy()
        data_copy['studentName'] = data.get('studentName', '').encode('utf-8').decode('utf-8')
        return super().to_internal_value(data_copy)


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField()