
class Newton:
    def __init__(self, f, df):
        self.f = f
        self.df = df

    def display(self, x): #คำสั่งเก็บข้อมูลไว้ มีคำว่า self เพื่อให้อ้างอิงข้อมูลให้อยู่ในคลาสเดียวกันให้ถูกต้อง
         print(f'f({x}) = {self.f(x)}') 
         print(f'df({x}) = {self.df(x)}')

    def solve(self, x, tol, max_iter):
        for i in range(max_iter):
            if self.df(x) == 0:
                 print('df(x) is zero')
                 break
            x = x - self.f(x)/self.df(x)
            self.display(x)
            if abs(self.f(x)) < tol:
                 break
        return x