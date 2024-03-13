from rest_framework import serializers

class ValidateQuestionSerializer(serializers.Serializer):
    question = serializers.CharField()
    options = serializers.ListField(child=serializers.CharField())
    answer = serializers.CharField()