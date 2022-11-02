def count_common_words(filename, word):
    """计算指定的单词在图书中出现了多少次。"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)

        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

filename = 'alice.txt'
count_common_words(filename, 'the')
