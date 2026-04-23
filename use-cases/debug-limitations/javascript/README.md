# Merge Sort Debugging Exercise

This exercise is designed to help you practice debugging skills with a JavaScript implementation of the merge sort algorithm.

## Overview

The repository contains:
- `merge_sort.js`: An implementation of merge sort with a bug
- `tests/merge_sort.test.js`: Jest tests that demonstrate the bug

## Requirements

- Node.js (any recent version)
- npm (comes with Node.js)

## Setup

Install the dependencies:

```bash
npm install
```

## Running the Code

You can run the merge sort implementation directly:

```bash
node merge_sort.js
```

However, this won't show much output, as the file only defines the functions without executing them.

## Running the Tests

Run the test suite to see the bug in action:

```bash
npm test
```

Or run tests in watch mode to see changes as you fix the code:

```bash
npm run test:watch
```

The tests will fail or time out due to the bug in the merge sort implementation.


## AI Solution Verification Challenge

### Bug Description
The merge sort implementation contained a bug in the `merge` function that caused an infinite loop. As a result, the Jest test suite failed or timed out instead of completing.

### AI Assistance
An AI tool was used to analyze the merge sort implementation. The AI identified that the issue was caused by incrementing the wrong index variable when copying remaining elements from the left array during the merge phase.

### Verification Process

#### Collaborative Solution Verification
The merge function was manually stepped through using small example arrays. It was observed that the loop condition depended on the variable `i`, but `i` was never incremented inside the loop. This confirmed that the function would never terminate.

#### Learning Through Alternative Approaches
The merge logic was compared with standard merge sort implementations. All correct references increment the same index variable that appears in the loop condition, confirming the AI’s recommendation.

#### Developing a Critical Eye
Edge cases where one sub-array finishes before the other were considered. These cases consistently caused the infinite loop until the index increment was corrected.

### Final Outcome
After fixing the index increment in the merge function, the merge sort implementation worked correctly and all Jest tests passed successfully.

