from newton import Newton

def test_newton_method_quadratic(): # หลัง test จะแก้เป็นตัวหนังสืออะไรก็ได้
    f = lambda x: x**2 - 4 #มาจาก def บลาๆ ยาวๆ อันนี้เป็นแบบย่อ
    df = lambda x: 2*x
    nm = Newton(f, df)
    assert round(nm.solve(10, 1e-10,100), 10) == 2
    assert round(nm.solve(-10, 1e-10,100), 10) == -2