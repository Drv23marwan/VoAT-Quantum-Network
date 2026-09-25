def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_str):
    text = ""
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))
    return text

def voat_transmission(message):
    binary_message = text_to_binary(message)
    received_bits = ""
    
    print(f"--- INITIALIZING VoAT QUANTUM NETWORK ---")
    print(f"Original Message: '{message}' -> Binary: {binary_message}\n")
    
    for bit in binary_message:
        bob_path_blocked = int(bit)
        
        if bob_path_blocked == 1:
            alice_detector_A = True  
        else:
            alice_detector_A = False 
            
        if alice_detector_A:
            received_bits += "1"
        else:
            received_bits += "0"
            
    decoded_message = binary_to_text(received_bits)
    print(f"Transmission Complete!")
    print(f"Decoded Message on Bob's End: '{decoded_message}'")
    return decoded_message

# Run the simulator with a One Piece nod
voat_transmission("LUFFY")
