# Perfecting-Your-Drawing
Many drawing tools, such as iPad, have a function that when you are drawing a shape by hand, they will guess what it is, and make the best fit one to replace it. For example, if you draw a lopsided circle, it will produce a perfect one for it. In this assignment, i do that using the magic from linear algebra.


## Table of Contents
* [implement.py](#implement)
* [implement5.py](#implement5)



## implement
### introduce
- to find best fitting circle:
uses "numpy.linalg.lstsq" to solve the least square problem.

- to find best fitting ellipse:
using least square algorithm ans the formula " c1 x^2 + c2 xy + c3 y^2 + c4 x + c5 y  =  1 ".
The formula can actually fit all kinds of curves from conic section.


### demo for circle
- test1:

![Example screenshot11](./img/case5.png)

![Example screenshot12](./img/case5_output .png)



### demo for ellipse


## implement5
### introduce
- find the minimum enclosing circle for the given points.


### demo
