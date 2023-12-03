def get_overhead_indices(l, r):
    """ l, r are already added offset """
    result = []
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
print(get_overhead_indices(10, 14))