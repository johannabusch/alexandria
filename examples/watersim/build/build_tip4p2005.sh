#!/bin/sh

LABEL=tip4p2005

SYSFILE=$LABEL.sys

cat > $SYSFILE <<EOF 
#
#    TIP4P/2005 model for liquid water:
#    J.L.F. Abascal and C. Vega, J. Chem. Phys. 123, 234505 (2005)
#
begin{sites}  
   OW     0.00     15.9994
   HW     0.5564    1.0079
   VW    -1.1128    0.0
end{sites}
begin{lorentz_lj}  
   OW   3.1589   93.2
   HW   0.0       0.0
   VW   0.0       0.0
end{lorentz_lj}
#
begin{molecule}
   label sol
   begin{configuration} 
      OW    0.0       0.0        0.0              
      HW    0.75695   0.585882   0.0        
      HW   -0.75695   0.585882   0.0        
      VW    0.0       0.15       0.0
   end{configuration}
   begin{virtual}
      4    1  0.743976   2  0.128012    3   0.128012
   end{virtual}
   begin{constraints} 
      1  2   0.9572
      1  3   0.9572
      2  3   1.5139
   end{constraints}
   begin{exclude}
      all
   end{exclude}
end{molecule}
#
begin{build}
   ecell         3.80 3.80 3.80 
   duplicate     4 4 4 
   frac          sol   0.5   0.5   0.5
   frac          sol   0.0   0.0   0.0
end{build}
EOF

sysbuild  -sys $SYSFILE > $LABEL.str


cat >moscito.par<<EOF
#...........................Forcefield declaration
#...........................Startup configuration
structurefile
#structurefile velocities
#restart
stop  momentum
#...........................Force calculation
rcut                9.0
neighborlist        linkcell  10 
rcutnb              12.0
#...........................SHAKE setup
shake               0.0001 
#...........................Ewald summation setup
ewald   # newton  
alpha   5.36
#kspace 5 5 5 27
kspace pme 16 16 16 4 
conserve
#...........................MD run specifications
timestep            2.0 
steps               400 
#...........................Weak coupling control
temperature         300.0 
pressure            0.1
scale  temperature  1.0
#scale  pressure     5.0e-7
#scale  pressure y   5.0e-7 independently
#scale  stop         500
#...........................MD-Output setup
firststep      1
#crddata      10 
#veldata      10    
sysdata        1
logdata       10  
restartdata 1000
EOF

moscito -par moscito.par -sys tip4p2005.sys -in $LABEL.str -v 
cat mosout.str | sortstr -sys tip4p2005.sys  > big.str
directdens=`infostr -sys tip4p2005.sys < big.str | grep Density | awk '{print $3}'`
erwartung=0.99712053360239020
factor=`echo "$erwartung / $directdens" | bc -l`
changedens ${factor}<big.str>scaled.str
mos2gro -sys tip4p2005.sys -in scaled.str -tip4p2005 1 -gv40 -g start.gro -t topol.top


