### Project Problem and Hypothesis

Vision Zero is a worldwide initiative that is adopted by cities to get all traffic related deaths down to zero. DC adopted this in 2015 with the goal of achieving Vision Zero by 2024. DC has published data on crashes from 2000 to 2016. The goal of this study is to analyze crashes in DC and predict whether a crash will be fatal or not (predicting a binary value). Similarly, this study will determine the greatest factors in fatal crashes. 

The results of this study can be used to inform appropriate advertising campaigns for Vision Zero. The results can also be used to inform the District on places where traffic calming initiatives should be instated. 

When considering what factors have on whether a crash is fatal or not, I predict that location and the type of crash will have the most impact. 

### Datasets

Crash data from Washington DC is available at http://opendata.dc.gov/datasets/95254fae17bc4792bd47b53f71c2e503_19. It is available for download in CSV format (along with accessible through an API). It has crashes from 2000 to 2016, has 152,744 rows, and 29 columns that we will use for this study. 

Data Dictionary: 

| ﻿Field                        | Description                                           | Data Type   |
|------------------------------|-------------------------------------------------------|-------------|
| X                            | X coordinate                                          | Location    |
| Y                            | Y coordinate                                          | Location    |
| CRASHID                      | Unique crash identification number                    | Integer     |
| CRIMEID                      | Unique crime identification number                    | Integer     |
| ISREPORTONSCENE              | Was the report made on scene                          | Categorical |
| SCHOOLBUSRELATED             | Does the crash involve a school bus                   | Categorical |
| INTERSECTIONTYPE             | Type of interesction where the crash occured          | Categorical |
| TRAFFICWAYRELATIONOTHER      | Where on the road the crash took place                | Categorical |
| ISWORKZONERELATED            | Did the crash happen at a work zone (0 = no, 1 = yes) | Categorical |
| STREETLIGHTING               | Street light conditions                               | Categorical |
| POSTEDSPEEDLIMIT             | Speed limit at crash location                         | Continuous  |
| FIRSTHARMFULEVENT            | What category the crash falls in                      | Categorical |
| FIRSTHARMFULEVENTSPECIFICS   | Specifics of the crash - what the car hit, etc        | Categorical |
| FIRSTHARMFULEVENTIMPACT      | Where the car got hit                                 | Categorical |
| FIRSTHARMFULEVENTRELATIVELOC | Relative road location of the crash                   | Categorical |
| NUMBERPHOTOSTAKEN            | Number of photos taken of the crash                   | Integer     |
| SOURCEADDTIME                | Date crash was added to the databsae                  | Date        |
| SOURCEMODTIME                | Date crash entry was modified                         | Date        |
| ADDRESS1                     | Address of the crash                                  | Location    |
| LIGHTCONDITION               | Light condition at time of crash                      | Categorical |
| WEATHER                      | Weather at time of crash                              | Categorical |
| REPORTDATE                   | Date of crash                                         | Date        |
| ISDRINKING                   | Did the crash involve  alcohol                        | Categorical |
| CYCLISTSINVOLVED             | How many cyclists were involved                       | Continuous  |
| PEDESTRIANSINVOLVED          | How many pedestrians were involved                    | Continuous  |
| MINORINJURIES                | How many minor injuries occurred                      | Continuous  |
| MAJORINJURIES                | How many major injuries occurred                      | Continuous  |
| FATALITIES                   | How many fatalities occurred                          | Continuous  |
| TRAFFICCONTROLDEVICES        | What traffic control devices were present             | Categorical |

### Domain Knowledge

I have worked with this dataset before (I completed a [study in R](https://github.com/sidewalkballet/visionzero) looking at crash and injury trends over the years). 

A study has been done before with this same premise. I have found the full PDF online and will use it as a reference.  

Al-Ghamdi, Ali. "Using logistic regression to estimate the influence of accident factors on accident severity". _Accident analysis and prevention_ (0001-4575), 34 (6), p. 729.

### Project Concerns 

Overall concerns for this project stem from the data available - the dataset has a large amount of null fields. I’m also concerned with the relatively small amount of fatal crashes: out of 152,744 crashes in the dataset only 364 were fatal. I’m not sure whether that poses a problem for my analysis or not.

Having access to traffic counts data would augment this study. There are datasets which have hourly traffic volumes for traffic count stations in DC from 2007 to 2014, but the locations are fairly sparse and would only be relevant for a handful of crash locations. That data can be found here: http://rtdc-mwcog.opendata.arcgis.com/datasets?q=traffic&sort_by=relevance

Risks of this model being wrong could actually be a matter of life and death - if results of this model are to be used by the District in efforts to lower the occurrences of fatal crashes, and the results are wrong, then efforts would be spent in the wrong places and the real issue wouldn’t be affected or resolved. 

### Outcomes

The output will be a logistic regression model and interpretation using odds ratios. The target audience of this study is the District Department of Transportation. This model doesn’t necessarily have to be very complicated - there are a large number of columns to use at the beginning, but it will be culled down to include the most significant features. 


