def compress(chars):
    chars_length = len(chars)

    if chars_length < 2:
        return chars_length
    
    start_of_group = 0
    write_idx = 0

    for char_idx, char in enumerate(chars):
        if (char_idx + 1) == chars_length or char != chars[char_idx + 1]:
            chars[write_idx] = char
            write_idx += 1

            if char_idx > start_of_group:
                repeats = char_idx - start_of_group + 1

                for num in str(repeats):
                    chars[write_idx] = num
                    write_idx += 1
            
            start_of_group = char_idx + 1

    return write_idx



test1 = ["a","a","b","b","c","c","c"]
print(compress(test1))
print(test1)