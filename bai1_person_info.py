class Nguoi:
    def __init__(self, ho_ten, tuoi, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.dia_chi = dia_chi

    def hien_thi_thong_tin(self):
        print("Ho ten:", self.ho_ten)
        print("Tuoi:", self.tuoi)
        print("Dia chi:", self.dia_chi)


class NhanVien(Nguoi):
    def __init__(self, ho_ten, tuoi, dia_chi, ma_nv, luong):
        super().__init__(ho_ten, tuoi, dia_chi)
        self.ma_nv = ma_nv
        self.luong = luong

    def hien_thi_nhan_vien(self):
        self.hien_thi_thong_tin()
        print("Ma nhan vien:", self.ma_nv)
        print("Luong:", self.luong)


class SinhVien(Nguoi):
    def __init__(self, ho_ten, tuoi, dia_chi, ma_sv, diem):
        super().__init__(ho_ten, tuoi, dia_chi)
        self.ma_sv = ma_sv
        self.diem = diem

    def hien_thi_sinh_vien(self):
        self.hien_thi_thong_tin()
        print("Ma sinh vien:", self.ma_sv)
        print("Diem:", self.diem)


class PersonInfo(NhanVien, SinhVien):
    def __init__(self, ho_ten, tuoi, dia_chi, ma_nv, luong, ma_sv, diem):
        Nguoi.__init__(self, ho_ten, tuoi, dia_chi)
        self.ma_nv = ma_nv
        self.luong = luong
        self.ma_sv = ma_sv
        self.diem = diem

    def hien_thi(self):
        self.hien_thi_thong_tin()
        print("Ma nhan vien:", self.ma_nv)
        print("Luong:", self.luong)
        print("Ma sinh vien:", self.ma_sv)
        print("Diem:", self.diem)


if __name__ == "__main__":
    p = PersonInfo("Luong Truong Viet Cuong", 20, "Da Nang",
                   "NV01", 8000000, "SV01", 8.7)
    print("--- THONG TIN CA NHAN ---")
    p.hien_thi()
