from django.db.models import Sum

def calcula_total(obj, campo):    
   return obj.aggregate(Sum(campo))[f'{campo}__sum'] 
    