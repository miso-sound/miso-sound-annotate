# miso-sound-annotate

Goal: annotating 5+ instances of 10+ audio files (e.g. onset & offset of sound of interest, salience)
Sound Search Steps:
- Populate "current_term_present" and "other_term_present" columns with "yes", "no", or "unsure". Populate "notes" with notable descriptions and any other present sounds. 
- Populate "background_noise_present" column. Use "yes", "no", or "unsure" labels. 
- Continue process for given class until 5 instances have "no" under "background_noise_present", then move to next class. 
Audacity Labeling Steps:
- Download each of the 5 sounds from 10 classes. 
- Highlight and label each sound in audacity (including the "other_term_present" labels). 
- file>export>export labels
- Save .txt file as "NumberAtTheEndOfURL_labels.txt" (Ex. "180150_labels.txt"). 
Taxonomy Labeling Steps:
- Add each label created in Audacity to the JSON viewer or JSON file directly in GitHub. Use appropriate parent sounds. 
- Commit changes to GitHub. 
