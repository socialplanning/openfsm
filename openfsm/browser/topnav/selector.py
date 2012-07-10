from Products.LinguaPlone.browser.selector import TranslatableLanguageSelector
#from opencore.nui.contexthijack import HeaderHijackable
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

class FSMTranslatableLanguageSelector(TranslatableLanguageSelector):
    """Language selector for translatable content.
    """

    render = ZopeTwoPageTemplateFile('selector.pt')


