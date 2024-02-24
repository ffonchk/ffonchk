#การคำนวณ newton method แบบง่าย

def f(x):
    return x**3 - 4

def df(x):
    return 3*x**2



#######################################################

from newton import Newton

x = 10
f_x = f(x)
df_x = df(x)
#print(f_x,df_x)
#print(f'f({x}) = {f_x}') #เราอยากให้แสดงพร้อมกับข้อความด้วย ตัวหนังสือข้างใน f(ตัวเลข) = คำตอบ
#print(f'df({x}) = {df_x}')

###
aaa = Newton(f, df)
aaa.solve(x, 1e-10, 100)



