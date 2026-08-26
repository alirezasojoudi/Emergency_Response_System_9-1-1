# 🚨 Emergency Response System (9-1-1)

A Python-based emergency response prototype with a graphical user interface for handling emergency requests and dispatching the appropriate emergency service.

## 📌 Overview

**Emergency Response System** is a desktop application designed to demonstrate the basic workflow of an emergency response platform.

The application allows an operator to select an emergency service, collect information from the caller, validate the submitted data, create an emergency request, and dispatch the appropriate service.

The current version supports three emergency services:

* 🚓 Police
* 🚑 Ambulance
* 🚒 Fire Station

The project is structured using separate modules for models, user interface, validation, logging, and testing.

## ✨ Features

* 🖥️ Graphical user interface built with Tkinter
* 🚓 Police emergency requests
* 🚑 Ambulance emergency requests
* 🚒 Fire station emergency requests
* 👤 Caller information management
* 📍 Emergency location input
* 📝 Emergency description
* ☎️ Phone number validation
* 🔤 Name validation
* 📍 Location validation
* 📋 Emergency request creation
* 🚨 Service dispatch workflow
* 📝 Application event logging
* 🧪 Basic automated/manual test scenarios
* 🧩 Modular object-oriented architecture

## 🏗️ Project Structure

```text
Emergency-Response-System/
│
├── .gitignore
├── main.py
│
└── project/
    │
    ├── __init__.py
    ├── .gitignore
    │
    ├── models/
    │   ├── __init__.py
    │   ├── person.py
    │   ├── caller.py
    │   ├── emergency_request.py
    │   ├── emergency_service.py
    │   ├── ambulance_service.py
    │   ├── police_service.py
    │   └── fire_service.py
    │
    ├── tools/
    │   ├── __init__.py
    │   ├── logger.py
    │   └── validator.py
    │
    ├── view/
    │   ├── __init__.py
    │   ├── emergency_form.py
    │   ├── icons_view.py
    │   └── icon_picture/
    │       ├── police.png
    │       ├── ambulance.png
    │       └── fire.png
    │
    └── test/
        ├── __init__.py
        └── test_all.py
```

## 🔄 Application Workflow

```text
Start Application
       │
       ▼
Emergency Service Selection
       │
       ├── Police
       ├── Ambulance
       └── Fire Station
              │
              ▼
       Emergency Form
              │
              ├── Name
              ├── Phone
              ├── Location
              └── Description
              │
              ▼
        Input Validation
              │
              ▼
       Create EmergencyRequest
              │
              ▼
       Dispatch Service
              │
              ▼
       Log Emergency Request
              │
              ▼
        Success Message
```

## 🧱 Architecture

The project follows a simple object-oriented and modular design.

### Models

The `models` package contains the main domain objects and emergency services.

* `Person` stores basic personal information.
* `Caller` represents the person requesting emergency assistance.
* `EmergencyRequest` represents an emergency request.
* `EmergencyService` provides the base service interface.
* `PoliceService` handles police dispatch.
* `AmbulanceService` handles ambulance dispatch.
* `FireService` handles fire station dispatch.

### View

The `view` package contains the graphical user interface.

`icons_view.py` provides the main service-selection window, while `emergency_form.py` provides the emergency request form.

### Tools

The `tools` package contains reusable utilities:

* `Validator` validates names, phone numbers, and locations.
* `Logger` provides application logging.

### Tests

The `test` package contains test scenarios covering the main classes and emergency services.

## 🛠️ Technologies

* **Python 3**
* **Tkinter** — Graphical User Interface
* **Pillow (PIL)** — Image handling
* **Regular Expressions** — Input validation
* **Python Logging** — Application logging
* **Object-Oriented Programming (OOP)**

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/alirezasojoudi/Emergency-Response-System.git
cd Emergency-Response-System
```

### 2. Create a virtual environment

#### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Install Pillow:

```bash
pip install Pillow
```

Tkinter is normally included with standard Python installations on Windows.

## ▶️ Running the Application

From the repository root:

```bash
python main.py
```

The main window should open and provide three emergency service options:

1. Police
2. Ambulance
3. Fire Station

Select a service, enter the caller information and emergency details, then submit the request.

## 🧪 Running the Tests

From the repository root:

```bash
python -m project.test.test_all
```

The test script demonstrates the main functionality of the system, including:

* `Person`
* `Caller`
* `EmergencyRequest`
* `PoliceService`
* `AmbulanceService`
* `FireService`

## 🔐 Validation

The application validates user input before creating an emergency request.

Currently, validation includes:

* **Name:** English alphabetic characters
* **Location:** Alphabetic characters and spaces
* **Phone:** Iranian phone number format

Invalid input results in an error message instead of creating the request.

## 📝 Logging

The application uses Python's built-in `logging` module to record application events and emergency requests.

Logging is used for events such as:

* Opening an emergency service window
* Creating emergency requests
* Recording information about dispatched requests
* Recording errors

> **Note:** The current implementation contains a machine-specific log-file path. For better portability, this path should be converted to a relative project path in a future version.

## 🖼️ User Interface

The application provides a simple desktop interface with dedicated buttons for:

* 🚓 Police
* 🚑 Ambulance
* 🚒 Fire Station

Each service opens its own emergency request form.

## ⚠️ Current Limitations

This project is currently a **prototype / educational implementation**.

The current version does not yet provide:

* Real emergency-service communication
* Real ambulance or police tracking
* GPS location detection
* Online maps
* Database persistence
* Authentication
* User accounts
* Real-time communication
* Cloud deployment
* AI-based emergency classification
* Automatic nearest-service selection
* Real-world emergency dispatch

These features can be considered for future development.

## 🚀 Future Improvements

Possible improvements include:

* 🗺️ GPS and map integration
* 📍 Automatic location detection
* 🚑 Nearest ambulance selection
* 🚓 Nearest police unit selection
* 🚒 Nearest fire station selection
* 🗄️ Database integration
* 👥 User and operator authentication
* 🌐 Web-based operator dashboard
* 🔔 Real-time notifications
* 📡 API-based communication
* 🤖 AI-assisted emergency classification
* 📊 Emergency statistics and reporting
* 🧪 Expanded unit and integration testing
* ⚙️ Configuration-based file paths
* 📦 Improved dependency management with `requirements.txt`

## 🎯 Project Goal

The goal of this project is to demonstrate how a basic emergency response workflow can be modeled using Python, object-oriented programming, modular architecture, input validation, logging, and a graphical user interface.

It can serve as a foundation for developing a more complete emergency management and dispatch platform.

## 📄 License

This project is currently provided for educational and development purposes.

## 👨‍💻 Author

**Alireza Sojoudi**

GitHub: [alirezasojoudi](https://github.com/alirezasojoudi)
