from django.db import models

# Create your models here.


class Felhasznalo(models.Model):
    fel_nev = models.CharField(max_length=25)
    jelszo = models.CharField(max_length=25)
    def __str__(self):
        return self.fel_nev


class Kutyak(models.Model):
    osszekoto = models.ForeignKey(Felhasznalo, on_delete=models.CASCADE)
    kutya_neve = models.CharField(max_length=30)
    fajta = models.CharField(max_length=30)
    kutya_szuletese = models.DateTimeField("date published")
    kutya_szuletese2 = models.DateField()
    kutya_testomeg = models.IntegerField(default=30)
    kutya_eletkora = models.PositiveIntegerField()
    NEMEK = [
        ("K", "Kan"),
        ("SZ", "Szuka"),
        ("E", "Egyéb"),
        ("S-S-F", "Samsung-Smart-Fridge"),
        ("E-1942-PA-T", "Eredeti 1942 panzerkampfwagen Hiir TIGRIS"),
        ("C-K-H-69", "Civil-Killer-hellikopter-69"),
    ]
    kutya_neme = models.CharField(max_length=11, choices=NEMEK)
    megjegyzes = models.TextField()
    ivartalanitott_e = models.BooleanField(default=False)
    bolhas = models.BooleanField(default=True)
    kullancs_fertozott = models.BooleanField(default=True)
    def __str__(self):
        return self.kutya_neve
    
    def kutya_eletkor_megallapito(self):
        if 0 < self.kutya_eletkora <= 2:
            return "Baby dog"
        elif 3 < self.kutya_eletkora <= 5:
            return "Child dog"
        elif 6 < self.kutya_eletkora <= 10:
            return "Serdülő dog"
        elif 11 < self.kutya_eletkora <= 15:
            return "adult dog"
        elif 12 < self.kutya_eletkora <= 20:
            return "old dog R.I.P"
        else:
            return "God/Evil/half-blood Doggo"

    @property
    def full_name(self):
        return f"{self.kutya_neve} {self.fajta} {self.kutya_eletkora} {self.kutya_neme}"





