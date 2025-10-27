def create_playfair_square(key):
    key = key.upper().replace("J", "I")
    square_chars = []
    for char in key:
        if char.isalpha() and char not in square_chars:
            square_chars.append(char)
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in square_chars:
            square_chars.append(char)
            
    matrix = [square_chars[i*5:(i+1)*5] for i in range(5)]
    return matrix

def find_char_location(matrix, char):
    for r_idx, row in enumerate(matrix):
        for c_idx, c in enumerate(row):
            if c == char:
                return r_idx, c_idx
    return None, None

def preprocess_message(message):
    message = message.upper().replace("J", "I")
    processed_message = []
    i = 0
    while i < len(message):
        char1 = message[i]
        if i + 1 < len(message):
            char2 = message[i+1]
            if char1 == char2:
                processed_message.append(char1)
                processed_message.append('X')
                i += 1
            else:
                processed_message.append(char1)
                processed_message.append(char2)
                i += 2
        else: 
            processed_message.append(char1)
            processed_message.append('X')
            i += 1
    return "".join(processed_message)

def playfair_encrypt(message, key):
    matrix = create_playfair_square(key)
    processed_msg = preprocess_message(message)
    
    ciphertext = []
    for i in range(0, len(processed_msg), 2):
        char1 = processed_msg[i]
        char2 = processed_msg[i+1]
        
        r1, c1 = find_char_location(matrix, char1)
        r2, c2 = find_char_location(matrix, char2)
        
        if r1 == r2: 
            ciphertext.append(matrix[r1][(c1 + 1) % 5])
            ciphertext.append(matrix[r2][(c2 + 1) % 5])
        elif c1 == c2:
            ciphertext.append(matrix[(r1 + 1) % 5][c1])
            ciphertext.append(matrix[(r2 + 1) % 5][c2])
        else: 
            ciphertext.append(matrix[r1][c2])
            ciphertext.append(matrix[r2][c1])
            
    return "".join(ciphertext)

def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_square(key)
    plaintext = []
    
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1]
        
        r1, c1 = find_char_location(matrix, char1)
        r2, c2 = find_char_location(matrix, char2)
        
        if r1 == r2:
            plaintext.append(matrix[r1][(c1 - 1) % 5])
            plaintext.append(matrix[r2][(c2 - 1) % 5])
        elif c1 == c2:
            plaintext.append(matrix[(r1 - 1) % 5][c1])
            plaintext.append(matrix[(r2 - 1) % 5][c2])
        else:
            plaintext.append(matrix[r1][c2])
            plaintext.append(matrix[r2][c1])
            
    return "".join(plaintext)

key = "MONARCHY"
message = "INSTRUMENTS"

encrypted_message = playfair_encrypt(message, key)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = playfair_decrypt(encrypted_message, key)
print(f"Decrypted Message: {decrypted_message}")
