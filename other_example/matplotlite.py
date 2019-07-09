
import matplotlib.pyplot as plt
from random import choice
class random_walk():
    def __init__(self,num_points=500):
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]

    def fill_walk(self):
        next_x=0
        next_y=0
        while len(self.x_values)<500:
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_steps=x_direction*x_distance
            y_direction=choice([1,-1])
            y_distance=choice([0,1,2,3,4])
            y_steps=y_direction*y_distance
            if x_steps==0 and y_steps==0:
                continue
            next_x+=x_steps
            next_y+=y_steps
            #next_x=self.x_values[-1]+x_steps
            #next_y=self.y_values[-1]+y_steps
            self.x_values.append(next_x)
            self.y_values.append(next_y)

            rw=random_walk()
            rw.fill_walk()
            point_numbers=list(range(rw.num_points))
            plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=15)
            plt.scatter(0,0,c="red",s=100)
            plt.scatter(rw.x_values[-1],rw.y_values[-1],c="red",s=100)