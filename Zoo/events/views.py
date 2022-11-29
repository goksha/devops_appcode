from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Event
from .design import EventForm
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

# Create a task
def event_creation(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("events:event_list"))
    else:
        form = EventForm()

    return render(request, "events/event_form.html", { "form": form, })


# Retrieve task list
def event_list(request):
    events = Event.objects.all()
    return render(request, "events/event_list.html", { "events": events,})


# Retrieve a single task
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, "events/event_detail.html", { "event": event, })


# Update a single task
def event_update(request, pk):
    event_obj = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(instance=event_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("events:event_detail", args=[pk,]))
    else:
        form = EventForm(instance=event_obj)

    return render(request, "events/event_form.html", { "form": form, "object": event_obj})


# Delete a single task
def event_delete(request, pk):
    event_obj = get_object_or_404(Event, pk=pk)
    event_obj.delete()
    return redirect(reverse("events:event_list"))







class TaskListView(ListView):
    model = Event
    context_object_name = 'events'

class TaskDetailView(DetailView):
    model = Event

class TaskCreateView(CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:event_list')

class TaskUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:event_list')

class TaskDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('events:event_list')

