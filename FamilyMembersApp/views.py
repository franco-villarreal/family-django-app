
from datetime import datetime
from django.shortcuts import render
from FamilyMembersApp.models import FamilyMember

def getFamilyMembers(request):
    familyMembers = FamilyMember.objects.all()
    context = { "familyMembers": familyMembers }
    return render(request, 'family.html', context)

def addFamilyMember(request, name, lastname):
    familyMember = FamilyMember(name=name, lastName=lastname, createdAt=datetime.now())
    familyMember.save()

    familyMembers = FamilyMember.objects.all()

    for member in familyMembers:
        print(member.name)

    context = { "familyMembers": familyMembers }

    return render(request,'family.html', context)