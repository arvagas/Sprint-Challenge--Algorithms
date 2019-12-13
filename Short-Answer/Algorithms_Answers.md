#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) `O(n)`: The loop is running linearly. Will run based on n variable


b) `O(n log n)`: The while loop is running at O(n). However the outer for loop has a higher time complexity.


c) `O(n)`: This is a basic recursive function that runs based on the number passed.

## Exercise II
- Start from the middle of the building (n/2)
- Run a loop that checks to see if the egg breaks
- If it doesn't break, return the floor
- If it breaks, ignore the top half and search the lower half starting from its middle
- Repeat previous step until egg doesn't break

TLDR; Binary search, O(log n)