from Patient_Generator import Patient_Generator
from Patient_Generator import Noise_Patient_Generator
from Patient_Generator import brusitis_patient_generator
import Shoulder_Patient
import numpy as np

import utils
import config
import args


# import decision tree related packages
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,mean_absolute_error
from sklearn.tree import export_graphviz

# import svm
from sklearn.svm import SVC

# import KNN
from sklearn.neighbors import KNeighborsClassifier

# import for Heatmap of confusion matrix
import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

# import for ROC curve
from sklearn.metrics import RocCurveDisplay



def main(input_name,dot_file_name):

    class_names = ['not_AC', 'AC']

    # Read dataset
    input_data = utils.read_file(config.IN_DIR / input_name)

    patient_data = []
    target = input_data[-1]

    for i in range(len(input_data)-1):
        patient_data.append(input_data[i])


    # Split training data and testing data
    training_data,testing_data,training_target,testing_target =train_test_split(patient_data,target,test_size = 0.2)

    #Build decision tree model
    decision_tree_model = tree.DecisionTreeClassifier().fit(training_data,training_target)
    max_depth_decision_tree_model = tree.DecisionTreeClassifier(max_depth=6).fit(training_data,training_target)
    y_predict = decision_tree_model.predict(testing_data)
    y_predict_max_depth = max_depth_decision_tree_model.predict(testing_data)

    decision_tree_score = round(accuracy_score(testing_target,y_predict),3)
    decision_tree_max_depth_score = round(accuracy_score(testing_target,y_predict_max_depth),3)

    print(f"Accuracy of decision tree: {decision_tree_score}")
    print(f"Accuracy of decision tree with depth: {decision_tree_max_depth_score}")


    # Build svm model
    svm = SVC(kernel='linear', max_iter = 1000,probability=True)
    svm.fit(training_data,training_target)
    svm_predict = svm.predict(testing_data)
    svm_score = round(accuracy_score(testing_target,svm_predict),3)

    print(f"Accuracy of svm: {svm_score}")


    # Find k
    knn_err = []
    knn_n_neighbor = [i for i in range(1,21)]
    max_accuracy_knn = 0

    for i in range(1,21):

        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(training_data,training_target)
        knn_predict = knn.predict(testing_data)
        knn_score = accuracy_score(testing_target,knn_predict)
        # print(knn_score)

        mae = mean_absolute_error(testing_target, knn_predict)
        # print(mae)
        knn_err.append(mae)

    max_accuracy_knn = find_min_value_index(knn_err) + 1


    # Build knn model
    knn = KNeighborsClassifier(n_neighbors=max_accuracy_knn)
    knn.fit(training_data,training_target)
    knn_predict = knn.predict(testing_data)
    knn_score = round(accuracy_score(testing_target,knn_predict),3)

    print(f"Accuracy of KNN: {knn_score}")


    # Generate confusion matrix
    sns.set()
    dt = confusion_matrix(y_true=testing_target,y_pred=y_predict)
    dt_max_depth = confusion_matrix(y_true=testing_target,y_pred=y_predict_max_depth)
    svm_confusion_matrix = confusion_matrix(y_true=testing_target,y_pred=svm_predict)
    knn_confusion_matrix = confusion_matrix(y_true=testing_target,y_pred=knn_predict)

    print(f"Confusion matrix of decision tree: {dt}")
    print(f"Confusion matrix of decision tree with max depth: {dt_max_depth}")
    print(f"Confusion matrix of SVM: {svm_confusion_matrix}")
    print(f"Confusion matrix of KNN: {knn_confusion_matrix}")

    # Heapmap of Decision tree classfier
    sns_labels = build_heatmap_notation(dt)


    # Heapmap of Decision tree classfier with max depth
    sns_labels_max_depth = build_heatmap_notation(dt_max_depth)

    # Heatmap of SVM
    sns_labels_svm = build_heatmap_notation(svm_confusion_matrix)

    #Heatmap of KNN
    sns_labels_knn = build_heatmap_notation(knn_confusion_matrix)

    # Display heatmap of confusion matrix
    fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2,2)
    sns.heatmap(dt,annot=sns_labels,cmap='Blues',fmt='',ax=ax1)
    sns.heatmap(dt_max_depth,annot=sns_labels_max_depth,cmap='Blues',fmt='',ax=ax2)
    sns.heatmap(svm_confusion_matrix,annot=sns_labels_svm,cmap='Blues',fmt='',ax=ax3)
    sns.heatmap(knn_confusion_matrix,annot=sns_labels_knn,cmap='Blues',fmt='',ax=ax4)

    ax1.set_title('Decision Tree without max depth')
    ax2.set_title('Decision Tree with max depth')
    ax3.set_title('SVM')
    ax4.set_title('KNN')
    plt.savefig('model.png')

    # Display ROC curve of classfiers
    plt.figure()
    ax5 = plt.gca()
    dt_roc = RocCurveDisplay.from_estimator(decision_tree_model,testing_data,testing_target,ax=ax5,name="Decision Tree without max depth")
    dt_max_depth_roc = RocCurveDisplay.from_estimator(max_depth_decision_tree_model,testing_data,testing_target,ax=ax5,name= "Decision Tree with max depth")
    svm_roc = RocCurveDisplay.from_estimator(svm,testing_data,testing_target,ax=ax5,name='SVM')
    knn_roc = RocCurveDisplay.from_estimator(knn,testing_data,testing_target,ax=ax5,name='KNN')
    ax5.set_title('ROC curve')
    plt.savefig('ROC.png')

    # Plot KNN error rate
    plt.figure()
    plt.plot(knn_n_neighbor,knn_err)
    plt.savefig('find_k.png')
    plt.title('error rate of knn')

    # Output decision tree figures
    with open(f"{dot_file_name}.dot", 'w') as f:
        f = export_graphviz(decision_tree_model, out_file=f,feature_names=Shoulder_Patient.Features,class_names= class_names,rounded=True, filled=True)

    with open(f"{dot_file_name}_maxdepth.dot", 'w') as f:
        f = export_graphviz(max_depth_decision_tree_model, out_file=f,feature_names=Shoulder_Patient.Features,class_names= class_names,rounded=True, filled=True)

    plt.show()


