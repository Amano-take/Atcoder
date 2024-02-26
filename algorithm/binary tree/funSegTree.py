from typing import TypeVar, Callable, Sequence
 

TypeT = TypeVar('TypeT')
 
 
class FunLazySegmentTree:
    def __init__(
            self,
            n: int,
            composition: Callable[[TypeT, TypeT], TypeT],
            id_factory: Callable[[], TypeT], ):
        n2 = 1 << (n - 1).bit_length()
        self.offset = n2
        self.composition = composition
        self.id_factory = id_factory
        self.lazy = [id_factory() for _ in range(n2 << 1)]
 
    def _propagate(self, i):
        lazy = self.lazy
 
        if i < self.offset:
            l = i << 1
            r = l + 1
            lazy[l] = self.composition(lazy[l], lazy[i])
            lazy[r] = self.composition(lazy[r], lazy[i])
 

        lazy[i] = self.id_factory()

 
    def _get_overhead_indices(self, l, r):
        """ l, r are already added offset """
        result = []
        #kisuu ni naru made agatteiku kisuu no sono ikkoue wo sasu
        l0 = (l // (l & -l)) >> 1
        r0 = (r // (r & -r)) >> 1
        while l0 != r0:
            if l0 > r0:
                result.append(l0)
                l0 >>= 1
            else:
                result.append(r0)
                r0 >>= 1
        while l0:
            result.append(l0)
            l0 >>= 1
        return result
 
    def apply(self, l: int, r: int, x: TypeT):
        lazy = self.lazy
        cp = self.composition
        l = max(0, l)
        r = min(self.offset + 1, r)
        l += self.offset
        r += self.offset
        #kodomo ga kawaru node no list (sita kara ue)
        rc_indices = self._get_overhead_indices(l, r)
 
        #kokohanakutemo ikeru (kakann)
        #seiyaku toshite ue ni huruinowo yurusanai -> ueni kakono ga aru baai ha oroshite kuru
        #"""
        for i in reversed(rc_indices):
            self._propagate(i)
        #"""
        while l < r:
            if l & 1:
                lazy[l] = cp(lazy[l], x)
                l += 1
            if r & 1:
                r -= 1
                lazy[r] = cp(lazy[r], x)
            l >>= 1
            r >>= 1
 
 
    def get(self, i:int) -> TypeT:
        i += self.offset
        lazy = self.lazy
        for l in reversed(self._get_overhead_indices(i, i + 1)):
            self._propagate(l)
        return lazy[i]
    
 
    def debug_print(self):
        i = 1
        while i <= self.offset:
            print(self.lazy[i:2 * i])
            i <<= 1
        print()


