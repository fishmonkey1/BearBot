from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
            'id',
            'user',
            'tweets',
            'followers',
            'following',
            'verified',
            'img',
            'description',
            'analysis_positive',
            'analysis_negative',
            'analysis_neutral',
            'acceptance_positive',
            'acceptance_negative',
            'acceptance_neutral',
            'created_on',
        )
