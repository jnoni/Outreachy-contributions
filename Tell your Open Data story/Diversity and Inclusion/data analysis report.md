# Let's Kaggle!

## Context

For the first time, Kaggle conducted an industry-wide survey to establish a comprehensive view of the state of data science and machine learning. The survey received over 16,000 responses and we learned a ton about who is working with data, what’s happening at the cutting edge of machine learning across industries, and how new data scientists can best break into the field.

## Content

The data includes 5 files:

- **`schema.csv`**: a CSV file with survey schema. This schema includes the questions that correspond to each column name in both the `multipleChoiceResponses.csv` and `freeformResponses.csv`.
- **`multipleChoiceResponses.csv`**: Respondents' answers to multiple choice and ranking questions. These are non-randomized and thus a single row does correspond to all of a single user's answers. -`freeformResponses.csv`: Respondents' freeform answers to Kaggle's survey questions. These responses are randomized within a column, so that reading across a single row does not give a single user's answers.
- **`conversionRates.csv`**: Currency conversion rates (to USD) as accessed from the R package "quantmod" on September 14, 2017
- **`RespondentTypeREADME.txt`**: This is a schema for decoding the responses in the "Asked" column of the schema.csv file.

I am going to deal with only the **`multipleChoiceResponses.csv`** data set from all these.

## Data Stastics:

These are the features of the dataset (column names):

