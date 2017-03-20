def answer(words):
    pass

def get_char_by_row_and_col(word_list, row, col):
    try:
        char = word_list[row][col]
    except Exception as e:
        return "0"
    else:
        return char

def make_col_pass(word_list, col):
    left_row_ptr = 0
    right_row_ptr = 1

    out_arr = []

    while right_row_ptr < len(word_list):
        left_char = get_char_by_row_and_col(word_list, left_row_ptr, col)
        right_char = get_char_by_row_and_col(word_list, right_row_ptr, col)

        if left_char == "0":
            left_row_ptr = right_row_ptr
            right_row_ptr = left_row_ptr + 1
        elif right_char == "0":
            left_row_ptr = right_row_ptr + 1
            right_row_ptr = left_row_ptr + 1
        elif left_char == right_char:
            right_row_ptr += 1
        else:
            out_arr.append(left_char)

            left_row_ptr = right_row_ptr
            right_row_ptr = left_row_ptr + 1

    return out_arr


some_words = ['mcdr', 'jnvpn', 'jjvls', 'ntzzv', 'uxuco', 'ibi', 'ezmlt', 'ayclq', 'rmjxw', 'qfqzn']

col = 0

while col < 5:
    print ''.join(make_col_pass(some_words, col))

    col += 1



def get_char_pair(word_list, col, row):
    pair = []

    try:
        char_1 = word_list[row][col]
    except:
        char_1 = "0"

    try:
        char_2 = word_list[row + 1][col]
    except:
        char_2 = "0"

    if char_1 == "0" or char_2 == "0":
        return None
    else:
        pair.append(char_1)
        pair.append(char_2)

        return pair


some_words = ['mcdr', 'jnvpn', 'jjvls', 'ntzzv', 'uxuco', 'ibi', 'ezmlt', 'ayclq', 'rmjxw', 'qfqzn']

print get_char_pair(some_words, 4, 0)


def build_first_row(word_list):
    left_row_ptr = 0
    right_row_ptr = 1
    col = 0

    out_arr = []

    while right_row_ptr < len(word_list):
        left_char = get_char_by_row_and_col(word_list, left_row_ptr, col)
        right_char = get_char_by_row_and_col(word_list, right_row_ptr, col)

        if left_char == right_char:
            right_row_ptr += 1
        else:
            if len(out_arr) > 0 and out_arr[len(out_arr) - 1] == left_char:
                out_arr.append(right_char)
            else:
                out_arr.append(left_char)
                out_arr.append(right_char)

            left_row_ptr = right_row_ptr
            right_row_ptr = left_row_ptr + 1

    return out_arr

def get_char_by_row_and_col(word_list, row, col):
    try:
        char = word_list[row][col]
    except:
        return "0"
    else:
        return char

def build_other_columns(word_list, col):
    left_row_ptr = 0
    right_row_ptr = 1

    out_arr = []

    while right_row_ptr < len(word_list):
        left_char = get_char_by_row_and_col(word_list, left_row_ptr, col)
        right_char = get_char_by_row_and_col(word_list, right_row_ptr, col)

        if left_char == "0" or right_char == "0":
            left_row_ptr = right_row_ptr
            right_row_ptr = left_row_ptr + 1
        elif left_char == right_char:
            right_row_ptr += 1
        else:
            if len(out_arr) > 0 and out_arr[len(out_arr) - 1] == left_char:
                out_arr.append(right_char)
            else:
                out_arr.append(left_char)
                out_arr.append(right_char)

            left_row_ptr = right_row_ptr
            right_row_ptr = left_row_ptr + 1

    return out_arr

some_words = ['mcdr', 'jnvpn', 'jjvls', 'ntzzv', 'uxuco', 'ibi', 'ezmlt', 'ayclq', 'rmjxw', 'qfqzn']

better_test = ['ab', 'cde', 'fde', 'fdr', 'fdxy']
better_test_first_row = 'acf'
better_test_second_row = 'bd'
better_test_third_row = 'erx'

