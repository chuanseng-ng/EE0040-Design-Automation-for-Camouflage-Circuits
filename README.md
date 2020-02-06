# FYP-EEE
AY19/20 EEE FYP Camouflaging Logic Gates <br/>

## Pre-requisites:
pip install pandas <br/>

Netlists (Clean/Edited) should be placed in '.\\Netlist' directory <br/>
Modify netlist to suit current library prior to usage <br/>

```
AND   -> HS65_LH_AND2X4     (.Z(c), .A(a), .B(b) )
OR    -> HS65_LH_OR2X4      (.Z(c), .A(a), .B(b) )
NAND  -> HS65_LH_NAND2X2    (.Z(c), .A(a), .B(b) )
NOR   -> HS65_LH_NOR2X2     (.Z(c), .A(a), .B(b) )
XOR   -> HS65_LHS_XOR2X3    (.Z(c), .A(a), .B(b) )
XNOR  -> HS65_LHS_XNOR2X3   (.Z(c), .A(a), .B(b) )
DFF   -> HS65_LH_DFPRQX4    (.D(d), .CP(CLK), .RN(RST), .Q(q) )
NOT   -> HS65_LH_IVX2       (.Z(b), .A(a) )
```
<br/>

Change the logic gate types and inputs based on the original logic gates <br/>

---------------------------------------------------------------------------------------------------------------------------------

## Walkthrough:
Hands-on guide on executing Camouflage and Attack <br/>

Run main.py <br/>
```python main.py``` <br/>

Following prompt will appear: <br/> 
```Choose 1 to camouflage, 2 to attack the logic circuit``` <br/>
Select 1 or 2 depending on user <br/>

Next prompt will ask user to choose clean netlist from '.\\Netlist' directory <br/>
```Select clean file:``` <br/> <br/>

### Camouflage -
If 1 is selected, prompt will request for user-inputted percentage of logic gates to be camouflage <br/>
```State percentage of gates to be camouflaged.\n Default choice is 10% of total logic gates. (%):``` <br/>
As stated in prompt, default is 10% <br/>

Optimal choice of logic gates to be camouflaged is rendered through the analysis of the output corruptibility <br/>
Total number of logic gates that is camouflaged will be prompted, along with the logic gates' details <br/> <br/>

---------------------------------------------------------------------------------------------------------------------------------

### Attack -
If 2 is selected, prompt will ask user to choose camouflaged netlist from '.\\Netlist' directory <br/>
```Select Camo file:``` <br/>

Prompt will request user to choose logic gate types to be used in the attack <br/>
```
Please input the camouflaged gate combinations, one at a time.
1 - AND
2 - NAND
3 - OR
4 - NOR
5 - XOR
6 - XNOR
7 - End
``` 
<br/>

Each logic gate type only needs to be chosen once as all the possible combinations will be analyzed <br/> <br/>

Current rendition of brute force attack algorithm eliminates combinations that produces wrong set of output bits at every input combination <br/>
All possible logic gate combinations will be prompted once the attack analysis is completed <br/>
The total number of tries and logic gate combinations will also be prompted <br/> <br/>

Total time used to execute each process will be prompted after the process is completed <br/>


---------------------------------------------------------------------------------------------------------------------------------
## Process Flow:

### Part 1 -
Camouflage logic gates based on pre-determined pattern <br/>

```
AND <-> NOR
OR  <-> NAND
XOR <-> XNOR
```
<br/>

Logic gates are chosen based on their output corruptibility (Number of bits that are different from original/Total bits) <br/>
Highest output corruptibility will be chosen to be camouflaged <br/>

Output corruptibility will only be calculated once, regardless of number of logic gates needed to be camouflaged <br/>
Number of logic gates to be camouflaged = user-inputted % of total number of logic gates <br/>

Example: <br/>
- 3 logic gates need to be camouflaged <br/>
  Logic gates with top 3 output corruptibility will be chosen <br/>

---------------------------------------------------------------------------------------------------------------------------------

### Part 2 -
Attacking camouflaged logic circuit to reveal original functionality of camouflaged logic gates <br/>
2 possible methods - <br/>
  1. Process one camouflage gate combination at a time after comparing all outputs with expected outputs <br/>
  2. Process all camouflage gate combination for each input combination after comparing the outputs with expected outputs and eliminate those that are different <br/>
 
Method 2 is faster than method 1 <br/>

---------------------------------------------------------------------------------------------------------------------------------

### Part 3 -
Allowing selection of logic gates that could be the correct gate <br/>

```
1. AND
2. NAND
3. OR
4. NOR
5. XOR
6. XNOR
```
<br/>

Process flow will be the same as before, but with the removal of the pre-determined pattern <br/>

---------------------------------------------------------------------------------------------------------------------------------

### Current issues/Future works -
Flip-flop implemented as a sequential buffer, instead of a clock-based buffer <br/>
Outputs produced might not be completely correct, if circuit is unable to stabilize before simulation cycle upper limit is reached <br/>

Long runtime due to metastability declaration analysis <br/>
