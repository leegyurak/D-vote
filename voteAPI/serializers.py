from rest_framework import serializers
from .models import vote

class makeVoteSerializer (serializers.ModelSerializer) :
    organizer = serializers.CharField(source='organizer.username', read_only=True)

    class Meta :
        model = vote
        fields = ['id', 'organizer', 'subject', 'item1', 'item2', 'item3', 'item4', 'item5']

class votingSerializer (serializers.ModelSerializer) :
    subject = serializers.CharField(read_only=True)
    item1 = serializers.CharField(read_only=True)
    item2 = serializers.CharField(read_only=True)
    item3 = serializers.CharField(read_only=True)
    item4 = serializers.CharField(read_only=True)
    item5 = serializers.CharField(read_only=True)

    class Meta :
        model = vote
        fields = ['pk', 'subject', 'item1', 'item2', 'item3', 'item4', 'item5', 'item1Cnt', 'item2Cnt', 'item3Cnt', 'item4Cnt', 'item5Cnt']

class voteListSerializer (serializers.ModelSerializer) :
    subject = serializers.CharField(read_only=True)

    class Meta :
        model = vote
        fields = ['pk', 'subject']


class voteAcceptSerializer (serializers.ModelSerializer) :
    organizer = serializers.CharField(source='organizer.username', read_only=True)
    subject = serializers.CharField(read_only=True)
    item1 = serializers.CharField(read_only=True)
    item2 = serializers.CharField(read_only=True)
    item3 = serializers.CharField(read_only=True)
    item4 = serializers.CharField(read_only=True)
    item5 = serializers.CharField(read_only=True)

    class Meta :
        model = vote
        fields = ['pk', 'organizer', 'subject', 'item1', 'item2', 'item3', 'item4', 'item5', 'select']