#!/usr/bin/env python3.8

from alexandria.gofr import Gofr
import MDAnalysis

trajectory="/home/ptc/Jneumann/examples/watersim/sim1.xtc"
topology="/home/ptc/Jneumann/examples/watersim/sim1.tpr"

u = MDAnalysis.Universe(topology, trajectory)
hgrp = u.select_atoms("name hw")
ogrp = u.select_atoms("name ow")
watergrp = u.select_atoms("resname SOL")

sitesite = Gofr(universe=u, agrp=hgrp, bgrp=ogrp, rmin=1.0, rmax=6, bins=200, mode="site-site", outfilename="h_o.dat")
cmscms = Gofr(universe=u, agrp=watergrp, bgrp=watergrp, rmin=1.0, rmax=6, bins=200, mode="cms-cms", outfilename="cms_cms.dat")
sitecms = Gofr(universe=u, agrp=hgrp, bgrp=watergrp, rmin=1.0, rmax=6, bins=200, mode="site-cms", outfilename="h_cms.dat")
