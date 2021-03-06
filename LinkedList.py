class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList(object):

    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):
        if self.head == None:
            self.head = node
            self.count += 1
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            self.count += 1

    def getdataIndex(self, data):
        curn = self.head
        idx = 0
        while curn:
            if curn.data == data:
                return idx
            curn = curn.next
            idx += 1
        return -1

    def insertNodeAtIndex(self, idx, node):
        curn = self.head
        prevn = None
        cur_i = 0

        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node  # self.head 대신 curn쓰면 안되나?
                self.head.next = nextn

                curn = node
                curn.next = nextn

            else:
                self.head = node
        else:
            while cur_i < idx:
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                node.next = curn
                prevn.next = node
            else:
                return -1

    def insertNodeAtData(self, data, node):
        idx = self.getdataIndex(data)
        if 0 <= idx:
            self.insertNodeAtIndex(idx, node)
        else:
            return -1

    def deleteAtIndex(self, idx):
        curn_i = 0
        curn = self.head
        prevn = None
        nextn = self.head.next

        if idx == 0:
            self.head = nextn

        else:
            while curn_i < idx:
                if curn.next:
                    prevn = curn
                    curn = nextn
                    nextn = nextn.next

                else:
                    break

                curn_i += 1

            if curn_i == idx:
                prevn.next = nextn
            else:
                return -1

    def clear(self):
        self.head = None

    def print(self):
        curn = self.head
        string = ""
        while curn:
            string += str(curn.data)
            if curn.next:
                string += "->"
            curn = curn.next
        print(string)