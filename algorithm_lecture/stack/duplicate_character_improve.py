from algorithm_lecture.stack.Stack import Stack

def duplicate_character_improve():
    sample_words = "abbaca"

    word_stack = Stack(len(sample_words))

    for word in sample_words:
        if word_stack.isEmpty():
            word_stack.push(word)
        else:
           if word == word_stack.peek():
               word_stack.pop()
           else:
               word_stack.push(word)

    word_stack.display()
if __name__ == '__main__':
    duplicate_character_improve()