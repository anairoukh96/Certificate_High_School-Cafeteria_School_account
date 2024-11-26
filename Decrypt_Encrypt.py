def transform(x):
    x = list(x)
    for i, n in enumerate(x):
        if n in ABC:
            x[i] = ABC.index(n)
    return x

# تشفير النص باستخدام مفتاح التشفير
def crypt(x, key):
    x = transform(x)
    x = [(n + key) % 26 if type(n) == int else n for i, n in enumerate(x)]
    return x

# فك التشفير باستخدام المفتاح
def decrypt(x, key):
    x = transform(x)
    if key is None:  # إذا كان المفتاح غير معروف
        d = []
        for k in range(26):  # جرب جميع المفاتيح من 0 إلى 25
            d.append(crypt(x, -k))
        x = d
    else:
        x = crypt(x, -key)
    return x

# وظيفة رئيسية لإجراء التشفير أو فك التشفير
def caesar(x, key, mod):
    v = []
    if mod:  # إذا كانت العملية هي التشفير
        x = crypt(x, key)
    else:  # إذا كانت العملية فك التشفير
        x = decrypt(x, key)
    for i, n in enumerate(x):
        if type(n) == int:
            x[i] = ABC[n]  # تحويل القيم الرقمية إلى أحرف
        elif type(n) == list:
            for j, m in enumerate(n):
                if type(m) == int:
                    n[j] = ABC[m]
            value = ''.join(n)
            v.append(f'==> key = {i} : {value}')
    if len(v) != 0:
        return '\n'.join(v)
    return f"==> {''.join(x)}"

# تعريف الأبجدية
ABC = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# البرنامج الرئيسي
if input('==> Encrypt or Decrypt ? : ').lower() == 'encrypt':
    x = input('Enter what you want to encrypt => ').upper()
    key = int(input('Enter the key [0-25] => '))
    mod = True
else:
    x = input('Enter what you want to decrypt => ').upper()
    if input('Do you have the key ? (y/n) :').lower() == 'y':
        key = int(input('Enter the key => '))
    else:
        key = None
    mod = False

# طباعة النتيجة
print(caesar(x, key, mod))