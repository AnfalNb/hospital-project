from django.test import TestCase

# Create your tests here.
from .models import *
from datetime import date

#---------------------------PatientSignUpTest---------------------------------
class PatientSignUpTest(TestCase):
    def test_sign_up(self):
        # Create a new patient object with some test data
        patient = patient_a(patientֹID='123', First_name='John', Last_name='Doe', Phone_Number='1234567890', Address='123 Main St', Email_Address='johndoe@example.com', Birth_Date='2000-01-01', password_patientֹ='password')
        patient.save()

        # Retrieve the patient object from the database
        retrieved_patient = patient_a.objects.get(patientֹID='123')

        # Check that the patient object matches the test data
        self.assertEqual(retrieved_patient.First_name, 'John')
        self.assertEqual(retrieved_patient.Last_name, 'Doe')
        self.assertEqual(retrieved_patient.Phone_Number, '1234567890')
        self.assertEqual(retrieved_patient.Address, '123 Main St')
        self.assertEqual(retrieved_patient.Email_Address, 'johndoe@example.com')
        self.assertEqual(retrieved_patient.Birth_Date, '2000-01-01')
        self.assertEqual(retrieved_patient.password_patientֹ, 'password')


#---------------------------PatientSignUpTest---------------------------------
class PatientSignUpTest(TestCase):
    def test_sign_up(self):
        # Create a new patient object with some test data
        patient = patient_a(patientֹID='123', First_name='John', Last_name='Doe', Phone_Number='1234567890', Address='123 Main St', Email_Address='johndoe@example.com', Birth_Date='2000-01-01', password_patientֹ='password')
        patient.save()

        # Retrieve the patient object from the database
        retrieved_patient = patient_a.objects.get(patientֹID='123')

        # Check that the patient object matches the test data
        self.assertEqual(retrieved_patient.First_name, 'John')
        self.assertEqual(retrieved_patient.Last_name, 'Doe')
        self.assertEqual(retrieved_patient.Phone_Number, '1234567890')
        self.assertEqual(retrieved_patient.Address, '123 Main St')
        self.assertEqual(retrieved_patient.Email_Address, 'johndoe@example.com')
        self.assertEqual(retrieved_patient.Birth_Date, date(2000, 1, 1))
        self.assertEqual(retrieved_patient.password_patientֹ, 'password')

#---------------------------DoctorSignUpTest---------------------------------
from .models import doctor_a
import tempfile
from django.core.files import File

class DoctorSignUpTest(TestCase):
    def test_sign_up(self):
        # Create a temporary file to use as the file diploma
        with tempfile.NamedTemporaryFile(suffix='.pdf') as f:
            diploma_file = File(f)

            # Create a new doctor object with some test data
            doctor = doctor_a(DoctorID='123', First_name='John', Last_name='Doe', Phone_Number1='1234567890', Address='123 Main St', Email_Address='johndoe@example.com', Birth_Date='2000-01-01', Medical_Field='Surgery', File_Diploma=diploma_file, password_Doctor='password')
            doctor.save()

            # Retrieve the doctor object from the database
            retrieved_doctor = doctor_a.objects.get(DoctorID='123')

            # Check that the doctor object matches the test data
            self.assertEqual(retrieved_doctor.First_name, 'John')
            self.assertEqual(retrieved_doctor.Last_name, 'Doe')
            self.assertEqual(retrieved_doctor.Phone_Number1, '1234567890')
            self.assertEqual(retrieved_doctor.Address, '123 Main St')
            self.assertEqual(retrieved_doctor.Email_Address, 'johndoe@example.com')
            self.assertEqual(retrieved_doctor.Birth_Date, date(2000, 1, 1))
            self.assertEqual(retrieved_doctor.Medical_Field, 'Surgery')
            self.assertIsInstance(retrieved_doctor.File_Diploma, File)
            self.assertEqual(retrieved_doctor.password_Doctor, 'password')


#---------------------------LoginPatientTest---------------------------------
from django.urls import reverse
from .models import patient_a

