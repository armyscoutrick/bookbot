def get_num_words(text):
    import re
    
    words = re.findall(r'\b[\w\'-]+\b', text)
    return len(words)
