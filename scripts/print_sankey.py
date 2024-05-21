from esmc.postprocessing.draw_sankey.output_to_sankey_csv import write_sankey_file
from esmc.postprocessing.draw_sankey.print_sankey_values import read_and_process_data
from esmc.postprocessing.draw_sankey.print_sankey_values import generate_sankey

write_sankey_file(space_id="BN_BN-IT_BN-YC_CB_CH_LP_OR_PA-NA_PT_SC_SC-AS_SC-CC_SC-CQ_SC-GB_SC-MI_SC-VC_SC-VL_TJ_TJ-BE_TJ-EP_TJ-OC", case_study="ref")
filepath = '/home/pjimenez/EnergyScope_multi_cells/case_studies/BN_BN-IT_BN-YC_CB_CH_LP_OR_PA-NA_PT_SC_SC-AS_SC-CC_SC-CQ_SC-GB_SC-MI_SC-VC_SC-VL_TJ_TJ-BE_TJ-EP_TJ-OC/ref/outputs/regional_results/'
num_decimals = 1
link_transparency = 0.5
node_color = '#3F7CAB'
df, labels = read_and_process_data(filepath, num_decimals)
generate_sankey(df, labels, link_transparency, node_color, filepath)
#drawSankey()