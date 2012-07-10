from opencore.nui.main.search import HomeView
import os


class OpenFSMHomeView(HomeView):
    """ Home page override """

    def render_static(self,fname):
        curdir = os.path.dirname(__file__)
        filename = os.path.join(curdir, fname)
        file_obj = file(filename)
        data = file_obj.read()
        file_obj.close()
        return data

    def news(self):
        news_path = '/'.join(self.context.portal.getPhysicalPath()) + '/news'
        query = dict(portal_type='Document',
                     sort_on='created',
                     sort_order='descending',
                     sort_limit=3,
                     path=news_path
                     )
        brains = self.catalog(**query)
        return brains

