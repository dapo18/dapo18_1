import math
import random

def objective_function(x, y):
    """Целевая функция: (x² + y² - 25)² + (x + y - 7)²"""
    term1 = x**2 + y**2 - 25
    term2 = x + y - 7
    return term1**2 + term2**2

def simulated_annealing(initial_temp=1000, final_temp=1e-8, alpha=0.99, 
                       max_iterations=10000, step_size=1.0, search_range=(-10, 10)):
    """Алгоритм имитации отжига для решения системы уравнений"""
    
    min_range, max_range = search_range
    
    # Генерация случайного начального решения
    x_current = random.uniform(min_range, max_range)
    y_current = random.uniform(min_range, max_range)
    current_energy = objective_function(x_current, y_current)
    
    # Сохраняем начальное решение
    x_start, y_start = x_current, y_current
    
    # Лучшее найденное решение
    x_best, y_best = x_current, y_current
    best_energy = current_energy
    
    T = initial_temp
    iteration = 0
    
    while T > final_temp and iteration < max_iterations:
        # Генерация нового решения-кандидата
        x_new = x_current + random.uniform(-step_size, step_size)
        y_new = y_current + random.uniform(-step_size, step_size)
        
        # Ограничиваем решение диапазоном
        x_new = max(min_range, min(max_range, x_new))
        y_new = max(min_range, min(max_range, y_new))
        
        new_energy = objective_function(x_new, y_new)
        
        # Разность энергий
        energy_diff = new_energy - current_energy
        
        # Критерий принятия решения
        if energy_diff < 0:
            # Новое решение лучше - принимаем
            x_current, y_current = x_new, y_new
            current_energy = new_energy
        else:
            # Новое решение хуже - принимаем с вероятностью
            probability = math.exp(-energy_diff / T)
            if random.random() < probability:
                x_current, y_current = x_new, y_new
                current_energy = new_energy
        
        # Обновляем лучшее решение
        if current_energy < best_energy:
            x_best, y_best = x_current, y_current
            best_energy = current_energy
        
        # Охлаждение
        T *= alpha
        iteration += 1
    
    return x_start, y_start, x_best, y_best, best_energy, iteration

# Запуск алгоритма
if __name__ == "__main__":
    print("Решение системы уравнений методом имитации отжига")
    print("Система уравнений:")
    print("x² + y² = 25")
    print("x + y = 7")
    print("-" * 50)
    
    x_start, y_start, x_best, y_best, best_energy, iterations = simulated_annealing()
    
    print(f"Начальное решение: x={x_start:.3f}, y={y_start:.3f}")
    print(f"Найденное решение: x={x_best:.3f}, y={y_best:.3f}")
    print(f"Значение целевой функции: {best_energy:.6f}")
    print(f"Проверка уравнений:")
    print(f"x² + y² = {x_best**2 + y_best**2:.3f} (должно быть 25)")
    print(f"x + y = {x_best + y_best:.3f} (должно быть 7)")
    print(f"Количество итераций: {iterations}")
