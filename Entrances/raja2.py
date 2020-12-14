from scipy import *
import numpy as np
from matplotlib.pyplot import *
#Not bisection ! but still bisection
def bisection(l,u,f):
	if f(l)*f(u)<0:
		for i in range (100):
			mid=(l+u)/2
			if f(l)*f(mid)<0:
				u=mid
			else:
				l=mid
	if f(l)*f(u)>0:
         mid=-1
	return mid

#rk4
def rk4(x_0,y_0,z_0,x_f,n,f,g,e):
	h=float((x_f-x_0)/n)
	x=np.linspace(x_0,x_f,n+1)
	y=np.zeros(n+1)
	z=np.zeros(n+1)
	y[0]=y_0
	z[0]=z_0
	k=1
	while k<n+1:
		k1=h*f(x_0,y_0,z_0)
		l1=h*g(x_0,y_0,z_0,e)
		k2=h*f(x_0+h/2,y_0+k1/2,z_0+l1/2)
		l2=h*g(x_0+h/2,y_0+k1/2,z_0+l1/2,e)
		k3=h*f(x_0+h/2,y_0+k2/2,z_0+l2/2)
		l3=h*g(x_0+h/2,y_0+k2/2,z_0+l2/2,e)
		k4=h*f(x_0+h,y_0+k3,z_0+l3)
		l4=h*g(x_0+h,y_0+k3,z_0+l3,e)
		y_f=y_0+(k1+2*(k2+k3)+k4)/6
		z_f=z_0+(l1+2*(l2+l3)+l4)/6
		x_0=x[k]
		y_0=y_f
		z_0=z_f
		y[k]=y_0
		z[k]=z_0
		k=k+1
	return x,y,z
#modified euler
def me(x0,y0,z0,xf,n,f,g,e):
	h=(xf-x0)/n
	x=np.linspace(x0,xf,n+1)
	y=np.zeros(n+1)
	z=np.zeros(n+1)
	y[0]=y0
	z[0]=z0
	k=1
	while k<n+1:
		k1=h*f(x0,y0,z0)
		l1=h*g(x0,y0,z0,e)
		k2=h*f(x0+h,y0+k1,z0+l1)
		l2=h*g(x0+h,y0+k1,z0+l1,e)
		yf=y0+(k1+k2)/2
		zf=z0+(l1+l2)/2
		y[k]=yf
		z[k]=zf
		y0=yf
		z0=zf
		k=k+1
	return x,y,z
#barrier potential
#fn for second order DE
def f1(x,y,z):
	return z
def g1(x,y,z,e):
	return -(e-V)*y
#fn for evaluating value of wavefunction at xf for given energy e  
def fb(e):
	a,b,c=rk4(x0,y0,z0,xf,n,f1,g1,e)
	return b[n]
#initializing
a1=0 
a2=10
x0=0
xf=10
y0=0
z0=1
n=100
#energy guess
E0=0.01
n1=50
V=0
E_g=np.linspace(E0,10,n1+1)
#array for storing energy
E_store=np.zeros(n1)
u=0
for i in range (0,n1):	
	E_store[i]=bisection(E_g[i],E_g[i+1],fb)
	if E_store[i]>0:
		u=u+1
print("pl",u)
#plot 
#I choosed e1 because graph isse hi shi aa rha tha baaki values par acha nhi aarha tha
E_store=np.sort(E_store)
print(E_store)
print("size",np.size(E_store),n1)
f12=E_store[n1-u:n1]
print("yhi",f12)
for i in range(0,u):
	a1,b1,c1=rk4(x0,y0,z0,xf,n,f1,g1,f12[i])
	plot(a1,b1)
savefig("infiniteshooting.pdf")
show()
#writing data in file
output=open("shootingdata.dat","w")
output.write("  X            Y ")
for i in range (0,n+1):
	output.write("\n%8.6f\t%8.6f"%(a1[i],b1[i]))
output.write("\n****************************************************************************************************")
output.write("\nValue of Energies")
for i in range (0,49):
		output.write("\n%8.6f"%(f12[i]))
output.close()