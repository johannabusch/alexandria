#!/usr/bin/env python3.8

import MDAnalysis
from MDAnalysis.analysis import hbonds
from alexandria.lifetime import calc_lifetime

trajectory="/home/ptc/Jneumann/examples/watersim/sim1.xtc"
topology="/home/ptc/Jneumann/examples/watersim/sim1.tpr"
universe = MDAnalysis.Universe(topology, trajectory)

ygrp = universe.select_atoms("name ow")
hgrp = universe.select_atoms("name hw")
xgrp = hbonds.find_hydrogen_donors(hgrp)

calc_lifetime(universe=universe, timestep=0.2, xgrp=xgrp, hgrp=hgrp, ygrp=ygrp, cutoff_hy=2.5, angle_cutoff=2.27, cutoff_xy=3.5)
