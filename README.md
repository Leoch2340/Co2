1. Общее описание:
&nbsp;&nbsp;&nbsp;&nbsp; <br/> В этом задании мы разработали инструмент командной строки на Python для визуализации графа зависимостей Python-пакетов, включая их транзитивные зависимости, без использования сторонних библиотек для получения данных. Мы использовали `importlib.metadata` для извлечения зависимостей по имени пакета и описали граф в формате Graphviz. Инструмент принимает параметры командной строки, такие как путь к программе для визуализации, имя пакета, путь к выходному файлу, максимальную глубину анализа и URL-адрес репозитория. Все функции визуализатора были протестированы для обеспечения корректности работы.

2. Описание всех функций и настроек: <br/>

&nbsp;&nbsp;&nbsp;&nbsp;1. get_dependencies(package_name, repo_url=None)<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;Функция для получения списка зависимостей пакета по его имени.<br/> 

&nbsp;&nbsp;&nbsp;&nbsp;Параметры:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;package_name (str): имя пакета, зависимости которого необходимо получить.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;repo_url (str, необязательный): URL репозитория, где хранятся данные о зависимостях пакетов.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;Описание работы:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Если repo_url указан, функция делает GET-запрос к адресу "{repo_url}/{package_name}/dependencies" для получения списка зависимостей пакета.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Если запрос успешен, результат обрабатывается и возвращается список зависимостей без указания версий. <br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Если repo_url не указан или произошла ошибка запроса, возвращается пустой список, и выводится сообщение об ошибке.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Возвращает: Список строк с именами зависимостей пакета.<br/> 

&nbsp;&nbsp;&nbsp;&nbsp;2. build_dependency_graph(package_name, max_depth, current_depth=0, graph=None, repo_url=None)<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;Рекурсивная функция для построения графа зависимостей пакета.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Параметры:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;package_name (str): имя анализируемого пакета.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_depth (int): максимальная глубина рекурсивного анализа зависимостей.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;current_depth (int): текущая глубина анализа (для рекурсии).<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graph (dict, необязательный): словарь для хранения построенного графа зависимостей.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;repo_url (str, необязательный): URL репозитория, передаваемый в get_dependencies для получения зависимостей.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;Описание работы:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;При достижении max_depth рекурсия прекращается.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Функция добавляет текущий пакет и его зависимости в граф, избегая зацикливания.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Рекурсивно вызывает себя для всех зависимостей текущего пакета.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Возвращает: Словарь, представляющий граф зависимостей.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;3. generate_graphviz_code(graph)<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;Функция для генерации кода Graphviz, который используется для визуализации графа зависимостей.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;Параметры:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graph (dict): граф зависимостей, представленный словарем, где ключи — пакеты, а значения — списки зависимостей.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;Описание работы:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Создает объект Digraph, добавляет узлы для каждого пакета и создает связи (ребра) между ними.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Возвращает сгенерированный код Graphviz.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Возвращает: Строка с кодом Graphviz для построенного графа.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;4. parse_args()<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;Функция для обработки аргументов командной строки.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;Описание работы:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Создает парсер для аргументов и добавляет следующие параметры:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--package (str, обязательный): имя анализируемого пакета.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--output (str, необязательный): путь для сохранения результата.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--depth (int, по умолчанию 1): максимальная глубина анализа зависимостей.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--graphviz-path (str, необязательный): путь к программе Graphviz.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--repo-url (str, обязательный): URL репозитория.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Возвращает: Разобранные аргументы командной строки.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;5. main()<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;Основная функция, которая управляет всем процессом.<br/> 

&nbsp;&nbsp;&nbsp;&nbsp;Описание работы:<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Вызывает parse_args() для получения аргументов командной строки.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Строит граф зависимостей с помощью build_dependency_graph, передавая repo_url из аргументов.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Генерирует код Graphviz для построенного графа.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Выводит результат на экран.<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Если указан параметр --output, сохраняет граф в указанный файл.<br/> 

3. Описание команд для сборки проекта:<br/>

&nbsp;&nbsp;&nbsp;&nbsp;Запуск - python dependency_visualizer.py --package graphviz --output graph.dot --depth 2 --graphviz-path /usr/bin/dot --repo-url https://github.com/graphp/graphviz<br/>
&nbsp;&nbsp;&nbsp;&nbsp;Запуск тестов - python -m unittest test_dependency_visualizer.py<br/> 

4. Примеры использования в виде скриншотов, желательно в анимированном/видео формате, доступном для web-просмотра:<br/>

![изображение](https://github.com/user-attachments/assets/a1c0b9f3-dbcc-4019-9074-9aae1075328b)


&nbsp;&nbsp;&nbsp;&nbsp;![изображение](https://github.com/user-attachments/assets/7713b9e2-37e8-4eb6-b658-86f7676149fb)
&nbsp;&nbsp;&nbsp;&nbsp;Тесты<br/>

