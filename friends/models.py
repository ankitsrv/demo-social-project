from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.

class FriendShip(models.Model):
    """
        friends table, bi-directional association between two users who
        both agreed to be friends
    """
    added = models.DateTimeField(auto_now_add=True, editable=False)

    """
        from_user : person who is sending the request ( better call him/her 'A')
        friend : person who is getting the request ( call him/her 'B')

        f(friendship): A --> B
    """

    from_user = models.ForeignKey(User, related_name="friendship_starter")
    friend = models.ForeignKey(User, related_name="friend_set")



    class Meta:
        unique_together = [("friend", "from_user")]

    #objects = FriendShipManager()

def friend_set_for(user):
    return set([obj["friend"] for obj in FriendShip.objects.friends_for_user(user)])

def are_friends(self, user1, user2):
        return self.filter(
            Q(from_user=user1, friend=user2) |
            Q(from_user=user2, friend=user1)
        ).count() > 0


class FriendShipInvitation(models.Model):

    # Invitation statuses for the friend request
    INVITE_STATUS = (
        (1, "Created"),
        (2, "Sent"),
        (3, "Accepted"),
        (4, "Declined"),
    )

    # import the 'Message' model class from message/models.py

    #Invite_message = models.ForeignKey(Message)
    #Invite_message = models.ForeignKey(message.Message)

    from_user = models.ForeignKey(User, related_name="invitation_from")
    friend = models.ForeignKey(User, related_name="invitations_to")

    sent_at = models.DateTimeField(default=datetime.date.today)
    status = models.IntegerField(choices=INVITE_STATUS)


