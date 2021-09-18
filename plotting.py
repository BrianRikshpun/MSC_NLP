import matplotlib.pyplot as plt
import numpy as np

class plotter():
    def __init__(self, precisionC, recallC, f1C, accC):
        self.precisionC = precisionC
        self.recallC = recallC
        self.f1C = f1C
        self.accC = accC



    def plotM(self, title = "none"):

        def addlabels(x, y):
            for i in range(len(x)):
                plt.text(i, round(y[i],5), round(y[i],5))


        names = ['Accuracy', 'F1_core', 'Precision', 'Recall']
        valuesC = [self.accC, self.f1C, self.precisionC, self.recallC]

        x = np.arange(len(names))  # the label locations
        width = 0.35

        fig, ax = plt.subplots()
        CRFbar = ax.bar(x - width / 2, valuesC, width)

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Percentage')
        ax.set_title(title)
        ax.set_xticks(x)
        ax.set_xticklabels(names)
        ax.legend()

#        ax.bar_label(CRFbar, padding=3)
#        ax.bar_label(HMMbar, padding=3)

        fig.tight_layout()
        addlabels(x,valuesC)
        plt.show()
