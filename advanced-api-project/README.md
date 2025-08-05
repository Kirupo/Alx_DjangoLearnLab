# Advanced API Project

## Overview
This project is a Django REST Framework (DRF) API that manages **Authors** and **Books** with advanced query capabilities. It supports **CRUD operations**, **filtering**, **searching**, **ordering**, and enforces **authentication and permissions**. Comprehensive **unit tests** are also included to ensure API reliability.

---

## Features
- ✅ CRUD operations for **Books** and **Authors**
- ✅ **Filtering** by title, author, and publication year
- ✅ **Search** by book title or author name
- ✅ **Ordering** results by title or publication year
- ✅ **Authentication & Permissions** for Create, Update, Delete operations
- ✅ **Unit Tests** for endpoint functionality, response data, and security controls

---

## Technologies Used
- Python 3.x
- Django
- Django REST Framework (DRF)
- django-filter

---

## Setup Instructions
1. **Clone the Repository**
    ```bash
    git clone <your_repo_url>
    cd advanced-api-project
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run Migrations**
    ```bash
    python manage.py migrate
    ```

4. **Create a Superuser (Optional)**
    ```bash
    python manage.py createsuperuser
    ```

5. **Start the Server**
    ```bash
    python manage.py runserver
    ```

---

## API Endpoints

| URL | Method | Description | Auth Required |
|-----|--------|-------------|---------------|
| `/api/authors/` | GET | List all Authors | No |
| `/api/authors/<id>/` | GET | Retrieve Author details | No |
| `/api/books/` | GET | List Books (Supports filter/search/order) | No |
| `/api/books/<id>/` | GET | Retrieve Book details | No |
| `/api/books/create/` | POST | Create a new Book | Yes |
| `/api/books/update/<id>/` | PUT | Update Book details | Yes |
| `/api/books/delete/<id>/` | DELETE | Delete a Book | Yes |

---

## API Query Examples

- **Filter by title:**
    ```
    GET /api/books/?title=Harry Potter
    ```

- **Search by Author Name:**
    ```
    GET /api/books/?search=Rowling
    ```

- **Order by Publication Year (Descending):**
    ```
    GET /api/books/?ordering=-publication_year
    ```

- **Filter & Order Combined:**
    ```
    GET /api/books/?title=Harry Potter&ordering=publication_year
    ```

---

## Running Unit Tests

Run the unit tests using:
```bash
python manage.py test api
