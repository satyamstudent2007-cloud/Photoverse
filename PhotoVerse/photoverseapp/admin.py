from django.contrib import admin
from .models import *


@admin.register(User)
class ShowUsers(admin.ModelAdmin):
    list_display = ["name", "email", "password", "dateJoined"]
    list_filter = ["dateJoined"]
    search_fields = ["name", "email"]
    list_per_page = 10


@admin.register(Country)
class ShowCountry(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(State)
class ShowStates(admin.ModelAdmin):
    list_display = ["country", "name"]
    list_filter = ["country"]
    search_fields = ["name", "country__name"]


@admin.register(City)
class ShowCity(admin.ModelAdmin):
    list_display = ["state", "name"]
    list_filter = ["state"]
    search_fields = ["name", "state__name"]


@admin.register(UserProfile)
class ShowUserProfile(admin.ModelAdmin):
    list_display = [
        "user",
        "phoneNo",
        "address",
        "UserProfileImage",
        "city",
        "state",
        "country"
    ]
    list_filter = ["country", "state", "city"]
    search_fields = ["user__name", "phoneNo"]


@admin.register(Photographer)
class ShowPhotographer(admin.ModelAdmin):
    list_display = [
        "name",
        "specialities",
        "experienceYears",
        "rating",
        "timestamp"
    ]
    list_filter = ["experienceYears"]
    search_fields = ["name", "specialities"]
    list_per_page = 10


@admin.register(Portfolio)
class ShowPortfolio(admin.ModelAdmin):
    list_display = [
        "photographer",
        "title",
        "description",
        "timestamp"
    ]
    list_filter = ["photographer"]
    search_fields = ["title", "photographer__name"]


@admin.register(Photo)
class ShowPhotos(admin.ModelAdmin):
    list_display = [
        "portfolio",
        "caption",
        "PhotoImage",
        "orderId",
        "orderStatus",
        "uploadedAt"
    ]
    list_filter = ["orderStatus"]
    search_fields = ["caption", "orderId"]
    list_per_page = 5


@admin.register(Booking)
class ShowBookings(admin.ModelAdmin):
    list_display = [
        "user",
        "photographer",
        "bookingDate",
        "eventDate",
        "status",
        "timestamp"
    ]
    list_filter = ["status"]
    search_fields = [
        "user__name",
        "photographer__name"
    ]


@admin.register(Payment)
class ShowPayments(admin.ModelAdmin):
    list_display = [
        "user",
        "booking",
        "amount",
        "paymentMethod",
        "paymentStatus",
        "paymentDate",
        "timestamp"
    ]
    list_filter = [
        "paymentMethod",
        "paymentStatus"
    ]
    search_fields = [
        "user__name",
        "booking__id"
    ]


@admin.register(Feedback)
class ShowFeedback(admin.ModelAdmin):
    list_display = [
        "user",
        "booking",
        "rating",
        "comment",
        "reviewDate",
        "timestamp"
    ]
    list_filter = ["rating"]
    search_fields = [
        "user__name",
        "comment"
    ]


@admin.register(ContactUs)
class ShowContactUs(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "subject",
        "phone",
        "timestamp"
    ]
    search_fields = [
        "name",
        "email",
        "subject"
    ]
    list_filter = ["timestamp"]


admin.site.site_header = "PhotoVerse Administration"
admin.site.site_title = "PhotoVerse Admin"
admin.site.index_title = "Welcome To PhotoVerse Dashboard"