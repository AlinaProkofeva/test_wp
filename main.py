passw = '4008 609136'

print(passw[:2] + ('*' * 7) + passw[-2:])
print(passw[-3:].rjust(11, '*'))

e = '\tПривет медвед\nдаёшь отступ нового абзаца'
print(e)

we = 'D\ns\t'
print(we)
we = r'D\ns\t'
print(we)