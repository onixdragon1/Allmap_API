from rest_framework import serializers
from .models import All_map

#serializer: 장고 모델 데이터를 JSON 타입으로 바꿔주는 직렬화 코드
#장고 모델의 데이터를 템플릿에 뿌려주면 웹에 보여지듯, JSON 타입으로
#뿌려주면 API로서 통신이 되는 것이며 내 데이터를 JSON으로 바꿔주는 기계

#All_map(Quiz)모델 데이터가 주어지면 title, body, answer를 포함한
#JSON 데이터로 변환해주는 시리얼라이저 완성
class All_mapSerializer(serializers.ModelSerializer):
    class Meta:
        model = All_map
        fields = ('title', 'body', 'answer')