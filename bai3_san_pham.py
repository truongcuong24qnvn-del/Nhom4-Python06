class SanPham:
    def __init__(self, ten, gia, so_luong):
        if gia < 0 or so_luong < 0:
            raise ValueError("Gia va so luong khong duoc am")
        self.ten = ten
        self.gia = gia
        self.so_luong = so_luong

    def get_price(self, so_luong_mua):
        if so_luong_mua <= 0:
            print("So luong mua phai lon hon 0")
            return None
        if so_luong_mua > self.so_luong:
            print("Khong du hang trong kho")
            return None
        if so_luong_mua < 10:
            giam_gia = 0
        elif so_luong_mua <= 99:
            giam_gia = 0.10
        else:
            giam_gia = 0.20
        return self.gia * so_luong_mua * (1 - giam_gia)

    def make_purchase(self, so_luong_mua):
        thanh_tien = self.get_price(so_luong_mua)
        if thanh_tien is None:
            return
        self.so_luong -= so_luong_mua
        print("Da mua:", so_luong_mua, self.ten)
        print("Thanh tien:", format(thanh_tien, ",.0f"), "dong")
        print("So luong con lai:", self.so_luong)


if __name__ == "__main__":
    sp = SanPham("Ao thun", 100000, 150)
    print("Gia khi mua 5 san pham:", format(sp.get_price(5), ",.0f"), "dong")
    print("Gia khi mua 20 san pham:", format(sp.get_price(20), ",.0f"), "dong")
    print("Gia khi mua 100 san pham:", format(sp.get_price(100), ",.0f"), "dong")
    print("\n--- MUA HANG ---")
    sp.make_purchase(20)
