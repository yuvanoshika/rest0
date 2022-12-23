from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.Serializer):
    cname = serializers.CharField(max_length=30)
    dur = serializers.IntegerField()
    fee = serializers.IntegerField()


    def create(self, validated_data):
        return Course.objects.create(**validated_data)
    
    def update(self, instance, validateddata):
        instance.cname = validateddata.get('cname',instance.cname)
        instance.dur = validateddata.get('dur',instance.dur)
        instance.fee = validateddata.get('fee',instance.fee)
        instance.save()
        return instance



