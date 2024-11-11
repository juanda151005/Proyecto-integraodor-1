
# Project-integrator-1

Welcome to **Travel Rate**! Follow this guide for a quick introduction to our project.

## Table of Contents
- [About](#about)
- [How to Install](#how-to-install)
- [Folder Structure](#folder-structure)
- [Running the Project](#running-the-project)
- [License](#license)

## About

**Travel Rate** is a web application developed by **Bayron Mena**, **Juan David Velasquez**, and **Samuel Villa** as part of the “Proyecto Integrador 1,” directed by **Juan David Martinez**. The platform helps users rate and review travel experiences.

## How to Install

To get a copy of the project up and running on your local machine, follow these steps:

1. (Optional) Fork the repository.
2. Clone the repository:

   ```bash
   git clone https://github.com/juanda151005/Proyecto-integrador-1.git
   ```

3. Navigate to the project folder:

   ```bash
   cd ./Project-integrator-1
   ```

4. Install the required libraries using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

5. Obtain your OpenAI API key and save it in a `.env` file located in the root folder of the project with the following structure:

   ```
   openai_apikey=<your_openai_api_key>
   ```

## Folder Structure

Once you've set up the project, your folder structure should look like this:

```bash
Project-integrator-1
├── accounts
├── city
├── media
├── ranking
├── reviews
├── routes
├── travelRate
├── .env
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

## Running the Project

1. Apply database migrations to set up the database structure:

   ```bash
   python manage.py migrate
   ```

   This will create the `db.sqlite3` file with all necessary tables and relationships.

2. Start the development server:

   ```bash
   python manage.py runserver
   ```

3. Open your web browser and navigate to `http://127.0.0.1:8000` to view the application.

## License

© 2024 Bayron Mena, Juan David Velasquez, Samuel Villa. All rights reserved.

---

