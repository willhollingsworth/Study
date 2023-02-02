import codewars_test as test


class SnakesLadders():
    def __init__(self):
        self.positions = [0,0]
        self.player_2_turn = False
        self.game_over = False
        self.snakes_ladders = { 
            2:38,7:14,8:31,15:26,16:6,21:42,28:84,36:44,46:25,49:11,
            51:67,62:19,64:60,71:91,74:53,78:98,87:94,89:68,92:88,95:75,99:80
            }

    def play(self, die1, die2):
        if self.game_over:
            return 'Game over!'
        position = self.positions[self.player_2_turn]     
        position += die1+die2
        if position == 100:
            self.game_over = True
            return 'Player {} Wins!'.format(self.player_2_turn+1)
        elif position > 100:
            position = 100 - (position - 100)
        if position in self.snakes_ladders:
            position = self.snakes_ladders[position]
        self.positions[self.player_2_turn] = position
        return_string = 'Player {} is on square {}'.format(self.player_2_turn+1 , position)
        if die1 != die2:
            self.player_2_turn = not self.player_2_turn
        return return_string

gametest = SnakesLadders()
print(gametest.play(1, 1))
print(gametest.play(1, 5))
# print(gametest.play(6, 2))
# print(gametest.play(1, 1))
# print(gametest.play(6, 6))
# print(gametest.play(6, 6))
# print(gametest.play(6, 6))
# print(gametest.play(6, 6))
# print(gametest.play(6, 6))
# print(gametest.play(6, 6))
# print(gametest.play(6, 6))
# print(gametest.play(6, 6))



# @test.describe('Example Tests')

# def example_tests():
#     game = SnakesLadders()
#     @test.it("Should return: 'Player 1 is on square 38'")
#     def example_test_case():
#         test.assert_equals(game.play(1, 1), "Player 1 is on square 38")

#     @test.it("Should return: 'Player 1 is on square 44'")
#     def example_test_case():
#         test.assert_equals(game.play(1, 5), "Player 1 is on square 44")

#     @test.it("Should return: 'Player 2 is on square 31'")
#     def example_test_case():
#         test.assert_equals(game.play(6, 2), "Player 2 is on square 31")

#     @test.it("Should return: 'Player 1 is on square 25'")
#     def example_test_case():
#         test.assert_equals(game.play(1, 1), "Player 1 is on square 25")
