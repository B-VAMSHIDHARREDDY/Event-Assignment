# IoT Project

## Overview

This project focuses on storing IoT device events. It features a Django backend with a MySQL database and a React frontend. The backend provides RESTful APIs to manage IoT events, while the frontend is used to interact with these APIs.

## Features

- **Data Model:** Stores IoT device events.
- **REST API:** Receives events from various sources like cloud services and MQTT.
- **Service Layer:** General design to support any persistence layer.
- **Event Queries:** Retrieve events by device and date range.
- **Summary Reports:** Generate summary reports including max, min, and average temperature per device for a given date range.

## Technical Stack

- **Backend:** Django 4.2.7
- **Database:** MySQL
- **Frontend:** React
- **ORM:** SQLAlchemy (for a generic design) and Django ORM
- **Testing:** pytest, mock
- **Code Quality:** SonarQube
- **UI Framework:** React (instead of Angular or Vue JS)

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js (for React)
- MySQL server
- `pip` (Python package installer)
- `npm` (Node.js package manager)

# Backend Setup

# Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

# Install Backend Dependencies
```
pip install -r requirements.txt
```
## Configure the Database
### Update `DATABASES` settings in `iot_project/settings.py` with your MySQL credentials
#### Example configuration:
```properties
DATABASES = {
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'iot_db',
        'USER': 'user',
       'PASSWORD': 'password',
       'HOST': 'localhost',
       'PORT': '3306',
   }
}
```

### Run Migrations
```properties
python manage.py migrate
```

### Create a Superuser (Optional, for Django Admin)
```
python manage.py createsuperuser
```

### Run the Development Server
```
python manage.py runserver
```


# Frontend Setup

### Navigate to the React Project Directory
```properties
cd iot-frontend
```
### Install Frontend Dependencies
```properties
npm install
```

### Run the React Development Server
```properties
npm start
```  



# API Documentation
### Postman published documentation: [https://documenter.getpostman.com/view/19430621/2sAXjRXqJh]



