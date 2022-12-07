from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from base.models import Event, Registrant
from .serializers import EventSerializer, RegistrantSerializer
from rest_framework.permissions import IsAdminUser

# Api for Event


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': 'api/events'},
        {'GET': 'api/events/id'},
        {'POST': 'api/create-events'},
        {'PUT': 'api/update-events/id'},
        {'DELETE': 'api/delete-events/id'},
        {'GET': 'api/registrants'},
        {'DELETE': 'api/delete-registrants/id'},
        # Registering for a specific event (id is for event)
        {'POST': '/api/create-registrants/id'}

    ]
    return Response(routes)


@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_event(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_event(request):
    user = request.user
    data = request.data
    event = Event.objects.create(
        type=data['type'],
        title=data['title'],
        owner=user,
        location=data['location'],
        description=data['description'],
        # image = data['image'],
        capacity=data['capacity'],
        date_time=data['date_time']
    )
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_event(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return Response('Event Deleted Successfully')


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def edit_event(request, pk):
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


# Api for registrant
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_registrans(request):
    registrants = Registrant.objects.all()
    serializer = RegistrantSerializer(registrants, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_registrant(request, pk):
    registrant = Registrant.objects.get(id=pk)
    event = registrant.event
    event.enrolled = event.enrolled - 1
    event.save()
    registrant.delete()
    return Response('Registrant Deleted Successfully')


@api_view(['POST'])
def create_registrant(request, pk):
    data = request.data
    event = Event.objects.get(id=pk)
    registrant = Registrant.objects.create(
        event=event,
        first_name=data['first_name'],
        last_name=data['last_name'],
        student_id=data['student_id'],
        phone_number=data['phone_number'],
        university=data['university']
    )
    event.enrolled = event.enrolled + 1
    event.save()
    serializer = RegistrantSerializer(registrant, many=False)
    return Response(serializer.data)
