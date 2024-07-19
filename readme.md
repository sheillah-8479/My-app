                                                    OBITUARY PLATFORM
Project Documentation: Obituary Platform


1. Overview
Project Name: Obituary Platform


2. Description: A web application for submitting, viewing, editing, and deleting obituaries.

Technologies Used: Python (Flask), SQLAlchemy, SQLite, HTML, CSS, Jinja2 templates.


3. Project Structure
   
File Structure:

app.py: Main Flask application file containing routes and database configuration.

models.py: Defines SQLAlchemy model (Obituary) for database interactions.

templates/: Directory containing HTML templates.

static/: Directory for static files (CSS, JavaScript).


4. Features
   
Submission:


Users can submit obituaries with fields for name, dates, content, and author.

Generates a unique slug for each obituary based on the name.

Viewing:


Displays a list of obituaries with search filters for name, month, and year.

Table format with columns for name, dates, content, author, and submission date.


Editing:

Allows authorized users to edit obituaries using a dedicated edit form.

Updates database records with new information.


Deleting:

Provides a mechanism to delete obituaries from the database.

Confirmation prompt for deletion action.


4. Code Details

   
app.py


Flask routes for rendering templates (index, submit_obituary, view_obituaries).


Database setup using SQLAlchemy (Obituary model).


Functions for generating slugs (generate_slug) and handling form submissions.


models.py


Defines the Obituary model with fields (id, name, date_of_birth, date_of_death, content, author, submission_date, slug).


Manages database interactions and relationships.
