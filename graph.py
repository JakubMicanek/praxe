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
            x_axis.append(lines[i][0])
        elif lines[i][0] == file_name:
            loc.append(int(lines[i][1]))
            tested_loc.append(int(lines[i][1]) - int(lines[i][2]))
    print(x_axis, loc, tested_loc)
    plt.title(file_name)
    plt.plot(x_axis, loc, label = "loc")
    plt.plot(x_axis,tested_loc, label = "tested_loc")
    plt.legend()
    plt.savefig(file_name.replace("/","_")+".png")
    plt.show()

lines = []
files = ["./data/fabric8-analytics-worker.coverage.0.txt","./data/fabric8-analytics-worker.coverage.1.txt","./data/fabric8-analytics-worker.coverage.2.txt","./data/fabric8-analytics-worker.coverage.3.txt"]

for file in files:
    opening(file)

draw_graph("/f8a_worker/f8a_worker/workers/victims.py")
