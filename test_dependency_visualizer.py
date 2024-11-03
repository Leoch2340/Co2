import unittest
from dependency_visualizer import get_dependencies, build_dependency_graph, generate_graphviz_code

class TestDependencyVisualizer(unittest.TestCase):  # Определяем класс тестов, наследуемый от unittest.TestCase
    # 1. Тест для получения зависимостей пакета
    def test_get_dependencies(self):
        """Тестируем получение зависимостей пакета requests"""  # Описание теста
        deps = get_dependencies("requests")  # Получаем зависимости для пакета requests
        self.assertIn("urllib3", deps)  # Проверяем, что urllib3 присутствует в зависимостях
        self.assertIn("certifi", deps)  # Проверяем, что certifi присутствует в зависимостях

    # 2. Тест для построения графа зависимостей
    def test_build_dependency_graph(self):
        """Тестируем построение графа зависимостей"""  # Описание теста
        graph = build_dependency_graph("requests", 1)  # Строим граф зависимостей для пакета requests на глубину 1
        self.assertIn("requests", graph)  # Проверяем, что пакет requests присутствует в графе
        self.assertIn("urllib3", graph["requests"])  # Проверяем, что urllib3 является зависимостью requests в графе

    # 3. Тест для генерации Graphviz кода
    def test_generate_graphviz_code(self):
        """Тестируем генерацию Graphviz кода для простого графа"""  # Описание теста
        # Определяем тестовый граф зависимостей
        graph = {
            "requests": ["urllib3", "certifi"],  # requests зависит от urllib3 и certifi
            "urllib3": [],  # urllib3 не имеет зависимостей
            "certifi": []  # certifi не имеет зависимостей
        }
        graphviz_code = generate_graphviz_code(graph)  # Генерируем код Graphviz для тестового графа
        self.assertIn('requests -> urllib3', graphviz_code)  # Проверяем наличие ребра между requests и urllib3 в коде
        self.assertIn('requests -> certifi', graphviz_code)  # Проверяем наличие ребра между requests и certifi в коде

# Запускаем тесты, если этот файл выполняется как основная программа
if __name__ == "__main__":
    unittest.main()  # Вызываем метод main для запуска всех тестов

# python -m unittest test_dependency_visualizer.py
