import json
import os

class Book:
    """Создание объекта 'книга'."""
    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """Конвертирование в словарь."""
        return self.__dict__

class Library:
    """Хранение данных в JSON файле."""
    def __init__(self, filename: str = "books.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        """Загрузка книг из JSON файла и обработка ошибок."""
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0: #Проверка файла
            with open(self.filename, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    self.books = [Book(**book) for book in data]
                except json.JSONDecodeError:
                    print("Ошибка чтения данных из файла. Файл может быть поврежден.")


    def save_books(self):
        """Сохранение книг в JSON файл."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """Довавляет новую книгу в библиотеку."""
        id = len(self.books) + 1 if self.books else 1
        new_book = Book(id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' добавлена с ID {id}.")

    def remove_book(self, id: int):
        """Удаляет книгу из библиотеки по ID."""
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                self.save_books()
                print(f"Книга с ID {id} удалена.")
                return
        print(f"Книга с ID {id} не найдена.")

    def search_books(self, query: str):
        """Ищет книги по названию, автору или году издания."""
        results = [book for book in self.books if query.lower() in book.title.lower() or
                   query.lower() in book.author.lower() or
                   query == str(book.year)]
        return results

    def display_books(self):
        """Показывает книги в библиотеке."""
        if not self.books:
            print("Нет доступных книг.")
            return
        for book in self.books:
            print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")

    def change_status(self, id: int, new_status: str):
        """Меняет статус книги в библиотеке."""
        for book in self.books:
            if book.id == id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                    print(f"Статус книги с ID {id} изменен на '{new_status}'.")
                else:
                    print("Неверный статус. Доступные статусы: 'в наличии', 'выдана'.")
                return
        print(f"Книга с ID {id} не найдена.")

def main():
    """Основная функция. Интерфейс."""
    library = Library()

    while True:
        print("\n1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск по книгам")
        print("4. Отобразить все книги в библиотеке")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            while True:
                try:
                    year = int(input("Введите год издания: "))
                    break
                except ValueError:
                    print("Вы вводите нечисловые символы. Попробуйте ещё раз.")
                    continue
            library.add_book(title, author, year)
        elif choice == '2':
            id = int(input("Введите ID книги для удаления: "))
            library.remove_book(id)
        elif choice == '3':
            query = input("Введите название, автора или год для поиска: ")
            results = library.search_books(query)
            if results:
                for book in results:
                    print(f"Найдена книга: ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
            else:
                print("Такая книга не найдена.")
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            library.change_status(id, new_status)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()