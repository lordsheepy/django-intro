from django.conf.urls import patterns, url


urlpatterns = patterns(
    'photoshare.views',

    url(r'^$',
        'front_view',
        name='front_page'),

    url(r'login/$',
        'login_view',
        name='login_page'),

    url(r'logout/$',
        'logout_view',
        name='logout_page'),

    url(r'^home/$',
        'home_view',
        name="home_page"),

    url(r'^home/album/(\d+)/$',
        'album_view',
        name="album_page"),

    url(r'^home/photo/(\d+)/$',
        'photo_view',
        name="photo_page"),

    url(r'^home/tag/(\w+)/$',
        'tag_view',
        name="tag_page"),

    url(r'^add/tag/$',
        'add_tag_view',
        name="add_tag_page"),

    url(r'^add/album/$',
        'add_album_view',
        name="add_album_page"),

    url(r'^add/photo/$',
        'add_photo_view',
        name="add_photo_page"),
)
