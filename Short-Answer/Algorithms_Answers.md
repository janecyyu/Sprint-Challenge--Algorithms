#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(log n)

b) O(n log n)

c) O(1)

## Exercise II

if f(floor) greater than egg's position:
egg broken, so eggs' quantity minus one

solution1:
f from 1(first floor)
if egg not broken, then we know the floor
\*runtime O(n)

solution2:
look from f/2,

while egg broken, means too high or equal, so go down, current floor divide 2 again

while egg not broke, go up to check if the egg broke, (f + current floor)/2
if egg broke, the answer will be current floor -1
