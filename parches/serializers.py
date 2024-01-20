from rest_framework import serializers
from .models import Actividad, EmpresaPersona

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'
        
class EmpresaPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaPersona
        fields='__all__'
