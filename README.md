# Fons Clinic - Hospital Management System

## Technical Overview

"Fons Clinic" is a website for a hospital management system that simplifies the process of patient admission to a doctor through appointment scheduling, digital referrals, and communication with doctors. The system supports three types of users: admin, doctor, and patient.

### System Architecture and Structure

The application is built using **Django**, a powerful Python framework, and uses **SQLite** for the database. The system leverages Django's built-in functionalities to manage the data, users, and access permissions.

#### System Components:
1. **Model-View-Template (MVT) Architecture:**
   - **Models:** Data entities (such as patients, doctors, appointments) are defined as models in Django.
   - **Views:** Views are responsible for fetching data from the models and rendering them to the user.
   - **Templates:** HTML files that represent the frontend of the application, using `django-crispy-forms` and `django-widget-tweaks` to enhance form design.

2. **User Access:**
   - **Admin:** Admins can manage users, such as deleting or adding patients and doctors, viewing doctor details, and configuring doctor schedules.
   - **Doctor:** Doctors can view patient histories, approve or reject referrals, and manage appointments.
   - **Patient:** Patients can schedule, update, and cancel appointments, send requests to renew referrals, and communicate with doctors.

#### Technical Features:
1. **Django Framework:**
   The system is based on **Django 4.1.3**, providing a clean separation between backend and frontend, allowing for efficient data management and user authentication.

2. **SQLite Database:**
   The database is managed using **SQLite**, a lightweight database engine suitable for small to medium-scale applications. It allows for local storage of data, making the system portable.

3. **Installation and Configuration:**
   - The project is configured through Python scripts.
   - Database migrations are managed using Django's built-in migration commands.
   - Dependencies are installed via `pip`.

4. **Digital Referrals:**
   The system supports digital referrals, allowing patients to send requests for referral renewals, improving the communication between doctors and patients.

### User Interface:
1. **Patient:**
   - **Appointment Scheduling:** Patients can choose a date and time based on the doctor's availability.
   - **Sending Messages:** Patients can send questions or requests to their doctors.
   - **Medical History:** Patients can view their previous treatments and consult with their doctors.

2. **Doctor:**
   - **Patient View:** Doctors can view detailed information about their patients, recommend treatments, and manage appointments.
   - **Referral Approval:** Doctors can approve or reject referral requests sent by patients.

3. **Admin:**
   - **User Management:** Admins can add, remove, or edit users (patients, doctors), manage their details, and oversee the doctor schedules.

### Access and Permissions Management:
The system provides secure access for different user types, with login authentication and role-based access control for each user:
- Admins have full control over all system functionalities.
- Doctors can manage appointments and referrals for their patients.
- Patients can manage their appointments and communicate with doctors.

### Email Integration:
The system supports email notifications for reminders and alerts related to appointments, referrals, and patient communications.

### Documentation:
The system includes clear documentation for medical staff and administrators, covering patient referrals, appointments, and communication with patients.

---

## How to Run the Project

### Prerequisites:
1. **Python 3.11**.
2. Install **Django 4.1.3** and required dependencies.
3. Set up SQLite as the database.
4. Run migrations to set up the database schema.

### Installation Steps:
1. Install Python 3.11.
2. Clone the project and open it locally.
3. Install Django and the required packages:
   ```bash
   py -m pip install Django
   pip install django-crispy-forms
   pip install django-widget-tweaks ```
4.Run the migrations:
```bash
python manage.py makemigrations
python manage.py migrate --run-syncdb
```
5.Start the server:
```bash
python manage.py runserver
 ```

## License & copyright

© Enas Jaber, Asia Nbary, Orzalena Elsayyed, Anfal Alnbbari.<br>
This project was developed as part of the "FUNDAMENTALS IN SOFTWARE ENGINEERING" course at SCE College.

## Enjoy!
