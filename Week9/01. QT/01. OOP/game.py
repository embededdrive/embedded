class GameMachine:
    def __init__(self) -> None:
        super().__init__()
        self.__coin: int = 0

    def insert_coin(self, n: int):
        if n <= 0 or n >= 10:
            print('코인에러')
            return
        self.__coin += n

    def play_game(self):
        if self.__coin <= 0:
            print('코인을 넣어라')
            return
        print('재밌다')
        self.__coin -= 1