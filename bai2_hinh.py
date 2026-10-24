from abc import ABC, abstractmethod
import math


class Hinh(ABC):
    @abstractmethod
    def tinh_chu_vi(self):
        pass

    @abstractmethod
    def tinh_dien_tich(self):
        pass


class HinhTron(Hinh):
    def __init__(self, ban_kinh):
        if ban_kinh <= 0:
            raise ValueError("Ban kinh phai lon hon 0")
        self.ban_kinh = ban_kinh

    def tinh_chu_vi(self):
        return 2 * math.pi * self.ban_kinh

    def tinh_dien_tich(self):
        return math.pi * self.ban_kinh ** 2


class HinhChuNhat(Hinh):
    def __init__(self, dai, rong):
        if dai <= 0 or rong <= 0:
            raise ValueError("Chieu dai va chieu rong phai lon hon 0")
        self.dai = dai
        self.rong = rong

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

    def tinh_dien_tich(self):
        return self.dai * self.rong


class HinhTamGiac(Hinh):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Cac canh phai lon hon 0")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Ba canh khong tao thanh tam giac")
        self.a, self.b, self.c = a, b, c

    def tinh_chu_vi(self):
        return self.a + self.b + self.c

    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


if __name__ == "__main__":
    ds_hinh = [HinhTron(3), HinhChuNhat(4, 5), HinhTamGiac(3, 4, 5)]
    for hinh in ds_hinh:
        print("\nLoai hinh:", type(hinh).__name__)
        print("Chu vi:", round(hinh.tinh_chu_vi(), 2))
        print("Dien tich:", round(hinh.tinh_dien_tich(), 2))
