## HW2: &nbsp;*Analyze self-generated data with machine learning models.*

Full report is in the HW2 directory

### Description:<br>
Analyze the **self-generated data** and **set rules** to classify the data with machine learning models. <br>
Then observe and analyze whether different classifiers can correctly identify the rules for classifying <br>
the data, and whether there are different results when the data contains noise.

### Arguments setting
* **--gen_data:** Name of the generated dataset, and the generated data will be stored in the input file.
* **--dataset:** Set the dataset you want to import and remember to include the file extension.
* **--dot_name:** Name of the .dot file for the decision tree, `DO NOT` add file extension in this augument because <br>
* the file extension has been pre-defined in the program. 

### Code Excution 
1. There are three arguments in the `args.py` file. You can modify the arguments in `args.py`, then enter `python main.py` or `python3 main.py` in the command line to run the program.
2. Alternatively, you can modify the arguments and run the program by directly referencing the parameters. To do so, <br>
enter `python main.py --gen_data --dataset --dot_name` or `python3 main.py --gen_data --dataset --dot_name` in the command line.<br>
* **Example** <br>
`python main.py --gen_data=data2.csv --dataset=data2.csv --dot_name=data2` 

### Structure of the report:<br>
1. Topic setting & Data design
2. Features list
3. Absolutely right rules setting
4. Data analysis with decision tree model
5. Data analysis with SVM model
6. Data analysis with KNN model

* **Topic setting** <br>
Evaluate whether patients over 40 years old with acute shoulder disorders also have early-stage adhesive capsulitis.
* **Data design** <br>
Due to the high incidence of Adhesive Capsulitis (AC) in patients over 40 years old, this study will evaluate <br>
whether patients with acute shoulder disorder also have early AC. Therefore, data will be limited to patients over 40 <br>
years old. The data will be subject to the following constraints to better reflect real-world conditions.
  * A. The patient's ROM is usually affected and is generally decreased by 5 degrees compared to the general population if the patient has diabetes. (Tiffany K. Gill, 2022) 
  * B. AROM<= PROM (AROM may be affected by factors such as muscle strength, whether the shoulder is injured, or whether the nearby muscles are tight. AROM is set to have a 20% chance of being less than PROM and an 80% chance of being equal to PROM. Generally, AROM = PROM for the general population.) 
  * C. If Active Flexion ROM is less than 90 degrees, the Empty Can Test cannot be performed. At this time, the Empty Can Test will be marked as -1 to indicate that it cannot be tested. 
  * D. The incidence of adhesive capsulitis in clinical settings is approximately 3-5%. In order to make the generated dataset closer to clinical data, the incidence of adhesive capsulitis patients will also be controlled within 3-5%. 
  * **Noise data**: <br>
  Adhesive capsulitis is occasionally misdiagnosed as bursitis or pseudo-adhesive capsulitis (caused by muscle guarding) if the Coracoid process test is not performed. Therefore, when analyzing noise data, there is an 0.08 probability that pseudo-adhesive capsulitis will be diagnosed as adhesive capsulitis, an 0.05 probability that bursitis will be diagnosed as adhesive capsulitis, and a 0.05 probability that adhesive capsulitis will be diagnosed as non-adhesive capsulitis. This simulates a dataset collected with clinical misdiagnosis.

* **Absolutely right rules setting** <br>
 1. Passive external rotation < 40°
 2. Passive abduction or Passive flexion < 125°
 3. Coracoid process test is positive
 4. Pain in your shoulder even though smallest movement
 5. Normal on X-rays

   **To be classified as a patient with Adhesive Capsulitis, one must meet all five of the above conditions.**

* **Conclusion** <br>
Among the three models, decision tree appears to be the best choice as an auxiliary diagnostic tool for adhesive capsulitis in clinical practice. Even with the addition of noise, the AUC is still above 0.8. If an additional model is needed, the combination of KNN and decision tree would be a better choice, but if a patient is classified as negative, the decision tree's judgment should be given more weight to reduce the risk of false negatives. <br>
In this experiment, we simulated the physical examination that may be performed for adhesive capsulitis in clinical practice. AROM and PROM will have a highly correlated relationship, so the decision tree's use of AROM as a feature is relatively acceptable. However, the decision tree model still accurately identified the other important physical examination features with PROM as the main feature. This is actually reasonable because many diagnoses in physical examination are based on if a certain condition is met, followed by testing another condition to gradually approach the suspected disease, which is very similar to the core concept of decision tree. Therefore, it is not surprising that the decision tree is the best-performing model. However, when noise is increased, the decision tree is highly sensitive to noise, and too many misdiagnosed data or erroneous labels can destroy the entire tree. Therefore, the misdiagnosed data cannot be too many, or the overall sample size must be large enough to dilute the impact of erroneous labels.
