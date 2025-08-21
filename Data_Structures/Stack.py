
class Stack:
    def __init__(self):
        self.item = []
    
    def push(self, item):
        self.item.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            return None
            
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            return None
            
    def is_empty(self):
        return self.item == []
        
    def size(self):
        return len(self.item)

class DelimiterMatcher:
    def __init__(self):
        self.pairs = {'(':')', '{':'}', '[':']'}
    
    def is_matching(self, code_string):
        stack = Stack()
        for char in code_string:
            if char in "([{":
                stack.push(char)
            elif char in ")]}":
                if stack.is_empty():
                    return False
                top = stack.pop()
                expected_opening = self.pairs.get(char)
                if top != expected_opening:
                    return False
        return stack.is_empty()

class DelimiterMatcher:
    def __init__(self):
        self.pairs = {'(': ')', '{': '}', '[': ']'}
    
    def is_matching(self, code_string):
        stack = Stack()
        for char in code_string:
            if char in "([{":
                stack.push(char)
            elif char in ")]}":
                if stack.is_empty():
                    return False
                top = stack.pop()
                if self.pairs[top] != char:  # ✅ fixed here
                    return False
        return stack.is_empty()

class PrefixToPostfixConverter:
    def __init__(self):
        pass

    def is_operand(self, ch):
        return ch.isalpha() or ch.isdigit()
        
    def convert(self, prefix_expr):
        stack = Stack()
        for char in reversed(prefix_expr):
            if self.is_operand(char):
                stack.push(char)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                new_expr = op1 + op2 + char
                stack.push(new_expr)
        return stack.pop()

# C code snippet for delimiter checking
c_code = """
#include <stdio.h>
int main(){
    int a=10;
    if (a>5){
        printf("hello");
    }else{
        printf("Bye");
    }
    return 0;
}
"""

# Delimiter check output
print("Delimiter check (C code):", "Balanced" if DelimiterMatcher().is_matching(c_code) else "Not Balanced")
expr1 = "{{}}()[]"
print("Delimiter check ({}()):", "Balanced" if DelimiterMatcher().is_matching(expr1) else "Not Balanced")
expr2 = "({)}"
print("Delimiter check ({)}):", "Balanced" if DelimiterMatcher().is_matching(expr2) else "Not Balanced")
expr3 = "(([]))"
print("Delimiter check (([])):", "Balanced" if DelimiterMatcher().is_matching(expr3) else "Not Balanced")
