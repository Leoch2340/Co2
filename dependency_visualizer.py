import argparse
import importlib.metadata
from graphviz import Digraph


# 1. Получение зависимостей пакета
def get_dependencies(package_name):
    """Получает зависимости пакета по его имени."""
    try:
        # Получаем информацию о дистрибутиве пакета по имени
        dist = importlib.metadata.distribution(package_name)
        # Извлекаем зависимости, если они есть, или возвращаем пустой список
        dependencies = dist.requires or []
        # Возвращаем список зависимостей без версионных ограничений
        return [dep.split()[0] for dep in dependencies]
    except importlib.metadata.PackageNotFoundError:
        # Если пакет не найден, выводим сообщение об ошибке
        print(f"Пакет {package_name} не найден.")
        return []  # Возвращаем пустой список


# 2. Построение графа зависимостей
def build_dependency_graph(package_name, max_depth, current_depth=0, graph=None):
    """Рекурсивно строит граф зависимостей до указанной глубины."""
    if graph is None:
        # Инициализируем пустой граф, если он не был передан
        graph = {}

    if current_depth > max_depth:
        # Если текущая глубина превышает максимальную, завершаем рекурсию
        return graph

    # Получаем зависимости для текущего пакета
    dependencies = get_dependencies(package_name)
    # Добавляем пакет и его зависимости в граф
    graph[package_name] = dependencies

    for dep in dependencies:
        # Для каждой зависимости проверяем, была ли она уже добавлена в граф
        if dep not in graph:  # Чтобы избежать зацикливания
            # Рекурсивно строим граф для зависимостей
            build_dependency_graph(dep, max_depth, current_depth + 1, graph)

    return graph  # Возвращаем построенный граф зависимостей


# 3. Генерация Graphviz кода
def generate_graphviz_code(graph):
    """Генерирует код Graphviz для визуализации графа зависимостей."""
    dot = Digraph(comment="Dependency Graph")  # Создаем новый объект графа с комментарием

    for package, dependencies in graph.items():
        dot.node(package)  # Добавляем узел для каждого пакета
        for dep in dependencies:
            dot.edge(package, dep)  # Создаем ребро между пакетом и его зависимостью

    return dot.source  # Возвращаем сгенерированный код Graphviz


# 4. Обработка аргументов командной строки
def parse_args():
    parser = argparse.ArgumentParser(description="Граф зависимостей Python-пакетов.")  # Создаем парсер аргументов
    parser.add_argument("--package", type=str, required=True, help="Имя анализируемого пакета")  # Обязательный аргумент для имени пакета
    parser.add_argument("--output", type=str, help="Путь к файлу для сохранения результата (необязательно)")  # Необязательный аргумент для сохранения графа
    parser.add_argument("--depth", type=int, default=1, help="Максимальная глубина анализа зависимостей")  # Максимальная глубина анализа
    parser.add_argument("--graphviz-path", type=str, help="Путь к программе Graphviz")  # Путь к исполняемому файлу Graphviz
    parser.add_argument("--repo-url", type=str, help="URL репозитория")

    return parser.parse_args()  # Возвращаем разобранные аргументы


# 5. Основная функция
def main():
    args = parse_args()  # Получаем аргументы командной строки

    # Строим граф зависимостей
    dependency_graph = build_dependency_graph(args.package, args.depth)

    # Генерируем Graphviz код
    graphviz_code = generate_graphviz_code(dependency_graph)

    # Выводим результат на экран
    print(graphviz_code)

    # Сохраняем результат в файл, если указан
    if args.output:
        with open(args.output, 'w') as f:  # Открываем файл для записи
            f.write(graphviz_code)  # Записываем сгенерированный код в файл
        print(f"Граф зависимостей сохранен в {args.output}")  # Сообщаем о сохранении


# Запуск программы
if __name__ == "__main__":
    main()  # Вызываем основную функцию для запуска программы

# python dependency_visualizer.py --package graphviz --output graph.dot --depth 2 --graphviz-path /usr/bin/dot --repo-url https://github.com/Leoch2340/Co2
