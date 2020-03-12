sns.boxplot(data=df_all_metrics['ComplexityPoints'], orient='h')

data_complexityPoints = df_all_metrics['complexityPoints']
print("Estatísticas dos dados de ComplexityPoints")
data_complexityPoints.describe().round(2)

print("Outliers dos dados de ComplexityPoints")
data_complexityPoints[data_complexityPoints > 300]

show_box_plot('technicalDebt')

my_describe('technicalDebt')

my_outliers('technicalDebt', 4000)

import pandas as pd
from sklearn import preprocessing

x = df_all_metrics.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled)

my_dict = {0:'maturity', 1:'totalDevelopers', 2:'complexityPoints', 3:'leadTime',4:'technicalDebt', 5:'taskScaling', 6:'taskGlobalDistance'}

### 1.5.3 Gráfico de Correlação entre complexityPoints (x2) e Technical Debt (y)
arraycomplexityPointsNormalized = df_my_all_metrics_normalized.complexityPoints.values
arrayTechnicalDebtNormalized = df_my_all_metrics_normalized.technicalDebt.values]

# plot
pyplot.scatter(arrayLeadTime, arrayTechnicalDebt)
pyplot.show()

sns.lmplot(x='leadTime', y='technicalDebt', data=df_all_metrics)

checkSpearmansCorrelations(coef,p, alfa):

##########
show_my_lmplot('leadTime')
calculate_spearman('leadTime')

feature2 = 
show_my_lmplot(feature2)
calculate_spearman(feature2)

feature3 = my_dict[2]
show_my_lmplot(feature3)
calculate_spearman(feature3)

feature4 = my_dict[3]
show_my_lmplot(feature4)
calculate_spearman(feature4)

feature5 = my_dict[4]
show_my_lmplot(feature5)
calculate_spearman(feature5)

feature6 = my_dict[5]
show_my_lmplot(feature6)
calculate_spearman(feature6)

LeadTimeRow = ['LeadTime', 'TD', coefLeadTimeNormalized, pLeadTimeNormalized, showCalcPSpearman(pLeadTime, 0.05)]
ComplexityPointsRow = ['ComplexityPoints', 'TD', coefComplexityPointsNormalized, pComplexityPointsNormalized,showCalcPSpearman(pComplexityPoints, 0.05)]
TotalDevelopersRow = ['TotalDevelopers', 'TD', coefTotalDevelopersNormalized, pTotalDevelopersNormalized,showCalcPSpearman(pTotalDevelopers, 0.05)]
TaskScalingRow = ['TaskScaling', 'TD', coefTaskScalingNormalized, pTaskScalingNormalized, showCalcPSpearman(pTaskScaling, 0.05)]
MaturityRow = ['Maturity', 'TD', coefMaturityNormalized, pMaturityNormalized, showCalcPSpearman(pMaturity, 0.05)]
TaskGlobalDistanceRow = ['TaskGlobalDistance', 'TD', coefTaskGlobalDistanceNormalized, pTaskGlobalDistanceNormalized, showCalcPSpearman(pTaskGlobalDistance, 0.05)]
analysisHeaders = ['Característica', 'Dívida Técnica', 'Spearmans Coef', 'p', 'Correlacionado']

print(tabulate([LeadTimeRow, ComplexityPointsRow, TotalDevelopersRow, 
                TaskScalingRow, MaturityRow, TaskGlobalDistanceRow],
               headers=analysisHeaders))

pd.DataFrame(data=np.append(modelo.intercept_, modelo.coef_), index=my_coeficientes, columns=['parêmetros'])

x = np.array([a, b, c])

x2 = np.array([['a','b'], ['b','c'], ['d','e']])
my_index = ['l1', 'l2', 'l3']
my_columns = ['c1', c2]

pd.DataFrame(data=x2, index=my_index, columns=my_columns)

modelo_4_score = modelo_4.score(X4_train, y4_train).round(2)
modelo_4_metrics_r2_score = metrics.r2_score(y4_test, y_previsto_4).round(2)

modelo_3_score = modelo_3.score(X3_train, y3_train).round(2)
modelo_3_metrics_r2_score = metrics.r2_score(y3_test, y_previsto_3).round(2)

modelo_2_score = modelo_2.score(X2_train, y2_train).round(2)
modelo_2_metrics_r2_score = metrics.r2_score(y2_test, y_previsto_2).round(2)

modelo_1_score = modelo_1.score(X1_train, y1_train).round(2)
modelo_1_metrics_r2_score = metrics.r2_score(y1_test, y_previsto_1).round(2)