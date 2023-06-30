from django.shortcuts import render, redirect
from myprops.models import Props
from myprops.forms import PropsForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def list_props(request):
    if request.method == "POST":
        prop_id = request.POST.get("prop_id")
        if prop_id:
            # Mark the prop as viewed
            prop = Props.objects.get(id=prop_id, recipient=request.user)
            prop.is_viewed = True
            prop.save()

    props = Props.objects.filter(recipient=request.user)
    new_props = props.filter(is_viewed=False)

    context = {
        "props": props,
        "new_props": new_props,
    }

    return render(request, "props/list_props.html", context)

@login_required
def send_props(request):
    if request.method == "POST":
        form = PropsForm(request.POST)
        if form.is_valid():
            props = form.save(commit=False)
            props.recipient = form.cleaned_data['recipient']
            props.sender_id = request.user.id
            props.sender_username = request.user.username
            props.save()

            return redirect("list_props")
    else:
        form = PropsForm()

    context = {
        "form": form,
    }

    return render(request, "props/send_props.html", context)



#######
@login_required
def mark_prop_viewed(request):
    if request.method == "POST":
        prop_id = request.POST.get("prop_id")
        if prop_id:
            # Mark the prop as viewed
            prop = Props.objects.get(id=prop_id, recipient=request.user)
            prop.is_viewed = True
            prop.save()

    return redirect("list_props")
