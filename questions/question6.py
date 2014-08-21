"""
Question 6

# Method decorators

Write a decorator for the class­based­view that you created in
Question 5 that ensures the view can only be seen by users with
permissions to edit the object being shown. Assume that there are
no third­party permissions modules in use, only the built­in auth
from Django.
"""

class MyView(View):

    def get(self, request, *args, **kwargs):
    	return HttpResponse(json.dumps({"status": "OK"}), mimetype='application/json')

    @method_decorator(login_required)
    @method_decorator(permission_required, 'myapp.change_object')
    def dispatch(self, *args, **kwargs):
        return super(MyView, self).dispatch(*args, **kwargs)