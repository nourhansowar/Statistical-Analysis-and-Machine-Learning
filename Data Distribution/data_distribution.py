import pandas as pd
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis 



def analyze_data_distibution(txt_file):
    data= np.loadtxt(txt_file)

    # Basic Statistical Measures: Mean, Median, Standard Deviation, Variance.
    mean= np.mean(data)
    median = np.median(data)
    std_dev= np.std(data)
    variance = np.var(data)
    
    #Quartile Values: 1st quartile (q1), 2nd quartile (q2), 3rd quartile (q3), Interquartile Range (IQR).
    Q1= np.percentile(data,25)
    Q2= np.percentile(data,50)
    Q3= np.percentile(data,75)
    IQR = Q3-Q1

    #Anomaly Detection:
    
    #--Outliers and Extreme Outliers
    outliers= [x for x in data if x< Q1-1.5*IQR or x> Q3+1.5*IQR]
    extreme_outliers= [x for x in data if x< Q1-3*IQR or x> Q3+3*IQR]

    #--Skewness and Kurtosis
    skewness= skew(data)
    kurtosis_val = kurtosis(data, axis=0, bias=True)

    
    #Suggested Data Transformations
    
    #Recommend transformations (like logarithmic, square root, etc.) to normalize the data based on skewness and kurtosis values.
    if skewness > 0:
        # Right-skewed data
        if kurtosis_val > 3:
            # Highly right-skewed data with heavy tails
            suggested_transform = "logarithmic"
        else:
            # Moderately right-skewed data
            suggested_transform = "square root"
    else:
        # Left-skewed data
        if kurtosis_val > 3:
            # Highly left-skewed data with heavy tails
            suggested_transform = "exponential"
        else:
            # Moderately left-skewed data
            suggested_transform = "none"
    
    # Analyze skewness and kurtosis to determine distribution type
    if abs(skewness) < 0.5 and abs(kurtosis_val - 3) < 1:
        data_distribution = "Normal"
    elif skewness > 0 and kurtosis_val > 3:
        data_distribution = "Right-skewed with heavy tails"
    elif skewness > 0 and kurtosis_val < 3:
        data_distribution = "Right-skewed"
    elif skewness < 0 and kurtosis_val > 3:
        data_distribution = "Left-skewed with heavy tails"
    elif skewness < 0 and kurtosis_val < 3:
        data_distribution = "Left-skewed"
    else:
        data_distribution = "Unknown"

    return {
        "Mean": mean,
        "Median": median,
        "Standard Deviation": std_dev,
        "Variance": variance,
        "Quartile 1": Q1,
        "Quartile 2": Q2,
        "Quartile 3": Q3,
        "Interquartile Range": IQR,
        "Outliers":outliers,
        "Extreme Outliers": extreme_outliers,
        "Skewness": skewness,
        "Kurtosis": kurtosis_val,
        "Suggested Transformation": suggested_transform,
        "Data Distribution": data_distribution
    }




print(analyze_data_distibution('Data-1.txt'))