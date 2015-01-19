
from django import forms
from friends.models import FriendShip


class FriendShipForm(forms.ModelForm):
    """
        manage friends connections
    """
    friends = forms.CharField(max_length=100, required=False)
    #friendm = forms.ModelChoiceField(queryset=FriendShip.objects.filter())
    class Meta:
        model = FriendShip