```
GenderSelect	Country	Age	EmploymentStatus	StudentStatus	LearningDataScience	CodeWriter	CareerSwitcher	CurrentJobTitleSelect	TitleFit	CurrentEmployerType	MLToolNextYearSelect	MLMethodNextYearSelect	LanguageRecommendationSelect	PublicDatasetsSelect	LearningPlatformSelect	LearningPlatformUsefulnessArxiv	LearningPlatformUsefulnessBlogs	LearningPlatformUsefulnessCollege	LearningPlatformUsefulnessCompany	LearningPlatformUsefulnessConferences	LearningPlatformUsefulnessFriends	LearningPlatformUsefulnessKaggle	LearningPlatformUsefulnessNewsletters	LearningPlatformUsefulnessCommunities	LearningPlatformUsefulnessDocumentation	LearningPlatformUsefulnessCourses	LearningPlatformUsefulnessProjects	LearningPlatformUsefulnessPodcasts	LearningPlatformUsefulnessSO	LearningPlatformUsefulnessTextbook	LearningPlatformUsefulnessTradeBook	LearningPlatformUsefulnessTutoring	LearningPlatformUsefulnessYouTube	BlogsPodcastsNewslettersSelect	LearningDataScienceTime	JobSkillImportanceBigData	JobSkillImportanceDegree	JobSkillImportanceStats	JobSkillImportanceEnterpriseTools	JobSkillImportancePython	JobSkillImportanceR	JobSkillImportanceSQL	JobSkillImportanceKaggleRanking	JobSkillImportanceMOOC	JobSkillImportanceVisualizations	JobSkillImportanceOtherSelect1	JobSkillImportanceOtherSelect2	JobSkillImportanceOtherSelect3	CoursePlatformSelect	HardwarePersonalProjectsSelect	TimeSpentStudying	ProveKnowledgeSelect	DataScienceIdentitySelect	FormalEducation	MajorSelect	Tenure	PastJobTitlesSelect	FirstTrainingSelect	LearningCategorySelftTaught	LearningCategoryOnlineCourses	LearningCategoryWork	LearningCategoryUniversity	LearningCategoryKaggle	LearningCategoryOther	MLSkillsSelect	MLTechniquesSelect	ParentsEducation	EmployerIndustry	EmployerSize	EmployerSizeChange	EmployerMLTime	EmployerSearchMethod	UniversityImportance	JobFunctionSelect	WorkHardwareSelect	WorkDataTypeSelect	WorkProductionFrequency	WorkDatasetSize	WorkAlgorithmsSelect	WorkToolsSelect	WorkToolsFrequencyAmazonML	WorkToolsFrequencyAWS	WorkToolsFrequencyAngoss	WorkToolsFrequencyC	WorkToolsFrequencyCloudera	WorkToolsFrequencyDataRobot	WorkToolsFrequencyFlume	WorkToolsFrequencyGCP	WorkToolsFrequencyHadoop	WorkToolsFrequencyIBMCognos	WorkToolsFrequencyIBMSPSSModeler	WorkToolsFrequencyIBMSPSSStatistics	WorkToolsFrequencyIBMWatson	WorkToolsFrequencyImpala	WorkToolsFrequencyJava	WorkToolsFrequencyJulia	WorkToolsFrequencyJupyter	WorkToolsFrequencyKNIMECommercial	WorkToolsFrequencyKNIMEFree	WorkToolsFrequencyMathematica	WorkToolsFrequencyMATLAB	WorkToolsFrequencyAzure	WorkToolsFrequencyExcel	WorkToolsFrequencyMicrosoftRServer	WorkToolsFrequencyMicrosoftSQL	WorkToolsFrequencyMinitab	WorkToolsFrequencyNoSQL	WorkToolsFrequencyOracle	WorkToolsFrequencyOrange	WorkToolsFrequencyPerl	WorkToolsFrequencyPython	WorkToolsFrequencyQlik	WorkToolsFrequencyR	WorkToolsFrequencyRapidMinerCommercial	WorkToolsFrequencyRapidMinerFree	WorkToolsFrequencySalfrod	WorkToolsFrequencySAPBusinessObjects	WorkToolsFrequencySASBase	WorkToolsFrequencySASEnterprise	WorkToolsFrequencySASJMP	WorkToolsFrequencySpark	WorkToolsFrequencySQL	WorkToolsFrequencyStan	WorkToolsFrequencyStatistica	WorkToolsFrequencyTableau	WorkToolsFrequencyTensorFlow	WorkToolsFrequencyTIBCO	WorkToolsFrequencyUnix	WorkToolsFrequencySelect1	WorkToolsFrequencySelect2	WorkFrequencySelect3	WorkMethodsSelect	WorkMethodsFrequencyA/B	WorkMethodsFrequencyAssociationRules	WorkMethodsFrequencyBayesian	WorkMethodsFrequencyCNNs	WorkMethodsFrequencyCollaborativeFiltering	WorkMethodsFrequencyCross-Validation	WorkMethodsFrequencyDataVisualization	WorkMethodsFrequencyDecisionTrees	WorkMethodsFrequencyEnsembleMethods	WorkMethodsFrequencyEvolutionaryApproaches	WorkMethodsFrequencyGANs	WorkMethodsFrequencyGBM	WorkMethodsFrequencyHMMs	WorkMethodsFrequencyKNN	WorkMethodsFrequencyLiftAnalysis	WorkMethodsFrequencyLogisticRegression	WorkMethodsFrequencyMLN	WorkMethodsFrequencyNaiveBayes	WorkMethodsFrequencyNLP	WorkMethodsFrequencyNeuralNetworks	WorkMethodsFrequencyPCA	WorkMethodsFrequencyPrescriptiveModeling	WorkMethodsFrequencyRandomForests	WorkMethodsFrequencyRecommenderSystems	WorkMethodsFrequencyRNNs	WorkMethodsFrequencySegmentation	WorkMethodsFrequencySimulation	WorkMethodsFrequencySVMs	WorkMethodsFrequencyTextAnalysis	WorkMethodsFrequencyTimeSeriesAnalysis	WorkMethodsFrequencySelect1	WorkMethodsFrequencySelect2	WorkMethodsFrequencySelect3	TimeGatheringData	TimeModelBuilding	TimeProduction	TimeVisualizing	TimeFindingInsights	TimeOtherSelect	AlgorithmUnderstandingLevel	WorkChallengesSelect	WorkChallengeFrequencyPolitics	WorkChallengeFrequencyUnusedResults	WorkChallengeFrequencyUnusefulInstrumenting	WorkChallengeFrequencyDeployment	WorkChallengeFrequencyDirtyData	WorkChallengeFrequencyExplaining	WorkChallengeFrequencyPass	WorkChallengeFrequencyIntegration	WorkChallengeFrequencyTalent	WorkChallengeFrequencyDataFunds	WorkChallengeFrequencyDomainExpertise	WorkChallengeFrequencyML	WorkChallengeFrequencyTools	WorkChallengeFrequencyExpectations	WorkChallengeFrequencyITCoordination	WorkChallengeFrequencyHiringFunds	WorkChallengeFrequencyPrivacy	WorkChallengeFrequencyScaling	WorkChallengeFrequencyEnvironments	WorkChallengeFrequencyClarity	WorkChallengeFrequencyDataAccess	WorkChallengeFrequencyOtherSelect	WorkDataVisualizations	WorkInternalVsExternalTools	WorkMLTeamSeatSelect	WorkDatasets	WorkDatasetsChallenge	WorkDataStorage	WorkDataSharing	WorkDataSourcing	WorkCodeSharing	RemoteWork	CompensationAmount	CompensationCurrency	SalaryChange	JobSatisfaction	JobSearchResource	JobHuntTime	JobFactorLearning	JobFactorSalary	JobFactorOffice	JobFactorLanguages	JobFactorCommute	JobFactorManagement	JobFactorExperienceLevel	JobFactorDepartment	JobFactorTitle	JobFactorCompanyFunding	JobFactorImpact	JobFactorRemote	JobFactorIndustry	JobFactorLeaderReputation	JobFactorDiversity	JobFactorPublishingOpportunity
```


### Loading required R packages

```r
#Loading Required Libraries 
library(dplyr)
library(stringr)
library(ggplot2)
library(ggthemes)
library(tidyr)
library(scales)
```
### Load the files in R environment

```r
#Load Input Data
complete_data <- read.csv(".../multipleChoiceResponses.csv",header =T, stringsAsFactors = F)
```

### Gender Distribution of the respondents?

