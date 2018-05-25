import matplotlib.pyplot as plt

def opening(name):
    with open(name,"r") as f:
        lines.append([name])
        for line in f:
            if line[0] == "/":
                words = line.split()
                lines.append(words)

def draw_graph(file_name):
    x_axis = []
    loc = []
    tested_loc = []
    for i in range(len(lines)):
        if len(lines[i])==1:
            name = lines[i][0].split("/")
            print(name)
        elif lines[i][0] == file_name:
            x_axis.append(name[-1])
            loc.append(int(lines[i][1]))
            tested_loc.append(int(lines[i][1]) - int(lines[i][2]))
    print(x_axis, loc, tested_loc)
    plt.title(file_name)
    plt.plot(x_axis, loc, label = "loc")
    plt.xticks(x_axis, rotation='vertical')
    plt.xticks(size=7)
    plt.yticks(size=10)
    plt.plot(x_axis,tested_loc, label = "tested_loc")

    plt.legend()
    plt.savefig(file_name.replace("/", "_") + ".png")
    plt.show()

lines = []
files = ["./data/fabric8-analytics-worker.coverage.0.txt","./data/fabric8-analytics-worker.coverage.1.txt","./data/fabric8-analytics-worker.coverage.2.txt","./data/fabric8-analytics-worker.coverage.3.txt"]

for file in files:
    opening(file)

for file in lines:
    if len(file) > 1:
        print(file[0])
        draw_graph(file[0])
