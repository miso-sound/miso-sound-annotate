# Annotation guide 

## Labeling relevant sounds

-   In Audacity, label the onset and offset (50 ms precision) of each instance of a sound with a salience label and a
sufficiently detailed descriptive label:

    - The salience label is a (subjective) assessment of the sound's 
    presence: 1 = foreground, 2 = background. [Here](https://github.com/miso-sound/urban-sound-example/tree/main/example_data) are some examples from the UrbanSound database.

    -   The descriptive label may not match the search terms exactly and
    may vary in level of detail (e.g. "woman sniffling" could be
    provided in the Freesound user metadata but if not, it may not be possible to
    determine a more detailed label than "sniffling"). For each new
    descriptor, add it to the [taxonomy file](https://github.com/miso-sound/miso-sound-taxonomy/blob/main/terms/taxonomy_for_annotations.json) containing descriptive
    labels and umbrella categories.

    - Each label has the following format: `C[salience_label]-[descriptive_label]`

- All the labels for each audio file are exported as a text file that is named in the following format: `[freesound_id]_labels.txt`

- Each text file has a corresponding entry in the [label metadata spreadsheet](https://github.com/miso-sound/miso-sound-annotate/blob/main/labels/label_info.csv) with the file name and the version of the taxonomy file used.
