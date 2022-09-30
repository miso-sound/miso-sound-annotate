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
|  0 | swallowing               |        31.5382   |        3.15382  |                         10 |                           7 |
|  1 | slurping                 |        49.8157   |        2.07565  |                         24 |                           6 |
|  2 | lip_smacks               |        70.1987   |        4.67991  |                         15 |                           6 |
|  3 | basketball_dribbling     |       112.998    |        4.91295  |                         23 |                           5 |
|  4 | human_breathing          |       131.001    |       13.1001   |                         10 |                           5 |
|  5 | water_drops              |       374.744    |       34.0676   |                         11 |                           5 |
|  6 | typing                   |       109.908    |        6.46515  |                         17 |                           5 |
|  7 | knife_cutting            |        71.0147   |        5.46267  |                         13 |                           5 |
|  8 | plastic_crumpling        |        32.9493   |        4.70705  |                          7 |                           5 |
|  9 | flipping_newspaper_pages |        78.3414   |        4.3523   |                         18 |                           5 |
| 10 | clearing_throat          |        55.9018   |        9.31697  |                          6 |                           5 |
| 11 | chewing_gum              |        50.0861   |        5.56512  |                          9 |                           5 |
| 12 | recording_artifact       |        28.3371   |        5.66742  |                          5 |                           4 |
| 13 | exhaling                 |        14.0364   |        1.55959  |                          9 |                           4 |
| 14 | coughing                 |        18.3845   |        3.67691  |                          5 |                           3 |
| 15 | talking                  |         8.72669  |        2.18167  |                          4 |                           3 |
| 16 | footsteps                |         2.07991  |        1.03996  |                          2 |                           2 |
| 17 | tapping                  |        13.2682   |        2.65363  |                          5 |                           2 |
| 18 | mouth_sounds_other       |         9.60523  |        3.20174  |                          3 |                           1 |
| 19 | birds_chirping           |         3.79394  |        3.79394  |                          1 |                           1 |
| 20 | sliding_ceramic          |         1.98347  |        0.991737 |                          2 |                           1 |
| 21 | squishing                |         4.94966  |        4.94966  |                          1 |                           1 |
| 22 | tearing_paper            |         1.86925  |        1.86925  |                          1 |                           1 |
| 23 | whimpering               |         0.214064 |        0.214064 |                          1 |                           1 |
<!---
stop_sync_summary_table_label
-->
