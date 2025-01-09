
# Bibliograph 📚

For this project, I built Bibliograph, a book and author search app, using the **Google Books API** 📖 and **Wikipedia API**. This Google API allows users to search for books and authors, retrieve detailed information, including **titles** 📚, **descriptions** 📝, and **links** 🔗 to more details on Google Books.

To create the app, I used **Flask**, a lightweight Python framework, for the backend. The app provides a simple and intuitive user interface where users can search for books by author or theme 📖. The results are displayed with book details like titles, descriptions, and images 📸, making it easy to explore new reads!

### **Tech Stack Used** ⚙️

- **Frontend**: CSS, HTML, Bootstrap 💻  
- **Backend**: Flask, Python ⚙️

###  **Search by Author** 🖋️
You can search for books by entering the name of an author. The app will display a list of books written by that author, including a brief description and a cover image. The **Wikipedia API** provides a preview of the author's biography, offering a quick glimpse into their life and works. It's a great way to explore an author's works and find your next read!

![Welcome](assets/searchByAuthor.gif)

###  **Search by Theme** 🔮
You can also search for books based on specific themes. Just type in the theme you're interested in (e.g., "Science Fiction," "Romance"), and the app will show you a selection of books related to that theme. A perfect way to discover new books in your favorite genre!

![Welcome](assets/searchByTheme.gif)

## Acknowledgements

 - [Google Books API](https://developers.google.com/books/docs/v1/getting_started?hl=fr) : sign up to get an API key and create credentials for free

## Run Locally

**Clone the project:**

```bash
  git clone git@github.com:emilours/Bibliograph.git
```

**Install dependencies:**

```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install flask
    pip install requests
    pip install beautifulsoup4
    pip install python-dotenv
```

**Create .env and fill it with you API key:**

```bash
  GOOGLE_BOOKS_API_KEY=your_api_key_here
```

**Run Locally:**

```bash
  python bibliographApp.py
```

**Go on localhost:**

```bash
  http://127.0.0.1:5000
```


