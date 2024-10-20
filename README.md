## Дипломная работа по теме: Анализ и сравнение написания web-приложений с использованием разных фреймворков.

#### **Дипломную работу выполнил: Александр Шабанов.**

Выбор данной темы дипломной работы обусловлен её актуальностью, потребностями рынка, практической значимостью и личным интересом для меня, как начинающего Python разработчика.

В своей работе я рассмотрю фреймворки Python для разработки веб-приложений на примере условного салона красоты.

Целью исследования было создание веб-приложения для работы с реляционной базой данных на трех различных фреймворках: Django, Flask и FastAPI;  сравнение их возможностей и оценка эффективности.
Основными задачами исследования являлись: написание дипломной работы, содержащей обзор и сравнительный анализ трех фреймворков на основе четких критериев, интерпретацию практических результатов и обощение выводов. Также были определены прикладные задачи работы, а имеено: разработка веб-приложения с аутентичной для каждого фреймворка backend частью и единообразной структурой frontend’а, интеграция БД на примере SQLite и осуществление базового функционала работы с данными при помощи CRUD методов. Цели и задачи исследования были направлены на получение практических результатов, которые позволли продемонстрировать возможности применения Django, Flask и FastAPI.

## ОБЗОР ПОПУЛЯРНЫХ ИНСТРУМЕНТОВ ДЛЯ РАЗРАБОТКИ ВЕБ-ПРИЛОЖЕНИЙ НА PYTHON.

Основными фреймворками, использующимся в современной backend разработке на Python являются Django, Flask и FastApi. Рассмотрим подробнее каждую из перечисленных технологий.

### Django
Django - это бесплатная платформа веб-разработки на Python с открытым исходным кодом, используемая при создании веб-сайтов. Он был создан в 2003 году c использованием архитектуры MVT (Model-View-Template). Благодаря своей надежной и простой природе, это один из самых популярных фреймворков во всем мире. Основными плюсами Django являются:
эффективная структура кода, позволяющая разработчикам добавлять большое количество функций на веб-сайты;
встроенная страница администрирования для управления данными;
ORM (Object-Relational Mapping) для работы с базами данных;
поддержка аутентификации пользователей и управления доступом;
мощная система маршрутизации URL;
шаблонизатор для создания HTML-шаблонов;
высокая степень безопасности, включающая защиту от SQL-инъекций и DDos-атак.
_Особенности применения:_
Идеально подходит для разработки веб-проектов любого размера, но особенно - для масштабных и сложных проектов благодаря своей полной экосистеме, например: агрегаторы бронирования, торговые платформы, сайты с расширенным функционалом (админ-панель, отправка писем и т.д).  В связи с громоздкой архитектурой Django проекта, скорость разработки может быть ограничена из-за множественного повторного использования одних и тех же модулей.

### Flask
Flask - это микро-веб-фреймворк, написанный на Python. Первый релиз вышел в 2010 году, но уже по состоянию на октябрь 2020 года Flask занимал второе место по количеству звезд на GitHub среди фреймворков веб-разработки Python, лишь немного отставая от Django.
 Flask поставляется с такими опциями, как механизмы шаблонов, ORM (Flask SQLAlchemy). Основной целью разработки данного фреймворка было создание простого и быстрого средства масштабирования сложных приложений и микросервисов. 
К преимуществам данного фреймворка следует отнести:
минималистичный подход, только основные компоненты без лишних зависимостей;
высокая степень гибкости. Большинство структурных частей Flask могут быть изменены;
Jinja2 для шаблонов и Werkzeug для маршрутизации и обработки запросов;
Данный фреймворк очень удобен для начинающих, ввиду своей простоты.

_Особенности применения:_
Подходит для небольших и средних проектов, где требуется простота и большая гибкость, например, таких как: статические сайты, боты, системы электронной коммерции и т. д.

### FastAPI
Это современный, высокопроизводительный фреймворк для создания API с Python 3.7+ на основе стандартов OpenAPI и JSON Schema. К основным достоинствам можно отнести:
высокая производительность благодаря использованию асинхронного программирования (async/await) на ASGI-серверах (Starlette и Uvicorn);
автоматическая генерация интерактивной документации API;
поддержка валидирования и аннотаций типов данных;
интеграция с различными библиотеками и инструментами, такими как Pydantic и SQLAlchemy.

_Особенности применения:_
Часто используется для создания API и микросервисов, также отлично масштабируется при развертывании моделей машинного обучения. Несмотря на подробную, качественную документацию, образовательных материалов очень мало, т.к. сообщество FastAPI разработчиков невелико по сравнению с другими фреймворками.

## ПРОЕКТИРОВАНИЕ ПРИЛОЖЕНИЯ

Проектирование приложения в соответствии с его описанием было разбито на несколько этапов: определение структуры приложения, выбор наиболее подходящей БД, разработка прототипа, реализация основного функционала Frontend и Backend, разработка логики для обработки запросов от пользовательского интерфейса (создание форм и страниц для взаимодействия с пользователем), интеграция компонентов приложения.

## Требования к архитектуре веб-приложения
Frontend и Backend: фронтенд (интерфейс пользователя) и бэкенд (серверная логика). Фронтенд может быть разработан с использованием HTML, CSS и JavaScript, а бэкенд должен быть реализован на Python с использованием фреймворков  FastAPI, Flask и Django. База данных: использование базы данных SQLite для хранения данных о пользователях и объектах учета.

