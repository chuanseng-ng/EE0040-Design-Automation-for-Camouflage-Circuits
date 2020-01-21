# FYP-EEE
AY19/20 EEE FYP Camouflaging Logic Gates

## Pre-requisites:
pip install pandas

Netlists (Clean/Edited) should be placed in '.\\Simulator\\Original Netlist\\Sample' directory

Modify netlists to suit current library format prior to usage

```
AND   -> HS65_LH_AND2X4
OR    -> HS65_LH_OR2X4
NAND  -> HS65_LH_NAND2X2
NOR   -> HS65_LH_NOR2X2
XOR   -> HS65_LHS_XOR2X3
XNOR  -> HS65_LHS_XNOR2X3
```

---------------------------------------------------------------------------------------------------------------------------------

## Part 1:
Camouflage logic gates based on pre-determined pattern

```
AND <-> NOR
OR  <-> NAND
XOR <-> XNOR
```

Logic gates are chosen based on their output corruptibility (Number of bits that are different from original/Total bits)
Highest output corruptibility will be chosen to be camouflaged

Output corruptibility will only be calculated once, regardless of number of logic gates needed to be camouflaged
Number of logic gates to be camouflaged = user-inputted % of total number of logic gates

- Example: 3 logic gates need to be camouflaged
  Logic gates with top 3 output corruptibility will be chosen

---------------------------------------------------------------------------------------------------------------------------------

## Part 2:
Attacking camouflaged logic circuit to reveal original functionality of camouflaged logic gates
2 possible methods -
  1. Process one camouflage gate combination at a time after comparing all outputs with expected outputs
  2. Process all camouflage gate combination for each input combination after comparing the outputs with expected outputs and eliminate those that are different
 
Method 2 is faster than method 1

---------------------------------------------------------------------------------------------------------------------------------

## Part 3:
Allowing selection of logic gates that could be the correct gate

```
1. AND
2. NAND
3. OR
4. NOR
5. XOR
6. XNOR
```

Process flow will be the same as before, but with the removal of the pre-determined pattern

---------------------------------------------------------------------------------------------------------------------------------

## Current issues:
Flip-flop implemented as a sequential buffer, instead of a clock-based buffer
Outputs produced might not be completely correct, if circuit is unable to stabilize before simulation cycle upper limit is reached

Long runtime due to metastability declaration analysis
