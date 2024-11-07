import argparse
import requests
from graphviz import Digraph


# 1. Получение зависимостей пакета с использованием репозитория
def get_dependencies(package_name, repo_url=None):
    """Получает зависимости пакета по его имени из указанного репозитория."""
    try:
        # Проверяем, если указан URL репозитория, используем его для получения зависимостей
        if repo_url:
            response = requests.get(f"{repo_url}/{package_name}/dependencies")
            response.raise_for_status()
            dependencies = response.json().get("dependencies", [])
        else:
            # Альтернативный вариант получения зависимостей (на случай отсутствия URL)
            print("URL репозитория не указан, невозможно получить зависимости.")
            return []

        # Убираем версионные ограничения
        return [dep.split()[0] for dep in dependencies]
    except requests.exceptions.RequestException as e:
        # Обработка ошибок, если запрос к URL не удался
        print(f"Ошибка при получении зависимостей пакета {package_name}: {e}")
        return []


# 2. Построение графа зависимостей
def build_dependency_graph(package_name, max_depth, current_depth=0, graph=None, repo_url=None):
    """Рекурсивно строит граф зависимостей до указанной глубины."""
    if graph is None:
        graph = {}

    if current_depth > max_depth:
        return graph

    dependencies = get_dependencies(package_name, repo_url)
    graph[package_name] = dependencies

    for dep in dependencies:
        if dep not in graph:  # Избегаем зацикливания
            build_dependency_graph(dep, max_depth, current_depth + 1, graph, repo_url)

    return graph


# 3. Генерация Graphviz кода
def generate_graphviz_code(graph):
    """Генерирует код Graphviz для визуализации графа зависимостей."""
    dot = Digraph(comment="Dependency Graph")

    for package, dependencies in graph.items():
        dot.node(package)
        for dep in dependencies:
            dot.edge(package, dep)

    return dot.source


# 4. Обработка аргументов командной строки
def parse_args():
    parser = argparse.ArgumentParser(description="Граф зависимостей Python-пакетов.")
    parser.add_argument("--package", type=str, required=True, help="Имя анализируемого пакета")
    parser.add_argument("--output", type=str, help="Путь к файлу для сохранения результата (необязательно)")
    parser.add_argument("--depth", type=int, default=1, help="Максимальная глубина анализа зависимостей")
    parser.add_argument("--graphviz-path", type=str, help="Путь к программе Graphviz")
    parser.add_argument("--repo-url", type=str, required=True, help="URL репозитория")

    return parser.parse_args()


# 5. Основная функция
def main():
    args = parse_args()

    # Строим граф зависимостей, передаем URL репозитория
    dependency_graph = build_dependency_graph(args.package, args.depth, repo_url=args.repo_url)

    # Генерируем Graphviz код
    graphviz_code = generate_graphviz_code(dependency_graph)

    # Выводим результат на экран
    print(graphviz_code)

    # Сохраняем результат в файл, если указан
    if args.output:
        with open(args.output, 'w') as f:
            f.write(graphviz_code)
        print(f"Граф зависимостей сохранен в {args.output}")


# Запуск программы
if __name__ == "__main__":
    main()

# python dependency_visualizer.py --package graphviz --output graph.dot --depth 2 --graphviz-path /usr/bin/dot --repo-url https://github.com/graphp/graphviz
