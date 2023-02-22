from Shoulder_Patient import Shoulder_Patient
from Shoulder_Patient import AC_patient
import numpy as np
import random

class Patient_Generator():
    def __init__(self):
        return

    def Generate_patients(self,number):

        shoulder_patients = []
        AC_count = 0
        flag = 0
        total_AC_count = 0
        AC_patient_pointer = 0
        ACP_max_pointer = 0
        pointer = 0

        for i in range(1,number+1):
            # print(flag)

            if flag == 0:

                patient = Shoulder_Patient()
                Shoulder_Patient.is_Adhesive_capsulitis(patient)
                if patient.label == 1:
                    AC_count += 1
                    total_AC_count += 1

                shoulder_patients.append(patient)
                pointer += 1

                if pointer % 97 == 0:

                    if AC_count < 3:
                        flag = 1
                        ACP_max_pointer = random.randint(2,4)

                    else :
                        AC_count = 0


            else:

                AC_count = 0
                if AC_patient_pointer < ACP_max_pointer:

                    patient = AC_patient()
                    total_AC_count += 1
                    shoulder_patients.append(patient)
                    AC_patient_pointer += 1

                else:

                    patient = AC_patient()
                    total_AC_count += 1
                    shoulder_patients.append(patient)

                    AC_patient_pointer = 0
                    flag = 0
                    pointer = 0


        print(f"Total AC count: {total_AC_count}")
        return shoulder_patients


    def Generate_datasets(self,number):
        shoulder_patients = self.Generate_patients(number)
        X = np.array([patient.to_list() for patient in shoulder_patients])
        y = np.array([patient.label for patient in shoulder_patients])

        return X,y


class Noise_Patient_Generator():
    def __init__(self):
        return

    def Generate_patients(self,number):

        shoulder_patients = []
        AC_count = 0
        flag = 0
        total_AC_count = 0
        AC_patient_pointer = 0
        ACP_max_pointer = 0
        pointer = 0

        for i in range(1,number+1):
            # print(flag)

            if flag == 0:

                patient = Shoulder_Patient()
                Shoulder_Patient.is_Adhesive_capsulitis(patient)

                # generate random noise
                random_noise_dice = random.random()
                bursitis_dice = random.random()


                if random_noise_dice < 0.08:
                    Shoulder_Patient.generate_noise(patient)
                    # print(patient.label)


                if bursitis_dice < 0.05:
                    Shoulder_Patient.shoulder_bursitis(patient)
                    # print(patient.label)

                if patient.label == 1:
                    AC_count += 1
                    total_AC_count += 1

                shoulder_patients.append(patient)
                pointer += 1

                if pointer % 97 == 0:

                    if AC_count < 3:
                        flag = 1
                        ACP_max_pointer = random.randint(2,4)

                    else :
                        AC_count = 0


            else:

                AC_count = 0

                if AC_patient_pointer < ACP_max_pointer:

                    patient = AC_patient()

                    # generate random noise
                    random_noise_dice = random.random()

                    if random_noise_dice < 0.05:
                        patient.label = 0

                    if patient.label == 1:
                        AC_count += 1
                        total_AC_count += 1
                        AC_patient_pointer += 1

                    shoulder_patients.append(patient)


                else:

                    patient = AC_patient()

                    # generate random noise
                    random_noise_dice = random.random()
                    if random_noise_dice < 0.05:
                        patient.label = 0

                    if patient.label == 1:
                        total_AC_count += 1

                    shoulder_patients.append(patient)

                    AC_patient_pointer = 0
                    flag = 0
                    pointer = 0


        print(f"Total AC count: {total_AC_count}")
        return shoulder_patients


    def Generate_datasets(self,number):
        shoulder_patients = self.Generate_patients(number)
        X = np.array([patient.to_list() for patient in shoulder_patients])
        y = np.array([patient.label for patient in shoulder_patients])

        return X,y

