scales = ['100100100100', '100100101100', '100100110100', '100101001100', '100101010100', '100101101100', '100110010100', '100110101100', '100110110100', '101001010100', '101001101100', '101010101100', '101010110100', '101011001100', '101011010100', '101100101100', '101100110100', '101101001100', '101101010100', '101101101100', '110011001100', '110011010100', '110100110100', '110101010100', '110101101100', '110110101100', '110110110100', '101010101010', '101010110110', '101011010110', '110110110110']
print("Enter notes like Ab B C#")
notes = {"Ab" : 2048,
         "A" : 1,
         "A#" : 2,
         "Bb" : 2, 
         "B" : 4,
         "B#" : 8,
         "Cb" : 4,
         "C" : 8,
         "C#" : 16, 
         "Db" : 16,
         "D" : 32,
         "D#" : 64,
         "Eb" : 64,
         "E" : 128,
         "E#" : 256,
         "Fb" : 128,
         "F" : 256,
         "F#" : 512,
         "Gb" : 512,
         "G" : 1024,
         "G#" : 2048,
}
notes2 = ["A ", "A#/Bb ", "B ", "C ", "C#/Db ", "D ", "D#/Eb ", "E ", "F ", "F#/Gb ", "G ", "G#/Ab "]

while True:
    input_chord = input("Notes: ").upper().split()
    chord = 0
    for note in input_chord:
        chord |= notes[note]
    chord = bin(chord)[2:].zfill(12)[::-1]

    def generate_rotations(binary_str):
        binary_str = binary_str.zfill(12)
        rotations = []
        for i in range(12):
            rotation = binary_str[i:] + binary_str[:i]
            rotations.append(rotation)
        return rotations

    n = 0
    for i in range(12):
        if bin(notes[input_chord[0]])[2:].zfill(12)[::-1][i] == '1':
            n = -i
            break
    for scale in scales:
        flag = False
        for rotated_scale in generate_rotations(scale):
            match_found = True
            for i in range(12):
                if chord[i] == '1' and rotated_scale[i] != '1':
                    match_found = False
                    break
            if match_found:
                answer = ""
                for i in range(12):
                    index = round(12 * abs(((i-n) / 12) - ((i-n) // 12)))
                    if rotated_scale[index] == '1':
                        answer += notes2[index]
                print(answer)
                flag = True
        if flag:
            print()
