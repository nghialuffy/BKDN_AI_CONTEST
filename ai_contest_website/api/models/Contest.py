from djongo import models
from api.models import User


class Contest(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_user = models.ForeignKey('user', on_delete=models.CASCADE, null=False, related_name='created_user')
    created = models.DateTimeField(auto_now_add=True)
    attended_contestants = models.ArrayReferenceField(
        to='user',
        on_delete=models.DO_NOTHING
    )
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

    class Meta:
        db_table = 'contest'

    # def __str__(self):
    #     return self

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Contest, self).save(**kwargs)
# print(list(User.objects.all()))

# e = User.objects.get(username='bkdn')
# c = Contest(title='bkdnContest', created_user=e)
# c.save()
# print(list(Contest.objects.all()))
