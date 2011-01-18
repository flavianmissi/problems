class BlockSet(object):
    def __init__(self, n):
        self.make_block(n)

    def get_blocks(self):
        return self.blocks

    def make_block(self, n):
        if n < 0 or n >= 25:
            raise ValueError("Number of blocks should be smaller then 25")
        self.blocks = range(0, n)
        self.n = n
        return self.blocks

    def move_a_onto_b(self, a, b):
        self.validate(a, b)
        self.reorder_blocks(a, b)
        self.blocks[b] = [a, b]
        self.blocks[a] = -1 
        return self.blocks

    def move_a_over_b(self, a, b):
        self.validate(a, b)
        if type(self.blocks[a]) == list:
            self.blocks = self.reorder_block_to_original(a)
            if type(self.blocks[b]) == list:
                self.blocks[b].insert(0, a)
                self.blocks[a] = -1
            else:
                self.move_a_onto_b(a, b)
        return self.blocks

    def pile_a_onto_b(self, a, b):
        self.validate(a, b)
        if type(self.blocks[b]) == list:
            self.blocks = self.reorder_block_to_original(b)
        if type(self.blocks[a]) == list:
            self.blocks[a].append(b)
            self.blocks[b] = self.blocks[a]
            self.blocks[a] = -1
        else:
            self.move_a_onto_b(a, b)
        return self.blocks

    def pile_a_over_b(self, a, b):
        self.validate(a, b)
        if type(self.blocks[b]) == list and type(self.blocks[a]) == list:
            for i in reversed(self.blocks[a]):
                self.blocks[b].insert(0, i)
                self.blocks[a] = -1
        elif type(self.blocks[b]) == list:
            self.blocks[b].insert(0, a)
            self.blocks[a] = -1
        elif type(self.blocks[a]) == list:
            self.pile_a_onto_b(a, b)
        return self.blocks
            

    def validate(self, a, b):
        if a == b:
            raise ValueError("Block numbers should not be equal")
 

    def reorder_blocks(self, a, b):
        self.blocks = self.reorder_block_to_original(a)
        self.blocks = self.reorder_block_to_original(b)
        self.reorder_where_block_in(a)
        self.reorder_where_block_in(b)

    def reorder_block_to_original(self, block_position):
        try:
            stack = self.blocks[block_position]
            for i in stack:
                self.blocks[i] = i
            return self.blocks
        except:
            return self.blocks

    def reorder_where_block_in(self, block):
        for i in self.blocks:
            if type(i) == list and block in i:
                for j in i:
                    self.blocks[j] = j
        return self.blocks
