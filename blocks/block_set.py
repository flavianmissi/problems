class BlockSet(object):
    def __init__(self, n):
        self.__make_block(n)

    @property
    def get_blocks(self):
        return self.__blocks

    def __make_block(self, n):
        if n < 0 or n >= 25:
            raise ValueError("Number of blocks should be smaller then 25")
        self.__blocks = range(0, n)
        self.n = n
        return self.__blocks

    def move_a_onto_b(self, a, b):
        self.__validate(a, b)
        self.__reorder_blocks(a, b)
        self.__blocks[b] = [a, b]
        self.__blocks[a] = -1 
        return self.__blocks

    def move_a_over_b(self, a, b):
        self.__validate(a, b)
        if type(self.__blocks[a]) == list:
            self.__blocks = self.__reorder_block_to_original(a)
            if type(self.__blocks[b]) == list:
                self.__blocks[b].insert(0, a)
                self.__blocks[a] = -1
            else:
                self.move_a_onto_b(a, b)
        return self.__blocks

    def pile_a_onto_b(self, a, b):
        self.__validate(a, b)
        if type(self.__blocks[b]) == list:
            self.__blocks = self.__reorder_block_to_original(b)
        if type(self.__blocks[a]) == list:
            self.__blocks[a].append(b)
            self.__blocks[b] = self.__blocks[a]
            self.__blocks[a] = -1
        else:
            self.move_a_onto_b(a, b)
        return self.__blocks

    def pile_a_over_b(self, a, b):
        self.__validate(a, b)
        if type(self.__blocks[b]) == list and type(self.__blocks[a]) == list:
            for i in reversed(self.__blocks[a]):
                self.__blocks[b].insert(0, i)
                self.__blocks[a] = -1
        elif type(self.__blocks[b]) == list:
            self.__blocks[b].insert(0, a)
            self.__blocks[a] = -1
        elif type(self.__blocks[a]) == list:
            self.pile_a_onto_b(a, b)
        return self.__blocks
            

    def __validate(self, a, b):
        if a == b:
            raise ValueError("Block numbers should not be equal")
 

    def __reorder_blocks(self, a, b):
        self.__blocks = self.__reorder_block_to_original(a)
        self.__blocks = self.__reorder_block_to_original(b)
        self.__reorder_where_block_in(a)
        self.__reorder_where_block_in(b)

    def __reorder_block_to_original(self, block_position):
        try:
            stack = self.__blocks[block_position]
            for i in stack:
                self.__blocks[i] = i
            return self.__blocks
        except:
            return self.__blocks

    def __reorder_where_block_in(self, block):
        for i in self.__blocks:
            if type(i) == list and block in i:
                for j in i:
                    self.__blocks[j] = j
        return self.__blocks
