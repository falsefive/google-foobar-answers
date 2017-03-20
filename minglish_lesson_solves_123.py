class DoubleLinkedNode:

    def __init__(self, value, last_node = None, next_node = None):
        self.value = value
        self.last_node = last_node
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(selfnew_value):
        self.value = new_value

    def get_last_node(self):
        return self.last_node

    def set_last_node(self, new_last_node):
        self.last_node = new_last_node

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node

class DoubleLinkedList:

    def __init__(self, head_node = None):
        self.head_node = head_node
        if head_node != None:
            self.link_count = 1
        else:
            self.link_count = 0

    def len(self):
        return self.link_count

    def get_head_node(self):
        return self.head_node

    def set_head_node(self, new_head_node):
        new_head_node.set_next_node(self.head_node)
        self.head_node = new_head_node

    def insert_node_before(self, node, new_node):
        new_node.set_next_node(node)
        last_node = node.get_last_node()

        if last_node == None:
            self.head_node = new_node
        else:
            last_node.set_next_node(new_node)

        self.link_count += 1

    def insert_node_after(self, node, new_node):
        new_node.set_next_node(node.get_next_node())
        node.set_next_node(new_node)

        self.link_count += 1

    def search(self, value):
        this_node = self.head_node

        while this_node != None:
            this_value = this_node.get_value()
            if this_value == value:
                return this_node
            else:
                this_node = this_node.get_next_node()

        return None

    def get_all_values_as_string(self):
        result_list = []
        this_node = self.head_node

        while this_node != None:
            result_list.append(this_node.get_value())

            this_node = this_node.get_next_node()

        return ''.join(result_list)


def get_alpha_list(word_list, alpha_list, max_col, col = 0):

    if col > max_col:
        return alpha_list

    this_row = 0
    next_row = this_row + 1

    while next_row < len(word_list):
        try:
            char_a = word_list[this_row][col]
            char_b = word_list[next_row][col]
        except:
            this_row = next_row
            next_row = this_row + 1
        else:
            if char_a == char_b:
                next_row += 1

            elif (word_list[this_row][0:col] == word_list[next_row][0:col] and
                    char_a != char_b):
                char_a_node = alpha_list.search(char_a)
                char_b_node = alpha_list.search(char_b)

                if char_a_node != None and char_b_node == None:
                    char_b_node = DoubleLinkedNode(char_b)
                    alpha_list.insert_node_after(char_a_node, char_b_node)

                elif char_a_node == None and char_b_node != None:
                    char_a_node = DoubleLinkedNode(char_a)
                    alpha_list.insert_node_before(char_b_node, char_a_node)

                this_row = next_row
                next_row = this_row + 1
            else:
                this_row = next_row
                next_row = this_row + 1

    return get_alpha_list(word_list, alpha_list, max_col, col + 1)


def get_max_columns(word_list):
    max_columns = 1

    for word in word_list:
        if len(word) > max_columns:
            max_columns = len(word)

    return max_columns

def answer(words):
    max_columns = get_max_columns(words)

    if len(words) == 1:
        return str(words[0][0])
    elif max_columns == 1:
        return ''.join(words)

    result_list = DoubleLinkedList(DoubleLinkedNode(words[0][0]))

    result_list = get_alpha_list(words, result_list, max_columns)

    return result_list.get_all_values_as_string()
