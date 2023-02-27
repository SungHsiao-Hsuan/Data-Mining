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
   2. You can modify `--ibm_dataset` parameter in `args.py` to input IBM data file then enter `python preprocessor.py` or `python3 preprocessor.py` in command line to run the program.
   
<br> 

`draw_graph.py` <br>

You can run `draw_graph.py` to to visualize what the `graph.txt` looks like. <br>
The graph you want to visualize is determined by the title argument in args.py.

### Structure of the report:<br>
 1. **Find a way**: Find a way to increase the authority, hub, PageRank, and SimRank of vertex 1 by adding or deleting nodes or edges.
 2. **Algorithm description**
 3. **Result analysis and discussion**
 4. **Effectiveness analysis**
 5. **Conclusion**
 
 
 * Find a way <br>
 To increase the authority, hub, and PageRank values of vertex 1, you can increase the number of its children nodes or parent nodes.<br>
 Deleting the edges that are not related to vertex 1 is also possible.

* Effectiveness analysis <br>
  * Execution time of three algorithms
 
 ![image](https://github.com/SungHsiao-Hsuan/Data-Mining/blob/main/HW3/README_picture/Time%20analysis%20of%20three%20algorithms.png) 
 
 
  * **Analysis:** <br>
 
    Based on the recorded time, it is evident that the program's execution time increases progressively from graph 1 to graph 6. <br>
    This is likely due to the larger number of edges or vertices in graph 5 and graph 6, which require more time for processing. <br>
    For further analysis, we will fix the number of vertices and edges.<br>
   
   
   `When the number of edges = 1000` <br> 
   
   ![image](https://github.com/SungHsiao-Hsuan/Data-Mining/blob/main/HW3/README_picture/edge%20%3D%201000.png) 
   
   `When the number of vertices = 100` <br> 

  ![image](https://github.com/SungHsiao-Hsuan/Data-Mining/blob/main/HW3/README_picture/vertex%20%3D%20100.png)

   The experimental results show that the execution time of all three algorithms increases as the number of vertices or edges increases, <br>
   regardless of whether the number of edges or vertices is fixed. Among the graphs graph1-6 and IBM5000, graph6 is the most complex with <br>
   the largest number of vertices and edges, which leads to the longest execution time.<br>
   
  **Analysis of three algorithms** <br>
  From the above table, it can be seen that the execution times of the three algorithms are in the following order: SimRank > HITS > PageRank. <br>
  The reason for this is that SimRank requires comparing the similarity of all the parents of a vertex, which can be very computationally intensive <br>
  since a vertex may have many parents. In addition, the algorithm also needs to calculate the similarity of each vertex with all other vertices. <br>
  Therefore, the execution time required for SimRank is the longest.<br>

  The second time-consuming algorithm is HITS, which is likely since it not only calculates the authority value of each vertex but also needs to <br>
  calculate the hub value. On the other hand, PageRank only needs to calculate the score of each parent and then divide it by the number of its children. 
