class Wordplay:
    def __init__(self, words):
        self.words = words

    def words_with_length(self, length):
        return [w for w in self.words if len(w) == length]

    def started_with(self, s):
        return [w for w in self.words if w.startswith(s)]

    def end_with(self, s):
        return [w for w in self.words if w.endswith(s)]

    def only(self, L):
        return [w for w in self.words if all(c in L for c in w)]

    def avoids(self, L):
        return [w for w in self.words if all(c not in L for c in w)]


if __name__ == "__main__":
    ds_tu = ["apple", "ant", "book", "banana", "cat", "dog", "door", "egg", "ab", "bb"]
    wp = Wordplay(ds_tu)
    print("Danh sach tu:", wp.words)
    print("Tu co 3 chu cai:", wp.words_with_length(3))
    print("Tu bat dau bang a:", wp.started_with("a"))
    print("Tu ket thuc bang g:", wp.end_with("g"))
    print("Tu chi chua cac chu trong 'ab':", wp.only("ab"))
    print("Tu khong chua chu nao trong 'ae':", wp.avoids("ae"))