initial_list = build_first_row(better_test)


def answer(words):
    pass

def build_initial_sorted_list(arg):
    pass


# row = word position
# column = char-in-word position
# Assume a vertically-oriented word list, by row to get word, by column to get
#   char of word.

def get_char_by_row_and_col(word_list, row, column):
    # If we have an IndexError, just return a non-[a-z] char and let caller
    #   deal with it.
    try:
        # Get a char from a string with 'str[index]'.
        char = word_list[row][col]
    except:
        # This can be any non-[a-z] char.
        return "0"
    else:
        return char

def get_adjacent_pair_list(word_list, adjacent_pair_list, max_column, row, column):
    cur_column = column
    next_column = cur_column + 1

    while True:
        this_char = get_char_by_row_and_col(word_list, row, cur_column)
        next_char = get_char_by_row_and_col(word_list, row, next_column)

        if cur_column > max_column:
            return adjacent_pair_list
        elif this_char == '0' or next_char == '0':
            cur_column = next_column
            next_column = cur_column + 1
        elif this_char == next_char:
            next_column += 1
        else:
            adjacent_pair = [this_char, next_char]
            adjacent_pair_list.append(adjacent_pair)

            cur_column = next_column
            next_column = cur_column + 1

            get_adjacent_pair_list(word_list, adjacent_pair_list, max_column, cur_row, next_column)

def get_char_by_row_and_col(word_list, row, column):
    # If we have an IndexError, just return a non-[a-z] char and let caller
    #   deal with it.
    try:
        # Get a char from a string with 'str[index]'.
        char = word_list[row][col]
    except:
        # This can be any non-[a-z] char.
        return "0"
    else:
        return char

def get_max_columns(word_list):
    max_columns = 1

    for word in word_list:
        if len(word) > max_column:
            max_column = len(word)

    return max_columns


def get_adjacent_pair_list(word_list, adjacent_pair_list, max_columns, row, column):

    # No more letters to work with.
    if column > max_columns:
        return adjacent_pair_list

    cur_row = row
    next_row = cur_row + 1

    # Otherwise...
    while cur_row < len(word_list):
        cur_char = get_char_by_row_and_col(word_list, cur_row, column)
        next_char = get_char_by_row_and_col(word_list, next_row, column)

        if this_char == '0' or next_char == '0':
            cur_row = next_row
            next_row = cur_row + 1
        elif this_char == next_char:
            next_row += 1
        else:
            adjacent_pair = [this_char, next_char]
            adjacent_pair_list.append(adjacent_pair)

            cur_row = next_row

            get_adjacent_pair_list(word_list, adjacent_pair_list, max_column, cur_row, next_column)







#
def get_max_columns(word_list):
    max_columns = 1

    for word in word_list:
        if len(word) > max_columns:
            max_columns = len(word)

    return max_columns

def get_char_by_row_and_col(word_list, row, column):
    try:
        char = word_list[row][column]
    except:
        return "0"
    else:
        return char


def build_char_list_from_column(word_list, column):
    char_list = []

    for row in range(0, len(word_list)):
        char_list.append(get_char_by_row_and_col(word_list, row, column))

    return char_list

def get_adjacent_pair_list(char_list):
    cur_index = 0
    next_index = cur_index + 1

    adjacent_pair_list = []



    while next_index < len(char_list):
        cur_char = char_list[cur_index]
        next_char = char_list[next_index]

        if cur_char == '0' or next_char == '0':
            cur_index = next_index
            next_index = cur_index + 1
        elif cur_char == next_char:
            next_index += 1
        else:
            adjacent_pair_list.append([cur_char, next_char])

            cur_index = next_index
            next_index = cur_index + 1

    return adjacent_pair_list

def get_list_index(list, item):
    try:
        return list.index(item)
    except:
        return -1

