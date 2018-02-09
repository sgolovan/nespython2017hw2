# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%% Task 1. Class of OLS-regression
class OLS:
    def __init__(self, X=0, y=0):
        import numpy as np
        self.X = X
        self.y = y
        self.XX = np.transpose(self.X).dot(X)
        self.coef = np.linalg.inv(self.XX).dot(np.transpose(self.X)).dot(self.y)
        n_k = 1/(self.X.shape[0]-self.X.shape[1])
        sigma = n_k*np.transpose(self.y-self.X.dot(self.coef)).dot(self.y-self.X.dot(self.coef))
        self.coef_var_matr = sigma*np.linalg.inv(self.XX)
    def predict(self,x):
        import numpy as np
        if np.shape(x)[0] == np.shape(self.X)[1]:
            return np.transpose(x).dot(self.coef)
        else:
            return 'Shape of x should be matched to number of X columns'
    def predict_dev(self,x):
        import numpy as np
        n_k = 1/(self.X.shape[0]-self.X.shape[1])
        sigma = n_k*np.transpose(self.y-self.X.dot(self.coef)).dot(self.y-self.X.dot(self.coef))
        XX_inverse = np.linalg.inv(self.XX)
        if np.shape(x)[0] == np.shape(self.X)[1]:
            return sigma*(1+np.transpose(x).dot(XX_inverse).dot(x))
        else:
            return 'Shape of x should be matched to number of X columns'
#%%
    import numpy as np
    X = np.random.randn(100, 3)
    y = X.dot(np.array([1,2,3])) + np.random.randn(100)
    
    model = OLS(X,y)
    model.coef
    x_new = np.array([1,1,1])
    pred = model.predict(x_new)
    pred_dev = model.predict_dev(x_new)
    var_matr = model.coef_var_matr
    pred_dev, pred
#%% Task 2. 
    from math import factorial
    import matplotlib.pyplot as plt
    from matplotlib import axes
    
    #Fix random state by usage of random.seed(0)
    np.random.seed(0)
    
    betas = np.random.rand(11)
    betas
    a = -5
    b = 5
    x = (b-a)*np.random.rand(200) + a
    u = 10*np.random.randn(200)
    
    #create matrix x_matr which will contain all degrees of x_i 
    x_matr = np.ones((1,200))
    for i in np.arange(1,11):
        x_matr = np.vstack((x_matr, (x ** i)/factorial(i)))
    
    #now we can obtain y_i via multiplication of betas and x_matr
    y = betas.dot(x_matr) + u
    
    #Let's draw point cloud
    plt.scatter(x, y, s =5, color = 'black')
    plt.xlabel("$x_i$")
    plt.ylabel("$y_i$")
    plt.savefig('/Users/nik/Documents/РЭШ/3 модуль/Data_analysis/HA3_3.pdf')
    plt.show()
    #Create y_pred which will contain y_i for all regressions.
    #'Order' is required to draw line without intersections. They appear because the data is not sorted.
    plt.scatter(x[np.newaxis,:], y, s =5, color = 'black')
    y_predicted = np.zeros((200,4))
    order = np.argsort(x)
    for k in np.arange(1,5):
        x_temp = x
        i = 1
        while i<k:
            x_temp = np.vstack((x_temp, x ** (i+1)))
            i+=1
        
        if k == 1:
            model = OLS(x_temp[:,np.newaxis],y)
            y_predicted[:,0] = model.predict(x_temp[:,np.newaxis].T)
            plt.plot(x[order],y_predicted[order,0], label= 'K=%d'%k)
        else:
            model = OLS(x_temp.T,y)
            for c in np.arange(0,200):
                y_predicted[c,k-1] = model.predict(x_temp[:,c])
            plt.plot(x[order],y_predicted[order,k-1], label= 'K=%d'%k)
        plt.legend()
        plt.xlabel("$x_i$")
        plt.ylabel("$y_i$")
        plt.savefig('/Users/nik/Documents/РЭШ/3 модуль/Data_analysis/HA3_2.pdf')

#%%
    from scipy import stats
    #Let's create lists of predicted values by regression of the 4th degree 'y_predicted_4' and 
    #their errors 'y_predicted_4_error'.
    y_predicted_4 = y_predicted[:,3]
    y_predicted_4_error = np.zeros(200)
    for c in np.arange(0,200):
        y_predicted_4_error[c] = model.predict_dev(x_temp[:,c])
    
    p = stats.t.ppf(1-0.05, y_predicted[:,3].shape)
    plt.scatter(x[np.newaxis,:], y, s =5, color = 'black')
    plt.plot(x[order],y_predicted[order,3], label= 'K=4', color = 'r')
    plt.fill_between(x[order],y_predicted_4[order]-p*np.sqrt(y_predicted_4_error[order]), y_predicted_4[order]+p*np.sqrt(y_predicted_4_error[order]), alpha=0.3)
    plt.legend()
    plt.xlabel("$x_i$")
    plt.ylabel("$y_i$")
    plt.savefig('/Users/nik/Documents/РЭШ/3 модуль/Data_analysis/HA3_1.pdf')

