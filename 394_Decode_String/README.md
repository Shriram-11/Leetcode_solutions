# Decoding String Solution

## Problem Description

Given an encoded string where some characters are followed by a count in square brackets, decode the string.

## Solution

The solution uses a stack to keep track of characters and counts while iterating through the encoded string. The key steps are:

1. Initialize an empty stack.
2. Iterate through each character in the encoded string.
3. If the character is not ']', push it onto the stack.
4. If the character is ']', start decoding the substring:
   - Pop characters from the stack until '[' is encountered to build the substring.
   - Pop digits from the stack to build the count of repetition.
   - Append the decoded substring repeated by the count to the stack.
5. Concatenate the elements in the stack to get the final decoded string.

The time complexity of the algorithm is O(n), where n is the length of the input string, and the space complexity is O(n) due to the stack.
