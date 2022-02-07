# -*- coding: utf-8 -*-
"""「Linear Algebra - hw3」的副本

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pt2-u_ZVZrxDgrmYWsJ0_ypQcb84i9a0
"""

import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
import math
import copy

# Mount your google drive to save your gif result.
from google.colab import drive
drive.mount('/content/drive')

# For question (4)
# you cannot use x to compute the center and the radius inside this function.
def dataSampling(x):
    #for q5
  

  

    pointset=[];

    xa = math.inf
    ya = math.inf

    #掃過 x，找[x,y]最小點 --> [xa,ya]
    for i in x:
      if i[0] < xa:
        xa = i[0]
        ya = i[1]
      elif i[0] == xa:
        if( i[1] < ya ):
          ya = i[1]

    # [xa,ya]加進pointset

    pointset.append([xa,ya])

    Pstart=[xa, ya]
    Pa=[xa, ya]
    xstart=xa
    ystart=ya
    ansx = -1
    ansy = -1
    Array=[]
    xc=-1
    yc=-1
    xb=-1
    yb=-1
    determine = 0
    passflag=0
    timeeeeee=0
    while ansx!=xstart or ansy!=ystart:
      
      
      for i in x:
        
        if(i[0] != xa or i[1] != ya):
          xb = i[0]
          yb = i[1]
          for j in x:
              #passflag=0
              if( (j[0] != xa or j[1] != ya) and (j[0] != xb or j[1] != yb)):
                  passflag=1
                  xc = j[0]
                  yc = j[1]
                  Array = [
                       [xa, xb, xc],
                       [ya, yb, yc],
                       [1, 1, 1]
                  ]
                  determine = xb*yc - xc*yb - xa*yc + ya*xc + xa*yb - xb*ya

                  
                    
                  if determine < 0:
                     #if((xb,yb)==(67,48)):
                      
                    passflag=0
                    break

          if(passflag == 1) :
         
            pointset.append([xb,yb])
            passflag=0
            xa=xb
            ya=yb
            ansx=xb
            ansy=yb
            break




   
    AA=[]
    times=0
    rradius = -math.inf
    p1=[-1,-1]
    p2=[-1,-1]
    p3=[-1,-1]
    mm = len(pointset)
    while( len(pointset)>3 ):
      p1=[-1,-1]
      p2=[-1,-1]
      p3=[-1,-1]
      rradius = -math.inf
      mm = len(pointset)
      for i in range( len(pointset) ):
        
        if(i+2<mm):
          AA = np.array( [  [2*pointset[i][0],2*pointset[i][1],1] ,
                [2*pointset[(i+1)][0],2*pointset[(i+1)][1],1] ,
                [2*pointset[(i+2)][0],2*pointset[(i+2)][1],1]
                ] )
          bb = [
                pointset[i][0]*pointset[i][0] + pointset[i][1]*pointset[i][1],
                pointset[(i+1)][0]*pointset[(i+1)][0] + pointset[(i+1)][1]*pointset[(i+1)][1],
                pointset[(i+2)][0]*pointset[(i+2)][0] + pointset[(i+2)][1]*pointset[(i+2)][1]

          ]
          xx = np.dot( np.linalg.inv( np.dot(AA.transpose(),AA) ), np.dot(AA.transpose(), bb)  )

          if(  math.sqrt( xx[0]*xx[0] + xx[1]*xx[1] + xx[2] ) > rradius   ):
            rradius = math.sqrt( xx[0]*xx[0] + xx[1]*xx[1] + xx[2] )
            p1=pointset[i]
            p2=pointset[(i+1)]
            p3=pointset[(i+2)]


      #case111111111111111--------------
      AA = np.array( [  [2*pointset[mm-2][0],2*pointset[mm-2][1],1] ,
                [2*pointset[(mm-1)][0],2*pointset[mm-1][1],1] ,
                [2*pointset[0][0],2*pointset[0][1],1]
                ] )
      bb = [
                pointset[mm-2][0]*pointset[mm-2][0] + pointset[mm-2][1]*pointset[mm-2][1],
                pointset[mm-1][0]*pointset[mm-1][0] + pointset[mm-1][1]*pointset[(mm-1)][1],
                pointset[0][0]*pointset[0][0] + pointset[(1)][1]*pointset[1][1]

          ]
      [xx, r, rank] = np.linalg.lstsq(AA, bb, rcond=None)[0:3]

      if(  math.sqrt( xx[0]*xx[0] + xx[1]*xx[1] + xx[2] ) > rradius   ):
            rradius = math.sqrt( xx[0]*xx[0] + xx[1]*xx[1] + xx[2] )
            p1=pointset[mm-2]
            p2=pointset[mm-1]
            p3=pointset[0]



      #case2222222222222222------------
      AA = np.array( [  [2*pointset[mm-1][0],2*pointset[mm-1][1],1] ,
                [2*pointset[0][0],2*pointset[(0)][1],1] ,
                [2*pointset[1][0],2*pointset[1][1],1]
                ] )
      bb = [
                pointset[mm-1][0]*pointset[mm-1][0] + pointset[mm-1][1]*pointset[mm-1][1],
                pointset[0][0]*pointset[(0)][0] + pointset[0][1]*pointset[(0)][1],
                pointset[1][0]*pointset[(1)][0] + pointset[1][1]*pointset[(1)][1]

          ]
     
      [xx, r, rank] = np.linalg.lstsq(AA, bb, rcond=None)[0:3]

      if(  math.sqrt( xx[0]*xx[0] + xx[1]*xx[1] + xx[2] ) > rradius   ):
            rradius = math.sqrt( xx[0]*xx[0] + xx[1]*xx[1] + xx[2] )
            p1=pointset[mm-1]
            p2=pointset[0]
            p3=pointset[1]


      #[ p1[0]-p2[0], p1[1]-p2[1] ]   [ p3[0]-p2[0], p3[1]-p2[1] ]   
      if ( (p1[0]-p2[0])*(p3[0]-p2[0]) + (p1[1]-p2[1])*(p3[1]-p2[1]) ) <= 0:
        pointset.remove(p2)
      
      else:
        pointset = [p1,p2,p3]
        break


   
    return pointset

