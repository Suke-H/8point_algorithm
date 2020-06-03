import sympy as sy
import numpy as np

def calc_inside_param(F, e, p11, p12, p21, p22, calc_phase="f"):

    # A1, A2
    # 今からa1, a2を求める
    sy.var('a1, a2')
    A1 = sy.Matrix([[a1, 0, p11],
                    [0, a1, p12],
                    [0, 0, 1]])
    A2 = sy.Matrix([[a2, 0, p21],
                    [0, a2, p22],
                    [0, 0, 1]])


    # sy.var('a11, a12, a21, a22')

    # if calc_phase == "f":

    #     A1 = sy.Matrix([[a11, 0, p11],
    #                     [0, a12, p12],
    #                     [0, 0, 1]])
    #     A2 = sy.Matrix([[a21, 0, p21],
    #                     [0, a22, p22],
    #                     [0, 0, 1]])

    # else:

    #     A1 = sy.Matrix([[p11, 0, a11],
    #                     [0, p12, a12],
    #                     [0, 0, 1]])
    #     A2 = sy.Matrix([[p21, 0, a21],
    #                     [0, p22, a22],
    #                     [0, 0, 1]])

    sy.var('t, e1, e2, e3, f11, f12, f13, f21, f22, f23, f31, f32, f33')

    # vec_t
    vec_t = sy.Matrix([1, t, 0])

    # # e
    # e = sy.Matrix([e1, e2, e3])
    # # F
    # F = sy.Matrix([[f11,f12,f13], 
    #                 [f21,f22,f23], 
    #                 [f31,f32,f33]])

    # e, Fをsympyに変換
    e = sy.Matrix([e[0], e[1], e[2]])
    F = sy.Matrix([[F[0,0],F[0,1],F[0,2]], 
                    [F[1,0],F[1,1],F[1,2]], 
                    [F[2,0],F[2,1],F[2,2]]])

    # eq1 = (e × t)^T * A1 * A1^T * (e1 × t) = 0
    tmp1 = A1.transpose() * e.cross(vec_t)
    eq1 = sy.expand((tmp1.transpose() * tmp1)[0])
    print(eq1)

    # eq1からt^0, t^1, t^2の係数を取り出す
    k10 = eq1.coeff(t, 0)
    k11 = eq1.coeff(t, 1)
    k12 = eq1.coeff(t, 2)
    print(k10, k11, k12)

    print("="*50)

    # eq2 = (F^T × t)^T * A2 * A2^T * (F^T × t) = 0
    tmp2 = A2.transpose() * F.transpose()*vec_t
    eq2 = sy.expand((tmp2.transpose() * tmp2)[0])
    print(eq2)

    print("="*50)
    
    # eq1からt^0, t^1, t^2の係数を取り出す
    k20 = eq2.coeff(t, 0)
    k21 = eq2.coeff(t, 1)
    k22 = eq2.coeff(t, 2)
    print(k20)
    print(k21)
    print(k22)

    print("="*50)

    # expr1 = k10*k21 - k11*k20
    expr1 = sy.expand(k10*k21 - k11*k20)
    # expr2 = k11*k22 - k21*k12
    expr2 = sy.expand(k11*k22 - k21*k12)
    print(expr1)
    print(expr2)

    print("="*50)

    # expr1 = expr2 = 0を解く(解はa1, a2)
    ans = sy.solve([expr1, expr2], [a1, a2])
    print(ans)

    return ans