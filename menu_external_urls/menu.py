from menus.base import Modifier
from menus.menu_pool import menu_pool
from menu_external_urls.models import MenuExternalUrl


class MenuExternalUrlMod(Modifier):
    """
    Adds ability to link page to an external URL.
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if post_cut:
            return nodes
        if breadcrumb:
            return nodes
        for node in nodes:
            try:
                #Load External URL into nodes
                menu_external_url = MenuExternalUrl.objects.get(page=node.id)
                node.url = menu_external_url.menu_external_url
            except:
                pass
        return nodes

menu_pool.register_modifier(MenuExternalUrlMod)
