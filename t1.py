import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from numpy.fft import fft

### Exercici 1 ###

## Senyal 4kHz
T= 2.5                               
fm=8000                              
fx=4000                              
A=4                                  
pi=np.pi                            
L = int(fm * T)                      
Tm=1/fm                              
t=Tm*np.arange(L)                    
x = A * np.cos(2 * pi * fx * t)      
sf.write('ex1_4khz.wav', x, fm)   
Tx=1/fx                                   
Ls=int(fm*5*Tx)    

# Representació
plt.figure(0)                            
plt.plot(t[0:Ls], x[0:Ls])                
plt.xlabel('t en segons')                 
plt.title('5 periodes de la sinusoide 4kHz')
plt.savefig('5_periodes_4khz.png')
plt.show()                                
sd.play(x, fm)    

# Domini transformat
N=5000                       
X=fft(x[0 : Ls], N)           
k=np.arange(N)                       
plt.figure(1)                         
plt.subplot(211)                      
plt.plot(k,abs(X))                    
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                  
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(X)))    
plt.xlabel('Index k')                 
plt.ylabel('$\phi_x[k]$')   
plt.savefig('TF_4khz.png')
plt.show()

## Senyal 1kHz
T= 2.5                              
fm=8000                            
fx=1000                             
A=4                               
pi=np.pi                            
L = int(fm * T)                      
Tm=1/fm                              
t=Tm*np.arange(L)                    
x = A * np.cos(2 * pi * fx * t)     
sf.write('ex1_1khz.wav', x, fm)   
Tx=1/fx                                  
Ls=int(fm*5*Tx)                          

# Representació
plt.figure(2)                             
plt.plot(t[0:Ls], x[0:Ls])                
plt.xlabel('t en segons')                
plt.title('5 periodes de la sinusoide 1kHz')
plt.savefig('5_periodes_1khz.png')
plt.show()                              
sd.play(x, fm)    

# Domini transformat
N=5000                        
X=fft(x[0 : Ls], N)           
k=np.arange(N)                      
plt.figure(3)                        
plt.subplot(211)                      
plt.plot(k,abs(X))                   
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')               
plt.subplot(212)                     
plt.plot(k,np.unwrap(np.angle(X)))  
plt.xlabel('Index k')                 
plt.ylabel('$\phi_x[k]$')
plt.savefig('TF_1khz.png')
plt.show() 


### Exercici 2 ###
x_r, fm = sf.read('ex1_4khz.wav')
Tm=1/fm
t=Tm*np.arange(len(x_r))
fx=fm/2
Tx=1/fx
Ls=int(fm*5*Tx)
plt.figure(4)
plt.plot(t[0:Ls], x_r[0:Ls])
plt.xlabel('t en segons')      
plt.title('5 periodes de la sinusoide 4kHz ex2')
plt.savefig('ex2_4khz.png')
plt.show()

sd.play(x_r, fm)    

N=5000                       
X=fft(x_r[0 : Ls], N)         
k=np.arange(N)                        
plt.figure(5)                        
plt.subplot(211)                     
plt.plot(k,abs(X))                   
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                 
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(X)))   
plt.xlabel('Index k')               
plt.ylabel('$\phi_x[k]$')
plt.savefig('ex2_TF_4khz.png')
plt.show()    


### Exercici 3 ###