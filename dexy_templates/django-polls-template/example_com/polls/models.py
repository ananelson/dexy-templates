### "models"
from django.db import models

### "date-utils"
from django.utils import timezone
import datetime

### "poll"
class Poll(models.Model):
    ### "poll-fields"
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    ### "poll-unicode"
    def __unicode__(self):
        return self.question

    ### "recent"
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    ### "admin-config"
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

### "choice"
class Choice(models.Model):
    ### "choice-fields"
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    ### "choice-unicode"
    def __unicode__(self):
        return self.choice_text
