import random
import copy


def population_generator(arr_val, arr_w, max_w, size):
        current_w = 0;
        population = []
        for i in range(size):
            rand = random.randint(0,1)
            if rand == 1 and max_w>=current_w+arr_w[i]:
                population.append(1)
                current_w = current_w+arr_w[i]
            else:
                population.append(0)
        return population
                
        
def crossover(chromo1, chromo2, arr_w, max_w, size):
             
    i_len = len(chromo1)
    select_x = i_len//2
    child1 = []
    child2 = []
    child1_w = 0
    child2_w = 0
    for i in range(select_x):
        child1.append(chromo1[i])
        if chromo1[i] == 1:
            child1_w = child1_w+arr_w[i] 
        child2.append(chromo2[i])
        if chromo2[i] ==1:
            child2_w = child2_w+arr_w[i]
    for i in range(select_x, i_len):
        if chromo2[i] == 1 and max_w>= child1_w+arr_w[i]:
            child1.append(1)
            child1_w = child1_w+arr_w[i]
        else:
            child1.append(0)
        if chromo1[i] == 1 and max_w>= child2_w+arr_w[i]:
            child2.append(1)
            child2_w = child2_w+arr_w[i]
        else:
            child2.append(0)
    return child1, child2
            
            
def mutate(mutable, arr_w, max_w, size):
    mutable_size = len(mutable)
    half = mutable_size//2
    pos1 = random.randint(0,half)
    pos2 = random.randint((half+1),(mutable_size-1))
    mutable_w = 0
    for i in range(len(mutable)):
        if mutable[i] == 1:
                mutable_w = mutable_w+ arr_w[i]
    if mutable[pos1] == 0:
        if max_w>= mutable_w+arr_w[pos1]:
                mutable[pos1] = 1
    else:
        mutable[pos1] = 0
    if mutable[pos2] == 0:
        if max_w>= mutable_w+arr_w[pos2]:
                mutable[pos2] = 1
    else:
        mutable[pos2] = 0
    return mutable    
        

def knapsack_genetic(arr_val, arr_w, max_w, size):
    initial_pop = []
    pop_size = 10
    pop_score = []
    gen_pop = [0 for i in range(6)]
    for i in range(pop_size):
        pop = population_generator(arr_val, arr_w, max_w, size)
        initial_pop.append(pop)
        score = 0
        for j in range(len(pop)):
            if pop[j] == 1:
                score = score + arr_val[j]
        pop_score.append(score)
    print("Generation 0\n", initial_pop)
    sorted_score = copy.deepcopy(pop_score)
    sorted_score.sort(reverse=True)
    print(sorted_score)
    parent1 = initial_pop[pop_score.index(sorted_score[0])]
    print(parent1)
    parent2 = initial_pop[pop_score.index(sorted_score[1])]
    print(parent2)
    child1, child2 = crossover(parent1, parent2, arr_w, max_w, size)
    non_elite1 = initial_pop[pop_score.index(sorted_score[2])]
    non_elite2 = initial_pop[pop_score.index(sorted_score[3])]
    non_elite3 = initial_pop[pop_score.index(sorted_score[4])]
    gen_pop[0] = parent1
    gen_pop[1] = child1
    gen_pop[2] = child2
    gen_pop[3] = non_elite1
    gen_pop[4] = non_elite2
    gen_pop[5] = non_elite3
    prob_mutation = random.randint(0,12)
    if prob_mutation<len(gen_pop):
            mutated = mutate(gen_pop[prob_mutation], arr_w, max_w, size)
            gen_pop[prob_mutation] = mutated
    print("Generation 1\n", gen_pop)
    gen_score = [0 for i in range(len(gen_pop))]
    for k in range(21):
        for i in range(len(gen_pop)):
                score = 0
                for j in range(len(gen_pop[i])):
                        if gen_pop[i][j] == 1:
                                score = score + arr_val[j]
                gen_score[i] = score
        sorted_score = copy.deepcopy(gen_score)
        sorted_score.sort(reverse=True)
        print(sorted_score)
        parent1 = gen_pop[gen_score.index(sorted_score[0])]
        print(parent1)
        parent2 = gen_pop[gen_score.index(sorted_score[1])]
        print(parent2)
        child1, child2 = crossover(parent1, parent2, arr_w, max_w, size)
        non_elite1 = gen_pop[gen_score.index(sorted_score[2])]
        non_elite2 = gen_pop[gen_score.index(sorted_score[3])]
        non_elite3 = gen_pop[gen_score.index(sorted_score[4])]
        gen_pop[0] = parent1
        gen_pop[1] = child1
        gen_pop[2] = child2
        gen_pop[3] = non_elite1
        gen_pop[4] = non_elite2
        gen_pop[5] = non_elite3
        prob_mutation = random.randint(0,15)
        if prob_mutation<len(gen_pop):
            mutated = mutate(gen_pop[prob_mutation], arr_w, max_w, size)
            gen_pop[prob_mutation] = mutated
        print("Generation", k+2, "\n", gen_pop)

def main():
    weight = [41,50,49,59,55,57,60]
    value = [442,525,511,593,546,564,617]
    W = 170
    arr_length = len(value)
    knapsack_genetic(value, weight, W, arr_length)


if __name__ == "__main__":
    main()
