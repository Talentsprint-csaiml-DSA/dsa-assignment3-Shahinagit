import heapq
from collections import defaultdict

# Helper class for building the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.freq < other.freq

# Function to count character frequencies in the string
def count_frequencies(string):
    frequency = defaultdict(int)
    for char in string:
        frequency[char] += 1
    return frequency

# Function to build the Huffman tree
def build_huffman_tree(frequencies):
    priority_queue = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        # Extract two nodes with the smallest frequencies
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        # Create a new internal node with these two nodes as children
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        # Insert the new node back into the priority queue
        heapq.heappush(priority_queue, merged)
    
    # The remaining node is the root of the Huffman tree
    return priority_queue[0]

# Function to generate Huffman codes from the Huffman tree
def generate_huffman_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}
    
    # Base case: if it's a leaf node (a character)
    if root is not None:
        if root.char is not None:
            codes[root.char] = current_code
        # Recurse for left and right children
        generate_huffman_codes(root.left, current_code + "0", codes)
        generate_huffman_codes(root.right, current_code + "1", codes)
    
    return codes

# Function to encode the input string using Huffman coding
def huffman_encode(string):
    # Step 1: Count the frequencies of characters
    frequencies = count_frequencies(string)
    
    # Step 2: Build the Huffman tree
    huffman_tree_root = build_huffman_tree(frequencies)
    
    # Step 3: Generate Huffman codes for each character
    huffman_codes = generate_huffman_codes(huffman_tree_root)
    
    # Step 4: Encode the input string using the Huffman codes
    encoded_string = ''.join(huffman_codes[char] for char in string)
    
    return encoded_string, huffman_codes

# Example usage
input_string = "huffman test"
encoded_string, huffman_codes = huffman_encode(input_string)

print("Input String:", input_string)
print("Encoded String:", encoded_string)
print("Huffman Codes:", huffman_codes)