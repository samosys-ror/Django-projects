from rest_framework import serializers
from .models import *
from rest_framework.reverse import reverse
# from django.contrib.auth.models import User
  
class villages(serializers.ModelSerializer): 
 polling_booth_url = serializers.SerializerMethodField()
 partyworker_url = serializers.SerializerMethodField()
 program_url = serializers.SerializerMethodField()
 helpeople_url = serializers.SerializerMethodField()
 class Meta :
      model = village  
      fields = ['village_name','congress','bjp','total_votting','polling_booth_url','partyworker_url','program_url','helpeople_url']



 def get_polling_booth_url(self, polling_booth):
     request = self.context["request"]
     return reverse("polling_detail-detail", kwargs={"village_name": polling_booth.uid}, request=request) 
     
 
 def get_partyworker_url(self, partywoker):
        request = self.context["request"]
        return reverse("partywoker-detail", kwargs={"village": partywoker.uid}, request=request)

 def get_program_url(self, programs):
        request = self.context["request"]
        return reverse("program-detail", kwargs={"village": programs.uid}, request=request) 

 def get_helpeople_url(self, helpedpeople):
        request = self.context["request"]
        return reverse("helped_pople-detail", kwargs={"village": helpedpeople.uid}, request=request)    



class polling_boothse(serializers.ModelSerializer): 
   class Meta :
      model = polling_booth  
      fields = ["village_name","polling_booth_name","polling_booth_address","total_votting","bjp","congress","uid"]    

class partyworkerse(serializers.ModelSerializer):     
   class Meta :
      model = partyworker 
      fields = ['name','mobile_no','age','gender','image'] 


class votterse(serializers.ModelSerializer): 
   class Meta :
      model = votter  
      fields = ['name','father_name','age','gender','house_no','voter_id']


class imageuploadse(serializers.ModelSerializer):      
  class Meta :
    model = imageupload 
    fields = ['election_campaign','image']         

class elction_campaignse(serializers.ModelSerializer):   
 img = imageuploadse(many = True,read_only = True)   
 class Meta :
    model = election_campaign  
    fields = ['id','about','img']

#  def to_representation(self, instance):
#    data = super(elction_campaignse, self).to_representation(instance)
#    print(data['image'])
#    data = {"title":data['title'],"image":{"image":data['image']},"about":data['about']}
#    return data       

class election_resultse(serializers.ModelSerializer):      
 class Meta :
    model = electionresult 
    fields = ['Bjp','congress','other','year'] 


class problemse(serializers.ModelSerializer):      
 class Meta :
    model = problem 
    fields = ['village','detailproblem'] 


class programsse(serializers.ModelSerializer):        
 class Meta :
    model = programs 
    fields = ['program_name','date','village','uid'] 


class programs_peoplese(serializers.ModelSerializer): 
 class Meta :
    model = programs_people
    fields = ['name','mobile_no','village','program'] 



class helpedpeoplese(serializers.ModelSerializer):      
 class Meta :
    model = helpedpeople 
    fields = ['name','mobile_no','problem','suppoters','village'] 


 
