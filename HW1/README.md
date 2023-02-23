## HW1: &nbsp;*Apriori-algorithm / FP-growth algorithm*
Full report is in the HW1 directory
### Description:<br>
Implement **Apriori-algorithm** and **FP-growth algorithm** , and use IBM Quest Synthetic Data Generator <br>
to generate some datasets to analyze how the support and confidence affect the association of data <br>
selected from the dataset. Furthermore,test and analyze datasets downloaded from Kaggle.
### Arguments setting 
* **--min_sup:** minimum support
* **--min_conf:** minimum confidence
* **--dataset:** Set the dataset you want to import and remember to include the file extension.

### Code Excution 
1. There are three arguments in the args.py file. You can modify the arguments in `args.py`, then enter `python main.py` or `python3 main.py` in the command line to run the program.
2. Alternatively, you can modify the arguments and run the program by directly referencing the parameters. To do so, <br>
enter `python main.py --min_sup --min_conf --dataset` or `python3 main.py --min_sup --min_conf --dataset` in the command line.<br>
* **Example** <br>
`python main.py --min_sup=0.11 --min_conf=0.9 --dataset=kaggle.txt` 

### Structure of the report:<br>
1. Introduction to the programming structure of apriori-algorithm and FP-growth algorithm
2. Explanation of parameters for self-generated datasets using IBM Data Generator.
3. Testing IBM Dataset with Apriori algorithm and FP-growth algorithm.
4. Analyze the results obtained in **four scenarios**:
   * High support, high confidence
   * High support, low confidence
   * Low support, low confidence
   * Low support, high confidence
5. Testing and analysis of Kaggle datasets
6. Difficulties encountered and solutions in completing the assignments.
7. Conclusion

|      Rules         |     Observed       |
| ------------------ | ------------------ |
| **High support, high confidence**  | Strong association is an ideal result, but based on observations from many datasets, it is rare to have such results. Unless the total number of transactions is very small and there are very few types of items, this kind of result may appear. This may be more suitable for small retailers to analyze the goods purchased by customers in a single day.  |
| **High support, low confidence**  | "Items with the high frequency of occurrence may have many subpatterns, leading to lower final confidence and relatively weak correlation between items, resulting in relatively low practicality."  |
| **Low support, low confidence**  | Generated rules may be very numerous, but it is necessary to filter them to find the ones that are more relevant, which have relatively low practicality or even almost none.  |
| **Low support, high confidence**  | Observing the most common results in many datasets, low support, and high confidence is easy to appear when there are many transactions or item types because it will reduce the frequency of item occurrence. However, it is possible to use confidence to filter the more related items, which is relatively practical in reality because most of the data have a larger number of transactions. It is possible to find higher association results with lift analysis.  |

* Besides confidence, the lift is also an important indicator of the strength of the association. The larger the lift, the stronger the association between the items, indicating a higher likelihood of them appearing in the same transaction.

* In my opinion, low support, high confidence is more commonly used, as it is difficult to achieve high support with a sufficient number of transactions or a variety of items sold. Even with low support, by combining confidence and lift, the strength of association between items can still be determined.