# Generate Dataset
def Dataset_generator(sample_number,gendata_name):

    PG = Patient_Generator()
    patient_data, target = PG.Generate_datasets(sample_number)

    generated_data = list(patient_data.copy())
    generated_data.append(target)

    utils.write_file(
        data= generated_data,
        filename= config.IN_DIR / gendata_name
    )


def Noise_Dataset_generator(sample_number,gendata_name):

    NPG = Noise_Patient_Generator()
    patient_data, target = NPG.Generate_datasets(sample_number)

    generated_data = list(patient_data.copy())
    generated_data.append(target)

    utils.write_file(
        data= generated_data,
        filename= config.IN_DIR / gendata_name
    )


# Find index of min value
def find_min_value_index(input_list):
    return input_list.index(min(input_list))


# Print predict failure data
def print_and_count_diff(data,target,predict_target):

    count = 0

    for i in range(len(target)):
        if target[i] != predict_target[i]:
            print("==========Predict failure Data==========")
            print(data[i])
            count += 1

    print(f"Total predict failed: {count}")


def build_heatmap_notation(confusion_matrix):
    group_names = ['True Neg','False Pos','False Neg','True Pos']
    group_count = ["{0:0.0f}".format(value) for value in confusion_matrix.flatten()]
    group_percentage = ["{0:.2%}".format(value) for value in confusion_matrix.flatten()/np.sum(confusion_matrix)]
    sns_labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(group_names,group_count,group_percentage)]

    sns_labels = np.asarray(sns_labels).reshape(2,2)

    return sns_labels

"""
若要產生Data再將Dataset_generator(sample_number,a.gendata)的function uncomment ，並設定sample數量即可產生 dataset
"""

if __name__ == "__main__":

    a = args.parse_args()
    sample_number = 1000
    Dataset_generator(sample_number,a.gendata)
    # Noise_Dataset_generator(sample_number,a.gendata)

    main(a.dataset,a.dot_name)
