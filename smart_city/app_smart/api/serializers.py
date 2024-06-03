#navaegação das informaçoes
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from app_smart.models import Sensor


#criptografia 
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    class Meta:
        model=User
        fields = ['id','username','email','password']
    extra_kwargs={'password':{'write_only': True}}#manter a segurança da informação e nao deixar que mostre a senha e cadastre diretamente no banco

#fazer a comunicacao com o sensor
#permitindo a serializacao do Sensor
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__' #Quando eu uso all eu permito o trafego de todos os campos