## **HW3:** &nbsp; *Implement HIS, PageRank, SimRank* <br>
Full report is in the HW3 directory

### Description:<br>
Implement **HITS**, **PageRank**, and **SimRank algorithms**, and calculate the **authority**, **hubs**, **Pagerank**, <br>
and **Simrank values** of each vertex in the graph to find out the important vertices and discover <br>
the characteristics of each algorithm.

### Arguments setting
##### Input file: <br>
* **--dataset:** Set the dataset you want to import and remember to include the file extension.
* **--ibm_dataset:** Convert the input IBM data generated from IBM Quest Synthetic Data Generator to the graph.txt format.
##### Output file <br>

* **--authority:** Name of authority output file.
* **--hub:** Name of authority output file.
* **--PageRank:** Name of PageRank output file.
* **--SimRank:** Name of SimRank output file.

### Code Excution 
 `main.py`

1. There are six arguments in the `args.py` file. You can modify the arguments in `args.py`, then enter `python main.py` or `python3 main.py` in the command line to run the program.<br>

      **Quickly modify**

      In `args.py`, there is a parameter called `title`.You can quickly complete the setting by modifying `title`.

2. Alternatively, you can modify the arguments and run the program by directly referencing the parameters. To do so, <br>
enter `python main.py --dataset --authority --hub --PageRank --SimRank --ibm_dataset ` or  <br>
`python3 main.py --dataset --authority --hub --PageRank --SimRank --ibm_dataset` in the command line.<br>

* **Example** <br>
`python main.py --dataset=graph.txt --authority=graph.txt --hub=graph.txt --PageRank=graph.txt --SimRank=graph.txt --ibm_dataset=ibm-5000.txt `

<br>

`preprocessor.py`<br>

   1. `preprocessor.py` is an IBM data converter that converts IBM data to the format of `graph.txt`
   2. You can modify --ibm_dataset parameter in args.py to input IBM data file then enter `python preprocessor.py` or `python3 preprocessor.py` in command line to run the program.
   
<br> 

`draw_graph.py` <br>

You can run `draw_graph.py` to to visualize what the `graph.txt` looks like. <br>
The graph you want to visualize is determined by the title argument in args.py.
