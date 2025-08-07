# Example JES/R Calculation(s)

### Contributors
Derek Anderson (building on work by Brian Page)

### Dependencies
  * [ROOT](https://root.cern.ch)
  * [PODIO](https://github.com/AIDASoft/podio)
  * [EDM4hep](https://github.com/key4hep/EDM4hep)
  * [EDM4eic](https://github.com/eic/EDM4eic)

### Description
This set of python scripts illustrates how to calculate
the charged jet JES/R from the output of EICrecon.  Reference
slides can be found [here](https://docs.google.com/presentation/d/1NZNMcm0mUWhFazt7HLmaMxuSXLtmBIa-MWaqda8uits/edit?usp=sharing)

Currently, the only example here makes use of the PODIO
interface, so it's recommended to run this in the eic-
shell. If you pester me enough, I might be able to put
together a pure Uproot + NumPy example...
