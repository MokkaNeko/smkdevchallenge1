# Ichsan Ardika Akbar
# SMKDEV Challenge basic

m_udin = 78
t_udin = 1.69
m_nanang = 92
t_nanang = 1.95
# m_udin = 95
# t_udin = 1.88
# m_nanang = 85
# t_nanang = 1.76
def bmi(m, t):
    return m / (t ** 2)
def compare(m1, t1, m2, t2):
    if bmi(m1, t1) > bmi(m2, t2):
        return True
    else:
        return False
if compare(m_udin, t_udin, m_nanang, t_nanang):
    print("BMI Udin", round(bmi(m_udin, t_udin), 2), "lebih tinggi dari BMI Nanang", round(bmi(m_nanang, t_nanang), 2))
else:
    print("BMI Nanang", round(bmi(m_nanang, t_nanang), 2), "lebih tinggi dari BMI Udin", round(bmi(m_udin, t_udin), 2))