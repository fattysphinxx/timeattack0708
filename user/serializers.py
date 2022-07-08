from rest_framework import serializers
from .models import JiwonGongo


class JiwonGongoSerializer(serializers.ModelSerializer):
    class Meta:
        model = JiwonGongo
        fields = ("id", "jiwon_company", 'interview_date')
