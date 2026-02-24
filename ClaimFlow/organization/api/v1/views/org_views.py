from rest_framework import serializers
from organization.models import Organization,Practice



class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('name','email','description')