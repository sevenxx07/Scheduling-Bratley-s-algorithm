# Graham’s notation
As there are many different scheduling problems, it is sometimes hard to find a relevant research and see
if the problem was already solved or not. For the categorization of scheduling problems, there exists a
Graham’s (or Graham-Blazewicz) notation, also called α|β|γ notation [1, 2]. This notation is trying to
characterize the scheduling problem based on 3 aspects:
α contains the characteristics of resources – the number (1 to ∞) and type (P for parallel identical,
Q for parallel uniform, etc.),
β specifies the characteristics of tasks and additional resources (rj means that each task has release
time, pmtn means that preemption is allowed, etc.),
γ denotes an optimality criterion (Cmax for minimizing the schedule length, Lmax for minimizing the
maximal lateness, P Uj for minimizing the number of tasks exceeding their due date, etc.).

# Monoprocessor scheduling and Bratley’s algorithm
Now, we will concentrate on a problem of 1|rj , ˜dj |Cmax, i.e., the problem with a single machine and tasks
characterized by release times and deadlines, where we want to minimize a total length of the schedule.
## Problem statement
Input: We are given a set to tasks T = {T1, . . . , Tn}, where each task Ti ∈ T is characterized by its
release time ri, deadline ˜di and processing time pi

# Bratley’s algorithm
Bratley’s algorithm is based on a branch-and-bound procedure.
It can be seen, that the complete permutation tree has n! leaves. To evaluate them all would be very
inefficient. However, usually we do not need to do that. We might be able to prune some nodes before
expanding them further.
We can try to derive some pruning rules using the objective function or the tasks constraints. In
each node of the tree, we can compute a lower bound LB (based on the current partial solution) and
compare it to global upper bound U B (which is obtained from some feasible solution/approximation
algorithm/estimation). On the other hand, we can also prune the current node using the characteristics
of non-scheduled tasks, e.g., when some nonscheduled task would surely miss its deadline, it would be
meaningless to expand this node further.
## Missed deadline
It might happen that unassigned task would miss its deadline when assigned to the current schedule,
if that is the case, prune this node. (It is meaningless to continue, because in the future, some task
would surely miss its deadline).
(∃ Tj ∈ V : max{c, rj } + pj > dj ) ⇒ prune this node. 
## Bound on the solution
We might have already found some feasible solution, which might not be optimal. However, we
can use its quality as an upper bound (U B). We can calculate lover bound (LB) of the current
solution and prune this node if LB ≥ U B.
## Decomposition
We might be able to detect, that the partial solution we have in the current node is optimal,
therefore it might not be necessary to backtrack.
(c ≤ min{rj }) ⇒ do not backtrack. 
That is because tasks in V need to be scheduled, but cannot be scheduled sooner, and so tasks in
T \ V will not affect the final Cmax. We can start the algorithm again for tasks in V and simply
concatenate the solution with the current partial solution of T \ V .
