# AY19/20 EEE FYP A2068-191 <br/>

- [AY19/20 EEE FYP A2068-191 <br/>](#ay1920-eee-fyp-a2068-191-br)
  - [Required Python Modules <br/>](#required-python-modules-br)
  - [Set-up <br/>](#set-up-br)
  - [Walkthrough: <br/>](#walkthrough-br)
    - [Camouflage <br/>](#camouflage-br)
    - [Attack <br/>](#attack-br)
    - [Execution Time <br/>](#execution-time-br)
  - [Process Flow: <br/>](#process-flow-br)
    - [Part 1 (Camouflage Implementation) <br/>](#part-1-camouflage-implementation-br)
    - [Part 2 (Camouflage Attack) <br/>](#part-2-camouflage-attack-br)
    - [Part 3 (User-selected Camouflage Attack) <br/>](#part-3-user-selected-camouflage-attack-br)
  - [Current Issues/Future Works: <br/>](#current-issuesfuture-works-br)
    - [Clock-based Flip-flop <br/>](#clock-based-flip-flop-br)
    - [Sensitization <br/>](#sensitization-br)
    - [Compounded Output Corruptibility](#compounded-output-corruptibility-)
    - [CPU/GPU Processing Capability](#cpugpu-processing-capability-)

---

## Required Python Modules <br/>

Install pandas in order for algorithm to operate as intended <br/>
`pip install pandas` <br/>

---

## Set-up <br/>

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

Change the logic gate types and inputs based on the original logic gates <br/>

Remove all sub-modules, leaving only the main module intact <br/>
Flip-flop modules, etc, are not needed in this analysis <br/>

Move flip-flops and inverters to the end of the list of logic gates to ensure that algorithm works <br/>
If in doubt, use existing files in '.\Netlist' as reference <br/> <br/>

---

## Walkthrough: <br/>

Hands-on guide on executing Camouflage and Attack <br/>

Run main.py</div> <br/>
`python main.py` <br/>

Following prompt will appear: <br/> 
`Choose 1 to camouflage, 2 to attack the logic circuit` <br/>
Select 1 or 2 depending on user <br/>

Next prompt will ask user to choose clean netlist from '.\\Netlist' directory <br/>
`Select clean file:` <br/> <br/>

---

### Camouflage <br/>

If 1 is selected, prompt will request for user-inputted percentage of logic gates to be camouflage <br/>
`State percentage of gates to be camouflaged.\n ` <br/>
`Default choice is 10% of total logic gates. (%):` <br/>
As stated in prompt, default is 10% <br/>

Optimal choice of logic gates to be camouflaged is rendered through the analysis of the output corruptibility <br/>
Total number of logic gates that is camouflaged will be prompted, along with the logic gates' details <br/> <br/>

---

### Attack <br/>

If 2 is selected, prompt will ask user to choose camouflaged netlist from '.\\Netlist' directory <br/>
`Select Camo file:` <br/>

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

Each logic gate type only needs to be chosen once as all the possible combinations will be analyzed <br/>

Current rendition of brute force attack algorithm eliminates combinations that produces wrong set of output bits at every input combination <br/>
All possible logic gate combinations will be prompted once the attack analysis is completed <br/>
The total number of tries and logic gate combinations will also be prompted <br/>

Total time used to execute each process will be prompted after the process is completed <br/> <br/>

---

### Execution Time <br/>

The execution time for each process are shown in the '.\Statistics' directory <br/>

```
Testing System Specs:
- CPU: i7-2670QM @ 2.20GHz
- RAM: 8GB DDR3 1600MHz
- GPU: GT555M
```

However, execution time is long due to under-utilization and inefficient usage of CPU <br/> <br/>

---

## Process Flow: <br/>

### Part 1 (Camouflage Implementation) <br/>

Camouflage logic gates based on pre-determined pattern <br/>

```
AND <-> NOR
OR  <-> NAND
XOR <-> XNOR
```

Logic gates are chosen based on their output corruptibility (Number of bits that are different from original/Total bits) <br/>
Highest output corruptibility will be chosen to be camouflaged <br/>

Output corruptibility will only be calculated once, regardless of number of logic gates needed to be camouflaged <br/>
Number of logic gates to be camouflaged = user-inputted % of total number of logic gates <br/>

Example: <br/>
- 3 logic gates need to be camouflaged <br/>
  Logic gates with top 3 output corruptibility will be chosen <br/>

---

### Part 2 (Camouflage Attack) <br/>

Attacking camouflaged logic circuit to reveal original functionality of camouflaged logic gates <br/>
2 possible methods - <br/>
  1. Process one camouflage gate combination at a time after comparing all outputs with expected outputs <br/>
  2. Process all camouflage gate combination for each input combination after comparing the outputs with expected outputs and eliminate those that are different <br/>
 
Method 2 is faster than method 1 <br/>

---

### Part 3 (User-selected Camouflage Attack) <br/>

Allowing selection of logic gates that could be the correct gate <br/>

```
1. AND
2. NAND
3. OR
4. NOR
5. XOR
6. XNOR
```

Process flow will be the same as before, but with the removal of the pre-determined pattern <br/>

Current attack algorithm utilizes elimination of non-viable logic gate combinations to reduce total execution time <br/>

Previous attack algorithm performs a full iteration of all logic gate combinations <br/>
Full iteration algorithm can be analyzed [here](https://github.com/waelectriz/EE0040-Old-Attack "Full Iteration") <br/>

---

## Current Issues/Future Works: <br/>

### Clock-based Flip-flop <br/>

Flip-flop implemented as a sequential buffer, instead of a clock-based buffer <br/>
Outputs produced might not be completely correct, if circuit is unable to stabilize before simulation cycle upper limit is reached <br/>

Long runtime due to metastability analysis can also be eliminated when a global clock is implemented <br/>

---

### Sensitization <br/>

Implement camouflaged logic gate sensitization <br/>

Sensitization is the process in which the primary inputs are traced towards the camouflaged logic gates' inputs, and the primary outputs are traced backwards to the camouflaged logic gates' outputs <br/>
This helps to determine the complete or partial functionality of the camouflaged logic gates <br/>

However, sensitization is only to reveal the partial functionality of cascaded camouflaged logic gates <br/>

---

### Compounded Output Corruptibility <br/>

Analyze suitability for logic gates to be camouflaged with relation to each other <br/>
Compounded output corruptibility calculation instead of current simple one <br/>
Produces cascaded camouflaged logic gates, which affect each other's inputs/outputs <br/>
Example: <br/>
- Recalculate output corruptibility whenever a logic gate is chosen to be camouflaged <br/>
- If 3 logic gates are needed to be camouflaged, initial output corruptibility list will be used to choose first gate <br/>
- Subsequent chosen logic gate will be determined by recalculating the output corruptibility list, while taking into account the modified logic gate <br/>

---

### CPU/GPU Processing Capability <br/>

Implementation of CPU Parallel Processing or GPU Processing to reduce the execution time <br/>
CPU excels in doing multiple tasks at the same time, while GPU excels in doing one task very quickly <br/>
