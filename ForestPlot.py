import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

''''''''' ForestPlot '''''''''

# Parameters

# Only model_estimate and text are mandatory. Other parameters are optional.

# 1. model_estimate - Model whose forest plot is to be made.
#                     Should be a dataframe with column names as Study,value1,value2 and mean.
#                     Study - name of the Studies done.
#                     value1 - lower limit of forest plot.
#                     value2 - upper limit of forest plot.
#                     mean - mean value or position of model estimates.

# 2. text - Data to be represented in tabular form - Should be a dataframe with column names as text,info,O1 and O2(O1 and O2 are Optional)
#           text - column1 header of the table and name of Studies.
#           info - data about the mean,lower and upper limits of forest plot.
#           O1 and O2 are treatment and control group ratios.

# 3. save_location - location and name of the forestplot to be saved (default - saves as png file with the name 'forestplot' in the working directory).

# 4. zero - Location of the null line (default - 1).

# 5. clip - Lower and upper limits for clipping credible intervals to arrows . Should be a list - [lower_clip_limit, upper_clip_limit] (default - [0,10]).

# 6. xlab - Title of the x-axis label (default - Lab)

# 7. reported_estimate - Reported estimate for model whose forest plot is to be made.
#                        Should be a dataframe with column names as Study,value1,value2 and mean (default - pd.DataFrame()).

