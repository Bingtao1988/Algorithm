class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score
    def get_name(self):
        return self._name
    def get_score(self):
        return self._score
    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)

class ScoreBoard:
    def __init__(self, capacity):
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        return self._board[k]

    def __str__(self, k):
        return '\n'.join(str(self._board[j])for j in range(self._n))

    def add(self, entry):
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self_n += 1

            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry

def InsertionSort(array):
    for cnt in range(1, len(array)):
        value = array[cnt]
        inner = cnt
        while inner > 0 and array[inner - 1] > value:
            array[inner] = array[inner - 1]
            inner -= 1
        A[inner] = value


class CaesarCipher:
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26

        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord("A"))
            decoder[k] = chr((k - shift) % 26 + ord("A"))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self):
        return self._transform(message, self._forward)

    def decrypt(self):
        return self._transform(message, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


    
