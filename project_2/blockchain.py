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
        self.head = None
        self.last = None

    def append(self, data):
        timestamp = datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temp_data = self.last
            self.last = Block(timestamp, data, temp_data)


# linked list
linked_list = LinkedList()
linked_list.append("Information A")
linked_list.append("Information B")

print("Linked list last data : ", linked_list.last.data)
print("Linked list last's previous hash data : ", linked_list.last.previous_hash.data)
