
# Algorithm Deconstruction Challenge

## Selected Algorithm
Task Manager – Task Handling and Priority Management (Python)

## Algorithm Breakdown

The Task Manager algorithm is responsible for creating, storing, updating, and retrieving tasks. Each task includes a priority, status, due date, and optional tags. The algorithm validates input before storing tasks and allows tasks to be filtered and analysed.

### Task Creation
When a task is created, the algorithm converts the priority value into a predefined priority type and validates the due date format. Invalid input prevents the task from being created.

### Task Listing and Filtering
The algorithm allows tasks to be listed based on different conditions such as priority, status, or overdue state. Conditional logic determines which filter is applied.

### Task Updates
Tasks can be updated by changing their status, priority, or due date. Completed tasks are handled differently to ensure accurate tracking.

### Task Statistics
The algorithm calculates statistics by iterating through all tasks and counting them by status, priority, overdue state, and recent completion.

## Algorithm Flow

Create Task  
→ Validate Inputs  
→ Store Task  
→ List or Filter Tasks  
→ Update Task  
→ Calculate Statistics  

## Reflection

This exercise helped me understand how multiple functions work together as part of a complete task management algorithm.

The most challenging part was understanding how statistics are calculated by looping through tasks with conditions.

I would explain this algorithm to a junior developer as a system that validates input, manages tasks, and summarises data using conditional logic.

The algorithm could be improved by separating statistics calculations into a dedicated component and making priority handling configurable.
``
