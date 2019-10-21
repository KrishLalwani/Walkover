import unittest
from GameOfLife import Life


class TestGameOfLife(unittest.TestCase):

    def setUp(self):
        self.obj = Life(3,3, [[0,0,0],[0,0,0],[0,0,0]])

    def tearDown(self):
        pass

    # Function to test Functioning of Check_Grid function in GameOfLife
    def test_CheckGrid(self):
        self.obj.current_generation = [[0,1,0],[0,0,0],[1,1,1]]
        self.assertEqual(self.obj.Check_Grid(), True)

        self.obj.current_generation = [[0,1,0],[0,2,0],[1,1,1]]
        self.assertEqual(self.obj.Check_Grid(), False)

        self.obj.current_generation = [[0,1,0],[0,0,-1],[1,1,1]]
        self.assertEqual(self.obj.Check_Grid(), False)

        self.obj.current_generation = [[0,1,0],[0,'a',0],[1,1,1]]
        self.assertEqual(self.obj.Check_Grid(), False)

        self.obj.current_generation = [[0,1,'*'],[0,0,0],[1,1,1]]
        self.assertEqual(self.obj.Check_Grid(), False)

        self.obj.current_generation = [[0,1,0],[0,0,0,0],[1,1,1]]
        self.assertEqual(self.obj.Check_Grid(), False)
        
        self.obj.current_generation = [[0,1,0],[0,0,0],[1,1,1],[0,1,0]]
        self.assertEqual(self.obj.Check_Grid(), False)

    # Function to test Functioning of Check_Stable function in GameOfLife
    def test_CheckStable(self):
        self.obj.current_generation = [[0,1,0],[0,0,0],[1,1,1]]
        self.obj.next_generation = [[0,1,0],[0,0,0],[1,1,1]]
        self.assertEqual(self.obj.Check_Stable(), True)

        self.obj.current_generation = [[0,1,0],[0,1,0],[1,1,1]]
        self.obj.next_generation = [[0,1,0],[0,0,0],[1,1,1]]
        self.assertEqual(self.obj.Check_Stable(), False)

    # Function to test Functioning of Compute_Next_Generation function in GameOfLife
    def test_ComputeNextGeneration(self):
        self.obj.current_generation = [[0,0,0],[0,0,0],[0,0,0]]
        self.obj.next_generation = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(self.obj.Compute_Next_Generation(), [[0,0,0],[0,0,0],[0,0,0]])

        self.obj.current_generation = [[1,1,1],[1,1,1],[1,1,1]]
        self.obj.next_generation = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(self.obj.Compute_Next_Generation(), [[1,0,1],[0,0,0],[1,0,1]])

        self.obj.current_generation = [[0,1,1],[0,1,0],[1,1,0]]
        self.obj.next_generation = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(self.obj.Compute_Next_Generation(), [[0,1,1],[0,0,0],[1,1,0]])

    # Function to test Functioning of Find_Stable_Grid function in GameOfLife
    def test_FindStableGrid(self):
        self.obj.current_generation = [[1,1,1],[1,1,1],[1,1,1]]
        self.obj.next_generation = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(self.obj.Find_Stable_Grid(), [[0,0,0],[0,0,0],[0,0,0]])

        self.obj.current_generation = [[0,1,1],[0,1,0],[1,1,0]]
        self.obj.next_generation = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(self.obj.Find_Stable_Grid(), [[0,0,0],[0,0,0],[0,0,0]])

if __name__ == '__main__':
    unittest.main()