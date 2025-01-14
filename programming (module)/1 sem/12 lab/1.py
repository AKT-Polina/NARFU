import os
from pathlib import Path
import shutil
from datetime import datetime

class FileManager:
    def __init__(self, root_dir="."):
        self.root_dir = Path(root_dir).resolve()
        
    def create_file(self, filename):
        file_path = self.root_dir / filename
        with open(file_path, 'w') as f:
            pass
        print(f"Файл '{file_path}' создан.")

    def create_directory(self, dirname):
        dir_path = self.root_dir / dirname
        try:
            os.mkdir(dir_path)
            print(f"Каталог '{dir_path}' создан.")
        except OSError as e:
            print(f"Ошибка при создании каталога: {e}")

    def remove_file(self, filename):
        file_path = self.root_dir / filename
        try:
            os.remove(file_path)
            print(f"Файл '{file_path}' удалён.")
        except OSError as e:
            print(f"Ошибка при удалении файла: {e}")

    def remove_directory(self, dirname):
        dir_path = self.root_dir / dirname
        try:
            shutil.rmtree(dir_path)
            print(f"Каталог '{dir_path}' удалён.")
        except OSError as e:
            print(f"Ошибка при удалении каталога: {e}")

    def rename_file_or_directory(self, old_name, new_name):
        old_path = self.root_dir / old_name
        new_path = self.root_dir / new_name
        try:
            os.rename(old_path, new_path)
            print(f"{old_path} переименован в {new_path}.")
        except OSError as e:
            print(f"Ошибка при переименовании: {e}")

    def search_files_by_mask(self, mask):
        files = []
        for file in self.root_dir.glob(mask):
            files.append(str(file))
        return files

    def search_files_by_extension(self, extension):
        files = []
        for file in self.root_dir.rglob(f"*.{extension}"):
            files.append(str(file))
        return files

    def search_files_by_date(self, start_date=None, end_date=None):
        files = []
        for file in self.root_dir.rglob("*"):
            modified_time = datetime.fromtimestamp(os.path.getmtime(file))
            if (start_date is None or modified_time >= start_date) and \
               (end_date is None or modified_time <= end_date):
                files.append((str(file), modified_time))
        return files

    def search_files_by_size(self, min_size=0, max_size=float('inf')):
        files = []
        for file in self.root_dir.rglob("*"):
            size = os.path.getsize(file)
            if min_size <= size <= max_size:
                files.append((str(file), size))
        return files


if __name__ == "__main__":
    fm = FileManager("C:\\Users\\NEO1\\Documents")  
    try:
        while(True):
            print("Выберите действие от 1 до 9:",
              "1 - создание файла\n2- создание каталога\n3 - удаление файла",
              "4 - удаление каталога\n5 - переименование\n6 - поиск по маске",
              "7 - поиск по расширению\n8-поиск по дате\n9 - поиск по размеру")
            a = int(input())

            if(a == 1):
                print("Создание файла")
                name = input()
                fm.create_file(name)
            elif(a == 2):
                print("Создание каталога")
                name = input()
                fm.create_directory(name)
            elif(a == 3):
                print("Удаление файла")
                name = input()
                fm.remove_file(name)
            elif(a==4):
                print("Удаление каталога")
                name = input()
                fm.remove_directory(name)
            elif(a==5):
                print("Переименование файла или каталога")
                name1 = input()
                name2 = input()
                fm.rename_file_or_directory(name1, name2)
            elif(a==6):
                print("Поиск файлов по маске")
                mask = input()
                results = fm.search_files_by_mask(mask)
                print("Результаты поиска по маске:")
                for file in results:
                    print(file)
            elif(a==7):
                print("Поиск файлов по расширению")
                extension = input()
                results = fm.search_files_by_extension(extension)
                print("\nРезультаты поиска по расширению:")
                for file in results:
                    print(file)
            elif(a==8):
                print("Поиск файлов по дате")
                start_date = datetime(2023, 1, 1)
                end_date = datetime.now()
                results = fm.search_files_by_date(start_date, end_date)
                print("\nРезультаты поиска по дате:")
                for file, date in results:
                    print(f"{file}: {date.strftime('%Y-%m-%d %H:%M:%S')}")
            elif(a==9):
                print("Поиск файлов по размеру")
                min_size = int(input())
                max_size = int(input())
                #min_size = 1024  # 1 КБ
                #max_size = 1048576  # 1 МБ
                results = fm.search_files_by_size(min_size, max_size)
                print("\nРезультаты поиска по размеру:")
                for file, size in results:
                    print(f"{file}: {size} байт")
            else:
                print("Выход")
                break
    except Exception:
        print("Error")
