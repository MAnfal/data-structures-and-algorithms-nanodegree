import hashlib
import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    @staticmethod
    def calc_hash():
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class LinkedList:
    def __init__(self):
        self.last = None

    def append(self, data):
        timestamp = datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

        if not self.last:
            self.last = Block(timestamp, data, 0)
        else:
            temp_data = self.last
            self.last = Block(timestamp, data, temp_data)


def print_block_value(block):
    if block:
        print('---------------------------------------------------------------------------------------------')
        print('Timestamp: {0}'.format(block.timestamp))
        print('Data: {0}'.format(block.data))
        print('SHA256 Hash: {0}'.format(block.hash))

        previous_hash = block.previous_hash.hash if block.previous_hash else block.previous_hash

        print('Previous Hash: {0}'.format(previous_hash))
        print('---------------------------------------------------------------------------------------------')


# linked list
linked_list = LinkedList()
linked_list.append("Information A")
linked_list.append("Information B")

# Print out the results.
current_block = linked_list.last

print_block_value(current_block)

while current_block.previous_hash:
    current_block = current_block.previous_hash

    print_block_value(current_block)