def circle(sp) :
    n=len(sp)
    A = np.zeros((n, 3))
    b = np.zeros((n))
    for i in range(n):
        pt = sp[i]
        A[i, :] = [2.*pt[0], 2.*pt[1], 1]
        b[i] = pt[0]*pt[0]+pt[1]*pt[1]
    return A, b

def draw_circle(x, h, w) :
    center = [x[0], x[1]]
    radius = math.sqrt(x[2]+x[0]*x[0]+x[1]*x[1])

    x_axis = np.linspace(0, w, 700)
    y_axis = np.linspace(0, h, 700)

    a, b = np.meshgrid(x_axis, y_axis)

    C = (a - x[0])*(a - x[0]) + (b - x[1])*(b - x[1]) - radius*radius
    return a, b, C

def ellipse(sp) :
    n=len(sp)
    # TODO: How many variable should use?
    A = np.zeros((n, 5))
    b = np.ones((n))
    for i in range(n):
        pt = sp[i]
        x = pt[0]
        y = pt[1]
        # TODO: ellipse formula here.
        A[i, :] = [ x*x, x*y, y*y, x, y]
        b[i] = 1
   

    return A, b

def draw_ellipse(x, h, w) :
    # plot the drawing and the fitted circle
    x_axis = np.linspace(0, w, 700)
    y_axis = np.linspace(0, h, 700)

    a, b = np.meshgrid(x_axis, y_axis)

    # TODO: ellipse formula here.
    C=x[0]*a*a+x[1]*a*b+x[2]*b*b+x[3]*a+x[4]*b-1 
    

    return a, b, C

"""# DO NOT MODIFY THE JUDGE CODE!!!"""

def judge_overlapping(points) :
    # calculate all sample point circle.
    A, b = circle(points)
    sol1 = np.linalg.lstsq(A, b, rcond=None)[0]
    x1 = sol1[0]
    y1 = sol1[1]
    r1 = math.sqrt(sol1[2]+x1**2+y1**2)

    sp = dataSampling(points)
    A, b = circle(sp)
    sol2 = np.linalg.lstsq(A, b, rcond=None)[0]
    x2 = sol2[0]
    y2 = sol2[1]
    r2 = math.sqrt(sol2[2]+x2**2+y2**2)

    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if r1+r2 <= d :
        # 1 point or no point
        return 0
    elif min(r1, r2) + d <= max(r1, r2) :
        # inner circle
        return (min(r1, r2)**2) / (max(r1, r2)**2)
   
    alpha = math.acos((r1**2 + d**2 - r2**2) / (2 * r1 * d))
    beta = math.acos((r2**2 + d**2 - r1**2) / (2 * r2 * d))

    overlapping = alpha * (r1**2) + beta * (r2**2) - (r1**2) * math.cos(alpha) * math.sin(alpha) - (r2**2) * math.cos(beta) * math.sin(beta)

    return overlapping / (max(r1**2, r2**2) * np.pi)

