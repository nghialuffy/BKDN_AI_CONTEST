from api.models import User
from rest_meets_djongo.serializers import DjongoModelSerializer, ObjectIdField


class OrganizerContestantsInContestSerializer(DjongoModelSerializer):
    class Meta:
        model = User
        fields = ('_id', 'username', 'first_name', 'last_name')
    