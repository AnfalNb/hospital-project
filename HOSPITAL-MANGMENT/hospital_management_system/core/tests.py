from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import doctor_a, patient_a, hospital_admin

# Create your tests here.

#login unittest
import unittest

def login(username, password):
    if username == "admin" and password == "password":
        return True
    return False

class TestLogin(unittest.TestCase):
    def test_login_success(self):
        self.assertTrue(login("admin", "password"))

    def test_login_failure(self):
        self.assertFalse(login("admin", "wrongpassword"))
        self.assertFalse(login("wrongusername", "password"))
        self.assertFalse(login("wrongusername", "wrongpassword"))

if __name__ == "_main_":
    unittest.main()

# Create your tests here


def login(username, password):
    if username == "admin" and password == "password":
        return True
    return False


class TestLogin(TestCase):
    def test_login_success(self):
        self.assertTrue(login("admin", "password"))

    def test_login_failure(self):
        self.assertFalse(login("admin", "wrongpassword"))
        self.assertFalse(login("wrongusername", "password"))
        self.assertFalse(login("wrongusername", "wrongpassword"))


class UrlTests(SimpleTestCase):
    def test_doctor_url(self):
        response = self.client.get(reverse("doctor_profile"))
        self.assertEqual(response.status_code, 200)

    def test_admin_url(self):  
        response = self.client.get(reverse("admin_profile"))
        self.assertEqual(response.status_code, 200)

    def test_patient_url(self):  
        response = self.client.get(reverse("patient_homepage"))
        self.assertEqual(response.status_code, 200)


class DoctorModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.doctor = doctor_a.objects.create(
            DoctorID="123",
            First_name="First",
            Last_name="Last",
            Phone_Number1="123456789",
            Address="add",
            Email_Address="email@gmai.com",
            Medical_Field="abc",
            password="123",
        )

    def test_model_content(self):
        self.assertEqual(self.doctor.DoctorID, "123")

class PatientModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.patient = patient_a.objects.create(
            patientID="123",
            First_name="First",
            Last_name="Last",
            Address="add",
            Email_Address="email@gmai.com",
            password="123",
        )

    def test_model_content(self):
        self.assertEqual(self.patient.patientID, "123")

class AdminModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin = hospital_admin.objects.create(
            username="name",
            password="123",
        )

    def test_model_content(self):
        self.assertEqual(self.admin.username, "name")  