def build_alphabetized_list(out_list, adjacent_pair_list):
    for pair in adjacent_pair_list:
        if len(pair) < 2:
            continue
        elif len(out_list) == 0:
            out_list.append(pair[0])
            out_list.append(pair[1])
        else:
            if get_list_index(out_list, pair[0]) == -1:
                out_list.insert(get_list_index(out_list, pair[1]), pair[0])
            else:
                out_list.insert(get_list_index(out_list, pair[0]) + 1, pair[1])

    return out_list

def answer(words):
    biggest_word = get_max_columns(some_words)

    if len(words) == 1:
        return words[0]
    elif biggest_word == 1:
        return words

    result_list = []

    for i in range(0, biggest_word):
        cur_char_list = build_char_list_from_column(some_words, i)

        build_alphabetized_list(result_list, cur_char_list)

    return result_list

some_words = ['y', 'z', 'xy']
print answer(some_words)

some_words = ['y', 'z', 'xy']

def get_max_columns(word_list):
    max_columns = 1

    for word in word_list:
        if len(word) > max_columns:
            max_columns = len(word)

    return max_columns

def get_char_by_row_and_col(word_list, row, column):
    try:
        char = word_list[row][column]
    except:
        return "0"
    else:
        return char


def build_char_list_from_column(word_list, column):
    char_list = []

    for row in range(0, len(word_list)):
        char_list.append(get_char_by_row_and_col(word_list, row, column))

    return char_list

def get_adjacent_pair_list(char_list):
    cur_index = 0
    next_index = cur_index + 1

    adjacent_pair_list = []

    while next_index < len(char_list):
        cur_char = char_list[cur_index]
        next_char = char_list[next_index]

        if cur_char == '0' or next_char == '0':
            cur_index = next_index
            next_index = cur_index + 1
        elif cur_char == next_char:
            next_index += 1
        else:
            adjacent_pair_list.extend([cur_char, next_char])

            cur_index = next_index
            next_index = cur_index + 1

    return adjacent_pair_list

#pair_list = []

char_list = []

for i in range(0, get_max_columns(some_words)):
    char_list.append(build_char_list_from_column(some_words, i))

print char_list

def build_alphabetized_list(out_list, adjacent_pair_list):
    for pair in adjacent_pair_list:
        if len(pair) < 2:
            continue
        elif len(out_list) == 0:
            out_list.append(pair[0])
            out_list.append(pair[1])
        else:
            if get_list_index(out_list, pair[0]) == -1:
                out_list.insert(get_list_index(out_list, pair[1]), pair[0])
            else:
                out_list.insert(get_list_index(out_list, pair[0]) + 1, pair[1])

def get_max_columns(word_list):
    max_columns = 1

    for word in word_list:
        if len(word) > max_columns:
            max_columns = len(word)

    return max_columns

def get_char_by_row_and_col(word_list, row, column):
    try:
        char = word_list[row][column]
    except:
        return "0"
    else:
        return char


def build_char_list_from_column(word_list, column):
    char_list = []

    for row in range(0, len(word_list)):
        char_list.append(get_char_by_row_and_col(word_list, row, column))

    return char_list

def alpha_adj_pair(alpha_list, adj_pair):
    if len(adj_pair) < 2:
        continue
    elif len(out_list) == 0:
        out_list.append(adj_pair[0])
        out_list.append(adj_pair[1])
    else:
        if get_list_index(out_list, adj_pair[0]) == -1:
            out_list.insert(get_list_index(out_list, adj_pair[1]), adj_pair[0])
        else:
            out_list.insert(get_list_index(out_list, adj_pair[0]) + 1, adj_pair[1])

def alpha_char_list(alpha_list, char_list):
    cur_index = 0
    next_index = cur_index + 1

    while next_index < len(char_list):
        cur_char = char_list[cur_index]
        next_char = char_list[next_index]

        if cur_char == '0' or next_char == '0':
            cur_index = next_index
            next_index = cur_index + 1
        elif cur_char == next_char:
            next_index += 1
        else:
            # alpha here

            cur_index = next_index
            next_index = cur_index + 1


