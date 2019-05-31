from rest_framework import serializers
from . import models


class PumpSerializer(serializers.ModelSerializer):

    #city = CitySerializer()
    #town = TownSerializer()
    #sector = SectorSerializer()

    class Meta:
        model = models.Pump
        fields = '__all__'


class SectorSerializer(serializers.ModelSerializer):

    #city = CitySerializer()
    #town = TownSerializer()
    pump_set = PumpSerializer(many=True)

    class Meta:
        model = models.Sector
        fields = ('title', 'town', 'lat', 'lon', 'modem_number', 'pump_count', 'pressure', 'discharge', 'dis_pressure', 'set_pressure',
                  'water_level', 'low_pressure', 'pump_open', 'pump_1_disorder', 'pump_2_disorder', 'pump_3_disorder', 'pump_4_disorder', 'pump_set')


class TownSerializer(serializers.ModelSerializer):

    #city = CitySerializer()
    sector_set = SectorSerializer(many=True)
    #pump_set = PumpSerializer(many=True)

    class Meta:
        model = models.Town
        fields = ('title', 'city', 'sector_set')


class CitySerializer(serializers.ModelSerializer):

    town_set = TownSerializer(many=True)
    #sector_set = SectorSerializer(many=True)
    #pump_set = PumpSerializer(many=True)

    class Meta:
        model = models.City
        fields = ('id', 'title', 'town_set')
