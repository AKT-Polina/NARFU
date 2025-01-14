import json
import os
import shutil
from pathlib import Path

def load_commands_from_json(json_file):
    """Загружает команды из JSON-файла."""
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data['commands']

def execute_command(command, args):
    """Выполняет команду с переданными аргументами."""
    if command == 'create':
        create(*args)
    elif command == 'copy':
        copy(*args)
    elif command == 'move':
        move(*args)
    else:
        raise ValueError(f"Неизвестная команда: {command}")

def create(path_type, path):
    """Создает файл или папку."""
    if path_type == 'file':
        Path(path).touch(exist_ok=True)
        print(f"Создан файл: {path}")
    elif path_type == 'folder':
        Path(path).mkdir(parents=True, exist_ok=True)
        print(f"Создана папка: {path}")
    else:
        raise ValueError(f"Неправильный тип пути: {path_type}")

def copy(source, destination):
    """Копирует файл или папку."""
    shutil.copy2(source, destination)
    print(f"Копирован объект: {source} -> {destination}")

def move(source, destination):
    """Перемещает файл или папку."""
    shutil.move(source, destination)
    print(f"Перемещен объект: {source} -> {destination}")


commands = load_commands_from_json('commands.json')
for cmd in commands:
    execute_command(cmd['command'], cmd['args'])
