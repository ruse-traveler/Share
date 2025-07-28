# =============================================================================
## @file   CalculateJESRWithPODIO.py
#  @author Derek Anderson, building on work by Brian Page
#  @date   07.28.2025
# -----------------------------------------------------------------------------
#  Example python script that calculates the Jet Energy Scale (JES) and
#  Resolution (JER) from EICrecon output using PODIO interface. This
#  builds on the calculation originally implemented by Brian Page at
#
#    https://github.com/eic/physics_benchmarks/blob/master/benchmarks/Jets-HF/jets/analysis/jets.cxx
#
# =============================================================================

from array import array
from podio.reading import get_reader

import numpy as np
import matplotlib.pyplot as plt



def Calculate(input_file="root://dtn-eic.jlab.org//volatile/eic/EPIC/RECO/25.06.1/epic_craterlake/DIS/NC/10x100/minQ2=10/pythia8NCDIS_10x100_minQ2=10_beamEffects_xAngle=-0.025_hiDiv_5.1287.eicrecon.edm4eic.root"):

    # use podio reader to open example EICrecon output
    reader = get_reader(input_file)

    # now loop through all events in output
    for iframe, frame in enumerate(reader.get("events")):

        # TEST
        print(f"This is event {iframe}")
        if iframe >= 100:
            break

        # grab collection of jets
        # available options:
        #   - ReconstructedChargedJets
        #   - GeneratedChargedJets
        #   - ReconstructedJets
        #   - GeneratedJets
        #   - ReconstructedCentauroJets
        #   - GeneratedCentauroJets
        gen_jets = frame.get("GeneratedChargedJets")
        rec_jets = frame.get("ReconstructedChargedJets")

        # loop through generated jets
        igen = 0
        for gjet in gen_jets:

            # TEST
            print(f"  This is gen jet {igen}")
            print(f"    energy = {gjet.getEnergy()}")
            igen = igen + 1

            # calculate pseudorapidity, azimuth
            gpt = np.sqrt((gjet.getMomentum().x**2) + (gjet.getMomentum().y**2))
            gphi = np.arctan2(gjet.getMomentum().y, gjet.getMomentum().x)
            gtheta = np.arctan2(gpt, gjet.getMomentum().z)
            geta = -np.log(np.tan(gtheta))/2
            print(f"    eta = {geta}, phi = {gphi}")

            # FIXME some eta's are NaNs...
            if np.isnan(geta):
                print(f"      ---> Gen NAN!") # TEST
                continue

            # select only jets in |eta_max| - R =
            # 3.5 - 1 = 2.5 (to avoid jets cut off
            # by acceptance)
            if np.abs(geta) > 2.5:
                print(f"      ---> Out of acceptance!") # TEST
                continue 

            # filter out generated jets with electrons
            # in them (to avoid DIS electron)
            has_electron = False
            for gcst in gjet.getParticles():
                if gcst.getPDG() == 11:
                    has_electron = True
                    print(f"      ---> has electron!") # TEST
                    continue

            # loop through reconstructed jets to find closest
            # one in eta-phi space
            irec = 0
            match = None
            min_dist = 9999.
            for rjet in rec_jets:

                # TEST
                print(f"      This is reco jet {irec}")
                print(f"        energy = {rjet.getEnergy()}")
                irec = irec + 1

                # calculate pseudorapidity, azimuth
                rpt = np.sqrt((rjet.getMomentum().x**2) + (rjet.getMomentum().y**2))
                rphi = np.arctan2(rjet.getMomentum().y, rjet.getMomentum().x)
                rtheta = np.arctan2(rpt, rjet.getMomentum().z)
                reta = -np.log(np.tan(rtheta))/2
                print(f"    eta = {reta}, phi = {rphi}")

                # FIXME some eta's are NaNs...
                if np.isnan(geta):
                    print(f"        ---> Rec NAN!") # TEST
                    continue

                # calculate distance in eta-phi space between
                # gen & reco jets
                deta = reta - geta
                dphi = rphi - gphi
                dist = np.sqrt((deta**2) + (dphi**2))

                # if reco jet is closest so far, set as match
                if dist < min_dist:
                    match = rjet
                    min_dist = dist


            # if no match found, continue 
            if match is None:
                continue

            # otherwise calculate ratios
            # TODO

# end =========================================================================
