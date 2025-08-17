# Node to represent a term in the polynomial
class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None

# Polynomial class
class Polynomial:
    def __init__(self):
        self.head = None

    def add_term(self, coeff, exp):
        if coeff == 0:
            return
        new = Node(coeff, exp)

        # Insert at the beginning or before head if exponent is largest
        if not self.head or exp > self.head.exp:
            new.next = self.head
            self.head = new
            return

        curr = self.head
        prev = None

        # Traverse to find the correct position or combine like terms
        while curr and curr.exp >= exp:
            if curr.exp == exp:
                curr.coeff += coeff
                # Remove term if coefficient becomes zero
                if curr.coeff == 0:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.head = curr.next
                return
            prev = curr
            curr = curr.next

        # Insert in the middle or end
        new.next = curr
        if prev:
            prev.next = new
        else:
            self.head = new

    def display(self):
        curr = self.head
        result = []
        while curr:
            coeff = curr.coeff
            exp = curr.exp
            if coeff > 0 and result:
                result.append(f"+ {coeff}x^{exp}")
            else:
                result.append(f"{coeff}x^{exp}")
            curr = curr.next
        print(" ".join(result) if result else "0")

    def add(self, other):
        return self._merge(other, add=True)

    def subtract(self, other):
        return self._merge(other, add=False)

    def _merge(self, other, add=True):
        p1 = self.head
        p2 = other.head
        result = Polynomial()

        while p1 and p2:
            if p1.exp == p2.exp:
                c = p1.coeff + p2.coeff if add else p1.coeff - p2.coeff
                result.add_term(c, p1.exp)
                p1, p2 = p1.next, p2.next
            elif p1.exp > p2.exp:
                result.add_term(p1.coeff, p1.exp)
                p1 = p1.next
            else:
                c = p2.coeff if add else -p2.coeff
                result.add_term(c, p2.exp)
                p2 = p2.next

        while p1:
            result.add_term(p1.coeff, p1.exp)
            p1 = p1.next
        while p2:
            c = p2.coeff if add else -p2.coeff
            result.add_term(c, p2.exp)
            p2 = p2.next

        return result

# Test Polynomials

# P1 = 3x^3 + 4x^2
p1 = Polynomial()
p1.add_term(3, 3)
p1.add_term(4, 2)

# P2 = 2x^3 + 5x^1
p2 = Polynomial()
p2.add_term(2, 3)
p2.add_term(5, 1)

print("P1:        ", end=""); p1.display()
print("P2:        ", end=""); p2.display()
print("P1 + P2:   ", end=""); p1.add(p2).display()
print("P1 - P2:   ", end=""); p1.subtract(p2).display()

# P3 = 3x^2 - 4x + 8
p3 = Polynomial()
p3.add_term(3, 2)
p3.add_term(-4, 1)
p3.add_term(8, 0)

# P4 = -x^2 - 2x + 3
p4 = Polynomial()
p4.add_term(-1, 2)
p4.add_term(-2, 1)
p4.add_term(3, 0)

print("\nP3:        ", end=""); p3.display()
print("P4:        ", end=""); p4.display()
print("P3 + P4:   ", end=""); p3.add(p4).display()

# P6 = 3x^5 + x^4 + 2x^3 - 2x + 5
p6 = Polynomial()
p6.add_term(3, 5)
p6.add_term(1, 4)
p6.add_term(2, 3)
p6.add_term(-2, 1)
p6.add_term(5, 0)

# P7 = 2x^6 + 3x^3 + 7x + 3
p7 = Polynomial()
p7.add_term(2, 6)
p7.add_term(3, 3)
p7.add_term(7, 1)
p7.add_term(3, 0)

print("\nP6:        ", end=""); p6.display()
print("P7:        ", end=""); p7.display()
print("P6 + P7:   ", end=""); p6.add(p7).display()
print("P6 - P7:   ", end=""); p6.subtract(p7).display()
