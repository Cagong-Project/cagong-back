from django.db import models

# 매장이름, 매장위치, 매장소개, owner_user_id, cafe 이미지는? (cafe_id)
class Cafe(models.Model):
    name = models.CharField(max_length=10)
    location = models.TextField()
    info = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True)
    owner = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    #QuerySet을 json 타입으로 바꾸기 위함.
    def cafeToDictionary(cafe_queryset):
        num = len(cafe_queryset) # 검색된 개수
        if num > 0: # queryset에 1개 이상의 cafe가 있다면
            result = {}
            for i in range(num):
                cafe = cafe_queryset[i] # i번째 cafe
                cafeDict = {}
                cafeDict["name"] = cafe.name
                cafeDict["location"] = cafe.location
                cafeDict["info"] = cafe.info
                cafeDict["owner"] = cafe.owner
                result[i] = cafeDict # 추가
        else:
            return None

        return result