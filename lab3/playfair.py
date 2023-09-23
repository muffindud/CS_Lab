upper_alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
lower_alphabet = "aăâbcdefghiîjklmnopqrsștțuvwxyz"


def encrypt(message: str, keyword: str) -> dict:
    message = message.replace(" ", "").upper().replace("Â", "Î")
    keyword = keyword.replace(" ", "").upper().replace("Â", "Î")
    encryption_text = ""
    encryption_matrix = []

    if any(letter not in upper_alphabet for letter in message):
        raise ValueError("The message must contain only letters and spaces.")

    if any(letter not in upper_alphabet for letter in keyword):
        raise ValueError("The keyword must contain only letters and spaces.")

    # Remove duplicate letters from the message pairs
    i = 0
    while i < len(message) - 1:
        if message[i] == message[i + 1]:
            message = message[:i + 1] + "X" + message[i + 1:]
        i += 2

    # If the message has an odd number of letters, add an X at the end
    if len(message) % 2 == 1:
        message += "X"

    # Create the encryption alphabet
    for letter in keyword:
        if letter not in encryption_text:
            encryption_text += letter

    for letter in upper_alphabet:
        if letter not in encryption_text and letter != "Â":
            encryption_text += letter

    # Create the encryption matrix
    for i in range(6):
        encryption_matrix.append(encryption_text[i * 5:i * 5 + 5])

    # Encrypt the message
    ciphertext = ""
    for i in range(0, len(message), 2):
        pair = message[i:i + 2]

        # Find the position of the letters in the encryption matrix
        for row in range(6):
            for column in range(5):
                if encryption_matrix[row][column] == pair[0]:
                    first_letter = (row, column)
                if encryption_matrix[row][column] == pair[1]:
                    second_letter = (row, column)

        if first_letter[0] == second_letter[0]:
            ciphertext += encryption_matrix[first_letter[0]][(first_letter[1] + 1) % 5]
            ciphertext += encryption_matrix[second_letter[0]][(second_letter[1] + 1) % 5]
        elif first_letter[1] == second_letter[1]:
            ciphertext += encryption_matrix[(first_letter[0] + 1) % 6][first_letter[1]]
            ciphertext += encryption_matrix[(second_letter[0] + 1) % 6][second_letter[1]]
        else:
            ciphertext += encryption_matrix[first_letter[0]][second_letter[1]]
            ciphertext += encryption_matrix[second_letter[0]][first_letter[1]]

    return {"message": message, "ciphertext": ciphertext, "keyword": keyword, "encryption_text": encryption_text}


def decrypt(ciphertext: str, keyword: str) -> dict:
    ciphertext = ciphertext.replace(" ", "").upper().replace("Â", "Î")
    keyword = keyword.replace(" ", "").upper().replace("Â", "Î")
    encryption_text = ""
    encryption_matrix = []

    if any(letter not in upper_alphabet for letter in ciphertext):
        raise ValueError("The ciphertext must contain only letters and spaces.")

    if ciphertext % 2 == 1:
        raise ValueError("The ciphertext must have an even number of letters.")

    if any(letter not in upper_alphabet for letter in keyword):
        raise ValueError("The keyword must contain only letters and spaces.")

    
