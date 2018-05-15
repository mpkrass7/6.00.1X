# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:01:28 2018

@author: pl89155
"""

tempList = ['306.07',	'51.64',	'189.84',	'412.69',	'164.36',	
            '389.53',	'241.42',	'187.62',	'154.31',	'198.75',	
            '358.85',	'74.66',	'1.47',	'123.93',	'38.63',	
            '10.33',	'131.32',	'175.04',	'78.2',	'383.27',	
            '523.81',	'48.23',	'760.07',	'160.26',	'687.49',	
            '66.35',	'507.87',	'760.92',	'199.51',	'88.65',	
            '199.71',	'171.82',	'522.8',	'87.98',	'45.31',	
            '499.02',	'252.3',	'11.84',	'368.04',	'177.22',	
            '54.27',	'45.18',	'503.19',	'346.08',	'255.82',	'39.92',	
            '157.86',	'528.12',	'436.44',	'10.94',	'7.27',	'10.09',	
            '105.39',	'161.99',	'176.69',	'54.03',	'495.55',	'54.99',	
            '83.69',	'706.62',	'649.07',	'108.66',	'149.7',	'271.58',	
            '140.15',	'403.2',	'5.85',	'201.98',	'351.19',	'133.95', '3',	
            '134.96',	'191.57',	'23.51',	'125.78',	'51.49',	'42.38',	
            '12.25',	'242.83',	'520.11',	'486.61',	'103.65',	'613.49',	'3.72',
            '0.24',	'607.55',	'410.46',	'10.26',	'612.74',	'14.37',	'618.62',	
            '437.66',	'753.33',	'286.34',	'43.93',	'301.22',	'310.96',	'69.67',	
            '363.63',	'294.1',
]

def makeBuckets(List, Buckets):
    for i in range(len(List)):
        List[i] = float(List[i])
    newList = sorted(List)
    bucketSize = round(sum(newList)/Buckets)
    print("List length:", len(List))
    print("Bucket Size with", Buckets, "buckets:", bucketSize, "\n")
    currentBucket = []
    fullBucket = []
    bucketCount = 1
    clientCount = 1
    for i in range(len(newList)):
        if sum(currentBucket) < bucketSize:
            currentBucket.append(newList[i])
            clientCount += 1
#            print("Current Bucket Size", sum(currentBucket))
        else:
            print("Bucket", bucketCount, "with", clientCount, "clients has " \
            "total value of", str(round(sum(currentBucket),2)) + ", average of", \
            str(round(sum(currentBucket)/len(currentBucket),2)) + ", and includes:\n", \
            currentBucket[:],"\n")
            fullBucket.append(currentBucket[:])
            currentBucket = [newList[i]]
            bucketCount += 1
            clientCount = 1
    print("Bucket", bucketCount, "with", clientCount, "clients has " \
    "total value of", str(round(sum(currentBucket),2)) + ", average of", \
    round(sum(currentBucket)/len(currentBucket),2), "and includes:\n", \
    currentBucket[:],"\n")
    fullBucket.append(currentBucket[:])
    return (fullBucket)

makeBuckets(tempList, 3
            )