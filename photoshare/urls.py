from django.conf.urls import patterns, url


urlpatterns = patterns(
    'photoshare.views',

    url(r'^$',
        'stub_view',
        name='front_page'),

    url(r'^home/(\d+)/$',
        'stub_view',
        name="home_page"),

    url(r'^home/album/$',
        'stub_view',
        name="album_view"),

    url(r'^home/photo/$',
        'stub_view',
        name="photo_view"),

    url(r'^home/tag/$',
        'stub_view',
        name="tag_view"),
)
