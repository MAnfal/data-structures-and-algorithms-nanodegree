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
        if data:
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

# Test case 1
linked_list.append("Information A")

# Test case 2
linked_list.append("Information B")

# Test case 3
linked_list.append("Information C")

# Test case 4
linked_list.append(None)

# Test case 5
linked_list.append(131231313)

# Test case 6
linked_list.append('')

# Print out the results.
current_block = linked_list.last

print_block_value(current_block)

while current_block.previous_hash:
    current_block = current_block.previous_hash

    print_block_value(current_block)


'''
Output

---------------------------------------------------------------------------------------------
Timestamp: 28/09/2022 07:25:21
Data: 131231313
SHA256 Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
Previous Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
Timestamp: 28/09/2022 07:25:21
Data: Information C
SHA256 Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
Previous Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
Timestamp: 28/09/2022 07:25:21
Data: Information B
SHA256 Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
Previous Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
Timestamp: 28/09/2022 07:25:21
Data: 
aaaa


SHA256 Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
Previous Hash: 0
---------------------------------------------------------------------------------------------
'''
