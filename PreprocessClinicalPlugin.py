import os
import pandas as pd


import PyPluMA
import PyIO

class PreprocessClinicalPlugin:
    def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)
    def run(self):
        pass
    def output(self, outputfile):
        clinical_data_file = PyPluMA.prefix()+"/"+self.parameters["clinical_data_file"]
        metagenomics_file = PyPluMA.prefix()+"/"+self.parameters["metagenomics_file"]
        metabolomics_file = PyPluMA.prefix()+"/"+self.parameters["metabolomics_file"]
        irrelevant_columns = PyIO.readSequential(PyPluMA.prefix()+"/"+self.parameters["irrelevant_columns"])
        clinical_df = pd.read_csv(clinical_data_file)
        clinical_df = clinical_df.drop(irrelevant_columns, axis=1)
        clinical_df_filtered = clinical_df.loc[:, (clinical_df != clinical_df.iloc[0]).any()]
        clinical_df_filtered = clinical_df_filtered.sort_values(by="pilotpid").reset_index(drop=True)
        metagen = pd.read_csv(metagenomics_file, index_col=0).reset_index(drop=True)
        metabolon = pd.read_csv(metabolomics_file, index_col=0).reset_index(drop=True)
        combined_df = clinical_df_filtered.join(metagen, how="left")
        combined_df = combined_df.join(metabolon, how="left")
        combined_df.to_csv(outputfile, index=False)

