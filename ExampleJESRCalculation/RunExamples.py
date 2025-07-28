# =============================================================================
## @file   RunExamples.py
#  @author Derek Anderson
#  @date   07.28.2025
# -----------------------------------------------------------------------------
#  Driver script to run example JES/R example
#  calculations 
# =============================================================================

import  CalculateJESRWithPODIO as cjpd



# example file from simulation campaign
example_file = "root://dtn-eic.jlab.org//volatile/eic/EPIC/RECO/25.06.1/epic_craterlake/DIS/NC/10x100/minQ2=10/pythia8NCDIS_10x100_minQ2=10_beamEffects_xAngle=-0.025_hiDiv_5.1287.eicrecon.edm4eic.root" 

# run calculation using PODIO interface 
cjpd.Calculate(example_file) 

# run calculation using pure uproot
# TODO

# make some histograms

# end =========================================================================
