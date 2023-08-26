# PreprocessClinical
# Language: Python
# Input: TXT
# Output: CSV
# Tested with: PluMA 1.1, Python 3.6
# Dependency: pandas==1.1.5

Clinical data preprocessor.

Input is a TXT file of keyword-value pairs (Tab-delimited):

clinical_data_file: Clinical data, CSV
metagenomics_file: Taxa abundances, CSV
metabolomics_file: Metabolite concentrations, CSV
irrelevant_columns: Columns to ignore

Output clinical data is CSV
