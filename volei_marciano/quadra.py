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

    def get_judges(self):
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

        return self.judges

        






