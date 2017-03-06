from .. import Solver
from Move import Move

class YellowCrossSolver(Solver):
    def apply_algorithm(self, solution):
        for move in ["F", "R", "U", "R'", "U'", "F'"]:
            self.move(move, solution)

    def move(self, m, solution):
        self.cube.move(Move(m))
        solution.append(m)

    def solution(self):
        solution = []
        # Apply F R U R' U' F' once, twice or thrice
        up_yellows = [edge for edge in ['FU', 'RU', 'LU', 'BU'] if self.cube.cubies[edge].color_facing('Y')]
        
        if len(up_yellows) == 1:
            self.apply_algorithm(solution)
            self.move("U2")
            self.apply_algorithm(solution)
            self.apply_algorithm(solution)
        elif len(up_yellows) == 2:
            # If not line position, it's L position
            if ('FU' in up_yellows and 'BU' in up_yellows) or ('RU' in up_yellows and 'LU' in up_yellows):
                # Rotate until L is at BU - LU
                while not self.cube.cubies['BU'].color_facing('Y') or not self.cube.cubies['LU'].color_facing('Y'):
                    self.move("Y", solution)
                self.apply_algorithm(solution)
             # Rotate until line is at RU - LU
            while not self.cube.cubies['RU'].color_facing('Y') or not self.cube.cubies['LU'].color_facing('Y'):
                self.move("Y", solution)   
            # Line position
            self.apply_algorithm(solution)

        return solution