class Acc2:
    def __init__(self,l,f,unit,inv):
        self.h,self.w=len(l),len(l[0])
        self.acc2=[[unit]*(self.w+1) for _ in range(self.h+1)]
        self.f,self.inv=f,inv
        for i in range(self.h):
            for j in range(self.w):
                self.acc2[i+1][j+1]=f(f(f(self.acc2[i][j+1],self.acc2[i+1][j]),inv(self.acc2[i][j])),l[i][j])
    def sum(self,i,j,i_,j_):
        return self.f(self.f(self.f(self.acc2[i_][j_],self.inv(self.acc2[i][j_])),self.inv(self.acc2[i_][j])),self.acc2[i][j])
    def get(self,i,j):
        return self.sum(i,j,i+1,j+1)
    def __str__(self):
        return '\n'.join([str(i) for i in self.acc2])