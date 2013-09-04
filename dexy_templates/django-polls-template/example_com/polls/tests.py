import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Poll

class PollMethodTests(TestCase):
    ### "old-poll"
    def test_was_published_recently_with_old_poll(self):
        """
        was_published_recently() should return False for polls whose pub_date is older than one day
        """
        old_poll = Poll(pub_date = timezone.now() - datetime.timedelta(days=30))
        self.assertEqual(old_poll.was_published_recently(), False)

    ### "recent-poll"
    def test_was_published_recently_with_recent_poll(self):
        """
        was_published_recently() should return True for polls whose pub_date is within the last day
        """
        recent_poll = Poll(pub_date = timezone.now() - datetime.timedelta(hours=1))
        self.assertEqual(recent_poll.was_published_recently(), True)

    ### "future-poll"
    def test_was_published_recently_with_future_poll(self):
        """
        was_published_recently() should return False for polls whose pub_date is in the future
        """
        future_poll = Poll(pub_date = timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(), False)
