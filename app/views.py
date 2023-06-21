from django.shortcuts import render
from .models import AgentName, AnnouncedLgaResult, AnnouncedPuResult,AnnouncedStateResult, AnnouncedWardResult, LGA, Party, PollingUnit, State, Ward
from django.db.models import Sum
# Create your views here.

#P means Polling
def P_unit_results(request):
    results = AnnouncedPuResult.objects.all()
    context = {
        "results": results
    }
    return render(request, 'P_unit_results.html', context)

#L_govn means local government
def L_govn_results(request):
    total_result = AnnouncedPuResult.objects.filter(polling_unit_uniqueid=27).aggregate(sum_result=Sum('party_score'))
    lga = LGA.objects.get(lga_id=35)
    context = {'total_result': total_result['sum_result'], 'lga': lga}
    return render(request, 'result.html', context)
    
    