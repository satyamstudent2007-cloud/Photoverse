from django.db import models
from django.utils.safestring import mark_safe


class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=60)
    dateJoined = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField()
    address = models.TextField()
    phoneNo = models.CharField(max_length=10)
    image = models.ImageField(upload_to="UserProfiles")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def UserProfileImage(self):
        return mark_safe('<img src={} width="100px">'.format(self.image.url))

    def __str__(self):
        return self.user.name


class Photographer(models.Model):
    name = models.CharField(max_length=60)
    bio = models.TextField()
    specialities = models.CharField(max_length=200)
    experienceYears = models.IntegerField()
    rating = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Portfolio")
    caption = models.CharField(max_length=200)
    uploadedAt = models.DateTimeField(auto_now=True)
    orderId = models.CharField(max_length=60)
    orderStatus = models.CharField(
        max_length=60,
        choices=[
            ("active", "Active"),
            ("inactive", "Inactive")
        ]
    )

    def PhotoImage(self):
        return mark_safe('<img src={} width="100px">'.format(self.image.url))

    def __str__(self):
        return self.caption


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    bookingDate = models.DateField()
    eventDate = models.DateField()
    status = models.CharField(
        max_length=60,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("completed", "Completed"),
            ("canceled", "Canceled")
        ]
    )

    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.name} / {self.photographer.name}"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.FloatField()
    paymentMethod = models.CharField(
        max_length=60,
        choices=[
            ("credit_card", "Credit Card"),
            ("debit_card", "Debit Card"),
            ("paypal", "Paypal"),
            ("other", "Other")
        ]
    )
    paymentStatus = models.CharField(
        max_length=60,
        choices=[
            ("pending", "Pending"),
            ("completed", "Completed"),
            ("failed", "Failed")
        ]
    )
    paymentDate = models.DateField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.booking.id)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    reviewDate = models.DateField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.name} - {self.rating}"


class ContactUs(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    phone = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name