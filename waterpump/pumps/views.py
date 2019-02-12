from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

# Create your views here.


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user
        managing_city = user.managing

        serializer = serializers.CitySerializer(managing_city)

        print(managing_city)

        return Response(data=serializer.data)


class ListAllCities(APIView):

    def get(self, request, format=None):

        all_cities = models.City.objects.all()

        serializer = serializers.CitySerializer(all_cities, many=True)

        return Response(data=serializer.data)


class ListAllTowns(APIView):

    def get(self, request, format=None):

        all_towns = models.Town.objects.all()

        serializer = serializers.TownSerializer(all_towns, many=True)

        return Response(data=serializer.data)


class ListAllSectors(APIView):

    def get(self, request, format=None):

        all_sectors = models.Sector.objects.all()

        serializer = serializers.SectorSerializer(all_sectors, many=True)

        return Response(data=serializer.data)


class ListAllPumps(APIView):

    def get(self, request, format=None):

        all_pumps = models.Pump.objects.all()

        serializer = serializers.PumpSerializer(all_pumps, many=True)

        return Response(data=serializer.data)
