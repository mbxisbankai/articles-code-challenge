import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.connection import CURSOR, CONN
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed():
    print("Seeding data...")

    try:
        with CONN:
            # Clear tables
            CURSOR.execute("DELETE FROM articles")
            CURSOR.execute("DELETE FROM authors")
            CURSOR.execute("DELETE FROM magazines")

            # Create authors
            author1 = Author.create("Mary Shelley")
            author2 = Author.create("George Orwell")

            # Create magazines
            mag1 = Magazine.create("Science Today", "Science")
            mag2 = Magazine.create("World Fiction", "Literature")

            # Create articles
            Article.create("AI Breakthrough", "Exploring neural nets", author1.author_id, mag1.magazine_id)
            Article.create("Dystopian Visions", "Surveillance and Society", author2.author_id, mag2.magazine_id)
            Article.create("Bioethics", "Editing the human genome", author1.author_id, mag1.magazine_id)
            
            # Create authors with articles
            Author.add_with_articles("Mary Shelley", [
                {"name": "AI Breakthrough", "title": "Exploring neural nets", "magazine_id": mag1.magazine_id},
                {"name": "Bioethics", "title": "Editing the human genome", "magazine_id": mag1.magazine_id}
            ])

            Author.add_with_articles("George Orwell", [
                {"name": "Dystopian Visions", "title": "Surveillance and Society", "magazine_id": mag2.magazine_id}
            ])

        print("Seeding complete.")
    except Exception as e:
        print(f"Seeding failed: {e}")

if __name__ == "__main__":
    seed()
