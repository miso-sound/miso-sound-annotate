# miso-sound-annotate

Goal: annotating 5+ instances of 10+ audio files (e.g. onset & offset of sound of interest, salience)

## Sound Search Steps
- Populate "current_term_present" and "other_term_present" columns with "yes", "no", or "unsure". Populate "notes" with notable descriptions and any other present sounds. 
- Populate "background_noise_present" column. Use "yes", "no", or "unsure" labels. 
- Continue process for given class until 5 instances have "no" under "background_noise_present", then move to next class. 

## Audacity Labeling Steps
- Download each of the 5 sounds from 10 classes. 
- Highlight and label each sound in audacity (including the "other_term_present" labels). 
- file>export>export labels
- Save .txt file as "NumberAtTheEndOfURL_labels.txt" (Ex. "180150_labels.txt"). 

## Taxonomy Labeling Steps
- Add each label created in Audacity to the JSON viewer or JSON file directly in GitHub. Use appropriate parent sounds. 
- Commit changes to GitHub.

## Summary of all labels

<!---
start_sync_summary_table_label
-->
|    | Label                    |   Total duration |   Mean duration |   Count of label instances |   Count of files with label |
|---:|:-------------------------|-----------------:|----------------:|---------------------------:|----------------------------:|
|  0 | talking                  |       345.675    |        5.2375   |                         66 |                           8 |
|  1 | swallowing               |        31.5382   |        3.15382  |                         10 |                           7 |
|  2 | slurping                 |        49.8157   |        2.07565  |                         24 |                           6 |
|  3 | plastic_crumpling        |        40.1139   |        5.01424  |                          8 |                           6 |
|  4 | lip_smacks               |        70.1987   |        4.67991  |                         15 |                           6 |
|  5 | artifact                 |        20.7815   |        1.15453  |                         18 |                           5 |
|  6 | hairdryer                |        68.145    |       11.3575   |                          6 |                           5 |
|  7 | water_drops              |       374.744    |       34.0676   |                         11 |                           5 |
|  8 | typing                   |       109.908    |        6.46515  |                         17 |                           5 |
|  9 | recording_artifact       |        33.1993   |        3.68881  |                          9 |                           5 |
| 10 | basketball_dribbling     |       112.998    |        4.91295  |                         23 |                           5 |
| 11 | human_breathing          |       131.001    |       13.1001   |                         10 |                           5 |
| 12 | harp                     |        50.3091   |       10.0618   |                          5 |                           5 |
| 13 | knife_cutting            |        71.0147   |        5.46267  |                         13 |                           5 |
| 14 | chewing_gum              |        50.0861   |        5.56512  |                          9 |                           5 |
| 15 | coughing                 |        24.8287   |        2.48287  |                         10 |                           5 |
| 16 | coffee_shop              |       812.557    |      162.511    |                          5 |                           5 |
| 17 | clearing_throat          |        55.9018   |        9.31697  |                          6 |                           5 |
| 18 | flipping_newspaper_pages |        78.3414   |        4.3523   |                         18 |                           5 |
| 19 | clicking                 |         2.62047  |        0.327559 |                          8 |                           4 |
| 20 | exhaling                 |        14.0364   |        1.55959  |                          9 |                           4 |
| 21 | laughing                 |         8.29786  |        1.38298  |                          6 |                           3 |
| 22 | footsteps                |         2.07991  |        1.03996  |                          2 |                           2 |
| 23 | tapping                  |        13.2682   |        2.65363  |                          5 |                           2 |
| 24 | sliding_ceramic          |        15.5101   |        3.87754  |                          4 |                           2 |
| 25 | squishing                |         4.94966  |        4.94966  |                          1 |                           1 |
| 26 | singing                  |        48.7992   |        9.75984  |                          5 |                           1 |
| 27 | mouth_sounds_other       |         9.60523  |        3.20174  |                          3 |                           1 |
| 28 | drumming                 |         7.69038  |        7.69038  |                          1 |                           1 |
| 29 | tearing_paper            |         1.86925  |        1.86925  |                          1 |                           1 |
| 30 | birds_chirping           |         3.79394  |        3.79394  |                          1 |                           1 |
| 31 | beeping                  |        44.2997   |       22.1499   |                          2 |                           1 |
| 32 | whimpering               |         0.214064 |        0.214064 |                          1 |                           1 |
<!---
stop_sync_summary_table_label
-->