class LoginPatientTest(TestCase):
    def setUp(self):
        self.valid_patient = patient_a.objects.create(patientֹID='123', First_name='John', Last_name='Doe', Phone_Number='1234567890', Address='123 Main St', Email_Address='johndoe@example.com', Birth_Date='2000-01-01', password_patientֹ='password')
        
    def test_login_patient_valid_credentials(self):
        response = self.client.post(reverse('login_patient'), {'p_id': '123', 'p_password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('patient_homepage'))
        self.assertEqual(response.wsgi_request.session['patient_id'], '123')

  

#------------------------------LoginDoctorTest-------------------------------------
from django.urls import reverse

class LoginDoctorTest(TestCase):
    def setUp(self):
        self.valid_doctor = doctor_a.objects.create(DoctorID='123', First_name='John', Last_name='Doe', Phone_Number1='1234567890', Address='123 Main St', Email_Address='johndoe@example.com', Birth_Date='2000-01-01', Medical_Field='General', File_Diploma='', password_Doctor='password')
        self.invalid_doctor_id = doctor_a.objects.create(DoctorID='124', First_name='Jane', Last_name='Doe', Phone_Number1='1234567890', Address='123 Main St', Email_Address='janedoe@example.com', Birth_Date='2000-01-01', Medical_Field='General', File_Diploma='', password_Doctor='password')
        self.invalid_doctor_password = doctor_a.objects.create(DoctorID='125', First_name='Mike', Last_name='Doe', Phone_Number1='1234567890', Address='123 Main St', Email_Address='mikedoe@example.com', Birth_Date='2000-01-01', Medical_Field='General', File_Diploma='', password_Doctor='wrongpassword')
    
    def test_login_doctor_valid_credentials(self):
        print("test_login_doctor_valid_credentials")
        response = self.client.post(reverse('login_Doctor'), {'doc_id': '123', 'doc_password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('doctor_profile'))
        self.assertEqual(response.wsgi_request.session['DoctorID'], '123')

    def test_login_doctor_invalid_doctor_id(self):
        print("test_login_doctor_invalid_doctor_id")
        response = self.client.post(reverse('login_Doctor'), {'doc_id': '124', 'doc_password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login_Doctor'))

    def test_login_doctor_invalid_password(self):
        print("test_login_doctor_invalid_password")
        response = self.client.post(reverse('login_Doctor'), {'doc_id': '125', 'doc_password': 'wrongpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login_Doctor'))



#=============================AdminLoginTest===================================
from django.urls import reverse

class AdminLoginTest(TestCase):
    def setUp(self):
        self.valid_admin = hospital_admin.objects.create(username='admin', password='password')
        self.invalid_admin_username = hospital_admin.objects.create(username='wrongadmin', password='password')
        self.invalid_admin_password = hospital_admin.objects.create(username='admin', password='wrongpassword')
    
    def test_admin_login_valid_credentials(self):
        print("test_admin_login_valid_credentials")
        response = self.client.post(reverse('AdminLogin'), {'username': 'admin', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_profile.html')

    def test_admin_login_invalid_username(self):
        print("test_admin_login_invalid_username")
        response = self.client.post(reverse('AdminLogin'), {'username': 'wrongadmin', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('AdminLogin'))
    
    def test_admin_login_invalid_password(self):
        print("test_admin_login_invalid_password")
        response = self.client.post(reverse('AdminLogin'), {'username': 'admin', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('AdminLogin'))

#=========================test_patient_test_patient_list_view==================================
#=========================test_doctor_list_view==================================

from django.test import TestCase
from django.urls import reverse
from .models import patient_a, doctor_a

class PatientDoctorListTest(TestCase):
    def setUp(self):
        self.patient1 = patient_a.objects.create(patientֹID='123', First_name='John', Last_name='Doe', Phone_Number='1234567890', Address='123 Main St', Email_Address='johndoe@example.com', Birth_Date='2000-01-01', password_patientֹ='password')
        self.patient2 = patient_a.objects.create(patientֹID='124', First_name='Jane', Last_name='Doe', Phone_Number='1234567890', Address='123 Main St', Email_Address='janedoe@example.com', Birth_Date='2000-01-01', password_patientֹ='password')
        self.doctor1 = doctor_a.objects.create(DoctorID='456', First_name='Mike', Last_name='Smith', Phone_Number1='1234567890', Address='456 Main St', Email_Address='mikesmith@example.com', Birth_Date='1990-01-01', Medical_Field='Surgery', password_Doctor='password')
        self.doctor2 = doctor_a.objects.create(DoctorID='457', First_name='Amy', Last_name='Johnson', Phone_Number1='1234567890', Address='789 Main St', Email_Address='amyjohnson@example.com', Birth_Date='1980-01-01', Medical_Field='Pediatrics', password_Doctor='password')
    print("PatientDoctorListTest")
    def test_patient_test_patient_list_view(self):
        response = self.client.get(reverse('patientList'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patientList.html')
        self.assertContains(response, self.patient1.patientֹID)
        self.assertContains(response, self.patient1.First_name)
        self.assertContains(response, self.patient1.Last_name)
        self.assertContains(response, self.patient1.Phone_Number)
        self.assertContains(response, self.patient1.Address)
        self.assertContains(response, self.patient1.Email_Address)
        self.assertContains(response, self.patient1.Birth_Date)
        self.assertContains(response, self.patient2.patientֹID)
        self.assertContains(response, self.patient2.First_name)
        self.assertContains(response, self.patient2.Last_name)
        self.assertContains(response, self.patient2.Phone_Number)
        self.assertContains(response, self.patient2.Address)
        self.assertContains(response, self.patient2.Email_Address)
        self.assertContains(response, self.patient2.Birth_Date)

    def test_doctor_list_view(self):
        response = self.client.get(reverse('doctorList'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctorList.html')
        self.assertContains(response, self.doctor1.DoctorID)
        self.assertContains(response, self.doctor1.First_name)
        self.assertContains(response, self.doctor1.Last_name)
        self.assertContains(response, self.doctor1.Phone_Number1)
        self.assertContains(response, self.doctor1.Address)
        self.assertContains(response, self.doctor1.Email_Address)
        self.assertContains(response, self.doctor1.Birth_Date)
        self.assertContains(response, self.doctor1.Medical_Field)
        self.assertContains(response, self.doctor2.DoctorID)
        self.assertContains(response, self.doctor2.First_name)
        self.assertContains(response, self.doctor2.Last_name)
        self.assertContains(response, self.doctor2.Phone_Number1)
        self.assertContains(response, self.doctor2.Address)
        self.assertContains(response, self.doctor2.Email_Address)
        self.assertContains(response, self.doctor2.Birth_Date)
        self.assertContains(response, self.doctor2.Medical_Field)


#============================================================================
from django.test import TestCase
from django.urls import reverse
from .models import patient_a
from .forms import patientform

class UpdatePatientTest(TestCase):
    def setUp(self):
        self.patient = patient_a.objects.create(patientֹID='123', First_name='John', Last_name='Doe', Phone_Number='1234567890', Address='123 Main St', Email_Address='johndoe@example.com', Birth_Date='2000-01-01', password_patientֹ='password')

    def test_update_patient(self):
        response = self.client.get(reverse('update_patient', args=[self.patient.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_patient.html')
        self.assertContains(response, self.patient.patientֹID)
        self.assertContains(response, self.patient.First_name)
        self.assertContains(response, self.patient.Last_name)
        self.assertContains(response, self.patient.Phone_Number)
        self.assertContains(response, self.patient.Address)
        self.assertContains(response, self.patient.Email_Address)
        self.assertContains(response, self.patient.Birth_Date)
        self.assertContains(response, self.patient.password_patientֹ)
            # Test updating the patient
        new_data = {
            'patientֹID': '123',
            'First_name': 'Jane',
            'Last_name': 'Doe',
            'Phone_Number': '0987654321',
            'Address': '456 Elm St',
            'Email_Address': 'janedoe@example.com',
            'Birth_Date': '1995-12-31',
            'password_patientֹ': 'password',
        }
        response = self.client.post(reverse('update_patient', args=[self.patient.pk]), data=new_data)
        self.assertRedirects(response, reverse('patient_homepage'))

        # Check that the patient was actually updated in the database
        updated_patient = patient_a.objects.get(pk=self.patient.pk)
        self.assertEqual(updated_patient.First_name, 'Jane')
        self.assertEqual(updated_patient.Last_name, 'Doe')
        self.assertEqual(updated_patient.Phone_Number, '0987654321')
        self.assertEqual(updated_patient.Address, '456 Elm St')
        self.assertEqual(updated_patient.Email_Address, 'janedoe@example.com')
        self.assertEqual(updated_patient.Birth_Date, '1995-12-31')
        self.assertEqual(updated_patient.password_patientֹ, 'password')

#---------------------------UpdateDoctorTest------------------------------
from django.test import TestCase
from django.urls import reverse
from .models import doctor_a
from .forms import doctorupdateform

class UpdateDoctorTest(TestCase):
    def setUp(self):
        self.doctor = doctor_a.objects.create(DoctorID='123', First_name='John', Last_name='Doe', Phone_Number1='1234567890', Address='123 Main St', Email_Address='johndoe@example.com', Birth_Date='2000-01-01', Medical_Field='Cardiology', File_Diploma='',password_Doctor='password')

    def test_update_doctor(self):
        response = self.client.get(reverse('update_doctor', args=[self.doctor.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_doctor.html')
        self.assertContains(response, self.doctor.DoctorID)
        self.assertContains(response, self.doctor.First_name)
        self.assertContains(response, self.doctor.Last_name)
        self.assertContains(response, self.doctor.Phone_Number1)
        self.assertContains(response, self.doctor.Address)
        self.assertContains(response, self.doctor.Email_Address)
        self.assertContains(response, self.doctor.Birth_Date)
        self.assertContains(response, self.doctor.Medical_Field)
        self.assertContains(response, self.doctor.File_Diploma)
        self.assertContains(response, self.doctor.password_Doctor)


#-========================================DoctorDetailViewTest============================================

from django.test import TestCase
from django.urls import reverse
from .models import doctor_a

class DoctorDetailViewTest(TestCase):
    def setUp(self):
        self.doctor = doctor_a.objects.create(DoctorID='123', First_name='John', Last_name='Doe', Phone_Number1='1234567890', Address='123 Main St', Email_Address='johndoe@example.com', Birth_Date='2000-01-01', Medical_Field='Cardiology', File_Diploma='',password_Doctor='password')

    def test_doctor_detail_view(self):
        response = self.client.get(reverse('doctor_detail', args=[self.doctor.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctor_detail.html')
        self.assertContains(response, self.doctor.DoctorID)
        self.assertContains(response, self.doctor.First_name)
        self.assertContains(response, self.doctor.Last_name)
        self.assertContains(response, self.doctor.Phone_Number1)
        self.assertContains(response, self.doctor.Address)
        self.assertContains(response, self.doctor.Email_Address)
        self.assertContains(response, self.doctor.Birth_Date)
        self.assertContains(response, self.doctor.Medical_Field)
        self.assertContains(response, self.doctor.File_Diploma)
        self.assertContains(response, self.doctor.password_Doctor)


#=====================================DeleteDoctorTest========================================
from django.test import TestCase
from django.urls import reverse
from .models import doctor_a

class DeleteDoctorTest(TestCase):
    def setUp(self):
        self.doctor = doctor_a.objects.create(DoctorID='123', First_name='John', Last_name='Doe', Phone_Number1='1234567890', Address='123 Main St', Email_Address='johndoe@example.com', Birth_Date='2000-01-01', Medical_Field='Cardiology', File_Diploma='',password_Doctor='password')

    def test_delete_doctor(self):
        # Test that the doctor exists in the database before deletion
        self.assertTrue(doctor_a.objects.filter(DoctorID='123').exists())

        # Test that the doctor is deleted successfully
        response = self.client.get(reverse('delete_doctor', args=[self.doctor.pk]))
        self.assertRedirects(response, reverse('doctorList'))

        # Test that the doctor no longer exists in the database after deletion
        self.assertFalse(doctor_a.objects.filter(DoctorID='123').exists())

#=====================================DeletePatientTest=========================================

from django.test import TestCase
from django.urls import reverse
from .models import patient_a

class DeletePatientTest(TestCase):
    def setUp(self):
        self.patient = patient_a.objects.create(patientֹID='123', First_name='John', Last_name='Doe', Phone_Number='1234567890', Address='123 Main St', Email_Address='johndoe@example.com', Birth_Date='2000-01-01',password_patientֹ='password')

    def test_delete_patient(self):
        response = self.client.get(reverse('delete_patient', args=[self.patient.pk]))
        self.assertRedirects(response, reverse('patientList'))

        # Check that the patient was actually deleted from the database
        with self.assertRaises(patient_a.DoesNotExist):
            patient_a.objects.get(pk=self.patient.pk)

#================================================================================================