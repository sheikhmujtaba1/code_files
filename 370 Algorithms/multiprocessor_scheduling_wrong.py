import itertools
import sys

def solve_scheduling(tasks, num_processors):
    N = num_processors
    perms = list(itertools.permutations(tasks))
##    print(perms)
    min_time = sys.maxsize
    min_perm = []
    for i in range(len(perms)):
        schedule = perms[i]
        p_tasks = [0]*N
        for j in range(len(schedule)):
            processor = j%N
            p_tasks[processor] = p_tasks[processor]+schedule[j]
##        print(p_tasks)
        time_taken = max(p_tasks)
        if time_taken<min_time:
            min_time = time_taken
            min_perm = schedule
    print("Min time taken = ", min_time)
   ## print("Schedule =", min_perm)
    final_tasks = [[] for _ in range(N)]
    for i in range(len(min_perm)):
         processor = i%N
         final_tasks[processor].append(min_perm[i])
    for i in range(len(final_tasks)):
        print("Tasks for processor ", i+1, "=", final_tasks[i])   
        
        

def main():
    tasks = [5, 10, 12, 3 ,4, 6, 9, 30]
    num_processors = 4
    solve_scheduling(tasks, num_processors)

if __name__ == "__main__":
    main()
