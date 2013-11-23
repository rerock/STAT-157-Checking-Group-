STAT-157 Checking Group 
========================
 
Members Status: 

| Members          | Emails|
| -------------    |:------:|
| Technical Lead: <a href="https://github.com/tristantao"> Tristan Tao </a> (t-rex) | yuqi.t@berkeley.edu |
| Operational Lead: <a href="https://https://github.com/wliang88"> Wen Liang</a> (wliang88) | wliang88@berkeley.edu |
|                     <a href="https://github.com/kimberlyle"> Kimberly Le</a> (kimberlyle) | kimberly_le@berkeley.edu |
| <a href="https://github.com/arifyali">Arif Ali</a> (arifyali) | arifyali@berkeley.edu |

File Descriptions
--------
main.py is our python code base that can call Quakers' R code on [error diagrams](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/mda_test.r)
of testing u from 4.7 to 6 based off [Luen’s code](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/etas-training.R).

**Step by Step instructions**

*For Mac*

If `x11()` `plot(1,1)` runs in your R studio, then `install.packages("sfsmisc")`, `library("sfsmisc")`
- Download & Install package ["Xquartz"](http://xquartz.macosforge.org/landing/)
- In your terminal `git clone https://github.com/wliang88/STAT-157-Checking-Group-`
- `cd STAT-157-Checking-Group-`
- `export DISPLAY=:0`
- `python main.py`

If `x11()` `plot(1,1)` doesn't runs in your R studio
- Download & Install package ["Xquartz"](http://xquartz.macosforge.org/landing/)
- Open the "Terminal" under "Application" in "Xquartz"
- open up R
- `install.packages("sfsmisc")`
- `library("sfsmisc")`
- exit R
- `git clone https://github.com/wliang88/STAT-157-Checking-Group-`
- `cd STAT-157-Checking-Group-`
- `python main.py`
 

Group Project goal
--------
Our overall group goal is to check the reproducibility of other groups work on the project. 
- We will be checking other group’s codes, graphs and analysis, make sure it is well documented and reproducible. 
- We will be writing the python code that will pipe together the different R code. 

Our plan is to create an overarching Python code that controls the different blocks of R code and that it can be called just once. 
This will ensure that our project remains centralized. Moreover, this will also decrease the complexity of having different code base 
for different part of the project. 


Road Blocks
------
(11-18-13) It is difficult to plan ahead of time our schedule since we just start this group task and many groups have not 
started/finished any of their work. 

(11-21-13) It is difficult to keep in track with every groups process. We went throught group evaluations and repos, but not every group has
done something that we can check in and not everything is planned as scheduled. 

Solutions
-----
(11-18-13) We tried to look through the group evaluations and their repos. We found out the Quakers have finished 
their R code on [error diagrams](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/mda_test.r)
of testing u from 4.7 to 6 based off
[Luen’s code](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/etas-training.R). 
Our immediate SMART goal for this 
week is to start attempting to call R from ipynb and to check the reproducibility of the Quaker’s code.

(11-21-13) Talked with Kristina, hope to have a point of contact from each group. Meantime, we will
  - Check whether we can run `aftershock_arrival_plots.ipynb` & `mda_with_curator_data.ipynb` from the [analyzers group](https://github.com/stat157/analyzers/tree/master/notebooks)
  - Check whether the python code base can also be called on the [plotting successors.R file](http://github.com/SunnySunnia/TheQuakers/tree/master/Successors) from the Quakers. 


Group Project Timeline 
===================
November 19 
-------
- Plan our new goals according to the project timeline as we have just formed the group 
after the [data curation](https://github.com/stat157/data-curators/commits/master) process. 
- Communicate with analyzer and visualizer groups, check into their repos, 
find out the things they have accomplished and overlook every group’s approximate project timeline and 
plan our goals according to their timeline. 

*Completed*

November 21 
---------
- Perform code review on any drafts that are completed 
- Start attempting to Call to R from ipynb and to check the reproducibility of Quakers'R code on 
[error diagrams](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/mda_test.r)
of testing u from 4.7 to 6 based off
[Luen’s code](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/etas-training.R). 

*Completed, please see the file descriptions for main.py. We now have python code base that can call Quakers' R code on [error diagrams](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/mda_test.r)
of testing u from 4.7 to 6 based off [Luen’s code](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/etas-training.R).* 

November 26
--------
- Successfully have a python code base that can call other group's R file
- Continue code review on the groups have finished part of their tasks and re-test our python code base 
  - Check whether we can run `aftershock_arrival_plots.ipynb` & `mda_with_curator_data.ipynb` from the [analyzers group](https://github.com/stat157/analyzers/tree/master/notebooks)
  - Check whether the python code base can also be called on the [plotting successors.R file](http://github.com/SunnySunnia/TheQuakers/tree/master/Successors) from the Quakers. 




November 28
-------
Thanksgiving (Academic Holiday, but group members can continue to check in other groups’ works)

December 3
----------
Think about the architecture of the project: How we can combine/organize everyone's code (from a directory point of view).
Where do we save the data (so that all R code can access them). 

December 5
---------
Have a clean repo, where everyone's R code can live a sub-directory; have data live in a separate direcotry.
We should have a main code file that needs to be called, which will orchestrate the whole process. 

December 10 
-------
Refactor, check for error, clean up

