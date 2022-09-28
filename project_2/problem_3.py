import sys


# encoding string process
def huffman_encoding(data):
    temp_dict = {}
    _charm_map = {}
    temp_str = '1'
    encoded_str = ""

    for char in data:
        temp_dict[char] = temp_dict.get(char, 0) + 1

    for num in sorted(temp_dict.items(), key=lambda x: x[1]):
        _charm_map[num[0]] = temp_str
        temp_str = '0' + temp_str

    for d in data:
        encoded_str += _charm_map[d]

    return encoded_str, _charm_map


def huffman_decoding(_data, _charm_map):
    temp_dict = {}
    temp_str, decoded_str = "", ""

    for c in _charm_map:
        temp_dict[_charm_map[c]] = c

    for d in _data:
        if d == '1':
            decoded_str += temp_dict[temp_str + d]
            temp_str = ''
        else:
            temp_str += d

    return decoded_str


def print_results(sentence):
    if sentence:
        print("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
        print("The content of the data is: {}\n".format(sentence))

        encoded_data, charm_map = huffman_encoding(sentence)

        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, charm_map)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))
    else:
        print('Empty string supplied.')


# Tests
print_results('The bird is the word')

print_results('aaaaaaaaaaaaaa')

print_results('')

print_results('a')
