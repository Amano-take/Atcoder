import random
class RollingHash:
    def __init__(self, S: str):
        le = len(S)
        if RConst.cf == 0:
            RConst.cf = random.randrange(1 << 31, RConst.Mod)

        if len(RConst.rui_cf) <= le:
            RConst.make_rui_cf(le)
            
        self.hash_arr = [1]
        for el in S:
            self.hash_arr.append(RConst.calc_mod(
                RConst.mul(self.hash_arr[-1], RConst.cf) + ord(el)))

    def get(self, l: int, r: int) -> int:
        "hash(S[l..r))"
        return RConst.sub(self.hash_arr[r],
                          RConst.mul(self.hash_arr[l], RConst.rui_cf[r - l]))

    def change(self, index: int, el: str):
        self.hash_arr[index] = RConst.calc_mod(
                RConst.mul(self.hash_arr[index-1], RConst.cf) + ord(el))

class RConst:
    Mask30 = (1 << 30) - 1
    Mask31 = (1 << 31) - 1
    Mod = (1 << 61) - 1
    cf = 0
    rui_cf = [1]

    @staticmethod
    def calc_mod(x: int) -> int:
        xu, xd = x >> 61, x & RConst.Mod
        ret = xu + xd
        if RConst.Mod <= ret:
            ret -= RConst.Mod
        return ret

    @staticmethod
    def sub(a: int, b: int) -> int:
        if a < b:
            return a + RConst.Mod - b
        return a - b

    @staticmethod
    def mul(a: int, b: int) -> int:
        au, ad = a >> 31, a & RConst.Mask31
        bu, bd = b >> 31, b & RConst.Mask31
        mid = ad * bu + au * bd
        midu, midd = mid >> 30, mid & RConst.Mask30
        return RConst.calc_mod(((au * bu) << 1) + midu + (midd << 31) + ad * bd)

    @staticmethod
    def make_rui_cf(x: int):
        l = len(RConst.rui_cf)
        for _ in range(x - l + 1):
            RConst.rui_cf.append(RConst.mul(RConst.cf, RConst.rui_cf[-1]))