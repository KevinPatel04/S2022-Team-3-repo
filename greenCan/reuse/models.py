from django.db import models
from recycle.models import ZipCode
from django.conf import settings
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from rewards.models import EarnGreenCredits
from django.contrib.contenttypes.fields import GenericRelation
from notification.utils import create_notification


class Post(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=250, null=False)
    category = models.CharField(max_length=200, null=False)
    phone_number = models.CharField(max_length=17, null=True)
    email = models.EmailField(null=True)
    zip_code = models.ForeignKey(ZipCode, null=False, on_delete=models.CASCADE)
    description = models.TextField(null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    approved = models.BooleanField(null=True, default=None)
    still_available = models.BooleanField(null=True, default=True)
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True, null=False)
    search_vector = SearchVectorField(null=True)
    green_credits = GenericRelation(EarnGreenCredits)

    def __str__(self):
        return str(self.id)

    class Meta:
        indexes = [
            GinIndex(fields=["search_vector"]),
        ]


class Image(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    url = models.URLField(max_length=2000, null=False)

    def __str__(self):
        return str(self.id)


class NGOLocation(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    zip_code = models.ForeignKey(ZipCode, null=False, on_delete=models.CASCADE)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    items_accepted = models.TextField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=17, null=True)
    address = models.TextField(null=False)
    hours = models.CharField(max_length=500, null=True)
    website = models.URLField(max_length=2000, null=True)

    def __str__(self):
        return str(self.id)


class PostConcernLogs(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    checked = models.BooleanField(default=False)
    message = models.TextField(null=True, max_length=500)

    def __str__(self):
        return str(self.id)

    def send_signals_and_moderate(self, admin_user, new_status, message=None):
        status = ""
        msg_type = ""
        post = self.post
        if new_status == 1:
            post.approved = True
            status = "approved"
            msg_type = "success"
        elif new_status == 0:
            post.approved = False
            status = "denied"
            msg_type = "error"
        post.save()

        # send notification to user
        sender = admin_user
        receiver = self.post.user
        msg = "Your post is " + status
        if message is not None:
            msg += "; " + message

        notification = {
            "sender": sender,
            "receiver": receiver,
            "msg_type": msg_type,
            "message": msg,
            "notification_obj": post,
        }
        create_notification(notification)
