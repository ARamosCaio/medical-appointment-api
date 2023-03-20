from tastypie.resources import ModelResource
from api.models import Doctor, Appointment
from tastypie.authorization import Authorization
from tastypie import fields

class DoctorResource(ModelResource):
    class Meta:
        queryset = Doctor.objects.all()
        res_name = 'doctor'
        authorization = Authorization()


class AppointmentResource(ModelResource):
    doctor = fields.ForeignKey(DoctorResource, "doctor")
    class Meta:
        queryset = Appointment.objects.all()
        res_name = 'appointment'        
        authorization = Authorization()

 