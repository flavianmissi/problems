from polygon import Polygon

class Quadra(object):
    def __init__(self, n):
        if n % 2 != 0 or n not in range(4,101):
            raise ValueError("Number of sides must be even and must be between 4 and 100")
        self.sides = n

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates
        if self.validate_coordinates():
            return True

    def validate_coordinates(self):
        if self.validate_xy() and self.validate_number_of_sides() and self.validate_xy_parallelism() and self.validate_sides_consistency():
            return True

    def validate_number_of_sides(self):
        if len(self.coordinates) != self.sides/2:
	        raise ValueError("Number of coordinates should be equivalent to number of sizes / 2")
        return True

    def validate_xy(self):
        for c in self.coordinates:
            if(len(c) != 2):
                raise ValueError("The coordinates should be in x y value")
    	return True

    def validate_xy_parallelism(self):
        error = "Some of the court lines are not parallel to the axis"
        for c in self.coordinates:
            x1 = c[0][0]; x2 = c[1][0]; y1 = c[0][1]; y2 = c[1][1]
            self.compare_x_and_y(x1, y1, x2, y2, error)
        return True

    def validate_sides_consistency(self):
        self.merge_list()
        error = "There is no sides consistency between some sides.."
        for c in range(1,len(self.merged_list)):
            x1 = self.merged_list[c-1][0]; y1 = self.merged_list[c-1][1]; x2 = self.merged_list[c][0]; y2 = self.merged_list[c][1]
            self.compare_x_and_y(x1, y1, x2, y2, error)
        else:
            #compare first line with last
            x1 = self.merged_list[0][0]; y1 = self.merged_list[0][1]
            self.compare_x_and_y(x1, y1, x2, y2, error)
        return True

    def merge_list(self):
        merged_list = []
        for i in self.coordinates:
            for j in i:
                merged_list.append(j)
        self.merged_list = merged_list

    def compare_x_and_y(self, x1, y1, x2, y2, error):
        if x1 != x2 and y1 != y2:
            raise ValueError(error)

    def is_coordinate_inside_figure(self, p):
        polygon = Polygon(self.merged_list)
        if self.is_coordinate_over_some_line(p):
            return True
        else:
            return polygon.belongs_to_polygon(p)

    def is_coordinate_over_some_line(self, p):
        x1 = p[0]; y1 = p[1]
        for i in range(1, len(self.merged_list)):
            if (x1 in range(self.merged_list[i-1][0], self.merged_list[i][0]+1) or x1 in range(self.merged_list[i][0], self.merged_list[i-1][0]+1)):
                if (y1 in range(self.merged_list[i-1][1], self.merged_list[i][1]+1) or y1 in range(self.merged_list[i][1], self.merged_list[i-1][1]+1)):
                    if (y1 == self.merged_list[i-1][1] and y1 == self.merged_list[i][1]) or (x1 == self.merged_list[i-1][0] and x1 == self.merged_list[i][0]):
                        return True
        else:
            if (x1 in range(self.merged_list[0][0], self.merged_list[i][0]+1) or x1 in range(self.merged_list[i][0], self.merged_list[0][0]+1)):
                if(y1 in range(self.merged_list[0][1], self.merged_list[i][1]+1) or y1 in range(self.merged_list[i][1], self.merged_list[0][1]+1)):
                    if (y1 == self.merged_list[0][1] and y1 == self.merged_list[i][1]) or (x1 == self.merged_list[0][0] and x1 == self.merged_list[i][0]):
                        return True
        return False

    def get_judges(self):
        special_judges = self.get_special_judges()
        self.get_judges_for_all_sides()
        return self.judges - special_judges

    def get_special_judges(self):
        "Special judges are the ones that can watch two lines in the same time"
        special_judges = 0
        for i in range(2, len(self.merged_list)):
            x1 = self.merged_list[i-2][0]; y1 = self.merged_list[i-2][1]
            x2 = self.merged_list[i][0]; y2 = self.merged_list[i][1]

            possibility_1 = [x1, y2]; possibility_2 = [x2, y1]

            if (not self.is_coordinate_inside_figure(possibility_1)) ^ (not self.is_coordinate_inside_figure(possibility_2)):
                special_judges += 1

        print "special judges"
        print special_judges

        return special_judges

    def get_judges_for_all_sides(self):
        xs = []; ys = []
        for i in range(1, len(self.merged_list)):
            x1 = self.merged_list[i-1][0]; y1 = self.merged_list[i-1][1]
            x2 = self.merged_list[i][0]; y2 = self.merged_list[i][1]
            if x1 == x2:
                xs.append(x1)
            if y1 == y2:
                ys.append(y1)
        else:
            x1 = self.merged_list[0][0]; y1 = self.merged_list[0][1]
            if x1 == x2:
                xs.append(x1)
            if y1 == y2:
                ys.append(y1)
        self.judges = len(set(xs)) + len(set(ys))







