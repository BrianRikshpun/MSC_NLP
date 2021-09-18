import hmmModule
import crfModule
import plotting
import matplotlib.pyplot as plt


arr = [1,5,100]

if __name__ == '__main__':


    for i in range(3):
        crf = crfModule.crfClinet(max_it = arr[i])
        precisionC, recallC, f1C, accC = crf.start()
        cp = plotting.plotter(precisionC, recallC, f1C, accC)
        cp.plotM(title = str(arr[i]))

#    chp = plotting.plotter(precisionC, recallC, f1C, accC, precisionH, recallH, f1H, accH)
#    chp.plotM()

