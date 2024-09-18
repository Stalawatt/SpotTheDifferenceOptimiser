import matplotlib.pyplot as plt, numpy as np, scipy.stats as st, seaborn as sb

def coordinate_Data(data):
    xCoords,yCoords = [],[]
    for i in data:
        xCoords.append(i[0])
        yCoords.append(i[1])

    return yCoords,xCoords

def drawArrows(data):
    for i in range(len(data)-1):
        
        if i != len(data)-1:
            plt.arrow(data[i][1],data[i][0],data[i+1][1] - data[i][1], data[i+1][0] - data[i][0],width = 0.08)

def drawPoints(data,ax):
    for each in data:
        ax.scatter(each[1],each[0])



def densityEstimate(data):
    data = np.array(data)
    new_data = np.cov(data, rowvar = False)
    mean = np.mean(data, axis = 0)
    print(str(new_data))
    data = np.random.multivariate_normal(mean,new_data,size=1000)
    """for i in data:
        xPosList.append(i[1])
        yPosList.append(i[0])"""
    xPosList = data[:,0]
    yPosList = data[:,1]

    xmin, xmax = 0,9
    ymin,ymax = 0,6
    xx,yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([xPosList,yPosList])
    kernel = st.gaussian_kde(values)
    f = np.reshape(kernel(positions).T, xx.shape)
    return f, xx, yy

def showData(data):
    yCoords,xCoords = coordinate_Data(data)
    f, xx, yy = densityEstimate(data)
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xlim(0,9)
    ax.set_ylim(0,6)
    cfset = ax.contour(xx,yy,f,cmap = "Blues")
    cset = ax.contour(xx,yy,f,colors = "k")
    ax.clabel(cset,inline = 1)

    #drawPoints(data,ax)
    #drawArrows(data)

    plt.show()


