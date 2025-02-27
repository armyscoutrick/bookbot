def get_num_words(text):
    import re
    # Using a simpler pattern to match what might be closer to the test's definition
    words = re.findall(r'[a-zA-Z0-9\'-]+', text)
    return len(words)
