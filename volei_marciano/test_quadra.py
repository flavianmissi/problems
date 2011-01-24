import unittest
from nose.tools import *
from quadra import Quadra

class QuadraTestCase(unittest.TestCase):
    @raises(ValueError)
    def test_if_court_has_even_number_of_sides(self):
        quadra = Quadra(5)

    @raises(ValueError)
    def test_if_number_of_court_sides_is_betwen_4_and_100_using_102(self):
        quadra = Quadra(102)

    @raises(ValueError)
    def test_if_number_of_court_sides_is_betwen_4_and_100_using_2(self):
        quadra = Quadra(2)

    @raises(ValueError)
    def test_if_number_of_coordinates_correspond_with_number_of_sides_using_6_coordinates_and_8_sides(self):
        quadra = Quadra(8)
        quadra.set_coordinates([[[3, 6], [4, 9]], [[2, 5], [5, 2]], [[9, 8], [4, 2]]])

    @raises(ValueError)
    def test_if_court_sides_are_parallel_to_x_or_y_with_non_parallel_sides(self):
        quadra = Quadra(6)
        quadra.set_coordinates([[[3, 6], [4, 9]], [[2, 5], [5, 2]], [[9, 8], [4, 2]]])

    def test_if_court_sides_are_parallel_to_x_or_y_with_4_parallel_sides(self):
        quadra = Quadra(4)
        assert_true(quadra.set_coordinates([ [ [3, 6], [3, 9] ], [ [5, 9], [5, 6] ] ]))

    def test_if_court_sides_are_parallel_to_x_or_y_with_6_parallel_sides(self):
        quadra = Quadra(6)
        A = [1, 2]; B = [1, 7]; C = [3, 7]; D = [3, 5]; E = [5, 5]; F = [5, 2]
        assert_true(quadra.set_coordinates([ [A, B], [C, D], [E, F] ]))

    @raises(ValueError)
    def test_court_sides_consistency_with_inconsistent_lines(self):
        quadra = Quadra(4)
        quadra.set_coordinates([[[3, 6], [3, 9]], [[2, 5], [5, 5]]])

    @raises(ValueError)
    def test_court_sides_consistency_with_inconsistency_in_last_line(self):
        quadra = Quadra(4)
        A = [3, 6]; B = [3, 9]; C = [5, 9]; D = [5, 5]
        quadra.set_coordinates([ [A, B], [C, D]  ])

    def test_court_sides_consistency_with_consistent_lines(self):
        quadra = Quadra(6)
        A = [1, 2]; B = [1, 7]; C = [3, 7]; D = [3, 5]; E = [5, 5]; F = [5, 2]
        assert_true(quadra.set_coordinates([ [A, B], [C, D], [E, F]  ]))

    def test_court_sides_consistency_with_8_consistent_lines(self):
        quadra = Quadra(8)
        A = [6, 6]; B = [6, 4]; C = [5, 4]; D = [5, 6]
        E = [2, 6]; F = [2, 3]; G = [8, 3]; H = [8, 6]
        assert_true(quadra.set_coordinates([ [A, B], [C, D], [E, F], [G, H]  ]))

    @raises(ValueError)
    def test_court_sides_consistency_with_8_inconsistent_lines(self):
        quadra = Quadra(8)
        A = [6, 6]; B = [6, 4]; C = [5, 4]; D = [5, 6]
        E = [2, 6]; F = [2, 3]; G = [8, 3]; H = [5, 6]
        quadra.set_coordinates([ [A, B], [C, D], [E, F], [G, H]  ])

    def test_if_number_of_judges_correspond_to_a_rectangle_court_with_4_judges(self):
        quadra = Quadra(4)
        A = [3, 6]; B = [3, 9]; C = [5, 9]; D = [5, 6]
        quadra.set_coordinates([ [A, B], [C, D]  ])
        assert_equals(quadra.get_judges(), 4)

    def test_if_a_court_with_8_lines_has_7_judges(self):
        quadra = Quadra(8)
        A = [6, 6]; B = [6, 4]; C = [5, 4]; D = [5, 6]
        E = [2, 6]; F = [2, 3]; G = [8, 3]; H = [8, 6]
        quadra.set_coordinates([ [A, B], [C, D], [E, F], [G, H]  ])
        assert_equals(quadra.get_judges(), 7)

    def test_if_8_and_6_are_the_biggest_numbers_in_figure(self):
        quadra = Quadra(8)
        A = [6, 6]; B = [6, 4]; C = [5, 4]; D = [5, 6]
        E = [2, 6]; F = [2, 3]; G = [8, 3]; H = [8, 6]
        quadra.set_coordinates([ [A, B], [C, D], [E, F], [G, H]  ])
        assert_equals(quadra.get_biggest_and_smallest_x_and_y(), {'max' : [8, 6], 'min' : [2, 3]})


    def test_if_coordinate_is_over_some_line_in_the_square(self):
        quadra = Quadra(4)
        A = [3, 6]; B = [3, 9]; C = [5, 9]; D = [5, 6]
        quadra.set_coordinates([ [A, B], [C, D]  ])
        assert_true(quadra.is_x_or_y_over_some_line([4, 6]))

    def test_if_coordinate_is_not_over_some_line_in_the_square(self):
        quadra = Quadra(4)
        A = [3, 6]; B = [3, 9]; C = [5, 9]; D = [5, 6]
        quadra.set_coordinates([ [A, B], [C, D]  ])
        assert_false(quadra.is_x_or_y_over_some_line([4, 1]))

    def test_if_coordinate_is_over_some_vertical_line_in_the_square(self):
        quadra = Quadra(4)
        A = [3, 6]; B = [3, 9]; C = [5, 9]; D = [5, 6]
        quadra.set_coordinates([ [A, B], [C, D]  ])
        assert_true(quadra.is_x_or_y_over_some_line([5, 8]))



    def test_if_a_court_with_6_lines_has_5_judges(self):
        quadra = Quadra(6)
        A = [2, 1]; B = [2, 5]; C = [4, 5]
        D = [4, 8]; E = [6, 8]; F = [6, 1]
        quadra.set_coordinates([ [A, B], [C, D], [E, F] ])
        assert_equals(quadra.get_judges(), 5)


