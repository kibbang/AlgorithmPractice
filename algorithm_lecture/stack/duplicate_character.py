from algorithm_lecture.stack.Stack import Stack

def duplicate_character():
    sample_words = "abbaca"

    void_stack = Stack(len(sample_words))

    for word in sample_words:
        if void_stack.isEmpty():
            void_stack.push(word)
        else:
           if word == void_stack.array[void_stack.top]:
               void_stack.pop()
           else:
               void_stack.push(word)

    for char in void_stack.array:
        if char is None:
            continue
        print(char, end="")

if __name__ == '__main__':
    duplicate_character()