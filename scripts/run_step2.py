# additional line for VS studio
import sys
sys.path.append('C:\\Users\\pathiran\\Documents\\Energy_system_modelling\\EnergyScope_multi_cells')
from esmc import Esmc


# TODO add logging

tds = [38]#[12,36]#np.arange(36,38,4)#[2,4,6,8,10,12]#,16,20,24,28,32,36,40,44,48]

for t in tds:
    print('Nbr_TDs',t)
    # dir_str = r'D:\case_studies\ES-PT_FR_IE-UK\TD_analysis\GwpLimit=136884_'+str(t)+r'TDs\outputs'
    #     #r'C:\Users\pathiran\Documents\Energy_system_modelling\EnergyScope_multi_cells\case_studies\ES-PT_FR_IE-UK\GwpLimit=136884_'+str(t)+r'TDs\outputs'
    # directory = Path(dir_str)

    gwp_limit_overall = 136884
    # define configuration
    config = {'case_study': 'GwpLimit='+str(gwp_limit_overall)+'_'+str(t)+'TDs',
              'comment': 'no comment',
              'regions_names': ['ES-PT', 'FR', 'IE-UK'],
              'ref_region': 'FR',
              'gwp_limit_overall': gwp_limit_overall,
              'year': 2035}
    # initialize EnergyScope Multi-cells framework
    my_model = Esmc(config, nbr_td=t)

    # read the indep data
    my_model.read_data_indep()

    # initialize the different regions and reads their data
    my_model.init_regions()

    # Initialize and solve the temporal aggregation algorithm:
    # if already run, set algo='read' to read the solution of the clustering
    # else, set algo='kmedoid' to run kmedoid clustring algorithm to choose typical days (TDs)
    my_model.init_ta(algo='kmedoid')

    # Print the time related data of the energy system optimization model using the TDs to represent it
    my_model.print_td_data()

    # Set the Energy Sytem Optimization Model (ESOM) as an ampl formulated problem
    my_model.set_esom()

    # # Read the outputs from previously solved proble
    # my_model.esom.read_outputs(directory=directory)
    # # Print as pickle
    # my_model.esom.print_outputs(directory=directory, solve_time=True)


    # Solving the ESOM
    my_model.solve_esom()
    # Printing the results
    # my_model.prints_esom(solve_time=True)

    # Getting and printing year results
    my_model.get_year_results()

    my_model.prints_esom(inputs=True, outputs=True, solve_time=True)

    # delete ampl object to free resources
    my_model.esom.ampl.close()