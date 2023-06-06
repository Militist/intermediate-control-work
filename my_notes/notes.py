import json
import datetime

class Note:
    def __init__(self, id, title, body, creation_date=None, update_date=None):
        self.id = id
        self.title = title
        self.body = body
        self.creation_date = creation_date if creation_date else datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        self.update_date = update_date if update_date else datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')

    def __str__(self):
        return f"{self.id}, {self.title}, {self.body}, {self.creation_date}, {self.update_date}"

class NotesManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []

    def load_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                notes = json.load(file)
                for note in notes:
                    self.notes.append(
                        Note(
                            note['id'],
                            note['title'],
                            note['body'],
                            note['creation_date'],
                            note['update_date']
                        )
                    )
        except Exception as e:
            print(e)

    def close_app(self):
        self.save_notes()

    def save_notes(self):
        with open(self.file_path, 'a') as file:
            notes = []
            for note in self.notes:
                notes.append(
                    {
                        "id": note.id,
                        "title": note.title,
                        "body": note.body,
                        "creation_date": note.creation_date,
                        "update_date": note.update_date
                    }
                )
            json.dump(notes, file)

    def add_note(self, title, body):
        if not title or not body:
            print("Заголовок и текст заметки должны быть заполнены")
            return
        new_note_id = len(self.notes) + 1
        self.notes.append(Note(new_note_id, title, body))
        self.save_notes()

    def delete_note_by_id(self, note_id):
        try:
            note_id = int(note_id)
        except ValueError:
            print("Некорректный id заметки")
            return

        deleted = False
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.save_notes()
                deleted = True
                break
        if deleted:
            print(f"Заметки с id={note_id} не существует")
        else:
            print(f"Заметка с id = {note_id} не существует")

    def edit_note_by_id(self, note_id, title, body):
        edited = False
        for note in self.notes:
            if note.id == note_id:
                note.title = title
                note.body = body
                note.update_date = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
                self.save_notes()
                edited = True
                break
        if not edited:
            print(f"Заметки с id={note_id} не существует")

    def print_notes(self, sort_by=None, reverse=False):
        sorted_notes = self.notes
        if sort_by and sort_by in ["creation_date", "update_date"]:
            sorted_notes = sorted(self.notes, key=lambda note: getattr(note, sort_by))
            if reverse:
                sorted_notes = reversed(sorted_notes)
            for note in sorted_notes:
                print(note)

    def search_notes_bykeyword(self, keyword):
        for note in self.notes:
            if keyword in note.title or keyword in note.body:
                print(note)


def main():
    notes_manager = NotesManager("notes.json")
    notes_manager.load_notes()

    try:
        while True:
            print("Выберите действие:")
            print("1. Посмотреть все заметки")
            print("2. Создать новую заметку")
            print("3. Редактировать заметку")
            print("4. Удалить заметку")
            print("5. Поиск заметки по ключевому слову")
            print("6. Сортировать заметки по дате создания")
            print("7. Сортировать заметки по дате последнео обновления")
            print("8. Выйти")

            user_choice = input("Введите номер действия: ")

            if user_choice == "1":
                notes_manager.print_notes()

            elif user_choice == "2":
                title = input("Введите заголовок заметки: ")
                body = input("Введите текст заметки: ")
                notes_manager.add_note(title, body)

            elif user_choice == "3":
                note_id = input("Введите id заметки, которую нужно отредактировать: ")
                title = input("Введите новый заголовок заметки: ")
                body = input("Введите новый текст заметки: ")
                notes_manager.edit_note_by_id(note_id, title, body)

            elif user_choice == "4":
                note_id = input("Введите id заметки, которую нужно удалить: ")
                notes_manager.delete_note_by_id(note_id)

            elif user_choice == "5":
                keyword = input("Введите ключевое слово: ")
                notes_manager.search_notes_bykeyword(keyword)

            elif user_choice == "6":
                notes_manager.print_notes(sort_by="craetion_date")

            elif user_choice == "7":
                notes_manager.print_notes("update_date")

            elif user_choice == "8":
                print("Завершение работы")

            elif user_choice == "save":
                notes_manager.save_notes()
                print("Данные сохранены.")

            else:
                print("Неправильный ввод, пожалуйста, попробуйте еще раз.")

    finally:
        notes_manager.close_app()




if __name__ == '__main__':
    main()
