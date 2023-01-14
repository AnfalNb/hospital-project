from django.test import TestCase
from django.urls import reverse
from .models import *
# Create your tests here.

from datetime import datetime, timedelta

class MedicalReferralTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.instance = MedicalReferral.objects.create(
            name_referral='Test Referral',
            start_time=datetime.now(),
            end_time=datetime.now() + timedelta(days=30),
            patient_id='12345'
        )

    def test_referrals_renewing(self):
        request = self.factory.get(reverse('renwe_ref'))
        response = referrals_renewing(request, self.instance.pk)
        self.instance.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            self.instance.start_time,
            datetime.now() + timedelta(days=90)
        )
        self.assertEqual(
            self.instance.end_time,
            datetime.now() + timedelta(days=120)
        )
        