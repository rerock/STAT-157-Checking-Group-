Group Project goal
--------
Our overall group goal is to check the reproducibility of other groups work on the project. 
- We will be checking other group’s codes, graphs and analysis, make sure it is well documented and reproducible. 
- We will be writing the python code that will pipe together the different R code. 

Our plan is to create an overarching Python code that controls the different blocks of R code and that it can be called just once. 
This will ensure that our project remains centralized. Moreover, this will also decrease the complexity of having different code base 
for different part of the project. 



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
