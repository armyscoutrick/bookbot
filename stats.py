def get_num_words(text):
    import re
    words = re.findall(r'\S+', text)
    return len(words)
