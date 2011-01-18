import unittest
from nose.tools import *
from block_set import BlockSet

class BlocksSetTestCase(unittest.TestCase):
    @raises(ValueError)
    def test_if_blockset_number_is_invalid(self):
        blocks = BlockSet(25)

    def test_if_blockset_number_is_valid(self):
	blocks = BlockSet(5)
        assert_equals(blocks.get_blocks(), [0, 1, 2, 3, 4])

    def test_if_move_3_onto_5(self):
        blocks = BlockSet(5)
        assert_equals(blocks.move_a_onto_b(a = 2, b = 4), [0, 1, -1, 3, [2, 4]])

    def test_if_move_5_onto_1(self):
        blocks = BlockSet(5)
        assert_equals(blocks.move_a_onto_b(a = 4, b = 0), [[4, 0], 1, 2, 3, -1])

    def test_if_grouped_blocks_2_3_are_putted_back_in_their_original_position(self):
        blocks = BlockSet(8)
        assert_equals(blocks.move_a_onto_b(a = 1, b = 2), [0, -1, [1, 2], 3, 4, 5, 6, 7])

    def test_if_puts_a_onto_b_and_reorder_their_stacked_blocks(self):
        blocks = BlockSet(8)
        assert_equals(blocks.move_a_onto_b(a = 2, b = 4), [0, 1, -1, 3, [2, 4], 5, 6 , 7])
        assert_equals(blocks.move_a_onto_b(a = 1, b = 2), [0, -1, [1, 2], 3, 4, 5, 6, 7])
        assert_equals(blocks.move_a_onto_b(a = 6, b = 1), [0, [6,1], 2, 3, 4, 5, -1, 7])

    @raises(ValueError)
    def test_if_a_equals_b_raises_error(self):
        blocks = BlockSet(4)
        blocks.move_a_onto_b(a = 3, b = 3)

    def test_move_a_over_b_takes_off_all_blocks_stacked_in_a(self):
        blocks = BlockSet(6)
        assert_equals(blocks.move_a_onto_b(a = 4, b = 2), [0, 1, [4, 2], 3, -1, 5])
        assert_equals(blocks.move_a_onto_b(a = 5, b = 3), [0, 1, [4, 2], [5, 3], -1, -1])
        assert_equals(blocks.move_a_over_b(a = 2, b = 3), [0, 1, -1, [2, 5, 3], 4, -1])

    def test_move_a_over_b_where_b_is_not_a_list(self):
        blocks = BlockSet(6)
        assert_equals(blocks.move_a_onto_b(a = 4, b = 2), [0, 1, [4, 2], 3, -1, 5])
        assert_equals(blocks.move_a_over_b(a = 2, b = 3), [0, 1, -1, [2, 3], 4, 5])
        
    def test_if_pile_a_onto_b_takes_off_all_blocks_stacked_in_b(self):
        blocks = BlockSet(6)
        assert_equals(blocks.move_a_onto_b(a = 5, b = 1), [0, [5, 1], 2, 3, 4, -1])
        assert_equals(blocks.move_a_onto_b(a = 4, b = 3), [0, [5, 1], 2, [4, 3], -1, -1])
        assert_equals(blocks.pile_a_onto_b(a = 1, b = 3), [0, -1, 2, [5, 1, 3], 4, -1])

    def test_pile_a_onto_b_where_b_is_not_a_list(self):
        blocks = BlockSet(6)
        assert_equals(blocks.move_a_onto_b(a = 5, b = 1), [0, [5, 1], 2, 3, 4, -1])
        assert_equals(blocks.pile_a_onto_b(a = 1, b = 3), [0, -1, 2, [5, 1, 3], 4, -1])

    def test_if_pile_a_onto_b_join_both_stacks(self):
        blocks = BlockSet(5)
        assert_equals(blocks.move_a_onto_b(a = 2, b = 1), [0, [2, 1], -1, 3, 4 ])
        assert_equals(blocks.move_a_onto_b(a = 4, b = 3), [0, [2, 1], -1, [4, 3], -1])
        assert_equals(blocks.pile_a_over_b(a = 1, b = 3), [0, -1, -1, [2, 1, 4, 3], -1])

    def test_pile_a_onto_b_where_b_is_not_a_list(self):
        blocks = BlockSet(5)
        assert_equals(blocks.move_a_onto_b(a = 2, b = 1), [0, [2, 1], -1, 3, 4 ])
        assert_equals(blocks.pile_a_over_b(a = 1, b = 3), [0, -1, -1, [2, 1, 3], 4])

    def test_pile_a_onto_b_where_a_is_not_a_list(self):
        blocks = BlockSet(5)
        assert_equals(blocks.move_a_onto_b(a = 4, b = 3), [0, 1, 2, [4, 3], -1])
        assert_equals(blocks.pile_a_over_b(a = 1, b = 3), [0, -1, 2, [1, 4, 3], -1])
        