```r
#Gender Distribution
complete_data %>% 
  filter(GenderSelect!='') %>% 
  group_by(GenderSelect) %>% 
  count() %>% 
  ggplot(aes(x = GenderSelect,y = (n / sum(n))*100))+
  geom_bar(stat = 'identity') + ylab('Percent') + theme_solarized() +
  theme(axis.text = element_text(size = 6)) + ggtitle('Gender Distribution of Kaggle Survey Respondents')
```

Graphical form:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Diversity%20and%20Inclusion/Plots/1.png)

#### With no surprise like many other Technical domain, Data Science is also dominated by Male Gender with more than 80% respondents being Male and less than 20% being Female.

### Split of Male and Female across countries of the participants:

```r
complete_data %>% filter(GenderSelect %in% c('Male','Female')) %>%
  group_by(Country,GenderSelect) %>% 
  summarise(count = n()) %>%
  arrange(desc(count)) %>% ggplot() + 
  geom_bar(aes(Country,count, fill = GenderSelect), stat = 'identity') +
  #facet_grid(.~GenderSelect)  + 
  theme_solarized() +
  theme(axis.text = element_text(size = 9),
        axis.text.x = element_text(angle = 40, vjust = 0.5, hjust = 0.5)) +
  ggtitle('Country wise Survey Respondends - M/F')
  ```
  
  Plot I got:
  
  ![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Diversity%20and%20Inclusion/Plots/2.png)
  
  With the US being the top country of Respondents followed by India, It can be seen how Male-Female split across Countries look like. While this chart very well represents the distribution of countries, it doesn’t reflect which country is doing good in terms of Female Gender in Data Science. To understand that, I create a new KPI – F2M Ratio (Female to Male Ratio % – which could be interpreted as the number of Female to 100 Male).
  
```r
complete_data %>% filter(GenderSelect %in% c('Male','Female') & Country!="") %>%
  group_by(Country,GenderSelect) %>% 
  summarise(count = n()) %>%
  spread(GenderSelect,count) %>% 
  mutate(F2M = (Female/Male)*100) %>% 
  arrange(desc(F2M)) %>%
  #mutate(F2M = percent(F2M)) %>% 
  ggplot() +
  geom_bar(aes(Country,F2M, fill = F2M), stat = 'identity') +
theme_solarized() +
  theme(axis.text = element_text(size = 9),
        axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 0.5)) +
  ggtitle('Female to Male Ratio - Country Wise') + scale_fill_continuous_tableau()
```

Plot:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Diversity%20and%20Inclusion/Plots/3.png)

#### It turns out that no Country has got this Female-to-Male ratio more than 50% which is not a very healthy insight, but there are three countries that fared above 40% – Ireland, Malaysia and Egypt are those. Ironically, The US and India that were on the top overall have got lesser than 30% and 20% respectively.

### Age distribution between Male and Female?

```r
complete_data %>% filter(GenderSelect %in% c('Male','Female')) %>%  
  ggplot() + geom_histogram(aes(Age),binwidth = 1) + 
  theme_solarized() + facet_grid(.~GenderSelect) +
  ggtitle('Age Distribution - Male vs Female')
```

Plot:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Diversity%20and%20Inclusion/Plots/4.png)

#### It could be inferred from the above Plot that the central tendency between Male and Female is similar, but it is very clear that Men seemed to start earlier than their Female counterparts – which could be a big factor to establish themselves in this industry with confidence.

### Language familiar among Data Enthusiasts?

```r
complete_data %>% group_by(LanguageRecommendationSelect) %>% summarize(count = n())
```

```
# A tibble: 14 x 2
   LanguageRecommendationSelect count                
 1                               5718
 2                     C/C++/C#   307
 3                           F#     4
 4                      Haskell    17
 5                         Java   138
 6                        Julia    30
 7                       Matlab   238
 8                        Other    85
 9                       Python  6941
10                            R  2643
11                          SAS    88
12                        Scala    94
13                          SQL   385
14                        Stata    28
```

#### Inference: 

Python followed by R

### Language that does well with our Female Data Enthusiasts?

```r
complete_data %>% filter(GenderSelect %in% c('Male','Female')) %>% group_by(LanguageRecommendationSelect,GenderSelect) %>% 
  summarize(count = n()) %>%
  spread(GenderSelect,count) %>% 
  mutate(F2M = Female/Male) %>% 
  arrange(desc(F2M)) %>%
  mutate(F2M = F2M * 100) %>%  ggplot() +
  geom_bar(aes(LanguageRecommendationSelect,F2M, fill = F2M), stat = 'identity') +
  theme_solarized() + 
  theme(axis.text = element_text(size = 9),
        axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 0.5)) +
  scale_fill_continuous_tableau() + ggtitle('F2M Ratio of Languages used by Kagglers')
  ```
  
  Plot:
  
  ![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Diversity%20and%20Inclusion/Plots/5.png)
  
 #### Inference: 
 
Stata has very well outperformed R and Python with Female Data Enthusiasts and the possible explanation for this could be the increased penetration of Stata as a language in Academia and Research.

Here ends our Kaggling. Hope you enjoyed!
