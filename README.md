### Сервис, стандартизирующий номер телефона

Данное задание выполнено в рамках курса по [Основы компьютерных и веб-технологий с Python от Диджитализируй](https://stepik.org/course/96018/info)

Сам сервис не представляет из себя большого интереса, я лишь хотел объеденить все знания накопленные во время прохождения курсов, изученных статей и прочитанных книг.

#### Правила форматирования номеров телефона.


1. `89xxxxxxxxx`, например, `89011234567`
2. `9xxxxxxxxx` — пропущена первая 7 или 8, например, `9011234567`
3. `79xxxxxxxxx`, например, `79011234567`
4. `+79xxxxxxxxx`, например, `+79011234567`
5. форматы выше с любыми нечисловыми символами в строке, например:
    `8 __()-! 901-123-45-67,`  
    `+7901-123-45   67`,  
    `#@!(zz8901-___123-45gg67 какая-то ещё петрушка R$&*z`  
    и тп. Все нечисловые символы должны быть проигнорированы при анализе телефонного номера, после очистки номер должен совпасть по формату с одним из шаблонов, перечисленных в 1-4 пунктах. 

В данном проекте я использовал:
- [fastapi](https://fastapi.tiangolo.com/)
- [tox](https://tox.wiki/en/latest/)
- [mypy](https://github.com/python/mypy)
- [flake8](https://github.com/PyCQA/flake8)
- [pytest](https://docs.pytest.org/en/7.1.x/)
- [logging](https://docs.python.org/3/library/logging.html)
- Применял [TDD](https://en.wikipedia.org/wiki/Test-driven_development) насколько хватает знаний
- а так же упаковал все в [Docker](https://www.docker.com/)

#### Микросервис обрабатывает HTTP POST запросы по адресу `/unify_phone_from_json` и принимает телефон в теле запроса в виде JSON.
```python
{"phone": "8900some random1234534"}
```

Пример запроса:
```bash
curl --header "Content-Type: application/json" \
--request POST \
--data '{"phone": "8900some random1234534"}' \
https://kapitonov.tech/unify_phone_from_json
```
![alter text](https://kapitonov.tech/img/8b125d52659e107.png)
---

#### Микросервис обрабатывает HTTP POST запрос по адресу `/unify_phone_from_form`  и принимает телефон в теле Form Data
![alter text](https://kapitonov.tech/img/0dba23060f22778.png)
---

#### Микросервис обрабатывает HTTP GET запросы по адресу `/unify_phone_from_query`  и принимает телефон query параметре.
![alter text](https://kapitonov.tech/img/75e2de01d59757d.png)
---

#### Микросервис обрабатывает HTTP GET запросы по адресу `/unify_phone_from_cookies` и принимает телефон в Cookie записи `phone`.
![alter text](https://kapitonov.tech/img/d2d584e339fa5a6.png)
--

#### Установка
Для установки данного модуля требуется выполнить:
```bash
pip install .
```
Для установки development-зависимостей:
```bash
pip install ".[dev]"
```

Для запуска тестов:
```bash
tox
```
