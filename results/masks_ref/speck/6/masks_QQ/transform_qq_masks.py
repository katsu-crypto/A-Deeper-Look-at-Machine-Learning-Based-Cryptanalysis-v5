import numpy as np
liste_all_mask = []
masksc0l = []
masksc0r = []
masksc1l = []
masksc1r = []

infile = open(
    "ciphertext_masks-same_input.txt",
            'r')
for line in infile:
    if "XOR" not in line:

        line2 =line.split("],[")[0]
        line3 = line.split("],[")[-1]
        line4 =line2.split(",")[0].replace("[","")
        line5 =line2.split(",")[-1]

        line6 = line3.split(",")[0]
        line7 = line3.split(",")[-1].replace("]\n", "").replace("]", "")


        #print(line4, line5, line6, line7)

        c0l = int(line4)
        c0r = int(line5)
        c1l = int(line6)
        c1r = int(line7)
        nc0 = np.sum(np.array([int(x) for x in list('{0:0b}'.format(c0l))]))
        nc1 = np.sum(np.array([int(x) for x in list('{0:0b}'.format(c0r))]))
        nc2 = np.sum(np.array([int(x) for x in list('{0:0b}'.format(c1l))]))
        nc3 = np.sum(np.array([int(x) for x in list('{0:0b}'.format(c1r))]))


        if (c0l, c0r, c1l, c1r) not in liste_all_mask:
            liste_all_mask.append((c0l, c0r, c1l, c1r))
            masksc0l.append(c0l)
            masksc0r.append(c0r)
            masksc1l.append(c1l)
            masksc1r.append(c1r)

infile.close()


with open("masks_"+str(len(masksc0l))+".txt","w") as file:
    file.write(str(masksc0l))
    file.write("\n")
    file.write(str(masksc0r))
    file.write("\n")
    file.write(str(masksc1l))
    file.write("\n")
    file.write(str(masksc1r))
    file.write("\n")