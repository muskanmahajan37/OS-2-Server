from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from .models import *
from .serializer import *
from django.core.mail import send_mail

# Create your views here.


def portfolio(request):
    context = {
        "projects": Project.objects.all().order_by("-id")[:3],
        "title": "Raghav Dhingra | Portfolio Profile | Portfolio.OS",
        "testimonials": Testimonial.objects.all(),
    }
    return render(request, 'portfolio.html', context)


def submitForm(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        html_format = " Name: {} \n Subject: {} \n Email: {} \n Message: {}".format(
            name, subject, email, message)
        try:
            send_mail(
                str(subject),
                str(html_format),
                'admin@raghavdhingra.com',
                ['admin@raghavdhingra.com', email],
                fail_silently=False,
            )
            return redirect("/")

        except Exception as e:
            print(e)
            return redirect("/")

    return redirect('/')


def projects(request):
    context = {
        "title": "Raghav Dhingra | Projects | Portfolio.OS",
        "testimonials": Testimonial.objects.all(),
        "projects": Project.objects.all().order_by("-id"),
    }
    return render(request, 'projects.html', context)


def whatsapp(request):
    return redirect("https://wa.me/919315387893")


def facebook(request):
    return redirect("https://www.facebook.com/raghav.dhingra15")


def twitter(request):
    return redirect("https://twitter.com/raghavdhingra15")


def linkedin(request):
    return redirect("https://www.linkedin.com/in/raghav-dhingra/")


def github(request):
    return redirect("https://github.com/raghavdhingra")


def codepen(request):
    return redirect("https://codepen.io/raghav-dhingra")


def instagram(request):
    return redirect("https://www.instagram.com/raghav.dhingra15/")


def telegram(request):
    return redirect("https://t.me/raghavdhingra")


def medium(request):
    return redirect("https://medium.com/@raghav.dhingra15")


def mail(request):
    context = {}
    return render(request, "mail.html", context)


def mobile(request):
    context = {}
    return render(request, "phone.html", context)


class AllProjects(APIView):

    def get(self, request):
        context = {
            "projects": ProjectSerializer(Project.objects.all().order_by("-id"), many=True).data,
            "message": "Project fetched successfully",
            "status": "success"
        }
        return Response(context, status=200)


class AllTestimonials(APIView):

    def get(self, request):
        context = {
            "projects": TestimonialSerializer(Testimonial.objects.all().order_by("-id"), many=True).data,
            "message": "Testimonials fetched successfully",
            "status": "success"
        }
        return Response(context, status=200)