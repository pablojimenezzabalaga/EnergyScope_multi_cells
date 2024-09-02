##########################
### OBJECTIVE FUNCTION ###
##########################

# Can choose between TotalGWP and TotalCost

#minimize obj:  sum{c in REGIONS} TotalCost[c] + 260 * (sum{c1 in REGIONS}(Exch_freight[c1]));
minimize obj:  sum{c in REGIONS} TotalCost[c];

## formula for GWP_op optimization
# sum{c in REGIONS, r in RESOURCES} (GWP_op [c,r]);
# 
