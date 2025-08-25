class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__ (self):
        self.root=None

    def insert(self,root,value):
        """Recursively inserts a value into the BST following those rules:
            -If the tree is empty,insert the new node as the root
            -If value is ;ess than current node's Data,insert in the left subtree.
            -If value is greater or equal,insert in the right subtree.
        """
        if root is None:
            return Node(value)
        if value < root.data:
            root.left = self.insert(root.left,value)
        else:
            root.right = self.insert(root.right,value)
        return root #Return The unchanged root pointer
    
    def Inorder(self,node):
        """
        Inorder Traversal(Left,Root,Right)
        Prints values in ascending order for a BST.
        """

        if node:
            self.Inorder(node.left)     #Visit Left Subtree
            print(node.data,end=" ")    #Visit Current node
            self.Inorder(node.right)    #Visit right Subtree

    
    def preorder(self,node):
        """
        Preorder Traversal (Root,Left,Right)
        Useful for creating a copy of the tree.
        """
        if node:
            print(node.data,end=" ")    #Visit Current node
            self.preorder(node.left)    #Visit left subtree
            self.preorder(node.right)   #Visit Right Subtree

    def postorder(self,node):
        """
        Postorder traversal (left,Right,Root)
        Useful for deleting the Tree(Deallocating memory)
        """

        if node:
            self.postorder(node.left)   #Visit Left Subtree
            self.postorder(node.right)  #Visit Right Subtree
            print(node.data,end=" ")    #Visit Current Node


dataset = [50,30,70,20,40,60,80]    #Dataset to build the BST
bst=BST()   #Create an instance of BST
#Insert all values from dataset into BST
for value in dataset:
    bst.root = bst.insert(bst.root,value)

#Traversal
print("Inorder Traversal (Sorted Order):")
bst.Inorder(bst.root)

print("\nPreorder Traversal:")
bst.preorder(bst.root)

print("\nPostorder Traversal: ")
bst.postorder(bst.root)

