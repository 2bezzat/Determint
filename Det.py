#!/usr/bin/python2.7
#
#By Abd El Rahamn Ezzat 
#29-11-2015
############# GETTING DATA #############

from __future__ import division 

def getR1():
	R1 = int(raw_input('pleas enter row one : '))
	return R1 

def getR2():
	R2 = int(raw_input('pleas enter row two : '))
	return R2

def getR3():
	R3 = int(raw_input('pleas enter row three : '))
	return R3 


R1 = getR1()
while R1 > 999 or R1 < 100  :
	R1=getR1()

print R1


R2 = getR2()
while R2 > 999 or R2 < 100:
	R2=getR2()

print R2


R3 = getR3()	
while R3 > 999 or R3 < 100:
	R3=getR3()

print R3 
	
######################## Dealing with data ############

R1_L = map(int,str(R1))

R2_L = map(int,str(R2))

R3_L = map(int,str(R3))

########################Showing Full Determint ############### 
print '######################\n'
print 'Full Determint\n'
print "		",R1_L[0],R1_L[1],R1_L[2]
print "		",R2_L[0],R2_L[1],R2_L[2]
print "		",R3_L[0],R3_L[1],R3_L[2]
print '\n######################\n'



############################# Solver ################


R1_2_solver = -R2_L[0] / R1_L[0] 	

R1_3_solver = -R3_L[0] / R1_L[0] 	



###################Row two after adding #######################

print "First multiplay row one with ", "'", R1_2_solver ,"'","and add it to row 2"

# print R1_L[0] * R1_2_solver + R2_L[0] , R1_L[1] * R1_2_solver + R2_L[1], R1_L[2] * R1_2_solver + R2_L[2]

R2_new = []
A = R1_L[0] * R1_2_solver + R2_L[0]
R2_new.append(A)
B = R1_L[1] * R1_2_solver + R2_L[1]
R2_new.append(B)
C = R1_L[2] * R1_2_solver + R2_L[2]
R2_new.append(C)


print R1_L[0],R1_L[1],R1_L[2]

print R2_new[0] , R2_new[1] , R2_new[2]


######################## Row Three After Editing ##################
print "\n secound multiplay row two with ", "' ", R1_3_solver," '","and add it to row 3\n"

R3_new =[]

E = R1_L[0] * R1_3_solver + R3_L[0]
R3_new.append(E)
F = R1_L[1] * R1_3_solver + R3_L[1]
R3_new.append(F)
K =  R1_L[2] * R1_3_solver + R3_L[2]
R3_new.append(K)

print R1_L[0],R1_L[1],R1_L[2]

print R2_new[0] , R2_new[1] , R2_new[2]

print R3_new[0] , R3_new[1] , R3_new[2]


############ A fucking missing part ############
##################### Gettimg The third Zero ################# 

third_solver = -R3_new[1] / R2_new[1]

print "\nLast step is multiplay row 2 with  " ,"'",third_solver,"'" ,"and add it to row three \n"


print R1_L[0],R1_L[1],R1_L[2]

print R2_new[0] , R2_new[1] , R2_new[2]

Q = R2_new[0] * third_solver + R3_new[0]
W = R2_new[1] * third_solver + R3_new[1]
E = R2_new[2] * third_solver + R3_new[2]

print Q , W , E 


######################3 Final Result #######

print " now it's the final step , Calcluate the Digonal ;) \n"

print "Your answer is : ", E * R2_new[1] * R1_L[0] 












