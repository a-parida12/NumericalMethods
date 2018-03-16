
def plotter_exp(p_exp,dt_all,tend,labels):
    import matplotlib.pyplot as plt
    #plt.figure()


    ##subplot for dt=1/2
    dt=dt_all[0]
    plt.subplot(2, 2, 1)
    t = np.arange(0,tend,dt)
    tip = np.arange(0,tend,dt_all[-1])
    p = 10/(1+(9*np.exp(-tip)))
    plt.title("function p(t) v/s t for dt="+str(dt))
    plt.xlabel("t")
    plt.ylabel("p(t)")
    handle1,=plt.plot(tip,p,'b',label='Analytic Soln')
    handle2,=plt.plot(t,p_exp[dt],'r',label=labels)
    plt.legend(handles=[handle1,handle2])

    ##subplot for dt=1/4
    dt=dt_all[1]
    plt.subplot(2, 2, 2)
    t = np.arange(0,tend,dt)
    tip = np.arange(0,tend,dt_all[-1])
    p = 10/(1+(9*np.exp(-tip)))
    plt.title("function p(t) v/s t for dt="+str(dt))
    plt.xlabel("t")
    plt.ylabel("p(t)")
    handle1,=plt.plot(tip,p,'b',label='Analytic Soln')
    handle2,=plt.plot(t,p_exp[dt],'r',label=labels)
    plt.legend(handles=[handle1,handle2])

    ##subplot for dt=1/8
    dt=dt_all[2]
    plt.subplot(2, 2, 3)
    t = np.arange(0,tend,dt)
    tip = np.arange(0,tend,dt_all[-1])
    p = 10/(1+(9*np.exp(-tip)))
    plt.title("function p(t) v/s t for dt="+str(dt))
    plt.xlabel("t")
    plt.ylabel("p(t)")
    handle1,=plt.plot(tip,p,'b',label='Analytic Soln')
    handle2,=plt.plot(t,p_exp[dt],'r',label=labels)
    plt.legend(handles=[handle1,handle2])

    ##subplot for dt=1/16
    dt=dt_all[3]
    plt.subplot(2, 2, 4)
    t = np.arange(0,tend,dt)
    tip = np.arange(0,tend,dt_all[-1])
    p = 10/(1+(9*np.exp(-tip)))
    plt.title("function p(t) v/s t for dt="+str(dt))
    plt.xlabel("t")
    plt.ylabel("p(t)")
    handle1,=plt.plot(tip,p,'b',label='Analytic Soln')
    handle2,=plt.plot(t,p_exp[dt],'r',label=labels)
    plt.legend(handles=[handle1,handle2])
    plt.show()




