# Artifical Nueral Network
import random
import string

NODE_COUNT_PER_LAYER = [4,3,2]

class Node:
    def __init__(self):
        self.children = []  # Connection to children
        self.node_name = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        self.children_connection_weights = []   # Weight of the connections to children

    def make_children(self, current_layer, nodes_per_layer_map):
        # Recursion end condition
        if current_layer >= len(nodes_per_layer_map):
            return
        
        # Creates children for this node
        for i in range(nodes_per_layer_map[current_layer]):
            self.children.append(Node())

        first_child = self.children[0]
        first_child.make_children(current_layer + 1, nodes_per_layer_map)
        # Connection from first child copied to each child
        for i in range(1, len( self.children ) ):
            self.children[i].children = first_child.children[:]

    def adjust_child_weights(self):
        # Recursion end condition
        if len(self.children) == 0:
            return

        self.children_connection_weights = []

        for i in range(len(self.children)):
            self.children_connection_weights.append(random.uniform(0, 1))
            self.children[i].adjust_child_weights()  # recurse

    def OUTPUT_children(self, layer):
        # Indentation per level
        indent = '    ' * layer
        # Recursion end case
        if len(self.children) == 0:
            print(f"{indent}{self.node_name}")
            return
        print(f"{indent}{self.node_name} is connected to ")

        for i in range(len(self.children)):
            self.children[i].OUTPUT_children(layer + 1)
            # Outputting weight if we have it
            if i < len(self.children_connection_weights):
                print(f" {indent} with weight {self.children_connection_weights[i]} ")

# Create a master node that we can use to connect to all the layers
INPUT_nodes = []
master_node = Node()
my_first_node = Node()

# make all the children FOR the first node
my_first_node.make_children(1, NODE_COUNT_PER_LAYER)
master_node.children.append(my_first_node)

# duplicate the first node FOR all INPUT nodes
for i in range(0, len(NODE_COUNT_PER_LAYER)):
    new_node = Node()
    # Copy children to the new node
    new_node.children = my_first_node.children[:]
    master_node.children.append(new_node)

# Outputs to see connections
master_node.OUTPUT_children(0)
print("!! Set Weights !!")
# init the weights
master_node.adjust_child_weights()
# OUTPUT out with weights
master_node.OUTPUT_children(0)
