# Assignment Project

## Installation

1. Clone the repository:

   ```terminal
   git clone https://github.com/PhaleshM/assignment.git
   cd assignment


2. Create a virtual environment:

   ```terminal
   python -m venv venv

3. Activate the virtual environment:

   ```terminal
   On Windows:
   git clone https://github.com/yourusername/assignment.git
   cd assignment

   On macOS and Linux:
   git clone https://github.com/yourusername/assignment.git
   cd assignment

4. Install dependencies:

   ```terminal
   pip install -r requirements.txt

## Features

### Log Ingestor App

- **Log Model:** Defines the structure of log entries with fields such as level, message, resourceId, timestamp, traceId, spanId, commit, and parentResourceId.

### Query Interface App

- **Log Model:** Utilizes the same Log model from the Log Ingestor app for querying log entries.

## Tech Stack

- Django: Web framework for building the project.
- Django Rest Framework: For building RESTful APIs.
- Other dependencies specified in `requirements.txt`.


