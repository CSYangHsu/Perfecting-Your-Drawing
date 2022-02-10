# Perfecting-Your-Drawing
Many drawing tools, such as iPad, have a function that when you are drawing a shape by hand, they will guess what it is, and make the best fit one to replace it. For example, if you draw a lopsided circle, it will produce a perfect one for it. In this project, i do that using the magic from linear algebra.  

## Algorithm
The used algorithm is based on the least square method. For example,to fit a circle,  
![image](https://user-images.githubusercontent.com/86723888/153364598-f3b6ccd5-517f-4522-8d44-4a78b58d0662.png)  
we need to find out what c1, c2 and r are so that  
![image](https://user-images.githubusercontent.com/86723888/153364708-0ac23f24-98f1-4231-a81d-de941a54ae28.png)  
is minimum for the given data (x1, y1),(x2, y2), . . . ,(xm, ym).  
The above problem is nonlinear, which is hard to solve. But we can approximate it by rewriting (1) with  
![image](https://user-images.githubusercontent.com/86723888/153364853-bddbac53-246b-4aa1-afce-04be47535581.png)  
for c3 = r^2 − (c1)^2 - (c2)^2　 , and making c1, c2, c3 independent variables.  
To transform the min f(c1,c2,c3) into matrix form. Let  
![image](https://user-images.githubusercontent.com/86723888/153365259-b7b70e00-33c4-4f4d-82ca-d5db978e0ee5.png),  
The original problem is to solve an over-determinded system, Ax = b.  
The problem is also called a least square problem, which can be solved by the normal equation A^T A x = A^T b.




## Table of Contents
* [implement.py](#implement)
* [implement5.py](#implement5)



## implement
### introduce
- to find best fitting circle:  
uses "numpy.linalg.lstsq" to solve the least square problem.

- to find best fitting ellipse:  
using least square algorithm with the formula   
" c1 x^2 + c2 xy + c3 y^2 + c4 x + c5 y  =  1 ".  
The formula can actually fit all kinds of curves from conic section.


### demo for circle
- example1:

![Example screenshot11](./img/hand_draw_circle1.png)

![Example screenshot12](./img/hand_draw_circle1_output.png)

- example2:

![Example screenshot11](./img/hand_draw_circle2.png)

![Example screenshot12](./img/hand_draw_circle2_output.png)

- example3:

![Example screenshot11](./img/hand_draw_circle3.png)

![Example screenshot12](./img/hand_draw_circle3_output.png)



### demo for ellipse
- example1:

![Example screenshot11](./img/hand_draw_ellipse1.png)

![Example screenshot12](./img/hand_draw_ellipse1_output.png)

- example2:

![Example screenshot11](./img/hand_draw_ellipse2.png)

![Example screenshot12](./img/hand_draw_ellipse2_output.png)

- example3:

![Example screenshot11](./img/hand_draw_ellipse3.png)

![Example screenshot12](./img/hand_draw_ellipse3_output.png)



## implement5
### introduce
- find the minimum enclosing circle for the given points.


### demo
- example1:

![Example screenshot11](./img/points1.png)

![Example screenshot12](./img/points1_output.png)

- example2:

![Example screenshot11](./img/points2.png)

![Example screenshot12](./img/points2_output.png)

- example3:

![Example screenshot11](./img/points4.png)

![Example screenshot12](./img/points4_output.png)

- example4:

![Example screenshot11](./img/points5.png)

![Example screenshot12](./img/points5_output.png)
