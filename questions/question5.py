"""
Question 5

Convert a function­based Django view to a class­based view
Recreate the following view as a modern class­based view:
"""


@login_required
def health_check(request):
    return HttpResponse(json.dumps({"status": "OK"}), mimetype='application/json')


#I have 2 options, wrap the dispatcher or craete a class view decorator

#OPTION 1
from django.views.generic import View

class MyView(View):

    def get(self, request, *args, **kwargs):
    	return HttpResponse(json.dumps({"status": "OK"}), mimetype='application/json')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyView, self).dispatch(*args, **kwargs)

#OPTION 2


from django.utils.decorators import method_decorator

def class_view_decorator(function_decorator):

    def returning_decorator(View):
        View.dispatch = method_decorator(function_decorator)(View.dispatch)
        return View

    return returning_decorator

@class_view_decorator(login_required)
class MyView(View):
    def get(self, request, *args, **kwargs):
    	return HttpResponse(json.dumps({"status": "OK"}), mimetype='application/json')