some_words = ['y', 'z', 'xy']
other_words = ['ba', 'ab', 'cb']

print answer(other_words)


def get_max_columns(word_list):
    max_columns = 1

    for word in word_list:
        if len(word) > max_columns:
            max_columns = len(word)

    return max_columns

def get_char_by_row_and_col(word_list, row, col):
    try:
        char = word_list[row][col]
    except:
        return "0"
    else:
        return char

def get_alpha_list(word_list, alpha_list, max_col, col):

    if col > max_col:
        return alpha_list

    this_row = 0
    next_row = this_row + 1

    while next_row < len(word_list):
        this_char = get_char_by_row_and_col(word_list, this_row, col)
        next_char = get_char_by_row_and_col(word_list, next_row, col)

        if this_char == '0' or next_char == '0':
            this_row = next_row
            next_row = this_row + 1
        elif this_char == next_char:
            next_row += 1
        else:
            if len(alpha_list) == 0:
                alpha_list.append(this_char)
                alpha_list.append(next_char)
            else:
                if alpha_list.count(this_char) == 0 and alpha_list.count(next_char) != 0:
                    alpha_list.insert(alpha_list.index(next_char), this_char)
                elif alpha_list.count(next_char) == 0 and alpha_list.count(this_char) != 0:
                    alpha_list.insert(alpha_list.index(this_char) + 1, next_char)

            this_row = next_row
            next_row = this_row + 1

    return get_alpha_list(word_list, alpha_list, max_col, col + 1)

def answer(words):
    if len(words) == 1:
        return words[0]

    max_word_size = get_max_columns(words)
    alpha_list = []
    alpha_list = get_alpha_list(words, alpha_list, max_word_size, 0)

    return ''.join(alpha_list)

some_words = ['y', 'z', 'xy']
other_words = ['ba', 'ab', 'cb']

print answer(other_words)


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

more_words = ['c', 'cac', 'cb', 'bcc', 'ba']
some_words = ['y', 'z', 'xy']
other_words = ['ba', 'ab', 'cb']

print answer(more_words)
print answer(some_words)
print answer(other_words)


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

# I should state that I found a test case at;
# https://github.com/WilbertHo/foobar/blob/master/minglish_lesson/py/tests/test_minglishlesson.py
# This assisted me in moving my own solution forward, however, I hope it is understood
# that this is all I took from viewing said file.



def get_max_columns(word_list):
    max_columns = 1

    for word in word_list:
        if len(word) > max_columns:
            max_columns = len(word)

    return max_columns

def build_adj_pair_list(word_list, adj_pair_list, max_cols, col = 0):

    if col > max_cols:
        return adj_pair_list

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
            # If roots match and chars do not, add to adj_pair_list.
            if (word_list[this_row][0:col] == word_list[next_row][0:col] and
                    char_a != char_b):
                adj_pair_list.append([char_a, char_b])

                this_row = next_row
                next_row = this_row + 1
            # If roots match and chars do, continue.
            elif (word_list[this_row][0:col] == word_list[next_row][0:col] and
                    char_a == char_b):
                next_row += 1
            else:
                this_row = next_row
                next_row = this_row + 1

    return build_adj_pair_list(word_list, adj_pair_list, max_cols, col + 1)

def swap(swap_list, item_a, item_b):
    # foo[i], foo[j] = foo[j], foo[i]
    swap_list[swap_list.index(item_a)], swap_list[swap_list.index(item_b)] = swap_list[swap_list.index(item_b)], swap_list[swap_list.index(item_a)]

    return swap_list

