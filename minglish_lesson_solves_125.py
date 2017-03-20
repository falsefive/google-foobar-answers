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
        else:
            continue

    return result_list


def answer(words):
    max_cols = get_max_columns(words)

    adj_pairs = set(build_adj_pair_list(words, [], max_cols))

    answer_list = build_alphabetized_list(adj_pairs)

    return ''.join(answer_list)

more_words = ['c', 'cac', 'cb', 'bcc', 'ba']
some_words = ['y', 'z', 'xy']
other_words = ['ba', 'ab', 'cb']

print answer(more_words)
#print answer(some_words)
#print answer(other_words)
