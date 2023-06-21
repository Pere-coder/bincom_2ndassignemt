from django.db import models

# Create your models here.
from django.db import models

class AgentName(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        db_table = 'agentname'


class AnnouncedLgaResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.lga_name} - {self.party_abbreviation}'

    class Meta:
        db_table = 'announced_lga_results'
        
class AnnouncedPuResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.polling_unit_uniqueid} - {self.party_abbreviation}'

    class Meta:
        db_table = 'announced_pu_results'
        
        
class AnnouncedStateResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.state_name} - {self.party_abbreviation}'

    class Meta:
        db_table = 'announced_state_results'
        
        

class AnnouncedWardResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.ward_name} - {self.party_abbreviation}'

    class Meta:
        db_table = 'announced_ward_results'
        
        
        
        
class LGA(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    lga_description = models.TextField(blank=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return self.lga_name

    class Meta:
        db_table = 'lga'
        
class Party(models.Model):
    id = models.AutoField(primary_key=True)
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)

    def __str__(self):
        return self.partyname

    class Meta:
        db_table = 'party'
        
class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField(null=True, blank=True)
    polling_unit_number = models.CharField(max_length=50, null=True, blank=True)
    polling_unit_name = models.CharField(max_length=50, null=True, blank=True)
    polling_unit_description = models.TextField(blank=True, null=True)  # Adjusted field
    lat = models.CharField(max_length=255, null=True, blank=True)
    long = models.CharField(max_length=255, null=True, blank=True)
    entered_by_user = models.CharField(max_length=50, null=True, blank=True)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.polling_unit_name

    class Meta:
        db_table = 'polling_unit'
        
        
        
class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name

    class Meta:
        db_table = 'states'
        
        
class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()
    ward_description = models.TextField(blank=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return self.ward_name

    class Meta:
        db_table = 'ward'
