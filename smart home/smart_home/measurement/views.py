from rest_framework.viewsets import ModelViewSet
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer


class SensorViewSet(ModelViewSet):

    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()


class MeasurementViewSet(ModelViewSet):

    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()
