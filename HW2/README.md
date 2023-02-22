## HW2: &nbsp;*Analyze self-generated data with machine learning models.*

Full report is in the HW1 directory

#### Description:<br>
Analyze the **self-generated data** and **set rules** to classify the data with machine learning models. <br>
Then observe and analyze whether different classifiers can correctly identify the rules for classifying <br>
the data, and whether there are different results when the data contains noise.

#### Structure of the report:<br>
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
  * **Noise data**: Adhesive capsulitis is occasionally misdiagnosed as bursitis or pseudo-adhesive capsulitis (caused by muscle guarding) if the Coracoid process test is not performed. Therefore, when analyzing noise data, there is an 0.08 probability that pseudo-adhesive capsulitis will be diagnosed as adhesive capsulitis, an 0.05 probability that bursitis will be diagnosed as adhesive capsulitis, and a 0.05 probability that adhesive capsulitis will be diagnosed as non-adhesive capsulitis. This simulates a dataset collected with clinical misdiagnosis.
