from asr_framework.asr_persistent import *
from asr_framework.asr_rules_dict import *

t383_dict=asr_load_csv_rules('lemmas_rules.csv','./open-data/dictionnaires/')
wr_dict=asr_load_csv_rules('wikipedia_dynamic_rules.csv','./open-data/dictionnaires/')
new_dict=asr_merge_rules_dicts(most_reliable_rules_dict=t383_dict,less_reliable_rules_dict=wr_dict)
asr_save_csv_rules(new_dict,file_name='rules_to_embed.csv',base_dir='./open-data/dictionnaires/')