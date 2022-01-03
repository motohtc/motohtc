import os
i=1
while i<10:
 os.system(f'echo test>>d:\\test\\{i}.txt')
 print(f'{i}.txt')
 i=i+1
 os.system(f'del /Q d:\\test\\{i-1}.txt')
