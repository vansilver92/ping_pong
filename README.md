# Pong Game - Сборка EXE

Инструкция по созданию исполняемого файла игры Pong

## Требования
- Python 3.7+
- PyInstaller
- Исходные файлы игры:
  - `pong.py`
  - `back.png`
  - `platform.png`
  - `ball.png`

## Установка зависимостей
```bash
pip install pyinstaller
pip install pygame
```

## Сборка EXE-файла

### Базовый вариант
```bash
pyinstaller --onefile pong.py
```

## Расположение файлов
После сборки:
- EXE-файл будет в папке `dist/`
- Если не использовали `--add-data`, скопируйте текстуры вручную в папку с EXE

## Запуск
Просто запустите `pong.exe` (или `Pong.exe` если использовали `--name`)

## Примечания
- Размер итогового EXE: ~5-15MB
- Для Windows рекомендуется использовать Python 3.7-3.10 (меньший размер EXE)
