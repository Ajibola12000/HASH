def rolling_hash(s, p=31, mod=1e9+9):
    mod = int(mod)
    n = len(s)
    hash_val = 0
    p_pow = 1
    for c in s:
        hash_val = (hash_val + (ord(c) - ord('a') + 1) * p_pow) % mod
        p_pow = (p_pow * p) % mod
    return hash_val

def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    p, mod = 31, int(1e9+9)
    
    pat_hash = rolling_hash(pattern, p, mod)
    text_hash = rolling_hash(text[:m], p, mod)
    
    p_m = pow(p, m-1, mod)  # Precompute p^(m-1)
    
    for i in range(n - m + 1):
        if text_hash == pat_hash and text[i:i+m] == pattern:
            print(f"Pattern found at index {i}")
        
        if i < n - m:
            # Slide the window
            left = (ord(text[i]) - ord('a') + 1)
            right = (ord(text[i + m]) - ord('a') + 1)
            text_hash = (text_hash - left + mod) % mod
            text_hash = (text_hash * pow(p, -1, mod)) % mod  # Divide by p
            text_hash = (text_hash + right * p_m) % mod

# Test
rabin_karp("thequickbrownfoxjumpsoverthelazydog", "brown")