def forestplot(model_estimate,text,save_location='forestplot.png',zero=1,clip=[0,10],xlab='Lab',reported_estimate=pd.DataFrame()):
       
       model_estimate['weight'] = 50/((model_estimate['value2']-model_estimate['value1']))
       Overall = model_estimate[model_estimate['Study'] == 'Overall'].reset_index()
       
       for i in range(len(model_estimate)-1):    
              
              if model_estimate['value1'][len(model_estimate)-i-2] < clip[0]:
                     line_range_model_estimate = [clip[0],model_estimate['value2'][len(model_estimate)-i-2]]  
                     label = [i+1,i+1]
                     study = [model_estimate['mean'][len(model_estimate)-i-2],model_estimate['mean'][len(reported_estimate)-i-2]]
                     sns.set_style('darkgrid')
                     plt.plot(line_range_model_estimate,label, color='b')
                     plt.scatter(study,label,marker='s',s=model_estimate['weight'][len(model_estimate)-i-2], color='b')
                     plt.plot([clip[0]+0.1,clip[0],clip[0]+0.1],[i+1.1,i+1,i+0.9], color='b')
              
              elif model_estimate['value2'][len(model_estimate)-i-2] > clip[1]:
                     line_range_model_estimate = [model_estimate['value1'][len(model_estimate)-i-2],clip[1]]  
                     label = [i+1,i+1]
                     study = [model_estimate['mean'][len(model_estimate)-i-2],model_estimate['mean'][len(model_estimate)-i-2]]
                     plt.plot(line_range_model_estimate,label, color='b')
                     plt.scatter(study,label,marker='s',s=model_estimate['weight'][len(model_estimate)-i-2], color='b')
                     plt.plot([clip[1]-0.1,clip[1],clip[1]-0.1],[i+1.1,i+1,i+0.9], color='b')
                     
              else:
                     line_range_model_estimate = [model_estimate['value1'][len(model_estimate)-i-2],model_estimate['value2'][len(model_estimate)-i-2]]  
                     label = [i+1,i+1]
                     study = [model_estimate['mean'][len(model_estimate)-i-2],model_estimate['mean'][len(model_estimate)-i-2]]
                     plt.plot(line_range_model_estimate,label, color='b')
                     plt.scatter(study,label,marker='s',s=model_estimate['weight'][len(model_estimate)-i-2], color='b')
       
       if not(reported_estimate.empty):
       
              reported_estimate['weight'] = 50/((reported_estimate['value2']-reported_estimate['value1']))
                    
              for i in range(len(reported_estimate)):   
                     
                     if reported_estimate['value1'][len(reported_estimate)-i-1] < clip[0]:
                            line_range_reported_estimate = [clip[0],reported_estimate['value2'][len(reported_estimate)-i-1]]  
                            label1 = [i+0.6,i+0.6]
                            study1 = [reported_estimate['mean'][len(reported_estimate)-i-1],reported_estimate['mean'][len(reported_estimate)-i-1]]
                            plt.plot(line_range_reported_estimate,label1, color='r')
                            plt.scatter(study1,label1,s=reported_estimate['weight'][len(reported_estimate)-i-1], color='r')
                            plt.plot([clip[0]+0.1,clip[0],clip[0]+0.1],[i+0.7,i+0.6,i+0.5], color='r')
                     
                     elif reported_estimate['value2'][len(reported_estimate)-i-1] > clip[1]:
                            line_range_reported_estimate = [reported_estimate['value1'][len(reported_estimate)-i-1],clip[1]]  
                            label1 = [i+0.6,i+0.6]
                            study1 = [reported_estimate['mean'][len(reported_estimate)-i-1],reported_estimate['mean'][len(reported_estimate)-i-1]]
                            plt.plot(line_range_reported_estimate,label1, color='r')
                            plt.scatter(study1,label1,s=reported_estimate['weight'][len(reported_estimate)-i-1], color='r')
                            plt.plot([clip[1]-0.1,clip[1],clip[1]-0.1],[i+0.7,i+0.6,i+0.5], color='r')
                            
                     else:
                            line_range_reported_estimate = [reported_estimate['value1'][len(reported_estimate)-i-1],reported_estimate['value2'][len(reported_estimate)-i-1]]  
                            label1 = [i+0.6,i+0.6]
                            study1 = [reported_estimate['mean'][len(reported_estimate)-i-1],reported_estimate['mean'][len(reported_estimate)-i-1]]
                            plt.plot(line_range_reported_estimate,label1, color='r')
                            plt.scatter(study1,label1,s=reported_estimate['weight'][len(reported_estimate)-i-1], color='r')
                            
       sns.set_style('darkgrid')
       plt.fill([Overall['value1'][0],Overall['mean'][0],Overall['value2'][0],Overall['mean'][0]],[0,-0.25,0,0.25], 'b')       
       plt.axvline(x=zero)
       plt.xlim(xmax=clip[1])
       plt.xlabel(xlab)
       plt.tick_params(axis='y', which='both',labelsize =0)
       
       #Legends
       
       if not(reported_estimate.empty):
              blue_patch = mlines.Line2D([], [], color='blue', marker='s', linestyle='None',
                          markersize=10, label='Model Estimates')
              red_patch = mlines.Line2D([], [], color='red', marker='o', linestyle='None',
                          markersize=10, label='Reported Estimates')
              plt.legend(handles=[blue_patch,red_patch],loc='upper center',bbox_to_anchor=(0.5, 1.1),ncol=2)
       
       # Tables
       
       left_table_data = text.loc[:,['text','info']]
       left_cell_value = []
       for i in range(len(left_table_data)):
              left_cell_value.append([left_table_data['text'].tolist()[i],left_table_data['info'].tolist()[i]])
              
       left_table = plt.table(cellText=left_cell_value,
                    cellLoc='left', colWidths=[0.5,0.5],
                    rowLoc='left', colLoc='left',
                    loc='left', bbox=[-0.65, 0, 0.55, 1.1],
                    edges='open')
       left_table.auto_set_font_size(False)
       left_table.set_fontsize(14)
       
       if('O1' in text and 'O2' in text):
              right_table_data = text.loc[:,['O1','O2']]
              right_cell_value = []
              for i in range(len(right_table_data)):
                     right_cell_value.append([right_table_data['O1'].tolist()[i],right_table_data['O2'].tolist()[i]])
              
              right_table = plt.table(cellText=right_cell_value,
                           cellLoc='left', colWidths=[0.5,0.5],
                           rowLoc='left', colLoc='left',
                           loc='right', bbox=[1.05, 0, 0.55, 1.1],
                           edges='open')
              right_table.auto_set_font_size(False)
              right_table.set_fontsize(14)
       
       plt.savefig(save_location, dpi=500, bbox_inches='tight')