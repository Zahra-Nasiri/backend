from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from base.models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAdminUser

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/events'}
    ]
    return Response(routes)

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEvent(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createEvent(request):
    user = request.user
    data = request.data    
    event = Event.objects.create(
        type = data['type'],
        title = data['title'],
        owner = user,
        location = data['location'],
        description = data['description'],
        # image = data['image'],
        capacity = data['capacity'],
        date_time = data['date_time']
    )
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return Response('Event Deleted Successfully')

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def editEvent(request,pk):
    data = request.data
    event = Event.objects.get(id=pk)
    event.title = data['title']
    event.type = data['type']
    event.location = data['location']
    event.description = data['description']
    event.capacity = data['capacity']
    event.date_time = data['date_time']
    event.held = data['held']
    event.save()

    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)











