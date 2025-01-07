import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, request, url_for
from bs4 import BeautifulSoup

load_dotenv()
google_books_api_key = os.getenv('GOOGLE_BOOKS_API_KEY')

app = Flask(__name__)

def search_book_by_author(author_name):
    url = f"https://www.googleapis.com/books/v1/volumes?q=inauthor:{author_name}&key={google_books_api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("DATA RECEIVED: ", data)
        if 'items' in data:
            book_info = []
            for book in data['items']:
                title = book['volumeInfo'].get('title', 'No Title Available')
                authors = book['volumeInfo'].get('authors', 'No Authors Available')
                infoLink = book['volumeInfo'].get('infoLink')
                if 'description' in book['volumeInfo']:
                    description = book['volumeInfo']['description']
                else:
                    description = 'No Description Available'
                if 'imageLinks' in book['volumeInfo']:
                    image = book['volumeInfo']['imageLinks'].get('thumbnail', url_for('static', filename='default_image.jpg'))
                else:
                    image = url_for('static', filename='default_image.jpg')

                book_info.append({
                    'title': title,
                    'authors': authors,
                    'description': description,
                    'image': image,
                    'infoLink': infoLink
                })
            return book_info
        else:
            print("JE RENTRE ICI")
            return f"No books found for the author '{author_name}'. Please try with a different author."
    else:
        return f"Error: {response.status_code}"

def search_book_by_theme(theme):
    url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{theme}&key={google_books_api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if 'items' in data:
            book_info = []
            for book in data['items']:
                title = book['volumeInfo'].get('title', 'No Title Available')
                authors = book['volumeInfo'].get('authors', 'No Authors Available')
                infoLink = book['volumeInfo'].get('infoLink')
                description = book['volumeInfo'].get('description', 'No Description Available')
                if 'imageLinks' in book['volumeInfo']:
                    image = book['volumeInfo']['imageLinks'].get('thumbnail', url_for('static', filename='default_image.jpg'))
                else:
                    image = url_for('static', filename='default_image.jpg')
            
                book_info.append({
                    'title': title,
                    'authors': authors,
                    'description': description,
                    'image': image,
                    'infoLink': infoLink
                    })
            return book_info
        else:
            return []
    else:
        return f"Error: {response.status_code}"

def get_author_bio(author_name):
    search_url = f"https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch={author_name}&format=json"
    search_response = requests.get(search_url)
    
    if search_response.status_code == 200:
        search_data = search_response.json()
        
        search_results = search_data.get("query", {}).get("search", [])
        
        if not search_results:
            return "No results found for this author."
        
        first_result = search_results[0]
        page_id = first_result["pageid"]

        details_url = f"https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=true&pageids={page_id}&format=json"
        details_response = requests.get(details_url)
        
        if details_response.status_code == 200:
            details_data = details_response.json()
            
            pages = details_data.get("query", {}).get("pages", {})
            page_data = pages.get(str(page_id), {})
            
            if "extract" in page_data and page_data["extract"].strip():
                # Utilisation de BeautifulSoup pour nettoyer le texte HTML
                raw_bio = page_data["extract"]
                soup = BeautifulSoup(raw_bio, "html.parser")
                clean_bio = soup.get_text(separator="\n").strip()
                return clean_bio
            else:
                return []
        else:
            return f"Error: {search_response.status_code}"


@app.route("/", methods=["GET", "POST"])
def index():
    books_by_author = None
    books_by_theme = None
    author_bio = None
    author_name = None 
    theme = None

    if request.method == "POST":
        author_name = request.form.get('author')
        theme = request.form.get('theme')

        if author_name:
            author_bio = get_author_bio(author_name)
            books_by_author = search_book_by_author(author_name)

        if theme:
            books_by_theme = search_book_by_theme(theme)

        return render_template('index.html',
                               books_by_author=books_by_author,
                               books_by_theme=books_by_theme,
                               author_bio=author_bio,
                               author_name=author_name,
                               theme=theme)
    
    return render_template('index.html', author_name=author_name, theme=theme)


if __name__ == "__main__":
    app.run(debug=True)
