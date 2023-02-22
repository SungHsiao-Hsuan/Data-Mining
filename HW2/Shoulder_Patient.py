import random
import scipy.stats as stats
import numpy as np

Features = ['Age','Gender','Height','Weight','BMI','Diabetes','PFROM','PEROM','PABDROM','PERROM','PIRROM','Xray','CPT','PAT','Trauma',
            'DS','UAP','PSM','ECT','AFROM','AEROM','AABDROM','AERROM','AIRROM']

class Shoulder_Patient():

    def __init__(self):

        # Base info
        self.age = random.randint(40,80)
        self.gender = random.randint(0,1)

        if self.gender == 0:
            self.height = round(np.random.normal(173,10.09),2)
            self.weight = round(np.random.normal(75,15.46),2)
        else:
            self.height = round(np.random.normal(160,11.19),2)
            self.weight = round(np.random.normal(60.9,11.36),2)

        self.BMI = round(self.weight / (self.height/100 * self.height/100),2)

        # Underlying disease
        self.diabetes = random.randint(0,1)

        # Random generate Shoulder PROM
        ## 有糖尿病會影響PROM的角度 (Tiffany K. Gill,2022)

        if self.diabetes == 1:

            # PFROM = Passive Flexion ROM
            self.PFROM = round(((stats.truncnorm((0-160.3)/17.2,(180-160.3)/17.2,loc = 160.3,scale = 17.2)).rvs(1)-5)[0],2)
            if self.PFROM < 0:
                self.PFROM = 0

            # PEROM = Passive Extension ROM
            self.PEROM = round(((stats.truncnorm((0-43)/12,(50-43)/12,loc = 43,scale = 12)).rvs(1)-5)[0],2)
            if self.PEROM < 0:
                self.PEROM = 0

            # PABDROM = Passive Abduction ROM
            self.PABDROM = round(((stats.truncnorm((0-151)/18.5,(180-151)/18.5,loc = 151,scale = 18.5)).rvs(1)-5)[0],2)
            if self.PABDROM < 0:
                self.PABDROM = 0

            # PERROM = Passive External Rotation ROM
            self.PERROM = round((stats.truncnorm((0-59)/17,(90-59)/17,loc = 59,scale = 17).rvs(1) -5)[0],2)
            if self.PERROM < 0:
                self.PERROM = 0

            # PIRROM = Passive Internal Rotation ROM
            self.PIRROM = round(((stats.truncnorm((0-63)/14,(70-63)/14,loc = 63,scale = 14)).rvs(1)-5)[0],2)
            if self.PIRROM < 0:
                self.PIRROM = 0

        else:
            self.PFROM = round(((stats.truncnorm((0-160.3)/17.2,(180-160.3)/17.2,loc = 160.3,scale = 17.2)).rvs(1))[0],2)
            self.PEROM = round(((stats.truncnorm((0-43)/12,(50-43)/12,loc = 43,scale = 12)).rvs(1))[0],2)
            self.PABDROM = round(((stats.truncnorm((0-151)/18.5,(180-151)/18.5,loc = 151,scale = 18.5)).rvs(1))[0],2)
            self.PERROM = round(((stats.truncnorm((0-59)/17,(90-59)/17,loc = 59,scale = 17)).rvs(1))[0],2)
            self.PIRROM = round(((stats.truncnorm((0-63)/14,(70-63)/14,loc = 63,scale = 14)).rvs(1))[0],2)


        # Test and other symptoms
        self.Xray = random.randint(0,1)
        self.Coracoid_Pain_Test = random.randint(0,1)
        self.Painful_arc_test = random.randint(0,1)
        self.shoulder_trauma = random.randint(0,1)
        self.difficult_sleep = random.randint(0,1)
        self.upper_arm_pain = random.randint(0,1)
        self.pain_small_mov = random.randint(0,1)

        # Random generate Shoulder AROM
        ## AROM = Active ROM
        ### AROM 可能因受傷、肌肉緊繃等因素影響，故讓三成的隨機程度的讓AROM != PROM (通常健康的人AROM = PROM)

        self.is_AROM_normal = random.random()

        if self.is_AROM_normal > 0.2:
            self.AFROM = self.PFROM
            self.AEROM = self.PEROM
            self.AABDROM = self.PABDROM
            self.AERROM = self.PERROM
            self.AIRROM = self.PIRROM

        else:
            self.AFROM = round(self.PFROM * random.uniform(0.75,0.95),2)
            self.AEROM = round(self.PEROM * random.uniform(0.75,0.95),2)
            self.AABDROM = round(self.PABDROM * random.uniform(0.75,0.95),2)
            self.AERROM = round(self.PERROM * random.uniform(0.75,0.95),2)
            self.AIRROM = round(self.PIRROM * random.uniform(0.75,0.95),2)

        # AFROM < 90 無法正確執行Empty can test 故設定為-1
        if self.AFROM < 90:
            self.Empty_can_test = -1
        else:
            self.Empty_can_test = random.randint(0,1)


        # Label for whether the patiten has Adhesive capsulitis
        self.label = 0


    # Absolute Rule of Adhesive capsulitis
    def is_Adhesive_capsulitis(self):
        if self.PERROM < 40:
            if ((self.PABDROM <125) or (self.PFROM < 125)) and self.Coracoid_Pain_Test == 1 and self.Xray == 1 and self.pain_small_mov == 1:
                self.label = 1

        else:
             self.label = 0

    # 有一定機率被診斷為假性五十肩
    def generate_noise(self):
        if self.Coracoid_Pain_Test == 0:
            self.label = 1

    def shoulder_bursitis(self):
        if self.PERROM >= 40:
            if self.PABDROM >=125 and self.PFROM >= 125 and self.Xray == 1 and self.pain_small_mov == 1 and self.Coracoid_Pain_Test == 0 and self.AFROM < 150 and self.AABDROM  < 150:
                self.label = 1


    # Patient Attribut to list
    def to_list(self):

        parameter_list = [self.age,self.gender,self.height,self.weight,self.BMI,self.diabetes,self.PFROM,self.PEROM,self.PABDROM,self.PERROM,
                            self.PIRROM,self.Xray,self.Coracoid_Pain_Test,self.Painful_arc_test,self.shoulder_trauma,self.difficult_sleep,
                            self.upper_arm_pain,self.pain_small_mov,self.Empty_can_test,self.AFROM,self.AEROM,self.AABDROM,self.AERROM,self.AIRROM]

        return parameter_list


