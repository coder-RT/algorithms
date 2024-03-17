"""
Given an encoded string, return its corresponding decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.

Note that your solution should have linear complexity because this is what you will be asked during an interview.

Example

For s = "4[ab]", the output should be
solution(s) = "abababab";

For s = "2[b3[a]]", the output should be
solution(s) = "baaabaaa";

For s = "z1[y]zzz2[abc]", the output should be
solution(s) = "zyzzzabcabc".

Explanation: https://www.youtube.com/watch?v=qB0zZpBJlh8

"""
ef solution(s):
    stack = []
    
    for c in s:
        if c != "]":
            stack.append(c)
        else:
            substr = ""
            while stack[-1] != "[":
                substr = stack.pop() + substr
            stack.pop() # pop out "["
            
            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(int(k) * substr)
    return "".join(stack)
