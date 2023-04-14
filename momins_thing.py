import numpy as np

def smoothListGaussian(list,degree=5):  
    window=degree*2-1  
    weight=np.array([1.0]*window)  
    weightGauss=[]  
    for i in range(window):  
        i=i-degree+1  
        frac=i/float(window)  
        gauss=1/(np.exp((4*(frac))**2))  
        weightGauss.append(gauss)  
    weight=np.array(weightGauss)*weight  
    smoothed=[0.0]*(len(list)-window)  
    for i in range(len(smoothed)):  
        smoothed[i]=sum(np.array(list[i:i+window])*weight)/sum(weight)  
    return smoothed  



    # Generate the polygon
theta = np.linspace(0,2*np.pi,200, endpoint=False)
r = np.random.lognormal(0,0.4,200)*2
r = np.pad(r,(9,10),mode='wrap')
    
r = smoothListGaussian(r, degree=10)

coords = [(np.cos(theta[i])*r[i], np.sin(theta[i])*r[i], 0) for i in range(len(theta))]