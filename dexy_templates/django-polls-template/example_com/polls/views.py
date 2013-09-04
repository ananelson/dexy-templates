from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from polls.models import Poll, Choice

### "index"
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'
    
    def get_queryset(self):
        """Return the last 5 published polls."""
        return Poll.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

### "detail"
class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

### "results"
class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

### "vote"
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay voting form
        return render(request, 'polls/detail.html', {
            'poll' : p,
            'error_message' : "You didn't select a choice."
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
