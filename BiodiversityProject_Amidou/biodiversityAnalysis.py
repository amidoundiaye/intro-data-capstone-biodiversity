#Amidou N'Diaye

#Biodiversity Project
#=====================

import codecademylib
#1.1) pandas and matplotlib
import pandas as pd
from matplotlib import pyplot as plt

# 1.2 Loading the Data
species = pd.read_csv('species_info.csv')

#1.3) Print and inspect dataFrame
 print species.head()

#2.1) How many different species are in the speciesDataFrame?
species_count = species.scientific_name.nunique()

#2.2) What are the different values of category in the DataFrame species?
species_type = species.category.unique()

#2.3) What are the different values of conservation_status?
conservation_statuses = species.conservation_status.unique()

#3.1) Use groupby to count how many scientific_name falls into each conservation_status criteria
conservation_counts = species.groupby('conservation_status').scientific_name.nunique().reset_index()

#3.2) Print conservation_counts and take a minute to think about what the DataFrame is telling you
print conservation_counts

#4.1) replace NaN in our DataFrame with 'No Intervention'
species.fillna('No Intervention', inplace = True)

#4.2) run the same groupby as before to see how many species require No Intervention
conservation_counts_fixed = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print conservation_counts_fixed

#5. Plotting Conservation Status by Species
#5.1) create a new DataFrame called protection_counts, which is sorted by scientific_name
protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')
#5.2)     
plt.figure(figsize=(10, 4))
ax = plt.subplot()
plt.bar(range(len(protection_counts)),protection_counts.scientific_name.values)
ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts.conservation_status.values)
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')
labels = [e.get_text() for e in ax.get_xticklabels()]
plt.show()

#6-  Investigating Endangered Species

#6.1) Create a new column in species called is_protected
species['is_protected'] = species.conservation_status != 'No Intervention'

#6.2) group by both category and is_protected
category_counts = species.groupby(['category', 'is_protected'])\
                  .scientific_name.nunique()\
                  .reset_index()

#6.3 Examine category_counts.head()
print category_counts.head()

#6.4) Pivot
category_pivot = category_counts.pivot(columns='is_protected',
                      index='category',
                      values='scientific_name')\
                      .reset_index()
#6.5) examine pivot  
print category_pivot


#7- Investigating Endangered Species II
#7.1) Renaming column
category_pivot.columns = ['category', 'not_protected', 'protected']

#7.2)
category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)

#7.3
print category_pivot


#8 - Chi-Squared Test for Significance
#8.1 & 8.2) Create a table called contingency
from scipy.stats import chi2_contingency
contingency = [[30, 146],
              [75, 413]]

#8.3) Run chi2_contingency on the contingencytable
pval = chi2_contingency(contingency)[1]
print(pval) # pval > 0.05 no significant difference


#8.4
contingency_reptile_mammal = [[30, 146],
                              [5, 73]]

pval_reptile_mammal = chi2_contingency(contingency_reptile_mammal)[1]
print(pval_reptile_mammal)# pval_reptile_mammal < 0.05, Significant difference



#10 - Observations DataFrame
import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'

observations = pd.read_csv('observations.csv')

print observations.head()

#11 - In Search of Sheep
import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'

observations = pd.read_csv('observations.csv')

species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)

species_is_sheep = species[species.is_sheep]

print species_is_sheep

sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]

print sheep_species

#12 - Merging Sheep and Observation DataFrames
import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'

observations = pd.read_csv('observations.csv')

species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)

species_is_sheep = species[species.is_sheep]

sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]

sheep_observations = observations.merge(sheep_species)

print sheep_observations.head()

obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()

print obs_by_park

#13 - Plotting Sheep Sightings
import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)
sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]

observations = pd.read_csv('observations.csv')

sheep_observations = observations.merge(sheep_species)

obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()

plt.figure(figsize=(16, 4))
ax = plt.subplot()
plt.bar(range(len(obs_by_park)),
        obs_by_park.observations.values)
ax.set_xticks(range(len(obs_by_park)))
ax.set_xticklabels(obs_by_park.park_name.values)
plt.ylabel('Number of Observations')
plt.title('Observations of Sheep per Week')
plt.show()

#14 - Foot and Mouth Reduction Effort - Sample Size Determination
baseline = 15

minimum_detectable_effect = 100*5./15

sample_size_per_variant = 870

yellowstone_weeks_observing = sample_size_per_variant/507

bryce_weeks_observing = sample_size_per_variant/250