#%% Task 3
    A = np.random.randn(100,100)
    
    #Let's calculate means and deviations with built-in tools of NumPy library (methods mean and std).
    #Quatile of t-distribution will be calculated with methods of SciPy.stats.t.ppf()
    #Information about columns and rows confidence intervals is contained in variables with addition _col and _row correspondingly.
    mu_col = np.mean(A, axis = 0)
    sigma_col = np.std(A, axis = 0)
    p = stats.t.ppf(1-0.05, A.shape[0])
    size = np.sqrt(A.shape[0]-1)
    
    logic_col = [True if (x-p*y <=0 and x+p*y/size >=0) else False for x,y in zip(mu_col,sigma_col)]
    true_col = sum([1 if x == True else 0 for x in logic_col])
    
    mu_row = np.mean(A, axis = 1)
    sigma_row = np.std(A, axis = 1)

    logic_row = [True if (x-p*y/size <=0 and x+p*y/size >=0) else False for x,y in zip(mu_row,sigma_row)]
    true_row = sum([1 if x == True else 0 for x in logic_row])
#%%
    true_col, true_row
#%% Task 4
    import pandas as pd
    path = '/Users/nik/Documents/РЭШ/3 модуль/Data_analysis/goalies-2014-2016.csv'
    df = pd.read_csv(path, sep=';',header = 0)
    df.iloc[0:5,0:6]
#%% Let's calculate 'save_percentage' via pandas tools by the division of according columns from DataFrame
    #Result of comparison will be settled in list 'logic'.
    #If there is False in 'logic' then difference will be calculated in 'dev' list, otherwise there will be zero. 
    save_percentage = df['saves']/df['shots_against']
    logic = [True if round(x,3) == round(y,3) else False for x,y in zip(save_percentage,df['save_percentage'])]
    dev = [0 if b else np.abs(x-y) for b,x,y in zip(logic,save_percentage,df['save_percentage'])]
    max(dev)
#%%
    df[['games_played', 'goals_against', 'save_percentage']].mean(axis = 0)
    df[['games_played', 'goals_against', 'save_percentage']].std(axis = 0)
#%% Firstly, we should select number of players in a whole list with 'games_played' > 40.
    #Then we choose the player from this shertened list player with the highest 'save_percentage'.
    df.ix[df['save_percentage'][np.array(df['games_played']>40) & np.array(df['season']=='2016-17')].idxmax(),['player','save_percentage']]
#%% Firstly, let's find out number of different seasons via np.unique().
    #Then we will looking for player with the biggest number of 'saves' and particular value of 'season'.
    #Then we will place this data in temp and eventually in variable 'info'.
    season = np.unique(df['season'])
    info = []
    for s in season:
        player = df['player'][df['saves'][df['season']==s].idxmax()]
        saves = df['saves'][df['saves'][df['season']==s].idxmax()]
        temp = (s,player,saves)
        info.append(temp)
    info
#%% In this task we have to check two conditions. So for this purpose we should transform our arrays into np.array
    #which is able to work with boolean variables. Results are supposed to be a list, that's why we use 
    #np.hstack() to match information in matrix for corresponding seasons. To add information for different seasons
    #we use np.vstack(). Eventually, we have to delete the first row wirh zeros by np.delete().
    season = np.unique(df['season'])
    keeps = np.array([0,0,0])
    for s in season:
        player = np.array(df['player'][np.array(df['wins']>=30) & np.array(df['season']==s)])
        wins = np.array(df['wins'][np.array(df['wins']>=30) & np.array(df['season']==s)])
        seas = np.array(df['season'][np.array(df['wins']>=30) & np.array(df['season']==s)])
        temp = np.hstack((player[:,np.newaxis],wins[:,np.newaxis],seas[:,np.newaxis]))
        keeps = np.vstack((keeps,temp))
    keeps_clean = np.delete(keeps,0,0)
    keeps_names = np.unique(keeps_clean[:,0])
    n,names = [],[]
    for c,value in enumerate(keeps_names):
        n.append((keeps_clean[:,0]==value).sum())
        if n[-1] == 3:
            names.append(value)
#%%   
    names