import pickle
from matplotlib import pyplot as plt

DATADIR0 = r"D:\K14\Dataset\K14 Prototyp 572x572\K14 Prototyp 572x572\ds0\img"
DATADIR1 = r"D:\K14\Dataset\K14 Prototyp 572x572\K14 Prototyp 572x572\ds0\masks_machine"
DATADIR2 = r"D:\K14\Dataset\K14 Prototyp 572x572\Prep.pickle"

def ImCompareGray(Im1, Im2, FigSize):
    f = plt.figure(figsize=FigSize)
    f.add_subplot(1,2, 1)
    plt.imshow(Im1, cmap="gray")
    f.add_subplot(1,2, 2)
    plt.imshow(Im2, cmap="gray")
    plt.show(block=True)

Dir = pickle.load(open(DATADIR2, "rb"))
for i in range(50):
    Im1 = Dir["TrainImages0"][i]
    Im2 = Dir["TrainImages1"][i]
    ImCompareGray(Im1, Im2, (15, 7))
    break