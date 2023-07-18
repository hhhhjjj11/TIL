from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name} 전문의"
    
# class Patient(models.Model):
#     name =models.TextField()

#     def __str__(self):
#         return f"{self.pk}번 환자 {self.name}"
    
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
#         # doctor 로 foreignkey 잡으면 db에는 doctor_id 언더바 id가 붙어서 들어간다.

class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through = 'Reservation', related_name="patients")
    name =models.TextField()

    def __str__(self):
        return f"{self.pk}번 환자 {self.name}"
    

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptoms = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
        # doctor 로 foreignkey 잡으면 db에는 doctor_id 언더바 id가 붙어서 들어간다.
