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
        fields = ('title', 'town', 'pump_set')


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
