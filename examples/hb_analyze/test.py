#!/usr/bin/env python3.8

from alexandria import hb_analyze
import MDAnalysis

trajectory="/home/ptc/Jneumann/examples/watersim/sim1.xtc"
topology="/home/ptc/Jneumann/examples/watersim/sim1.tpr"
xname = "ow"
hname = "hw"

u = MDAnalysis.Universe(topology, trajectory, tpr_resid_from_one=False)
xgrp = u.select_atoms("name "+str(xname))
hgrp = u.select_atoms("name "+str(hname))[::2]

hb_analyze.hb_analyze(universe=u, xgrp=xgrp, hgrp=hgrp, rmin=1.5, rmax=5, cosalphamin=-1, cosalphamax=1, bins=50)
