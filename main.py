#!/usr/bin/env python3
 
class Solution:
    def __init__(self):
        self.upper_bound = None
        self.feasible = False
        self.decompose = False
        self.sol = None
 
 
def parse_input(input_file):
    with open(input_file, 'r') as file:
        l1 = file.readline().split()
        num = int(l1[0])
        dur = []
        release = []
        dead = []
        for i in range(num):
            line = file.readline().split()
            dur.append(int(line[0]))
            release.append(int(line[1]))
            dead.append(int(line[2]))
    return num, dur, release, dead
 
 
def is_schedule_feasible(solution, dead, dur, release, selected, add, num):
    selected2 = selected.copy()
    selected2.append(add)
    curr = release[selected2[0]]
    for task in selected2:
        curr = max(curr, release[task])
        curr += dur[task]
    unselected = []
    unselected_rel = []
    unselected_dur = []
    for i in range(num):
        if i not in selected2:
            unselected.append(i)
            unselected_rel.append(release[i])
            unselected_dur.append(dur[i])
    for task in unselected:
        start = max(curr, release[task])
        if start + dur[task] > dead[task]:
            return False
    if len(unselected)== 0:
        minimal_time = 0
    else:
        minimal_time = min(unselected_rel)
    start = max(curr, minimal_time)
    all = sum(unselected_dur)
    lower_bound = start + all
    if lower_bound >= solution.upper_bound:
        return False
    if curr <= minimal_time:
        solution.decompose = True
    return True
 
 
def find_optimal_schedule(solution, tasks, dead, release, dur, selected=[]):
    print(selected)
    if len(selected) == len(tasks):
        print("solution found")
        curr = release[selected[0]]
        for task in selected:
            curr = max(curr, release[task])
            curr += dur[task]
        solution.upper_bound = curr
        solution.feasible = True
        solution.sol = selected
    else:
        for task in tasks:
            if task not in selected:
                if is_schedule_feasible(solution, dead, dur, release, selected, task, len(tasks)):
                    find_optimal_schedule(solution, tasks, dead, release, dur, selected+[task])
                    if solution.decompose:
                        break
                else:
                    continue
 
 
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import sys
 
    # Load inputs
    input_file = sys.argv[1]
    output_file = sys.argv[2]
 
    num, dur, release, dead = parse_input(input_file)
    print(num)
    tasks = [i for i in range(num)]
    print(tasks)
 
    solution = Solution()
    solution.upper_bound = max(dead) + 1
    find_optimal_schedule(solution, tasks, dead, release, dur)
 
    print(solution.sol)
 
    file = open(output_file, "w")
 
    if not solution.feasible:
        file.write("-1\n")
    else:
        ret = [0 for i in range(len(solution.sol))]
        curr = release[solution.sol[0]]
        for task in solution.sol:
            if curr < release[task]:
                curr = release[task]
            ret[task] = curr
            curr += dur[task]
        for i in range(len(solution.sol)):
            file.write(str(ret[i]) + "\n")
