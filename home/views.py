from django.shortcuts import render, redirect


def main_view(request):

    if not request.user.is_authenticated:
        return redirect('account:login')

    return render(request, "home.html", {})
