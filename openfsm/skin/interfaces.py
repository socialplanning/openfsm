from zope.publisher.interfaces.browser import IBrowserRequest
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class IOpenFSMLayer(IBrowserRequest):
    """The `openfsm` layer."""


class IOpenFSMSkin(IOpenFSMLayer, IDefaultBrowserLayer):
    """The `openfsm` skin."""
