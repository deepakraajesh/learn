import string

alpha = set(string.ascii_lowercase)
gstri = 'the quick brown fox jumps over the lazy dog'

print(set(alpha)-set(gstri))