def build_alphabetized_list(adj_pair_list):
    this_pair = adj_pair_list.pop(0)

    char_a = this_pair[0]
    char_b = this_pair[1]

    result_list = [char_a, char_b]

    while len(adj_pair_list) > 0:
        this_pair = adj_pair_list.pop(0)

        char_a = this_pair[0]
        char_b = this_pair[1]
        try:
            index_a = result_list.index(char_a)
        except:
            index_a = None

        try:
            index_b = result_list.index(char_b)
        except:
            index_b = None

        if index_a == None and index_b == None:
            adj_pair_list.append(this_pair)
        elif index_a != None and index_b == None:
            result_list.insert(index_a + 1, char_b)
        elif index_a == None and index_b != None:
            result_list.insert(index_b, char_a)
        elif index_a > index_b:
            result_list = swap(result_list, char_a, char_b)
        else:
            continue

    return result_list

def answer(words):
    max_cols = get_max_columns(words)

    adj_pairs = build_adj_pair_list(words, [], max_cols)

    answer_list = build_alphabetized_list(adj_pairs)

    return ''.join(answer_list)


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

    def get_node_index(self, node):
        node_index = 0

        this_node = self.head_node

        while this_node != None:
            this_value = this_node.get_value()
            if this_value == node.get_value():
                return node_index
            else:
                node_index += 1
                this_node = this_node.get_next_node()

        return None

    def swap_nodes(self, node_a, node_b):
        temp_value = node_b.get_value()

        node_b.set_value(node_a.get_value())
        node_a.set_value(temp_value)

    def get_all_values_as_string(self):
        result_list = []
        this_node = self.head_node

        while this_node != None:
            result_list.append(this_node.get_value())

            this_node = this_node.get_next_node()

        return ''.join(result_list)

def build_adj_pair_list(word_list, adj_pair_list, max_cols, col = 0):

    if col > max_cols:
        return adj_pair_list

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
            # If roots match and chars do not, add to adj_pair_list.
            if (word_list[this_row][0:col] == word_list[next_row][0:col] and
                    char_a != char_b):
                adj_pair_list.append([char_a, char_b])

                this_row = next_row
                next_row = this_row + 1
            # If roots match and chars do, continue.
            elif (word_list[this_row][0:col] == word_list[next_row][0:col] and
                    char_a == char_b):
                next_row += 1
            else:
                this_row = next_row
                next_row = this_row + 1

    return build_adj_pair_list(word_list, adj_pair_list, max_cols, col + 1)

def get_max_columns(word_list):
    max_columns = 1

    for word in word_list:
        if len(word) > max_columns:
            max_columns = len(word)

    return max_columns

def build_alphabetized_list(adj_pair_list):
    this_pair = adj_pair_list.pop(0)

    char_a = this_pair[0]
    char_b = this_pair[1]

    node_a = DoubleLinkedNode(char_a)
    node_b = DoubleLinkedNode(char_b)

    result_list = DoubleLinkedList(node_a)
    result_list.insert_node_after(node_a, node_b)

    while len(adj_pair_list) > 0:
        this_pair = adj_pair_list.pop(0)

        char_a = this_pair[0]
        char_b = this_pair[1]

        node_a = result_list.search(char_a)
        node_b = result_list.search(char_b)

        if node_a == None and node_b == None:
            adj_pair_list.append(this_pair)
        elif node_a != None and node_b == None:
            result_list.insert_node_after(node_a, DoubleLinkedNode(char_b))
        elif node_a == None and node_b != None:
            result_list.insert_node_before(node_b, DoubleLinkedNode(char_a))
        elif result_list.get_node_index(node_a) > result_list.get_node_index(node_b):
            result_list.swap_nodes(node_a, node_b)
        else:
            continue

    return result_list

def answer(words):
    max_columns = get_max_columns(words)

    if len(words) == 1:
        return str(words[0][0])

    adj_pair_list = build_adj_pair_list(words, [], max_columns)

    result_list = build_alphabetized_list(adj_pair_list)

    return result_list.get_all_values_as_string()

more_words = ['c', 'cac', 'cb', 'bcc', 'ba']
some_words = ['y', 'z', 'xy']
other_words = ['ba', 'ab', 'cb']

print answer(more_words)
print answer(some_words)
print answer(other_words)