В соответствии с указанными требованиями была разработана серверная логика с использованием фреймворков Django, FastAPI и Flask, создан пользовательский интерфейс с использованием DTL/Jinja2 для шаблонов и элементами Bootstrap для стилизации.
![UI with CSS](https://github.com/user-attachments/assets/a767bd48-2636-407e-b8e0-112c08cd9ba9)

### Интеграция базы данных:

Были разработаны модели с необходимыми полями для записи в базу данных, осуществлена интеграция базы в приложение и ее инициализация. 
Создание и миграция базы данных проводилась в Django встроенными инструментами (Django ORM, query set), для FastAPI использовалась библиотеки SQLAlchemy, Alembic и Swagger, для Flask использовалась база данных, аналогичная БД для FastAPI.

![Пример вывода данных из БД](https://github.com/user-attachments/assets/551f51bd-e8d0-4a99-abce-62add7978004)

![Создание БД FastAPI](https://github.com/user-attachments/assets/db3f7f8f-5f78-426c-9f9f-7a016fec392c)

## АНАЛИЗ И ИНТЕРПРЕТАЦИЯ РЕЗУЛЬТАТОВ

### Сравнение фреймворков

По завершении разработки приложений на разных фреймворках проведено их сравнение. Были протестированы три фреймворка языка Python на предмет работы с реляционной базой данных SQLite.
Основные метрики, такие как скорость разработки, скорость работы, удобство в использовании, были использованы для оценки развертывания и производительности каждого фреймворка на субъективном уровне.

Обобщенные параметры использованных фреймворков для анализа:

![Сравнение параметров фреймворков](https://github.com/user-attachments/assets/53bf36bd-25c2-4d81-a59e-e082c3d9747d)
 <sup>под асинхронностью принимается асинхронность из коробки.</sup>

Субъективные оценки, полученные в процессе разработки по шкале от 1 до 5, где 1 - худшая, 5 - лучшая оценка:

![Субъективные оценки](https://github.com/user-attachments/assets/33cfc7c8-c3f0-4caa-bd3c-f300e36336e8)

## Интерпретация результатов

Все три фреймворка языка Python были успешно протестированы на предмет работы с базой данных SQLite, определены сильные и слабые стороны каждого из них.

Django является популярным и полнофункциональным серверным веб-фреймворком. Удобен своей строгой структуризацией. Его полный стек предлагает все, что нужно для разработки приложения, включая ORM, админку, аутентификацию и т.д. Админка Django позволяет легко управлять данными в БД, что крайне удобно в плане администрирования разрабатываемого или действующего сайта. Использует в своей работе множество модулей и библиотек, которые ускоряют разработку и тестирование проектов. Благодаря своей модульности позволяет легко масштабировать создаваемые приложения.

 Flask самый «легковесный» из рассматриваемых фреймворков. Предоставляет разработчику полный контроль над структурой приложения (минимализм), но требует больше работы по настройке. Легко интегрируется с любыми сторонними библиотеками (гибкость). На нем удобно быстро разрабатывать простые веб-страницы, сайты-визитки и т. д. Не имеет строгой структуры. Для написания кода подходит как программирование в одном файле, так и через создание структуры каталогов проекта. Скорость работы в сети - высокая. Отсутствуют встроенные механизмы, такие как админка или аутентификация.
 
FastAPI — фреймворк, использующий асинхронное программирование. Благодаря чему позволяет выполнятся приложению с высокой скоростью. Хорошо использовать для организации микросервисов на сервере. Также не имеет строгой структуризации: базовый код может быть написан как в одном файле, так и через структуру из нескольких файлов. Предоставляет удобный функционал документирования Swagger, широкие возможности аннотаций типов данных (Pydentic).

Выбор фреймворка зависит от потребностей проекта: Django подойдет для крупных проектов с множеством связанных компонентов. Flask хорош для небольших или средних приложений, где важна гибкость. FastAPI оптимален для приложений, где критична производительность и асинхронная работа.

## ЗАКЛЮЧЕНИЕ

Проектирование и разработка веб-приложений для работы с реляционной базой данных на примере веб-приложения “Салон красоты” были успешно завершены в соответствии с изначальными требованиями, предъявляемыми к проекту. Развернутые приложения включают функционал интерактивного управления отображаемого контента на сайте за счет подключения к БД и обработки запросов к ней: четыре из пяти разделов сайта имеют динамическое отображение контента, одна - статическое. К шаблонам HTML добавлена стилизация из библиотеки Bootstrap и JavaScript. Реализованные приложения соответствуют требованиям и демонстрирует высокую скорость работы с БД.

Все три фреймворка языка Python были успешно применены на практике при реализации веб-приложений, подтверждены сильные и слабые стороны каждого из них. БД SQLite зарекомендовала себя как простой и удобный способ хранений и администрирования данных для повседневных задач, однако для улучшения функциональности, безопасности и надежности хранения данных возможно использование других РБД.

Django, Flask и FastAPI предлагают разные подходы к веб-разработке, каждый со своими уникальными преимуществами и ограничениями. Важно изначально определить на входе, что лучше всего соответствует вашим требованиям, чтобы выбрать подходящий инструмент для своего проекта.



