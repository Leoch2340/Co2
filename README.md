1. Общее описание:
&nbsp;&nbsp;&nbsp;&nbsp; <br/> В этом задании мы разработали инструмент командной строки на Python для визуализации графа зависимостей Python-пакетов, включая их транзитивные зависимости, без использования сторонних библиотек для получения данных. Мы использовали `importlib.metadata` для извлечения зависимостей по имени пакета и описали граф в формате Graphviz. Инструмент принимает параметры командной строки, такие как путь к программе для визуализации, имя пакета, путь к выходному файлу, максимальную глубину анализа и URL-адрес репозитория. Все функции визуализатора были протестированы для обеспечения корректности работы.

2. Описание всех функций и настроек: <br/>
&nbsp;&nbsp;&nbsp;&nbsp; 1. **get_dependencies(package_name)**:<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Эта функция получает зависимости указанного пакета по его имени.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Использует модуль `importlib.metadata` для извлечения метаданных пакета и возвращает список зависимостей без версионных ограничений.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - В случае, если пакет не найден, выводит сообщение об ошибке и возвращает пустой список.<br/>

&nbsp;&nbsp;&nbsp;&nbsp; 2. **build_dependency_graph(package_name, max_depth, current_depth=0, graph=None)**:<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Рекурсивная функция для построения графа зависимостей.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Принимает имя пакета, максимальную глубину анализа, текущую глубину и словарь для хранения графа.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Если текущая глубина превышает максимальную, функция завершает выполнение.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Вызывает `get_dependencies` для получения зависимостей и добавляет их в граф. Если зависимость еще не добавлена в граф, функция рекурсивно обрабатывает её.<br/>

&nbsp;&nbsp;&nbsp;&nbsp; 3. **generate_graphviz_code(graph)**:<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Генерирует код в формате Graphviz для визуализации графа зависимостей.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Создает объект `Digraph` и добавляет узлы и ребра для каждого пакета и его зависимостей.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Возвращает строку с кодом Graphviz.<br/>

&nbsp;&nbsp;&nbsp;&nbsp; 4. **parse_args()**:<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Обрабатывает аргументы командной строки с помощью библиотеки `argparse`.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Определяет следующие ключи:<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - `--package`: имя анализируемого пакета (обязательный параметр).<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - `--output`: путь к файлу для сохранения результата (необязательный параметр).<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - `--depth`: максимальная глубина анализа зависимостей (по умолчанию 1).<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - `--graphviz-path`: путь к программе Graphviz для визуализации графов.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - `--repo-url`: URL-адрес репозитория (необязательный параметр).<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Возвращает объект с разобранными аргументами.<br/>

&nbsp;&nbsp;&nbsp;&nbsp; 5. **main()**:<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Основная функция, которая связывает все другие функции.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Вызывает `parse_args()` для получения аргументов командной строки.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Строит граф зависимостей с помощью `build_dependency_graph()` и генерирует код Graphviz с помощью `generate_graphviz_code()`.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - Выводит полученный код на экран и, если указан путь к выходному файлу, сохраняет его в файл.<br/>

&nbsp;&nbsp;&nbsp;&nbsp; Настройки командной строки<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; При запуске инструмента командной строки необходимо указать следующие параметры:<br/>

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - **Путь к программе для визуализации графов** (`--graphviz-path`): указывает, где находится программа Graphviz (например, `C:\Program Files\Graphviz\bin\dot.exe`).<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - **Имя анализируемого пакета** (`--package`): имя пакета, для которого нужно получить зависимости (обязательный параметр).<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - **Путь к файлу-результату** (`--output`): опциональный путь к файлу, в который будет сохранен результат в формате Graphviz.<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - **Максимальная глубина анализа зависимостей** (`--depth`): задает, насколько глубоко будут исследоваться зависимости (по умолчанию 1).<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; - **URL-адрес репозитория** (`--repo-url`): дополнительный параметр, который может использоваться для указания URL репозитория, связанного с пакетом.<br/>

3. Описание команд для сборки проекта:<br/>

&nbsp;&nbsp;&nbsp;&nbsp;Запуск - python dependency_visualizer.py --package graphviz --output graph.dot --depth 2 --graphviz-path /usr/bin/dot --repo-url https://github.com/Leoch2340/Co2<br/>
&nbsp;&nbsp;&nbsp;&nbsp;Запуск тестов - python -m unittest test_dependency_visualizer.py<br/> 

4. Примеры использования в виде скриншотов, желательно в анимированном/видео формате, доступном для web-просмотра:<br/>

![изображение](https://github.com/user-attachments/assets/a1c0b9f3-dbcc-4019-9074-9aae1075328b)


&nbsp;&nbsp;&nbsp;&nbsp;![изображение](https://github.com/user-attachments/assets/7713b9e2-37e8-4eb6-b658-86f7676149fb)
&nbsp;&nbsp;&nbsp;&nbsp;Тесты<br/>

