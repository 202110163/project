def min_cost_assignment(a, workloads):
    num_workers = len(a)
    num_jobs = len(workloads)
    max_possible_cost = max(a) * max(workloads) + 1
    min_cost_assignment = [] 
    
    for job in range(num_jobs):
        min_cost = max_possible_cost 
        assigned_worker = None
        
        for worker in range(num_workers):
            cost = a[worker] * workloads[job] 
            if cost < min_cost:
                min_cost = cost
                assigned_worker = worker
        
        min_cost_assignment.append((assigned_worker, min_cost))  
    
    return min_cost_assignment

a = [5, 7, 3, 6]
workloads = [2, 3, 1, 4]

assignment_result = min_cost_assignment(a, workloads)

for i, (worker, cost) in enumerate(assignment_result, start=1):
    print(f"Job {i}을(를) Worker {chr(worker + ord('A'))}에게 배정합니다. (비용: {cost})")
