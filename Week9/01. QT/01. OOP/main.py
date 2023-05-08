from game import GameMachine

if __name__ == '__main__':
    g = GameMachine()

    g.insert_coin(1)
    g.insert_coin(-1)
    g.play_game()