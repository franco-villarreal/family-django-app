from django.urls import path
from FamilyMembersApp.views import addFamilyMember, getFamilyMembers

urlpatterns = [
    path('members/', getFamilyMembers),
    path('members/add/<name>/<lastname>', addFamilyMember)
]