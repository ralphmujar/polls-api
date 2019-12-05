from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from .apiviews import PollViewSet, \
#        ChoiceList, CreateVote, UserCreate



from .apiviews import PollList, PollDetail, UserCreate, LoginView \
        , PollViewSet, ChoiceList
#router = DefaultRouter()
#router.register('polls', PollViewSet, base_name='polls')
#
#urlpatterns = [
#    path('user/', UserCreate.as_view(), name='user_create'),
#    path('<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
#    path('<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
#        ]
#
#urlpatterns += router.urls



#better url structures
urlpatterns = [
    path('user/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),
    path('', PollList.as_view(), name='polls_list'),
    #path('', PollViewSet.destroy, name='polls_list'),
    path('<int:pk>/', PollDetail.as_view(), name='polls_detail'),
#    path('choices/', ChoiceList.post, name='choice_list'),
    path('<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
#    path('vote/', CreateVote.as_view(), name='create_vote'),
        ]

