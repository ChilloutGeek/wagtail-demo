from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel,InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

# Create your models here.

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    
    def get_context(self, request):
        context = super().get_context(request)
        bloglists = self.get_children().live().order_by('-first_published_at')
        context['bloglists'] = bloglists
        return context    

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
class Picture(models.Model):
    
    image = models.ForeignKey(
        'wagtailimages.Image', blank=True, null=True, on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]


class BlogGalleryPage(Picture):
    
    page = ParentalKey('BlogPage', blank=True, null=True, on_delete=models.SET_NULL, related_name='gallery_images')

    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('caption'),
    ]