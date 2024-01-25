def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # Convert text to uppercase to handle case-insensitivity
    text_upper = text.upper()

    morse_translation = []
    for char in text_upper:
        # Check if the character is alphabetic
        if char.isalpha():
            # Lookup the Morse code equivalent for the character
            morse_code = morse_code_dict[char]
            morse_translation.append(morse_code)
        elif char == " ":
            # Add a forward slash for word separation
            morse_translation.append("/")
    
    # Join the Morse code for each character and return the translation
    return " ".join(morse_translation)

# Test cases
print(morse_translator("HELLO WORLD"))  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(morse_translator("Python"))  # Expected output: ".--. -.-- - .... --- -."
print(morse_translator("Morse Code"))  # Expected output: "-- --- .-. ... . / -.-. --- -.. ."