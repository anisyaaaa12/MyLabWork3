# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NZJxQUSCQPEGDg38XeG__EX4V7nKdnWb
"""

import os
import logging
import asyncio

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_file(file_path):
    """Читает содержимое файла и возвращает его."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        logging.error("Файл не найден: %s", file_path)
        return None
    except Exception as e:
        logging.error("Ошибка при чтении файла: %s", str(e))
        return None

def write_file(file_path, data):
    """Записывает данные в файл."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
            logging.info("Данные успешно записаны в %s", file_path)
    except Exception as e:
        logging.error("Ошибка при записи в файл: %s", str(e))

async def async_read_file(file_path):
    """Асинхронно читает файл."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, read_file, file_path)

async def async_write_file(file_path, data):
    """Асинхронно записывает данные в файл."""
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, write_file, file_path, data)

async def process_files():
    """Демонстрация работы с файлами асинхронно."""
    file_name = "example.txt"
    data = "Пример содержимого файла."

    await async_write_file(file_name, data)
    content = await async_read_file(file_name)

    if content:
        print("Содержимое файла:")
        print(content)

await process_files()