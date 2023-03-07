import pandas as pd
import matplotlib.pyplot as plt
Exam_data = {'Name' : ['English', 'hindi', 'maths', 'social', 'science'],
             'Marks obtained' : [ 90, 87, 85, 70, 83]}

df = pd.DataFrame(Exam_data) 
plt.bar(df['Name'], df['Marks obtained'])
plt.xlabel("Name")
plt.ylabel("Marks obtained")
plt.show()

  
