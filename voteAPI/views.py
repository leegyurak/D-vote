from .models import vote
from authAPI.models import User
from .serializers import makeVoteSerializer, votingSerializer, voteListSerializer, voteAcceptSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class makeVoteView (GenericAPIView) :
    serializer_class = makeVoteSerializer
    permission_classes = [IsAuthenticated]

    def post (self, request) :
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organizer=request.user)

        user = User.objects.get(username=serializer.data['organizer'])
        Vote = vote.objects.get(id=serializer.data['id'])

        if serializer.data['item3'] != None :
            Vote.item3Cnt = 0
            Vote.save()
        
        if serializer.data['item4'] != None :
            Vote.item4Cnt = 0
            Vote.save()

        if serializer.data['item5'] != None :
            Vote.item5Cnt = 0
            Vote.save()

        if user.identity == 'teacher' :
            Vote.is_consent = True
            Vote.save()

            return Response({'message': '투표 등록이 완료 되었습니다.'}, status=201)

        return Response({'message': '대기열 등록이 완료 되었습니다.'}, status=200)

class votingView (ModelViewSet) :
    serializer_class = votingSerializer
    permission_classes = [IsAuthenticated]
    queryset = vote.objects.filter(is_consent=True)

class voteListView (ModelViewSet) :
    serializer_class = voteListSerializer
    permission_classes = [IsAuthenticated]
    queryset = vote.objects.filter(is_consent=True).order_by('pk')

class voteAcceptListView (ModelViewSet) :
    serializer_class = voteListSerializer
    permission_classes = [IsAuthenticated]
    queryset = vote.objects.filter(is_consent=False).order_by('pk')
    queryset.filter(is_denied=False)

class voteAcceptView (GenericAPIView) :
    serializer_class = voteAcceptSerializer
    permission_classes = [IsAuthenticated]

    def put (self, request, pk) :
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organizer=request.user)

        user = User.objects.get(username=serializer.data['organizer'])
        Vote = vote.objects.get(pk=serializer.data['pk'])

        if user.identity == 'student' :
            return Response({'message': '권한이 없습니다.'}, status=401)

        if serializer.data['select'] == 'accept' :
            Vote.is_consent = True
            Vote.save()
            return Response({'message': '투표가 등록 되었습니다.'}, status=200)

        elif serializer.data['select'] == 'deny' :
            Vote.is_denied = True
            Vote.save()
            return Response({'message': '거부 되었습니다.'}, status=200)