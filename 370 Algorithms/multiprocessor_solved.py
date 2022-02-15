import itertools
import sys

def create_combinations(N, num_tasks):
    processors = list(range(0,N))
    ##print(processors)
    combinations = [y for y in itertools.product(processors, repeat= num_tasks)]
    ##print(combinations)
    return combinations

def solve_scheduling(tasks, N):
    min_time = sys.maxsize
    min_perm = []
    combinations = create_combinations(N, len(tasks))
    for i in range(len(combinations)):
        schedule = combinations[i]
        p_tasks = [0]*N
        for j in range(len(schedule)):
            p_tasks[schedule[j]] = p_tasks[schedule[j]]+ tasks[j]
        time_taken = max(p_tasks)
        if time_taken<min_time:
            min_time = time_taken
            min_perm = schedule
    print("Min time taken = ", min_time)
    print("Schedule =", min_perm)
    final_tasks = [[] for _ in range(N)]
    for i in range(len(min_perm)):
        final_tasks[min_perm[i]].append(tasks[i])
    for i in range(len(final_tasks)):
        print("Tasks for processor ", i+1, "=", final_tasks[i])   
    
        
        

def main():
    tasks = [5, 10, 12, 3 ,4, 8, 17, 21]
    num_processors = 3
    solve_scheduling(tasks, num_processors)


if __name__ == "__main__":
    main()
