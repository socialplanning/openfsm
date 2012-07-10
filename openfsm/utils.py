from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from opencore.nui.wiki.interfaces import IWikiHistory
from opencore.project.utils import project_noun
from zope.app.component.hooks import getSite

def member_title(id):
    context = getSite()
    pid = getToolByName(context, 'portal_url').getPortalObject().id
    mt = getToolByName(context, 'membrane_tool')
    try:
        meta = mt.getMetadataForUID('/%s/portal_memberdata/%s' % (pid, id))
        return meta['Title']
    except KeyError:
        #if not in the catalog, fall back on the member id
        return id

class OpenFSMUtils(BrowserView):
    """convenience functions that several templates use"""

    def member_title(self, id):
        return member_title(id)

    def project_noun(self):
        return project_noun()

    def modification_time(self, date):
        day = date.strftime('%d').lstrip('0')
        hour = date.strftime('%I').lstrip('0')
        return date.strftime('%A, %B ' + day + ' at ' + hour + ':%M%p')

    def difflink_info(self, context=None):
        if context is None:
            context = self.context
        history = IWikiHistory(context)
        nhistory = len(history)
        if nhistory < 2:
            return dict()
        return dict(first=nhistory-1, second=nhistory-2)
