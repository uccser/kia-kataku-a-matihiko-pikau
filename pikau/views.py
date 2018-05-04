"""Views for the pikau application."""

from django.views import generic
from pikau.models import (
    GlossaryTerm,
    Goal,
    Level,
    PikauCourse,
    ProgressOutcome,
    Tag,
    Topic,
)


class IndexView(generic.TemplateView):
    """View for the pikau homepage that renders from a template."""

    template_name = "pikau/index.html"


class GlossaryList(generic.ListView):
    """View for the glossary list page."""

    template_name = "pikau/glossary.html"
    context_object_name = "glossary_terms"
    model = GlossaryTerm
    ordering = "term"


class GoalList(generic.ListView):
    """View for the goal list page."""

    context_object_name = "goals"
    model = Goal
    ordering = "slug"


class LevelList(generic.ListView):
    """View for the level list page."""

    context_object_name = "levels"
    model = Level
    ordering = "name"


class LevelDetail(generic.DetailView):
    """View for a level."""

    context_object_name = "level"
    model = Level


class PikauCourseList(generic.ListView):
    """View for the pīkau course list page."""

    context_object_name = "pikau_courses"
    model = PikauCourse
    ordering = "name"


class PikauCourseDetail(generic.DetailView):
    """View for a pīkau course."""

    context_object_name = "pikau_course"
    model = PikauCourse


class ProgressOutcomeList(generic.ListView):
    """View for the progress outcome list page."""

    context_object_name = "progress_outcomes"

    def get_queryset(self):
        """Get queryset of all progress outcomes.

        Returns:
            Queryset of ProgressOutcome objects ordered by name.
        """
        return ProgressOutcome.objects.order_by("name")

    def get_context_data(self, **kwargs):
        """Provide the context data for the view.

        Returns:
            Dictionary of context data.
        """
        context = super(ProgressOutcomeList, self).get_context_data(**kwargs)
        topics = Topic.objects.order_by("name")
        context["topics"] = topics
        for progress_outcome in self.object_list:
            topic_counts = dict()
            for topic in topics:
                topic_counts[topic.slug] = progress_outcome.pikau_courses.filter(topic=topic).count()
            progress_outcome.topic_counts = topic_counts
            print(topic_counts)
        return context

class TagList(generic.ListView):
    """View for the tag list page."""

    context_object_name = "tags"
    model = Tag
    ordering = "name"


class TagDetail(generic.DetailView):
    """View for a tag."""

    context_object_name = "tag"
    model = Tag


class TopicList(generic.ListView):
    """View for the topic list page."""

    context_object_name = "topics"
    model = Topic
    ordering = "name"


class TopicDetail(generic.DetailView):
    """View for a topic."""

    context_object_name = "topic"
    model = Topic
