from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Pump)
class PumpAdmin(admin.ModelAdmin):

    list_display = (
        'sector',
        'title',  # 카드뷰에 나오는 펌프이름
        'auto',  # 통신 상태
        'operating_rate',  # 가입창명
        'current',  # 모뎀번호
        'freq',  # 위도
        'power',  # 경도
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
    list_display = (
        'town',
        'title',  # 카드뷰에 나오는 펌프이름
        'lat',  # 통신 상태
        'lon',  # 가입창명
        'modem_number',  # 모뎀번호
        'pump_count',  # 펌프개수
        'pressure',  # 흡입압력 표시여부
        'discharge',  # 유량
        'dis_pressure',
        'set_pressure',
        'water_level',
        'low_pressure',
        'pump_open',
        'pump_1_disorder',
        'pump_2_disorder',
        'pump_3_disorder',
        'pump_4_disorder',
        'updated_at'
    )
