from django.conf.urls import patterns, include, url

from .views import ProjectList, Tickets, TicketDetails, ProjectCreate, TicketCreate, TicketEdit


urlpatterns = patterns('project.views',
    url(r'^$', ProjectList.as_view(), name='projects'),
    url(r'^project/create/$', ProjectCreate.as_view(), name='project-create'),
    url(r'^project/(?P<pk>\d+)/$', Tickets.as_view(), name='project'),
    url(r'^project/(?P<pk>\d+)/create/$', TicketCreate.as_view(), name='ticket-create'),
    url(r'^ticket/(?P<pk>\d+)/$', TicketDetails.as_view(), name='ticket'),
    url(r'^ticket/(?P<pk>\d+)/edit/$', TicketEdit.as_view(), name='ticket-edit'),
)
