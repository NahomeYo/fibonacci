# Fibonacci

## Complexity

- Best: O(n)
- Worst: O(n)
- Avg: O(n)
- Space: O(n)

## Problem Description

This implementation computes the `n`th Fibonacci number with dynamic programming. The Fibonacci sequence starts with 0 and 1, and every later value is the sum of the two values that come before it. That creates a very simple recurrence, but it also creates repeated subproblems if the sequence is computed with a naive recursive method.

Instead of recomputing the same smaller Fibonacci values over and over, this version stores earlier answers in a table and builds the result from the bottom up. Even though Fibonacci is a small example, it shows the central idea behind dynamic programming very clearly: solve smaller subproblems once, save their answers, and reuse them when building larger ones.

## Code

```javascript
/**
 * Compute the nth Fibonacci number with bottom-up dynamic programming.
 *
 * @param {number} n Target Fibonacci index.
 * @returns {number} The nth Fibonacci value.
 */
function fibonacci(n) {
    if (n === 0) {
        return 0;
    }

    const values = [];
    values[0] = 0;
    values[1] = 1;

    for (let index = 2; index <= n; index++) {
        // Each value depends only on the two previous Fibonacci values.
        values[index] = values[index - 1] + values[index - 2];
    }

    return values[n];
}

/**
 * Run the Fibonacci demonstration.
 *
 * @returns {void}
 */
function main() {
    const n = 8;

    console.log("Original input =", n);
    console.log("Fibonacci value =", fibonacci(n));
}

main();
```

## Algorithm Steps

1. Create an array to store the Fibonacci values for smaller indices.
2. Set the base cases `F[0] = 0` and `F[1] = 1`.
3. Loop from index 2 up to `n`.
4. At each index, compute `F[i] = F[i - 1] + F[i - 2]`.
5. Return `F[n]` after the table is complete.

## Explanation

A naive recursive Fibonacci solution looks simple, but it performs a large amount of repeated work because it recalculates the same smaller Fibonacci values many times. That causes the recursive version to grow exponentially. This bottom-up dynamic programming version avoids that repetition by storing each Fibonacci value exactly once.

After the base cases `F[0] = 0` and `F[1] = 1` are set, every later value is built with the recurrence `F[i] = F[i - 1] + F[i - 2]`. Since the two needed previous values have already been computed and saved, each new step takes constant time. The algorithm therefore moves through the table in a clean, predictable way without any repeated subproblem work.

The loop performs one constant-time update for each index from 2 through `n`, so the runtime is `O(n)`. Because the implementation stores all Fibonacci values from 0 through `n`, the space usage is also `O(n)`.
