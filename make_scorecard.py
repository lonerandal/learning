def make_scorecard(formular,woe,basescore=600.0,base_odds=50.0/1.0,pdo=50.0):
    """
    一般行业规则，一般设定当odds为50时，score为600
    Odds翻倍时，score+20
    score = -(woe*b +a/n)*factor + offset/n
    factor = pdo/np.log(2)
    offset = basescore - factor*np.log(base_odds)

    basescore = float(600)
    base_odds = 50.0/1.0
    pdo = float(50)
    #计算所需要的参数
    """
    a = formular[formular[u"参数"] == "Intercept"].ix[0,u"估计值"]
    formular = formular.iloc[1:,:]
    n = float(len(formular))
    factor = pdo/np.log(2)
    offset = basescore - factor*np.log(base_odds)

#生成评分卡

    scorecard = pd.DataFrame()
    for i in formular[u"参数"]:
        woe_frame = woe[woe['var_name'] == i][['var_name','interval','min','max','PctRec','bad_rate','WOE']]
        beta_i = formular[formular[u"参数"] == i][u"估计值"].iloc[0]
        #woe_frame['score'] = woe_frame['WOE'].apply(lambda woe : offset/n - factor*(a/n-np.abs(beta_i)*woe))
        woe_frame['score'] = woe_frame['WOE'].apply(lambda woe : offset/n - factor*(a/n+beta_i*woe))
        scorecard = pd.concat((scorecard,woe_frame),axis=0)

    return scorecard