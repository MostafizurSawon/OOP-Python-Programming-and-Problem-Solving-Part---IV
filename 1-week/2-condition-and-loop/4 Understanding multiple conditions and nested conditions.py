 
job_exam = 'BCS'
job_passed = False
second = "Bank"

"""
if(job_exam == 'BCS') :
    print('1st class govt job')

if(job_passed == True) : 
    print('Congrats You are a job holder now!')
else:
    print('Try next year again!') 
"""


"""
if job_exam == 'BCS' and job_passed == True :
    print('congrats you are a 1st class govt job holder now!')
    print("Time to be rich!")
else:
    print("Alas!")

"""

if job_exam == 'BCS' or second == 'Bank' :
    print("You got a job!")
else:
    print("Jobless!")