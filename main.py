import hmmModule
import crfModule
import plotting
import matplotlib.pyplot as plt


arr = ['lbfgs', 'l2sgd', 'ap', 'pa' , 'arow']

if __name__ == '__main__':


    for i in range(5):
        crf = crfModule.crfClinet(algorithm = arr[i])
        precisionC, recallC, f1C, accC = crf.start()
        cp = plotting.plotter(precisionC, recallC, f1C, accC)
        cp.plotM(title = str(arr[i]))

#    chp = plotting.plotter(precisionC, recallC, f1C, accC, precisionH, recallH, f1H, accH)
#    chp.plotM()

