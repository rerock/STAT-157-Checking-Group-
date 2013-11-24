As of 2013-11-23

- [**Group 1 & 3**](http://github.com/aparker92/error_analyzers) *We can't check in yet but their deadline is 11/25*
  - Refactor [Luen's code](https://github.com/aparker92/error_analyzers/blob/master/etas-training.R) to generate an error diagram given a dataset and a model; code includes includig both etas testing and MDA testing codes Luen used for his paper.
  - Their [group task](https://github.com/aparker92/error_analyzers/blob/master/taskfornov21.txt), deadline is 11/25. 

- [**Group 2**](https://github.com/stat157/analyzers) *We can run `aftershock_arrival_plots.ipynb` & `mda_with_curator_data.ipynb` but need to install scipy*
  - Created [aftershock_arrival_plots.py](https://github.com/stat157/analyzers/blob/master/notebooks/aftershock_arrival_plots.py): plot aftershock arrival times, binned by magnitude in the x-axis, time in the Y-axis. 
  - Created [mda_with_curator_data.py](https://github.com/stat157/analyzers/blob/master/notebooks/mda_with_curator_data.py): Iterate upon aftershock-arrival plotting code to take the curators' sample data as input. Try different bin sizes (e.g. binning in magnitude ranges of 0.1, 0.2, 0.5, etc.), try if they can expand on the 2013 catalog to include more years.

- [**Group Q**](https://github.com/SunnySunnia/TheQuakers):   *We have our python code base that can call Quakers' R code on error diagrams, will check whether the python code base can also be called on the [plotting successors.R file](http://github.com/SunnySunnia/TheQuakers/tree/master/Successors).* 

  - Finished their R code on [error diagrams](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/mda_test.r) of testing u from 4.7 to 6 based off [Luen’s code](https://github.com/SunnySunnia/TheQuakers/blob/master/MDA/etas-training.R). 
  - Trying to figure out an algorithm to compare the models, but were not able to vary tao on the x-axis of the error diagram for one specific window function. Waitting for Luen's explanation on his code about how he inplement K as in Ku^M in his code, namely, how did he vary different tao for the error diagram.
  - Currently working on the [optimization approach](https://github.com/SunnySunnia/TheQuakers/tree/master/Successors): simply gather all the times of first successors of earthquakes that are larger that magnitude 3 within an increment of 0.1, then find thier 90 percentile cut points as our window length for earthquakes within that magnitude range. 
  
- [**Group ❤**](https://github.com/annyeongjs/visualheart.task8): *We can't check in yet*
  - Currently [proofreading](https://github.com/annyeongjs/visualheart.task8/blob/master/LuenSummary.md) on Luen, Stark: [Testing Earthquake Predictions](http://projecteuclid.org/DPubS?verb=Display&version=1.0&service=UI&handle=euclid.imsc/1207580090&page=record)
  - Planning to [improve graphs](https://github.com/annyeongjs/visualheart.task8/blob/master/ImprovingGraphs.md)
  
- [**Group #**](https://github.com/ashleysia/TeamHASHTAG): *We can't check in yet*
  - Looking at various D3 visualizations and figuring out what type of interactive plot/graph/visual

- [**Group $**](https://github.com/joyyqchen/EarthquakeProject.Team-Chen.Hsiao.Kirschner.Liou.Tsai): *We can't check in yet*
  - Using D3 for Visuals: Research and learn how to employ D3 to create a dynamic visualization for the data

- [**Group C**](https://github.com/davidwang001/Group-C-Repo): *We can't check in yet*

  - Compliling notes on Luen's dissertation and Chris' HTML presentation.
  - Come up with a comprehensive list of new goals for the class to pursue
