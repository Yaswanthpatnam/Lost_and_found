#  Lost & Found Web App

A Django-based web application for managing lost and found items in a community (e.g., college, office, public spaces).  
The platform allows users to report **found** items, search for **lost** items, and connect with the rightful owner.

---

## ✨ Features

- **User Authentication**  
  - Registration and Login  
  - Secure password hashing  

- **Lost & Found Posting**  
  - Add found items with details (description, location, image)    
  - Attach images for better identification  

- **Search & Filter**  
  - Search items by keywords  
  - Filter by category or date  

- **Responsive UI**  
  - Mobile-friendly Bootstrap 5 design  
  - Persistent footer & navigation bar  

- **Admin Panel**  
  - Manage users and posts  
  - Moderate content  

---

## 🛠 Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, Bootstrap 5  
- **Database:** SQLite 
- **Static Files:** Django static file handling  

---

##  Getting Started

Follow these steps to clone and run the project locally.

1️⃣ Clone the Repository

```bash
git clone https://github.com/Yaswanthpatnam/Lost_and_found.git
cd my_project


2️⃣ Create and Activate Virtual Environment
```bash

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


3️⃣ Install Dependencies

``` bash

pip install -r requirements.txt


4️⃣ Run Migrations
``` bash

python manage.py migrate


5️⃣ Create a Superuser (Admin Access)
```bash

python manage.py createsuperuser


6️⃣ Run the Development Server
```bash

python manage.py runserver

Now visit: http://127.0.0.1:8000 in your browser.

