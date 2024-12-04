# Library
Консольное приложение для управления библиотекой. Возможности:
1. Добавление книги с названием, автором и годом издания. При попытке ввода нечисловых символов в пункте 'год издания' появится соответсвующее сообщение.
2. Удаление книги. Для удаления необходимо ввести ID книги. При попытке удаления несуществующей книги выведется соответсвующее сообщение.
3. Поиск по библиотеке. Можно осуществлять поиск по названию, автору или году издания. Не обязательно полностью вводить название или автора для точного поиска. Если книга не найдена – будет соответсвующее сообщение.
4. Отображение всех книг в библиотеке.
5. Функция изменения статуса книги – 'выдана' и 'в наличии'. При попытке ввода других слов при изменении статуса всплывёт соответсвующее сообщение.
6. Выход из приложения.<br>

Сохранение данных происходит в файле books.json.<br>
Приложение протестировано и защищено от ошибок, например таких, как ошибка JSON файла.<br>
Использовались только стандартная библиотека Python.
