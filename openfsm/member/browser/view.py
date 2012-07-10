from opencore.member.browser.view import ProfileEditView
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

class FSMProfileEditView(ProfileEditView):
    template = ZopeTwoPageTemplateFile('profile-edit.pt')
    