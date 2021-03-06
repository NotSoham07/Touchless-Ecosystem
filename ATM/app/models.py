from django.db import models
from django.contrib.auth.models import User
# import DO_NOTHING

# Create your models here.


class Account(models.Model):
    BANK_NAMES = (
        ("axis", "Axis Bank"),
        ("sbi", "State Bank of India"),
        ("pnb", "Punjab National Bank"),
        ("icici", "ICICI Bank"),
        ("hdfc", "HDFC Bank"),
        ("citi", "Citi Bank"),
        ("indus", "IndusInd Bank"),
        ("idbi", "IDBI Bank"),
        ("bob", "Bank of Baroda"),
    )
    account_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bank_name = models.CharField(
        max_length=100, choices=BANK_NAMES, default="axis")
    ifsc = models.CharField(max_length=100, default="UTI0025")
    branch_name = models.CharField(
        max_length=100, default="Kalyan(West) UI0025")
    pin = models.CharField(max_length=4)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.account_id) + str("|") + str(self.name)


class Transfer(models.Model):
    transfer_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(
        Account, on_delete=models.DO_NOTHING, related_name='sender')
    receiver = models.ForeignKey(
        Account, on_delete=models.DO_NOTHING, related_name='receiver')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.transfer_id)


class Image(models.Model):
    Main_Img = models.ImageField(upload_to='images/')
