import matplotlib.pyplot as plt


SSD_64 = [0.124651,
0.143387,
0.129854,
0.146307,
0.158032,
0.158281,
0.157612,
0.119928,
0.125398,
0.155733
]
SSD_128 = [0.272421,
0.254795,
0.289622,
0.271395,
0.245908,
0.256446,
0.245882,
0.251662,
0.245855,
0.271395
]

HDD_64 = [0.20214,0.221585,0.213342,0.208043,0.193229,0.218692,0.213001,0.185827,0.208043,0.213342]
HDD_128 = [0.477034,
0.416293,
0.409917,
0.402235,
0.399446,
0.42474,
0.439957,
0.411123,
0.428927,
0.43392,
]
X_axis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print(HDD_64)
# print(HDD_128)
# print(SSD_64)
# print(SSD_128)
plt.figure(figsize=(5, 2.2))
# plt.xlim([0.5, 10.5])

group_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#显示全部刻度
plt.ylim([0.05,0.58])
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Trials", fontsize=14)
plt.ylabel("Reading Time (s)", fontsize=14)
plt.plot(X_axis, SSD_64,  color="blue", marker="s",label="SSD-64MB")
plt.plot(X_axis, SSD_128, color="blue",marker="o",label="SSD-64MB*2" )
plt.plot(X_axis, HDD_64, color="red", marker="s",label="HDD-64MB")
plt.plot(X_axis, HDD_128, color="red", marker="o",label="HDD-64MB*2")
plt.xticks(X_axis, group_labels)
plt.legend(loc="upper right", ncol=2, prop={'size': 7})
file_name = "fig_motivation5.eps"
plt.savefig(file_name, bbox_inches='tight', format='eps', dpi=5000)
plt.show()
