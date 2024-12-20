import random
import time
import matplotlib.pyplot as plt

def generate_array(size, max_value, seed=42):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(size)]

def is_unique(array):
    return len(array) == len(set(array))

def measure_time(func, *args):
    start_time = time.perf_counter()
    func(*args)
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time

def main():
    sizes = [100, 150, 200, 250, 300, 350, 400, 500]
    stambuk_saya = 38 
    max_value = 250 - stambuk_saya
    seed = 42  

    worst_case_durations = []
    average_case_durations = []

    # Write results to 'worst_avg.txt'
    with open('worst_avg.txt', 'w') as f:
        for size in sizes:
            array = generate_array(size, max_value, seed)
            worst_case_array = [1] * size

            worst_case_duration = measure_time(is_unique, worst_case_array)
            average_case_duration = measure_time(is_unique, array)

            worst_case_durations.append(worst_case_duration)
            average_case_durations.append(average_case_duration)

            f.write(f"Size = {size}, Worst: {worst_case_duration:.10f} s, Avg: {average_case_duration:.10f} s\n")
            print(f"Size = {size}, Worst: {worst_case_duration:.10f} s, Avg: {average_case_duration:.10f} s")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, worst_case_durations, 'ro-', label='Worst Case')
    plt.plot(sizes, average_case_durations, 'bs-', label='Average Case')
    plt.title('Performance: Worst vs Average Case')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
