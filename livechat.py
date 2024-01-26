
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
import pytchat
from datetime import datetime
ptime=1;
i=0;
val = input("Enter youtube live stream:")
val = val.split("https://www.youtube.com/watch?v=",1)[1]
print("Note: Please enter time as 0 seconds to exit the program")

while ptime!=0:
        i=i+1
        try:
            ptime = int(input("Poll time in seconds: "))
            print("The number entered in sec for ", i, " poll is:", ptime)
        except ValueError:
            print("Invalid input. Please enter an integer.")
        List_m = []
        List_a = []
        List_t = []
        allowed = ["a","b","c","d","e","A","B","C","D","E"]
        #allowed = set(('a','b','c','d','e','A','B','C','D','E'))
        chat = pytchat.create(video_id= val)
        t1 = datetime.now()
        while (datetime.now()-t1).seconds <= ptime:
            for c in chat.get().sync_items():
                if c.message[:1] in allowed and c.author.name not in List_a:
                    List_a.append(c.author.name)
                    List_m.append(c.message[:1].replace('a','A').replace('b','B').replace('c','C').replace('d','D').replace('e','E'))
                    List_t.append(str(datetime.now()-t1)[6:8])
        for a in range(len(List_m)):
            print(List_a[a]+" "+List_m[a]+" "+List_t[a])
        ax =sns.set_style(style="darkgrid")
        left = [1, 2, 3, 4, 5]
        tick_label = ['A', 'B', 'C', 'D', 'E']
        if ptime == 0:
            break
        y= len(List_a)/100
        height = [List_m.count('A')/y, List_m.count('B')/y,List_m.count('C')/y,List_m.count('D')/y, List_m.count('E')/y]
        print(height)
        sc = plt.bar(left, height, tick_label = tick_label,
                width = 0.8, color = ['red', 'green','blue','orange'])
        plt.xlabel('Options')
        plt.ylabel('Responses')
        plt.show()

print("Please close this window,Thankyou")



