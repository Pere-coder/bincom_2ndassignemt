from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        selected_lga_id = request.POST.get('lga_id')
        polling_units = PollingUnit.objects.filter(lga_id=selected_lga_id)
        total_result = AnnouncedPuResult.objects.filter(polling_unit_uniqueid__in=polling_units.values('uniqueid')).aggregate(sum_result=Sum('party_score'))
        lga = LGA.objects.get(lga_id=selected_lga_id)
        context = {'polling_units': polling_units, 'total_result': total_result['sum_result'], 'lga': lga}
        return render(request, 'select_lga.html', context)

    lgas = LGA.objects.all()
    context = {'lgas': lgas}
    return render(request, 'result.html', context)
    
    # if request.method == 'POST':
    #     id = request.POST.get('id')
        
    
    # total_result = AnnouncedPuResult.objects.filter(polling_unit_uniqueid=27).aggregate(sum_result=Sum('party_score'))
    # # lga = LGA.objects.get(lga_id=id)
    # context = {'total_result': total_result['sum_result']}
    # return render(request, 'result.html', context)
    
    
    
    

def new_polling_unit_result(request):
    if request.method == 'POST':
        polling_unit_id = request.POST.get('polling_unit_id')
        party_scores = request.POST.getlist('party_score')
        
        # Retrieve the polling unit
        try:
            polling_unit = PollingUnit.objects.get(uniqueid=polling_unit_id)
        except PollingUnit.DoesNotExist:
            # Handle polling unit not found error
            return redirect('new_polling_unit_result')
        
        # Clear existing results for the polling unit
        AnnouncedPuResult.objects.filter(polling_unit_uniqueid=polling_unit_id).delete()
        
        # Save the results for all parties
        for party, score in zip(Party.objects.all(), party_scores):
            AnnouncedPuResult.objects.create(
                polling_unit_uniqueid=polling_unit,
                party_abbreviation=party,
                party_score=score,
                entered_by_user=request.user.username,  # Update with appropriate user handling
                date_entered=datetime.now(),  # Update with appropriate date handling
                user_ip_address=request.META['REMOTE_ADDR']  # Update with appropriate IP handling
            )
        
        # Redirect to a success page or appropriate location
        return redirect('success_page')

    parties = Party.objects.all()
    context = {'parties': parties}
    return render(request, 'new_polling_unit_result.html', context)