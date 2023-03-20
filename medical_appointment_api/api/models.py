from django.db import models

class Doctor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    med_specialization = models.CharField(
        max_length=2,
        choices= [
            ('OR', 'Orthopedist'),
            ('OP', 'Ophthalmologist'),
            ('GP', 'General Practitioner')
        ],
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.med_specialization}"

class Appointment(models.Model):
    appointment_time = models.TimeField()
    appointment_date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.appointment_date} {self.appointment_time}"


