# LeetCode Solutions 💡

![LeetCode Progress](https://img.shields.io/badge/LeetCode-100%2B%20Solved-yellow)
![MIT License](https://img.shields.io/badge/License-MIT-green)

Welcome to my LeetCode repository! 🎉 This repository contains well-categorized, optimized, and beginner-friendly solutions to various LeetCode problems.  
All solutions are licensed under the [MIT License](LICENSE).

---

## 📖 **Table of Contents**
- [Array](#array) 🧮
- [Strings](#strings) ✍️
- [Linked Lists](#linked-lists) 🔗
- [Graphs](#graphs) 🌐
- [Dynamic Programming](#dynamic-programming) 🤖
- [Other Topics](#other-topics) 📚

---
---

## 🧮 **Arrays**

| 🆔 **Problem #** | 📜 **Title**                                    | 🔗 **Solution**                                           | 🚦 **Difficulty** | 📝 **Notes**                                           |
|-----------------|-------------------------------------------------|--------------------------------------------------------|------------------|-------------------------------------------------------|
| 1               | Two Sum                                         | [Python](solutions/arrays/two_sum.py)                   | Easy             | Hash map for efficient lookup.                        |
| 26              | Remove Duplicates from Sorted Array             | [Python](solutions/arrays/remove_duplicates.py)         | Easy             | Two-pointer technique.                                |
| 27              | Remove Element                                  | [Python](solutions/arrays/remove_element.py)            | Easy             | In-place updates using a pointer.                    |
| 88              | Merge Sorted Array                              | [Python](solutions/arrays/merge_sorted_array.py)        | Easy             | Merge using two-pointer approach.                    |
| 605             | Can Place Flowers                               | [Python](solutions/arrays/can_place_flowers.py)         | Easy             | Iterative check for flower placement.                |
| 238             | Product of Array Except Self                    | [Python](solutions/arrays/product_except_self.py)       | Medium           | Prefix and suffix multiplications.                   |
| 1346            | Check If N and Its Double Exist                 | [Python](solutions/arrays/check_double_exist.py)        | Easy             | Uses a set for efficient lookups.                    |
| 2554            | Maximum Number of Integers to Choose From a Range | [Python](solutions/arrays/2554_max_count.py)           | Medium           | Iteration, set lookup, and sum constraints.           |
| 3152            | Special Array II                                | [Python](solutions/arrays/3152_special_array_ii.py)     | Medium           | Check if subarray has alternating even-odd parity.    |
| 2779            | Maximum Beauty of an Array After Applying Operation | [Python](solutions/arrays/2779_maximum_beauty_of_an_array_after_applying_operation.py) | Medium | Sliding window and prefix sum to track overlapping intervals. |
| 2593            | Find Score of an Array After Marking All Elements | [Python](solutions/arrays/2593_find_score.py)           | Medium           | Use heap to always get the smallest unmarked element. |
| 2762            | Continuous Subarrays                            | [Python](solutions/arrays/2762_continuous_subarrays.py) | Medium           | Sliding window with deques to maintain min/max of subarrays. |
| 3264            | Final Array State After K Multiplication Operations | [Python](solutions/arrays/3264_final_array_state.py)   | Easy             | Greedy approach to repeatedly update the minimum value in the array. |
| 1475         | Final Prices With a Special Discount in a Shop | [Python](solutions/arrays/1475_final_prices_with_discount.py) | Easy          | Brute-force approach to find the nearest smaller price for each item. |

---
# ✍️ **Heap, Greedy, Priority Queue**

| 🆔 **Problem #** | 📜 **Title**                            | 🔗 **Solution**                                      | 🚦 **Difficulty** | 📝 **Notes**                                       |
|-----------------|-----------------------------------------|-----------------------------------------------------|-------------------|---------------------------------------------------|
| 2558            | [Take Gifts From the Richest Pile](https://leetcode.com/problems/take-gifts-from-the-richest-pile/) | [Python](solutions/Heap%20Greedy%20Priority%20Queue/2558_take_gifts_from_the_richest_pile.py) | 🟢 Easy         | Use a max-heap to efficiently pick and update the largest gift pile. |
| 1792            | [Maximum Average Pass Ratio](https://leetcode.com/problems/maximum-average-pass-ratio/) | [Python](solutions/Heap%20Greedy%20Priority%20Queue/1792_max_average_pass_ratio.py) | 🟡 Medium       | Use a max-heap to maximize potential gains in pass ratios for each class. |
| 2182            | [Construct String With Repeat Limit](https://leetcode.com/problems/construct-string-with-repeat-limit/) | [Python](solutions/Heap%20Greedy%20Priority%20Queue/2182_construct_string_with_repeat_limit.py) | 🟡 Medium       | Use a max-heap to prioritize characters and maintain repeat limits. |

---

---

## ✍️ **Strings**

| 🆔 Problem # | 📜 Title                                                       | 🔗 Solution                                     | 🚦 Difficulty | 📝 Notes                                |
|--------------|---------------------------------------------------------------|------------------------------------------------|---------------|-----------------------------------------|
| 2000         | Reverse Prefix of Word                                       | [Python](solutions/reverse_prefix.py)          | Easy          | String slicing and iteration.          |
| 345          | Reverse Vowels of a String                                   | [Python](solutions/reverse_vowels.py)          | Easy          | Two-pointer swap technique.            |
| 151          | Reverse Words in a String                                    | [Python](solutions/reverse_words.py)           | Medium        | Splitting and reversing words.         |
| 1071         | Greatest Common Divisor of Strings                            | [Python](solutions/gcd_strings.py)             | Easy          | Utilized GCD for substring checks.     |
| 1455         | Check If a Word Occurs As a Prefix of Any Word in a Sentence  | [Python](solutions/strings/prefix_check.py)    | Easy          | Split sentence, check prefix using `startswith`. |
| 2109         | Adding Spaces to a String                                    | [Python](solutions/strings/2109_add_spaces_to_string.py) | Medium        | Efficient use of slicing and list join |
| 2825         | Make String a Subsequence Using Cyclic Increments | [Python](solutions/strings/2825_make_subsequence.py) | Medium        | Two-pointer technique and cyclic character check | 
| 2337         | Move Pieces to Obtain a String           | [Python](solutions/strings/2337_move_pieces.py)     | Medium        | Two-pointer technique, movement constraints      |
| 2981         | Find Longest Special Substring That Occurs Thrice | [Python](solutions/strings/2981_find_longest_special_substring_that_occurs_thrice.py) | Medium        | Identify the longest special substring that occurs at least 3 times. |
---

## 🔗 **Linked Lists**

| 🆔 Problem # | 📜 Title                          | 🔗 Solution                       | 🚦 Difficulty | 📝 Notes                                |
|--------------|----------------------------------|-----------------------------------|---------------|-----------------------------------------|
| 3217         | Delete Nodes From Linked List Present in Array | [Python](solutions/delete_nodes.py) | Medium | Traversal and removal of marked nodes.|

---
## ✍️ **Binary Search, Greedy**

| 🆔 Problem # | 📜 Title                                   | 🔗 Solution                                            | 🚦 Difficulty | 📝 Notes                                       |
|--------------|-------------------------------------------|------------------------------------------------------|---------------|------------------------------------------------|
| 1760         | Minimum Limit of Balls in a Bag           | [Python](solutions/BST/1760_minimum_balls_in_bag.py)      | Medium        | Binary search for minimal penalty, with operation count |
| 2054         | Two Best Non-Overlapping Events           | [Python](solutions/BS%20&%20G/2054_two_best_events.py)           | Medium        | Greedy + Binary Search, Find max non-overlapping event pairs |
---

## 🌐 **Graphs**

| 🆔 Problem # | 📜 Title                          | 🔗 Solution                       | 🚦 Difficulty | 📝 Notes                                |
|--------------|----------------------------------|-----------------------------------|---------------|-----------------------------------------|
| 2577         | Minimum Time to Visit a Cell In a Grid | [Python](solutions/min_time_grid.py) | Hard | BFS with a priority queue.           |
| 773          | Sliding Puzzle                  | [Python](solutions/sliding_puzzle.py) | Hard  | BFS with state hashing.              |

---

## 🤖 **Dynamic Programming**

| 🆔 Problem # | 📜 Title                          | 🔗 Solution                       | 🚦 Difficulty | 📝 Notes                                |
|--------------|----------------------------------|-----------------------------------|---------------|-----------------------------------------|
| 1508         | Range Sum of Sorted Subarray Sums | [Python](solutions/range_sum.py) | Medium | Prefix sums with sorted subarrays.   |

---

## 📚 **Other Topics**

| 🆔 Problem # | 📜 Title                          | 🔗 Solution                       | 🚦 Difficulty | 📝 Notes                                |
|--------------|----------------------------------|-----------------------------------|---------------|-----------------------------------------|
| 455          | Assign Cookies                  | [Python](solutions/assign_cookies.py) | Easy  | Greedy approach with sorting.        |

---

### 🌟 **How to Use This Repository**
1. Navigate to the section of interest using the [Table of Contents](#table-of-contents).  
2. Click the solution link to view the implementation details.  
3. Solutions are concise, optimized, and beginner-friendly.  
4. Feel free to contribute or suggest improvements via pull requests! 🤝

---

### ⚡ **Contributing**
- Fork the repository and make changes.
- Submit a pull request with a description of your improvements.

---

🌟 *Happy Coding!* 🌟
