from rest_framework import serializers

from .models import PriorityModel


class PriorityModelSerializer(serializers.ModelSerializer):
    color = serializers.RegexField(r"#([a-f]|\d)+", max_length=7, required=False)
    class Meta:
        model = PriorityModel
        fields = [
            'id',
            'name',
            'color',
        ]

# print(repr(PriorityModelSerializer()))