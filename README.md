STAT-157 Checking Group 
========================
 
Members Status: 

| Members          | Emails|
| -------------    |:------:|
| Technical Lead: <a href="https://github.com/tristantao"> Tristan Tao </a> (t-rex) | yuqi.t@berkeley.edu |
| Operational Lead: <a href="https://https://github.com/wliang88"> Wen Liang</a> (wliang88) | wliang88@berkeley.edu |
|                     <a href="https://github.com/kimberlyle"> Kimberly Le</a> (kimberlyle) | kimberly_le@berkeley.edu |
| <a href="https://github.com/arifyali">Arif Ali</a> (arifyali) | arifyali@berkeley.edu |

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
(11-18-19) It is difficult to plan ahead of time our schedule since we just start this group task and many groups have not 
started/finished any of their work. 

Solutions
-----
(11-18-19) We tried to look through the group evaluations and their repos. We found out the Quakers have finished 
their R code on [error diagrams](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/mda_test.r)
of testing u from 4.7 to 6 based off
[Luen’s code](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/etas-training.R). 
Our immediate SMART goal for this 
week is to start attempting to call R from ipynb and to check the reproducibility of the Quaker’s code. 

Group Project Timeline 
===================
November 19
-------
1)	We need to plan our new goals according to the project timeline as we have just formed the group 
after the [data curation](https://github.com/stat157/data-curators/commits/master) process. 
2)	Communicate with analyzer and visualizer groups, check into their repos, 
find out the things they have accomplished and overlook every group’s approximate project timeline and 
plan our goals according to their timeline. 

November 21
---------
1)	Perform code review on any drafts that are completed 
2)	Start attempting to Call to R from ipynb and to check the reproducibility of Quakers'R code on 
[error diagrams](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/mda_test.r)
of testing u from 4.7 to 6 based off
[Luen’s code](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/etas-training.R). 
Our

November 26
--------
1)	Successfully have a python code base that can call other group's R file
2)	Continue code review on 

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