def judge_sampling(points) :
    old_points = list(points)
    all_point = len(points)
    sp = dataSampling(points)
    sp_len = 0
    for p in sp :
        for ss in old_points :
            if ss[0] == p[0] and ss[1] == p[1] :
                sp_len += 1
    
    if (old_points != points) :
        return 0

    return (all_point - sp_len) / all_point


def judge(points) :
    sample = judge_sampling(points)
    overlap = judge_overlapping(points)

    print("The score of this question is : ")
    print("20 * (0.3 * ? (Efficiency, need your report) + 0.3 * {:f} (correctness) + 0.4 * {:f} (sampling) ) =  ? + {:f}".format(overlap, sample, 20 * (0.3 * overlap + 0.4 * sample)))

from numpy.core.multiarray import dot
from numpy.core.fromnumeric import transpose
def main(file, mode="circle") :
    # read image and get circle points
    #im1 = img.imread('puddle.png')
    im1 = img.imread(file)
    [h, w, c] = np.array(im1).shape
    points = [];
    for i in range(h):
        for j in range(w):
            if (all(im1[i,j,:])==0):
                points.append([i, j])


    # sampling data
    sp = dataSampling(points)

    if mode == "circle":
        # create matrix for fitting
        
        A, b = circle(sp)

        # solve the least square problem
        #TA gived  (compare)
        [x, r, rank] = np.linalg.lstsq(A, b, rcond=None)[0:3]
        #print('rank:',rank)
        #x = np.dot( np.linalg.inv( np.dot(A.transpose(),A) ), np.dot(A.transpose(), b)  )

        a, b, C = draw_circle(x, h, w)


        

    elif mode == "ellipse":
        # create matrix for fitting
        A, b = ellipse(points)

        # solve the least square problem
        [x, r, rank] = np.linalg.lstsq(A, b, rcond=None)[0:3]

        a, b, C = draw_ellipse(x, h, w)

    figure, axes = plt.subplots(1)
    plt.imshow(im1) 
    axes.contour(b, a, C, [0])
    axes.set_aspect(1)
    plt.savefig(file+'.output.png')
    plt.show()
    points = [];
    for i in range(h):
        for j in range(w):
            if (all(im1[i,j,:])==0):
                points.append([i, j])
    judge(points)
    print("="*50)

files = ['case1.png', 'case2.png', 'case3.png']
#for f in files :
#    main('/content/drive/My Drive/' + f, mode="circle")
#    main('/content/drive/My Drive/' + f, mode="ellipse")
#main('/content/drive/My Drive/line.png', mode="circle")
#main('/content/drive/My Drive/case1.png', mode="circle")
#main('/content/drive/My Drive/case2.png', mode="circle")
#main('/content/drive/My Drive/case3.png', mode="circle")
#main('/content/drive/My Drive/case4.png', mode="circle")
#main('/content/drive/My Drive/case5.png', mode="circle")

#main('/content/drive/My Drive/circle.png', mode="circle")
#main('/content/drive/My Drive/puddle.png', mode="circle")

#main('/content/drive/My Drive/hand_draw_circle1.png', mode="circle")
#main('/content/drive/My Drive/hand_draw_circle2.png', mode="circle")
#main('/content/drive/My Drive/hand_draw_circle3.png', mode="circle")
main('/content/drive/My Drive/points4.png', mode="circle")
main('/content/drive/My Drive/points2.png', mode="circle")
main('/content/drive/My Drive/points.png', mode="circle")
main('/content/drive/My Drive/pointt.png', mode="circle")
#main('/content/drive/My Drive/hand_draw_ellipse1.png', mode="ellipse")
#main('/content/drive/My Drive/hand_draw_ellipse2.png', mode="ellipse")
#main('/content/drive/My Drive/hand_draw_ellipse3.png', mode="ellipse")