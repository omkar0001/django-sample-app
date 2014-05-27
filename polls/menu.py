from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

from .models import Poll

class PollsMenu(CMSAttachMenu):
    name = _("Polls Menu") # give the menu a name, this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        for poll in Poll.objects.all():
            # the menu tree consists of NavigationNode instances
            # Each NavigationNode takes a label as its first argument, a URL as
            # its second argument and a (for this tree) unique id as its third
            # argument.
            node = NavigationNode(
                poll.question,
                reverse('polls:detail', args=(poll.pk,)),
                poll.pk
            )
            nodes.append(node)
        n1 = NavigationNode(_('sample settings page'), "/coool/", 2)
        nodes.append(n1)

        return nodes

from cms.menu_bases import CMSAttachMenu

class TestMenu(CMSAttachMenu):

    name = _("test menu")

    def get_nodes(self, request):
        nodes = []
        n = NavigationNode(_('sample root page'), "/", 100)
        n2 = NavigationNode(_('sample settings page'), "/bye/", 200)
        n3 = NavigationNode(_('sample account page'), "/hello/", 300)
        n4 = NavigationNode(_('sample my profile page'), "/hello/world/", 400, 300)
        nodes.append(n)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        return nodes

menu_pool.register_menu(TestMenu)


menu_pool.register_menu(PollsMenu) # register the menu.