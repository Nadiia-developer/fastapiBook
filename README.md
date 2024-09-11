# FastAPI Book
___
## Features 
- RESTful API with FastAPI
- Interactive API documentation using Swagger (auto-generated)
- Manage books and authors using SQLAlchemy ORM
- Data validation using Pydantic models
- Enum-based filtering for book types (Disk, E-Book)
- Database migrations using Alembic

## Setup
1. Clone the repository or download the files
- Clone project from [GitHub](https://github.com/Nadiia-developer/fastapiBook.git)
- git clone https://github.com/Nadiia-developer/fastapiBook.git

2. Create a virtual environment
- python -m venv venv
- On Mac: source venv/bin/activate 
- On Windows: venv\Scripts\activate

3. Install dependencies
- pip install -r requirements.txt

4. Apply the migration
- alembic upgrade head

5. Run the FastAPI development server
- uvicorn main:app --reload

## Endpoints
1. Access the Swagger UI: http://127.0.0.1:8000/docs
2. List of authors endpoint
3. Create author endpoint
4. List of books endpoint
5. Detail book endpoint
6. Create book endpoint