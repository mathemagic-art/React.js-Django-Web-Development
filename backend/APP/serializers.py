from rest_framework import serializers

class Function(serializers.Serializer):
    
    equation = serializers.CharField(max_length=300)

class Function_Two_Numeric(serializers.Serializer):
    
    equation = serializers.CharField(max_length=300)
    first = serializers.FloatField()
    second = serializers.FloatField()

class Function_Three_Numeric(serializers.Serializer):

    equation = serializers.CharField(max_length=300)
    first = serializers.FloatField()
    second = serializers.FloatField()
    third = serializers.FloatField()

class Three_Function(serializers.Serializer):
    equation = serializers.CharField(max_length=300)
    first = serializers.CharField(max_length=300)
    second = serializers.CharField(max_length=300)
