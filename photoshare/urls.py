from django.conf.urls import patterns, url


urlpatterns = patterns(
    'photoshare.views',

    url(r'^$',
        'front_view',
        name='front_page'),

    url(r'login/$',
        'login_view',
        name='login_page'),

    url(r'^home/$',
        'home_view',
        name="home_page"),

    url(r'^home/album/$',
        'stub_view',
        name="album_page"),

    url(r'^home/photo/$',
        'stub_view',
        name="photo_page"),

    url(r'^home/tag/$',
        'stub_view',
        name="tag_page"),
)
