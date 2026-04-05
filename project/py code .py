def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the words back into a string
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Example usage
input_str = "Hello world this is Python"
output_str = reverse_words(input_str)
print("Original:", input_str)
print("Reversed:", output_str)