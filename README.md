# Сортування Вставками (Insertion Sort)

## Опис
Цей проєкт реалізує алгоритм **сортування вставками** (Insertion Sort) для дослідження його продуктивності на різних наборах даних. Сортування вставками ефективно для невеликих обсягів даних, і цей проєкт допоможе дослідити його продуктивність на випадкових, зростаючих та спадних послідовностях із різною кількістю елементів.

Алгоритм **сортування вставками** проходить по масиву, розбиваючи його на дві частини: відсортовану та невідсортовану. Елемент з невідсортованої частини на кожному кроці вставляється на правильну позицію у відсортованій частині.

## Основні функції
- Реалізація алгоритму **сортування вставками**.
- Генерація трьох типів послідовностей: 
  - Випадкові числа.
  - Зростаюча послідовність.
  - Спадна послідовність.
- Підрахунок часу виконання, кількості порівнянь та операцій присвоювання під час сортування.
- Виведення результатів у вигляді таблиці для різних обсягів вхідних даних.

## Структура проєкту
- **main.py**: Основний файл, який містить програму для запуску алгоритму, вимірювання часу та кількості операцій сортування.
- **sort.py**: Файл із реалізацією алгоритму сортування вставками.
- **utils.py**: Допоміжні функції для генерації послідовностей і підрахунку порівнянь та присвоювань під час виконання сортування.

## Вимоги
- Python 3.x

## Як запустити
1. Завантажте або склонуйте цей репозиторій.
2. Запустіть файл main.py командою:

