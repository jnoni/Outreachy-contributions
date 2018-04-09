# How happy is your country? Shall we find out?

I recently came across [this](http://happyplanetindex.org/) metric which is defined as an index of human well-being and environmental impact that was introduced by NEF, a UK-based economic think tank promoting social, economic and environmental justice. It ranks 140 countries according to “what matters most — sustainable wellbeing for all”.

Formula for calculating it is:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Determine%20happiness%20of%20your%20country/Plots/11.PNG)

It’s tells us “how well nations are doing at achieving long, happy, sustainable lives”. The index is weighted to give progressively higher scores to nations with lower ecological footprints.

The dataset used is the 2016 dataset from the HPI website. I have uploaded the data set [here](https://github.com/Rupal-IIITD/Outreachy-contributions/tree/master/Tell%20your%20Open%20Data%20story/Determine%20happiness%20of%20your%20country/Plots). I am interested to find correlations among happiness, wealth, life expectancy, footprint and so on, and then put these 140 countries into different clusters, according to the above measures.

So, let's begin.

We'll go step by step building our analysis upon the data. Follow the steps here:

## Packages:

```r
library(dplyr)
library(plotly)
library(stringr)
library(cluster)
library(FactoMineR)
library(factoextra)
library(ggplot2)
library(reshape2)
library(ggthemes)
library(NbClust)
```

## Data pre-processing

```r
hpi <- hpi[c(3:14)]
hpi <- hpi[-c(146:163), ]
hpi <- hpi[-c(1:4),]

names(hpi) <- c('country', 'region', 'life_expectancy', 'wellbeing', 'happy_years', 'footprint','inequality_outcomes', 'adj_life_expectancy', 'adj_wellbeing', 'hpi_index', 'gdp', 'population')

hpi <- hpi[-1, ]
```

## Handling the data types

```r
hpi$country <- as.character(hpi$country)
hpi$region <- as.character(hpi$region)
hpi$life_expectancy <- as.numeric(hpi$life_expectancy)
hpi$wellbeing <- as.numeric(hpi$wellbeing)
hpi$happy_years <- as.numeric(hpi$happy_years)
hpi$footprint <- as.numeric(hpi$footprint)
hpi$inequality_outcomes <- as.numeric(hpi$inequality_outcomes)
hpi$adj_life_expectancy <- as.numeric(hpi$adj_life_expectancy)
hpi$adj_wellbeing <- as.numeric(hpi$adj_wellbeing)
hpi$hpi <- as.numeric(hpi$hpi)
hpi$gdp <- as.numeric(hpi$gdp)
hpi$population <- as.numeric(hpi$population)
```

## Data structure

```r
str(hpi)
```

Output:

```
'data.frame':	140 obs. of  12 variables:
$ country            : chr  "Afghanistan" "Albania" "Algeria" "Argentina" ##...
$ region             : chr  "Middle East and North Africa" "Post-communist" ##"Middle East and North Africa" "Americas" ...
$ hpi_index          : num  20.2 36.8 33.3 35.2 25.7 ...
$ life_expectancy    : num  59.7 77.3 74.3 75.9 74.4 ...
$ happy_years        : num  12.4 34.4 30.5 40.2 24 ...
$ footprint          : num  0.79 2.21 2.12 3.14 2.23 9.31 6.06 0.72 5.09 7.44 ...
$ gdp                : num  691 4247 5584 14357 3566 ...
$ inequality_outcomes: num  0.427 0.165 0.245 0.164 0.217 ...
$ wellbeing          : num  3.8 5.5 5.6 6.5 4.3 7.2 7.4 4.7 5.7 6.9 ...
$ adj_life_expectancy: num  38.3 69.7 60.5 68.3 66.9 ...
$ adj_wellbeing      : num  3.39 5.1 5.2 6.03 3.75 ...
$ population         : num  29726803 2900489 37439427 42095224 2978339 ...
```

## Summary

```r
summary(hpi[, 3:12])
```

```
 hpi_index     life_expectancy  happy_years      footprint     
Min.   :12.78   Min.   :48.91   Min.   : 8.97   Min.   : 0.610  
1st Qu.:21.21   1st Qu.:65.04   1st Qu.:18.69   1st Qu.: 1.425  
Median :26.29   Median :73.50   Median :29.40   Median : 2.680  
Mean   :26.41   Mean   :70.93   Mean   :30.25   Mean   : 3.258  
3rd Qu.:31.54   3rd Qu.:77.02   3rd Qu.:39.71   3rd Qu.: 4.482  
Max.   :44.71   Max.   :83.57   Max.   :59.32   Max.   :15.820  
     gdp           inequality_outcomes   wellbeing     adj_life_expectancy
Min.   :   244.2   Min.   :0.04322     Min.   :2.867   Min.   :27.32      
1st Qu.:  1628.1   1st Qu.:0.13353     1st Qu.:4.575   1st Qu.:48.21      
Median :  5691.1   Median :0.21174     Median :5.250   Median :63.41      
Mean   : 13911.1   Mean   :0.23291     Mean   :5.408   Mean   :60.34      
3rd Qu.: 15159.1   3rd Qu.:0.32932     3rd Qu.:6.225   3rd Qu.:72.57      
Max.   :105447.1   Max.   :0.50734     Max.   :7.800   Max.   :81.26      
adj_wellbeing     population       
Min.   :2.421   Min.   :2.475e+05  
1st Qu.:4.047   1st Qu.:4.248e+06  
Median :4.816   Median :1.065e+07  
Mean   :4.973   Mean   :4.801e+07  
3rd Qu.:5.704   3rd Qu.:3.343e+07  
Max.   :7.625   Max.   :1.351e+09
```

```r
ggplot(hpi, aes(x=gdp, y=life_expectancy)) + 
  geom_point(aes(size=population, color=region)) + coord_trans(x = 'log10') +
  geom_smooth(method = 'loess') + ggtitle('Life Expectancy and GDP per Capita in USD log10') + theme_classic()
```

Plot we got:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Determine%20happiness%20of%20your%20country/Plots/12.PNG)

After log transformation, the relationship between GDP per capita and life expectancy is more clear and looks relatively strong. These two variables are correlated. The Pearson correlation between this two variable is reasonably high, at approximate 0.62.

```r
cor.test(hpi$gdp, hpi$life_expectancy)
```
Output:

```
Pearson's product-moment correlation

data:  hpi$gdp and hpi$life_expectancy
t = 9.3042, df = 138, p-value = 2.766e-16
alternative hypothesis: true correlation is not equal to 0
95 percent confidence interval:
 0.5072215 0.7133067
sample estimates:
      cor 
0.6208781
```
```r
ggplot(hpi, aes(x=life_expectancy, y=hpi_index)) + 
  geom_point(aes(size=population, color=region)) + geom_smooth(method = 'loess') + ggtitle('Life Expectancy and Happy Planet Index Score') + theme_classic()
```

Plot we got:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Determine%20happiness%20of%20your%20country/Plots/13.PNG)

### Observation:

Many countries in Europe and Americas end up with middle-to-low HPI index probably because of their big carbon footprints, despite the long life expectancy.

```r
ggplot(hpi, aes(x=gdp, y=hpi_index)) + geom_point(aes(size=population, color=region)) + geom_smooth(method = 'loess') + ggtitle('GDP per Capita(log10) and Happy Planet Index Score') + coord_trans(x = 'log10')
```

Plot we get:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Determine%20happiness%20of%20your%20country/Plots/14.PNG)

### Observation:

Clearly money can’t buy happiness. The correlation between GDP and Happy Planet Index score is indeed very low, at about 0.11.

```r
cor.test(hpi$gdp, hpi$hpi_index)
```

```
Pearson's product-moment correlation

data:  hpi$gdp and hpi$hpi_index
t = 1.3507, df = 138, p-value = 0.179
alternative hypothesis: true correlation is not equal to 0
95 percent confidence interval:
 -0.05267424  0.27492060
sample estimates:
      cor 
0.1142272
```

## Scaling the data

An important step of meaningful clustering consists of transforming the variables such that they have mean zero and standard deviation one.

```r
hpi[, 3:12] <- scale(hpi[, 3:12])
summary(hpi[, 3:12])
```

```
hpi_index        life_expectancy    happy_years         footprint      
Min.   :-1.86308   Min.   :-2.5153   Min.   :-1.60493   Min.   :-1.1493  
1st Qu.:-0.71120   1st Qu.:-0.6729   1st Qu.:-0.87191   1st Qu.:-0.7955  
Median :-0.01653   Median : 0.2939   Median :-0.06378   Median :-0.2507  
Mean   : 0.00000   Mean   : 0.0000   Mean   : 0.00000   Mean   : 0.0000  
3rd Qu.: 0.70106   3rd Qu.: 0.6968   3rd Qu.: 0.71388   3rd Qu.: 0.5317  
Max.   : 2.50110   Max.   : 1.4449   Max.   : 2.19247   Max.   : 5.4532  
     gdp          inequality_outcomes   wellbeing       adj_life_expectancy
Min.   :-0.6921   Min.   :-1.5692     Min.   :-2.2128   Min.   :-2.2192    
1st Qu.:-0.6220   1st Qu.:-0.8222     1st Qu.:-0.7252   1st Qu.:-0.8152    
Median :-0.4163   Median :-0.1751     Median :-0.1374   Median : 0.2060    
Mean   : 0.0000   Mean   : 0.0000     Mean   : 0.0000   Mean   : 0.0000    
3rd Qu.: 0.0632   3rd Qu.: 0.7976     3rd Qu.: 0.7116   3rd Qu.: 0.8221    
Max.   : 4.6356   Max.   : 2.2702     Max.   : 2.0831   Max.   : 1.4059    
adj_wellbeing       population     
Min.   :-2.1491   Min.   :-0.2990  
1st Qu.:-0.7795   1st Qu.:-0.2740  
Median :-0.1317   Median :-0.2339  
Mean   : 0.0000   Mean   : 0.0000  
3rd Qu.: 0.6162   3rd Qu.:-0.0913  
Max.   : 2.2339   Max.   : 8.1562
```