class AC_patient():

    def __init__(self):

        # Base info
        self.age = random.randint(40,80)
        self.gender = random.randint(0,1)

        if self.gender == 0:
            self.height = round(np.random.normal(173,10.09),2)
            self.weight = round(np.random.normal(75,15.46),2)
        else:
            self.height = round(np.random.normal(160,11.19),2)
            self.weight = round(np.random.normal(60.9,11.36),2)

        self.BMI = round(self.weight / (self.height/100 * self.height/100),2)

        # Underlying disease
        self.diabetes = random.randint(0,1)

        # Random generate Shoulder PROM
        ## 多設定條件讓條件可以接近原本五十肩病人可能產生的狀況
        random_dice = random.randint(0,2)

        if random_dice == 0:
            self.PFROM = round(((stats.truncnorm((0-110)/17.2,(125-110)/17.2,loc = 110,scale = 17.2)).rvs(1))[0],2)
            self.PEROM = round(((stats.truncnorm((0-43)/12,(50-43)/12,loc = 43,scale = 12)).rvs(1))[0],2)
            self.PABDROM = round(((stats.truncnorm((0-151)/18.5,(180-151)/18.5,loc = 151,scale = 18.5)).rvs(1))[0],2)

        elif random_dice == 1:
            self.PFROM = round(((stats.truncnorm((0-160.3)/17.2,(180-160.3)/17.2,loc = 160.3,scale = 17.2)).rvs(1))[0],2)
            self.PEROM = round(((stats.truncnorm((0-43)/12,(50-43)/12,loc = 43,scale = 12)).rvs(1))[0],2)
            self.PABDROM = round(((stats.truncnorm((0-100)/18.5,(125-100)/18.5,loc = 100,scale = 18.5)).rvs(1))[0],2)

        else:
            self.PFROM = round(((stats.truncnorm((0-110)/17.2,(125-110)/17.2,loc = 110,scale = 17.2)).rvs(1))[0],2)
            self.PEROM = round(((stats.truncnorm((0-43)/12,(50-43)/12,loc = 43,scale = 12)).rvs(1))[0],2)
            self.PABDROM = round(((stats.truncnorm((0-100)/18.5,(125-100)/18.5,loc = 100,scale = 18.5)).rvs(1))[0],2)


        self.PERROM = round(((stats.truncnorm((0-27)/17,(40-27)/17,loc = 27,scale = 17)).rvs(1))[0],2)
        self.PIRROM = round(((stats.truncnorm((0-63)/14,(70-63)/14,loc = 63,scale = 14)).rvs(1))[0],2)


        # Test and other symptoms
        self.Xray = 1
        self.Coracoid_Pain_Test = 1
        self.Painful_arc_test = random.randint(0,1)
        self.shoulder_trauma = random.randint(0,1)
        self.difficult_sleep = random.randint(0,1)
        self.upper_arm_pain = random.randint(0,1)
        self.pain_small_mov = 1

        # Random generate Shoulder AROM
        ## AROM = Active ROM
        ### AROM 可能因受傷、肌肉緊繃等因素影響，故讓三成的隨機程度的讓AROM != PROM (通常健康的人AROM = PROM)

        self.is_AROM_normal = random.random()

        if self.is_AROM_normal > 0.2:
            self.AFROM = self.PFROM
            self.AEROM = self.PEROM
            self.AABDROM = self.PABDROM
            self.AERROM = self.PERROM
            self.AIRROM = self.PIRROM

        else:
            self.AFROM = round(self.PFROM * random.uniform(0.75,0.95),2)
            self.AEROM = round(self.PEROM * random.uniform(0.75,0.95),2)
            self.AABDROM = round(self.PABDROM * random.uniform(0.75,0.95),2)
            self.AERROM = round(self.PERROM * random.uniform(0.75,0.95),2)
            self.AIRROM = round(self.PIRROM * random.uniform(0.75,0.95),2)

        # AFROM < 90 無法正確執行Empty can test 故設定為-1
        if self.AFROM < 90:
            self.Empty_can_test = -1
        else:
            self.Empty_can_test = random.randint(0,1)


        # Label for whether the patiten has Adhesive capsulitis
        self.label = 1


    # 有一定機率被診斷為假性五十肩
    def generate_noise(self):
        if self.Coracoid_Pain_Test == 0:
            self.label = 1


    def shoulder_bursitis(self):
        if self.PERROM >= 40:
            if self.PABDROM >=125 and self.PFROM >= 125 and self.Xray == 1 and self.pain_small_mov == 1 and self.Coracoid_Pain_Test == 0 and self.AFROM < 150 and self.AABDROM  < 150:
                self.label = 1

    def to_list(self):

        parameter_list = [self.age,self.gender,self.height,self.weight,self.BMI,self.diabetes,self.PFROM,self.PEROM,self.PABDROM,self.PERROM,
                            self.PIRROM,self.Xray,self.Coracoid_Pain_Test,self.Painful_arc_test,self.shoulder_trauma,self.difficult_sleep,
                            self.upper_arm_pain,self.pain_small_mov,self.Empty_can_test,self.AFROM,self.AEROM,self.AABDROM,self.AERROM,self.AIRROM]

        return parameter_list
