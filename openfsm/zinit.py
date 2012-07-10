from Products.PlacelessTranslationService.PlacelessTranslationService \
     import catalogRegistry
from openfsm import OPENFSM
import pkg_resources

import logging
logger = logging.getLogger('openfsm.zinit')

def initialize(context):
    """
    Initialization function that bootstraps us as a Zope product.
    We're forcing our .po files into the PTS catalog registry, and
    making sure they're _before_ the OpenPlans ones, so our
    translations will win.
    """
    cp = context._ProductContext__app.Control_Panel
    try:
        cp_ts = cp.TranslationService
    except AttributeError:
        logger.warn("No TranslationService")
        return
    i18n_path = pkg_resources.resource_filename(OPENFSM, 'openfsm/i18n')
    cp_ts._load_i18n_dir(i18n_path)

    # it seems to always be first, but we force it here just in case
    oc_keys = [key for key in catalogRegistry.keys() if key[1] == 'opencore']
    for key in oc_keys:
        new_order = []  # <-- must be Blue Monday again
        cats = catalogRegistry.get(key)
        for cat in cats:
            if cat.startswith('openfsm'):
                new_order.insert(0, cat)
            else:
                new_order.append(cat)
        catalogRegistry[key] = new_order
        cp_ts._p_changed = True
