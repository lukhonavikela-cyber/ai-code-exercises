
# Testing Exercise Reflection

## Overview
This exercise focused on improving my testing skills using AI as a learning aid.
I worked with a Python-based task prioritization system and used AI to guide my
thinking rather than to generate solutions for me.

## Part 1: Understanding What to Test
I began by analysing the behaviour of the `calculate_task_score` function before
writing any tests. This helped me understand how priority, due dates, task updates,
and other factors influence task scoring. Creating a test plan first made the
subsequent testing more structured and intentional.

## Part 2: Improving a Single Test
I started with a simple unit test to validate basic functionality, then improved
it by clarifying its purpose and making the assertions more precise. I added
additional tests for overdue tasks to ensure important edge cases were covered.

## Part 3: Test-Driven Development
I practiced Test-Driven Development by first writing a failing test for a new
feature where tasks assigned to the current user receive a score boost. I then
implemented the minimal code required to make the test pass.

I also used TDD to fix a bug in the days-since-update calculation. Writing a failing
test helped expose issues such as incorrect time handling, early returns, and
inconsistent data access. Fixing the bug ensured that future regressions are
prevented.

## Part 4: Integration Testing
I wrote an integration test to verify that task scoring, sorting, and selection of
top-priority tasks all work correctly together. This confirmed that the system
behaves as expected when individual components are combined.

## What I Learned
This exercise showed me the importance of understanding behaviour before writing
tests. Using AI as a guide helped me identify edge cases and improve test quality
without relying on generated solutions. I learned how disciplined testing, TDD,
and integration tests contribute to more reliable and maintainable code.
