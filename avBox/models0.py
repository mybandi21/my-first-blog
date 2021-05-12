from django.db import models

# Create your models here.
class LinkFields(models.Model):
    link_external = models.URLField(
        "External link",
        blank=True,
        null=True,
        help_text='Set an external link if you want to describe the event from an other web site',
    )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='+',
        help_text='Choose an existing page (event must have already been created)',
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
    ]

    class Meta:
        abstract = True

class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        InlinePanel('related_links', label="Related events"),
    ]


class EventsPage(Page):

    # Database fields

    date = models.DateField("Event date")
    topicTag = models.CharField(max_length = 25)
    name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 20, default="Where it is")
    place = models.CharField(max_length = 20, blank=True)
    body = RichTextField(blank=True)

    # Search index configuration

    search_fields = Page.search_fields + (
        index.SearchField('topicTag'),
        index.SearchField('place'),
        index.FilterField('date'),
    )

    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('topicTag'),
        FieldPanel('name', classname="title"),
        FieldPanel('city'),
        FieldPanel('place'),
        FieldPanel('body'),
    ]


class EventsRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('HomePage', related_name='related_links')


class Article(models.Model):
    av_code = models.CharField(max_length=256)
    av_title = models.CharField(max_length=256)
    av_contents = models.TextField()
    av_url = models.URLField('url', blank=True, null=True)
    av_tag = models.TextField()
    av_actor = models.TextField()
    av_cover_path = model.LinkField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)

 title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', blank=True, null=True)
