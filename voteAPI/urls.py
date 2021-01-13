from django.urls import path
from .views import makeVoteView, votingView, voteListView, voteAcceptListView, voteAcceptView

urlpatterns = [
    path('post', makeVoteView.as_view()),
    path('detail/<int:pk>', votingView.as_view({"get": "retrieve", "patch": "partial_update", "delete": "destroy"})),
    path('feed', voteListView.as_view({'get': 'list'})),
    path('accept', voteAcceptListView.as_view({'get': 'list'})),
    path('accept/<int:pk>', voteAcceptView.as_view()),
]