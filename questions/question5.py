"""
Question 5

Convert a function­based Django view to a class­based view
Recreate the following view as a modern class­based view:
"""


@login_required
def health_check(request):
    return HttpResponse(json.dumps({"status": "OK"}), mimetype='application/json')

