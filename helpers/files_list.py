class Node:
    def __init__(self, new_data):
        self.data: str = new_data
        self.next = None

class Files_List:
    def __init__(self):
        self.head: Node = None

    def insert(self, new_data):
        is_repeated = self.search_item(self.head, new_data)
        if is_repeated:
            raise ValueError('Item already exists')
        
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        return True
    
    def search_item(self, current_node: Node, key: str):
        while current_node is not None:
            if current_node.data == key:
                return True
            
            current_node = current_node.next

        return False
    
    def list_length(self):
        count = 0
        current = self.head
        
        while current is not None:
            count += 1
            current = current.next

        return count

    
    def print_items(self):
        items = []
        current = self.head
        
        while current is not None:
            items.append(current.data)
            current = current.next
        
        return items
    

