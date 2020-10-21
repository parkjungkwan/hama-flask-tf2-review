import os

from com_sba_api.utils.file_helper import FileReader
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.tree import DecisionTreeClassifier # dtree
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.naive_bayes import GaussianNB # nb
from sklearn.neighbors import KNeighborsClassifier # knn
from sklearn.svm import SVC # svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold  # k value is understood as count
from sklearn.model_selection import cross_val_score

from pathlib import Path
# dtree, rforest, nb, knn, svm,  

"""
context: /Users/bitcamp/SbaProjects
fname: 
PassengerId
Survived: The answer that a machine learning model should match 
Pclass: Boarding Pass 1 = 1st-class seat, 2 = 2nd, 3 = 3rd,
Name,
Sex,
Age,
SibSp accompanying brothers, sisters, spouses
Parch accompanying parents, children,
Ticket : Ticket Number
Fare : Boarding Charges
Cabin : Room number
Embarked : a Port Name on Board C = Cherbourg, Q = Queenstown, S = Southhampton
"""


class UserService:
    def __init__(self):
        self.fileReader = FileReader()  
        self.data = os.path.abspath("com_sba_api/user/data")
        self.odf = None

    def hook(self):
        train = 'train.csv'
        test = 'test.csv'
        this = self.fileReader
        this.train = self.new_model(train) # payload
        this.test = self.new_model(test) # payload
        
        '''
        Original Model Generation
        '''
        self.odf = pd.DataFrame(

            {
             'userid' : this.train.PassengerId,
             'password' : '1',
             'name' : this.train.Name
             }
        )
        
        this.id = this.test['PassengerId'] # This becomes a question. 
        # print(f'Preprocessing Train Variable : {this.train.columns}')
        # print(f'Preprocessing Test Variable : {this.test.columns}')
        this = self.drop_feature(this, 'Cabin')
        this = self.drop_feature(this, 'Ticket')
        # print(f'Post-Drop Variable : {this.train.columns}')
        this = self.embarked_norminal(this)
        # print(f'Preprocessing Embarked Variable: {this.train.head()}')
        this = self.title_norminal(this)
        # print(f'Preprocessing Title Variable: {this.train.head()}')
        # name 변수에서 title 을 추출했으니 name 은 필요가 없어졌고, str 이니 
        # 후에 ML-lib 가 이를 인식하는 과정에서 에러를 발생시킬것이다.
        this = self.drop_feature(this, 'Name')
        this = self.drop_feature(this, 'PassengerId')
        this = self.age_ordinal(this)
        # print(f'Preprocessing Age Variable: {this.train.head()}')
        this = self.drop_feature(this, 'SibSp')
        this = self.sex_norminal(this)
        # print(f'Preprocessing Sex Variable: {this.train.head()}')
        this = self.fareBand_nominal(this)
        # print(f'Preprocessing Fare Variable: {this.train.head()}')
        this = self.drop_feature(this, 'Fare')
        # print(f'Preprocessing Train Result: {this.train.head()}')
        # print(f'Preprocessing Test Result: {this.test.head()}')
        # print(f'Train NA Check: {this.train.isnull().sum()}')
        # print(f'Test NA Check: {this.test.isnull().sum()}')
        this.label = self.create_label(this) # payload
        this.train = self.create_train(this) # payload
        # print(f'Train Variable : {this.train.columns}')
        # print(f'Test Variable : {this.train.columns}')
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        
        # print(this)
        df = pd.DataFrame(

            {
             'pclass': this.train.Pclass,
             'gender': this.train.Sex, 
             'age_group': this.train.AgeGroup,
             'embarked' : this.train.Embarked,
             'rank' : this.train.Title
             }
        )
     
        # print(self.odf)
        # print(df)
        sumdf = pd.concat([self.odf, df], axis=1)
        
        '''
userid password                                               name  pclass  gender age_group  embarked  rank
0         1        1                            Braund, Mr. Owen Harris       3       0         4         1     1
1         2        1  Cumings, Mrs. John Bradley (Florence Briggs Th...       1       1         6         2     3
2         3        1                             Heikkinen, Miss. Laina       3       1         5         1     2
3         4        1       Futrelle, Mrs. Jacques Heath (Lily May Peel)       1       1         5         1     3
4         5        1                           Allen, Mr. William Henry       3       0         5         1     1
..      ...      ...                                                ...     ...     ...       ...       ...   ...
886     887        1                              Montvila, Rev. Juozas       2       0         5         1     6
887     888        1                       Graham, Miss. Margaret Edith       1       1         4         1     2
888     889        1           Johnston, Miss. Catherine Helen "Carrie"       3       1         2         1     2
889     890        1                              Behr, Mr. Karl Howell       1       0         5         2     1
890     891        1                                Dooley, Mr. Patrick       3       0         5         3     1

[891 rows x 8 columns]
        
        '''
        return sumdf
        
    
    def new_model(self, payload) -> object:
        this = self.fileReader
        this.data = self.data
        this.fname = payload
        return pd.read_csv(Path(self.data, this.fname)) # p.139  df = tensor

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1) # Train is a dataset in which the answer is removed. 

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived'] # Label is the answer.

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis = 1) 
        return this


    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def sex_norminal(this) -> object:
        combine = [this.train, this.test] # Train and test are bound.
        sex_mapping = {'male':0, 'female':1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)
        this.train = this.train # overriding
        this.test = this.test
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test 
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
         # age 를 평균으로 넣기도 애매하고, 다수결로 넣기도 너무 근거가 없다...
         # 특히 age 는 생존률 판단에서 가중치(weigth)가 상당하므로 디테일한 접근이 필요합니다.
         # 나이를 모르는 승객은 모르는 상태로 처리해야 값의 왜곡을 줄일수 있어서 
         # -0.5 라는 중간값으로 처리했습니다.
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf] # 이 파트는 범위를 뜻합니다.
         # -1 이상 0 미만....60이상 기타 ...
         # [] 에 있으니 이것은 변수명이겠군요..라고 판단하셨으면 잘 이해한 겁니다.
        labels = ['Unknown', 'Baby', 'Child', 'Teenager','Student','Young Adult', 'Adult', 'Senior']
        # [] 은 변수명으로 선언되었음
        train['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
        test['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
        age_title_mapping = {
            0: 'Unknown',
            1: 'Baby',
            2: 'Child',
            3: 'Teenager',
            4: 'Student',
            5: 'Young Adult',
            6: 'Adult',
            7: 'Senior'
        } # 이렇게 []에서 {} 으로 처리하면 labels 를 값으로 처리하겠네요.
        for x in range(len(train['AgeGroup'])):
            if train['AgeGroup'][x] == 'Unknown':
                train['AgeGroup'][x] = age_title_mapping[train['Title'][x]]
        for x in range(len(test['AgeGroup'])):
            if test['AgeGroup'][x] == 'Unknown':
                test['AgeGroup'][x] = age_title_mapping[test['Title'][x]]
        
        age_mapping = {
            'Unknown': 0,
            'Baby': 1,
            'Child': 2,
            'Teenager': 3,
            'Student': 4,
            'Young Adult': 5,
            'Adult': 6,
            'Senior': 7
        }
        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)
        this.train = train
        this.test = test
        return this

    @staticmethod
    def sibsp_numeric(this) -> object:
        return this

    @staticmethod
    def parch_numeric(this) -> object:
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        this.train['FareBand'] = pd.qcut(this['Fare'], 4, labels={1,2,3,4})
        this.test['FareBand'] = pd.qcut(this['Fare'], 4, labels={1,2,3,4})
        return this


    @staticmethod
    def fareBand_nominal(this) -> object:  # 요금이 다양하니 클러스터링을 하기위한 준비
        this.train = this.train.fillna({'FareBand' : 1})  # FareBand is a non-existent variable added
        this.test = this.test.fillna({'FareBand' : 1})
        return this

    @staticmethod
    def embarked_norminal(this) -> object:
        this.train = this.train.fillna({'Embarked': 'S'}) # S is the most common, filling in empty spaces.
        this.test = this.test.fillna({'Embarked': 'S'}) 
        '''
        Many machine learning libraries expect class labels to be encoded as * integer*
        mapping: blue = 0, green = 1, red = 2
        '''
        this.train['Embarked'] = this.train['Embarked'].map({'S': 1, 'C' : 2, 'Q' : 3}) # ordinal 아닙니다.
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C' : 2, 'Q' : 3})
        return this

    @staticmethod
    def title_norminal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona', 'Mme'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess','Lady','Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Ms','Miss')
            dataset['Title'] = dataset['Title'].replace('Mlle','Mr')
        title_mapping = {'Mr':1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        for dataset in combine:
            dataset['Title'] = dataset['Title'].map(title_mapping)
            dataset['Title'] = dataset['Title'].fillna(0) # Unknown
        this.train = this.train
        this.test = this.test
        return this

    # Dtree, rforest, nb, nnn, svm among Learning Algorithms use this as a representative

    @staticmethod
    def create_k_fold():
        return KFold(n_splits=10, shuffle=True, random_state=0)
    

    def accuracy_by_dtree(self, this):
        dtree = DecisionTreeClassifier()
        score = cross_val_score(dtree, this.train, this.label, cv=UserService.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    def accuracy_by_rforest(self, this):
        rforest = RandomForestClassifier()
        score = cross_val_score(rforest, this.train, this.label, cv=UserService.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)
    
    def accuracy_by_nb(self, this):
        nb = GaussianNB()
        score = cross_val_score(nb, this.train, this.label, cv=UserService.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)
    
    def accuracy_by_knn(self, this):
        knn = KNeighborsClassifier()
        score = cross_val_score(knn, this.train, this.label, cv=UserService.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    def accuracy_by_svm(self, this):
        svm = SVC()
        score = cross_val_score(svm, this.train, this.label, cv=UserService.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    def learning(self, train, test):
        service = self.service
        this = self.modeling(train, test)
        print(f'결정트리 검증결과: {service.accuracy_by_dtree(this)}')
        print(f'랜덤포리 검증결과: {service.accuracy_by_rforest(this)}')
        print(f'나이브베이즈 검증결과: {service.accuracy_by_nb(this)}')
        print(f'KNN 검증결과: {service.accuracy_by_knn(this)}')
        print(f'SVM 검증결과: {service.accuracy_by_svm(this)}')

    def submit(self, train, test): # machine 이 된다. 이 단계는 캐글에게 내 머신이를 보내서 평가받게 하는 것 입니다. 마치 수능장에 자식보낸 부모님 마음 ...
        this = self.modeling(train, test)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        
        print(this)
        # Pclass  Sex   Age  Parch  Embarked  Title AgeGroup
        df = pd.DataFrame(

            {
             'pclass': this.train.Pclass,
             'gender': this.train.Sex, 
             'age_group': this.train.AgeGroup,
             'embarked' : this.train.Embarked,
             'rank' : this.train.Title
             }
        )
      
        # print(self.odf)
        # print(df)
        sumdf = pd.concat([self.odf, df], axis=1)
        print(sumdf)
        return sumdf
'''
service = UserService()
service.hook()
'''