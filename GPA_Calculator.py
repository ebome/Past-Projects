'''
HWAM in USYD calculator
'''

ye2=input('enter 2nd yr subject scores, not incld X111:')
year2 = eval(ye2)
ye3=input('enter 3rd yr subject scores, not incld X111:') # input as a string, but cast into list
year3 = eval(ye3)
ye4=input('enter 4th yr subject scores, not incld X111:')
year4 = eval(ye4)
# thesis=input('enter thesis scores:')
# thesis_score = eval(thesis)

enggX111=input('enter x111 subject scores:')
ENGGx1111=eval(enggX111)

accumulation=0
for yr2 in year2:
    accumulation = accumulation + 2*6*yr2
for yr3 in year3:
    accumulation = accumulation + 3*6*yr3
for yr4 in year4:
    accumulation = accumulation + 4*6*yr4
for x111 in enggX111:
    accumulation = accumulation + 2*2*yr2
    
denominator = 2*6*len(year2)+3*6*len(year3)+4*6*len(year4)+2*(2 + 3 + 4)

HWMA = accumulation/denominator

print('your current hwam is:' + str(HWMA))

# https://www.jianshu.com/p/0424d49f325d