A simple correlation heatmap

```r
qplot(x=Var1, y=Var2, data=melt(cor(hpi[, 3:12], use="p")), fill=value, geom="tile") +
  scale_fill_gradient2(limits=c(-1, 1)) + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) + 
             labs(title="Heatmap of Correlation Matrix", 
                  x=NULL, y=NULL)
```

Plot:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Determine%20happiness%20of%20your%20country/Plots/15.PNG)

## Group countries by wealth, development, carbon emissions, and happiness

When using clustering algorithms, k must be specified. I use the following method to help to find the best k.

```r
number <- NbClust(hpi[, 3:12], distance="euclidean",
               min.nc=2, max.nc=15, method='ward.D', index='all', alphaBeale = 0.1)
```

Output:

```
*** : The Hubert index is a graphical method of determining the number of clusters.
                In the plot of Hubert index, we seek a significant knee that corresponds to a 
                significant increase of the value of the measure i.e the significant peak in Hubert
                index second differences plot. 
 
*** : The D index is a graphical method of determining the number of clusters. 
                In the plot of D index, we seek a significant knee (the significant peak in Dindex
                second differences plot) that corresponds to a significant increase of the value of
                the measure. 
 
******************************************************************* 
* Among all indices:                                                
* 4 proposed 2 as the best number of clusters 
* 7 proposed 3 as the best number of clusters 
* 1 proposed 5 as the best number of clusters 
* 5 proposed 6 as the best number of clusters 
* 3 proposed 10 as the best number of clusters 
* 3 proposed 15 as the best number of clusters 

                   ***** Conclusion *****                            
 
* According to the majority rule, the best number of clusters is  3
```

I will apply K=3 in the following steps:

```r
set.seed(2017)
pam <- pam(hpi[, 3:12], diss=FALSE, 3, keep.data=TRUE)
fviz_silhouette(pam)
```

Output:

```
cluster size ave.sil.width
1       1   43          0.46
2       2   66          0.32
3       3   31          0.37
```

Number of countries assigned in each cluster

```r
hpi$country[pam$id.med]
```
```
[1] "Liberia" "Romania" "Ireland"
```

This prints out one typical country represents each cluster.

```r
fviz_cluster(pam, stand = FALSE, geom = "point",
             ellipse.type = "norm")
```

Plot:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Determine%20happiness%20of%20your%20country/Plots/18.PNG)

## World map of three clusters

```r
hpi['cluster'] <- as.factor(pam$clustering)
map <- map_data("world")
map <- left_join(map, hpi, by = c('region' = 'country'))
ggplot() + geom_polygon(data = map, aes(x = long, y = lat, group = group, fill=cluster, color=cluster)) +
  labs(title = "Clustering Happy Planet Index", subtitle = "Based on data from:http://happyplanetindex.org/", x=NULL, y=NULL) + theme_minimal()
```

Plot:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Determine%20happiness%20of%20your%20country/Plots/19.PNG)

## Conclusion

The Happy Planet index has been criticized for weighting the ecological footprint too heavily; and the ecological footprint is a controversial concept. In addition, the Happy Planet Index has been misunderstood as a measure of personal “happiness”, when in fact, it is a measure of the “happiness” of the planet.

Nevertheless, the Happy Planet Index has been a consideration in the political area. For us, it is useful because it combines well being and environmental aspects, and it is simple and understandable.

### References:

1. [factoextra](https://www.r-bloggers.com/factoextra-r-package-easy-multivariate-data-analyses-and-elegant-visualization/)
2. [FactomineR](http://factominer.free.fr/)
3. [Nbclust](https://www.rdocumentation.org/packages/NbClust/versions/3.0/topics/NbClust)
