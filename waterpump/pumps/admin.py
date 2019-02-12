from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Pump)
class PumpAdmin(admin.ModelAdmin):

    list_display = (
        'sector',
        'title',  # 카드뷰에 나오는 펌프이름
        'comstate',  # 통신 상태
        'name',  # 가입창명
        'modem_number',  # 모뎀번호
        'latitude',  # 위도
        'longitude',  # 경도
        'pump_count',  # 펌프개수
        'pressure',  # 흡입압력 표시여부

        'pump_1_freq',  # 1번 펌프 주파수
        'pump_1_current',  # 1번 펌프 전류
        'pump_2_freq',  # 2번 펌프 주파수
        'pump_2_current',  # 2번 펌프 전류
        'pump_3_freq',  # 3번 펌프 주파수
        'pump_3_current',  # 3번 펌프 전류
        'updated_at'
    )

    search_fields = (
        'sector',
        'title',
        'name',
        'modem_number',
    )

    list_filter = (
        'sector',
    )


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Town)
class TownAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Sector)
class SectorAdmin(admin.ModelAdmin):
    pass
