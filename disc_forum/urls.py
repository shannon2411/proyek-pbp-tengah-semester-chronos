from django.urls import path
from .views import create_disc, del_post, del_rep, edit_post, forum, add_reply, get_forum_flutter, get_reply_flutter

urlpatterns = [
    path('', forum, name='disc_forum'),
    path('add-disc', create_disc, name='add_disc'),
    path('<int:id>/add-reply', add_reply, name='add_rep'),
    path('<int:id>/edit', edit_post, name='edit_post'),
    path('<int:id>/del-post', del_post, name='del_post'),
    path('<int:id>/del-rep', del_rep, name='del_rep'),
    path('get-forum', get_forum_flutter, name="forum_flutter"),
    path('get-reply', get_reply_flutter, name="reply_flutter"),

]