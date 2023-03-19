from tastypie.resources import ModelResource
from api.models import Doctor, Appointment
from tastypie.authorization import Authorization

class DoctorResource(ModelResource):
    class Meta:
        queryset = Doctor.objects.all()
        res_name = 'doctor'
        authorization = Authorization()


class AppointmentResource(ModelResource):
    class Meta:
        queryset = Appointment.objects.all()
        res_name = 'appointment'        
        authorization = Authorization()