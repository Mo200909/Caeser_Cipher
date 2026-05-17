# Caesar Cipher

A classic encryption tool that shifts letters in a message by a fixed number of positions in the alphabet, 
implementing the Caesar Cipher technique. The program supports both encryption and decryption modes, 
prompting the user to choose a direction and supply a numeric key between 1 and 26. Non-letter characters 
and spaces are preserved as-is during transformation. It uses a clean modular approach, with a unified 
`encrypt_decrypt` function that handles both directions by negating the key for decryption. 
