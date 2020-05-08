# AY19/20 EEE FYP A2068-191

- [AY19/20 EEE FYP A2068-191](#ay1920-eee-fyp-a2068-191)
  - [Required Python Modules](#required-python-modules)
  - [Set-up](#set-up)
  - [Walkthrough:](#walkthrough)
    - [Camouflage](#camouflage)
    - [Attack](#attack)
  - [Process Flow:](#process-flow)
    - [Part 1 (Camouflage Implementation)](#part-1-camouflage-implementation)
    - [Part 2 (Camouflage Attack)](#part-2-camouflage-attack)
    - [Part 3 (User-selected Camouflage Attack)](#part-3-user-selected-camouflage-attack)
  - [Current Issues/Future Works:](#current-issuesfuture-works)
    - [Clock-based Flip-flop](#clock-based-flip-flop)
    - [Compounded Output Corruptibility](#compounded-output-corruptibility)
    - [Sensitization](#sensitization)
    - [Customizable Logic Gate Attack Pattern](#customizable-logic-gate-attack-pattern)
    - [CPU/GPU Processing Capability](#cpugpu-processing-capability)

---

## Required Python Modules

Install pandas in order for algorithm to operate as intended <br/>
`pip install pandas` <br/>
`pip install tqdm` <br/>

---

## Set-up

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

## Walkthrough:

Hands-on guide on executing Camouflage and Attack <br/>

Run main.py</div> <br/>
`python main.py` <br/>

Following prompt will appear: <br/> 
`Choose 1 to camouflage, 2 to attack the logic circuit` <br/>
Select 1 or 2 depending on user <br/>

Next prompt will ask user to choose clean netlist from '.\\Netlist' directory <br/>
`Select clean file:` <br/> <br/>

---

### Camouflage

If 1 is selected, prompt will request for user-inputted percentage of logic gates to be camouflage <br/>
`State percentage of gates to be camouflaged.\n ` <br/>
`Default choice is 10% of total logic gates. (%):` <br/>
As stated in prompt, default is 10% <br/>

Optimal choice of logic gates to be camouflaged is rendered through the analysis of the output corruptibility <br/>
Total number of logic gates that is camouflaged will be prompted, along with the logic gates' details <br/> <br/>

---

### Attack

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

## Process Flow:

### Part 1 (Camouflage Implementation)

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

### Part 2 (Camouflage Attack)

Attacking camouflaged logic circuit to reveal original functionality of camouflaged logic gates <br/>
2 possible methods - <br/>
  1. Process one camouflage gate combination at a time after comparing all outputs with expected outputs <br/>
  2. Process all camouflage gate combination for each input combination after comparing the outputs with expected outputs and eliminate those that are different <br/>
 
Method 2 is faster than method 1 <br/>

---

### Part 3 (User-selected Camouflage Attack)

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

## Current Issues/Future Works:

### Clock-based Flip-flop

Flip-flop implemented as a sequential buffer, instead of a clock-based buffer <br/>
Outputs produced might not be completely correct, if circuit is unable to stabilize before simulation cycle upper limit is reached <br/>

Long runtime due to metastability analysis can also be eliminated when a global clock is implemented <br/>

---

### Compounded Output Corruptibility

Analyze suitability for logic gates to be camouflaged with relation to each other <br/>
Compounded output corruptibility calculation instead of current simple one <br/>
Produces cascaded camouflaged logic gates, which affect each other's inputs/outputs <br/>
Example: <br/>
- Recalculate output corruptibility whenever a logic gate is chosen to be camouflaged <br/>
- If 3 logic gates are needed to be camouflaged, initial output corruptibility list will be used to choose first gate <br/>
- Subsequent chosen logic gate will be determined by recalculating the output corruptibility list, while taking into account the modified logic gate <br/>

---

### Sensitization

Implement camouflaged logic gate sensitization <br/>

Sensitization is the process in which the primary inputs are traced towards the camouflaged logic gates' inputs, and the primary outputs are traced backwards to the camouflaged logic gates' outputs <br/>
This helps to determine the complete or partial functionality of the camouflaged logic gates <br/>

However, sensitization is only to reveal the partial functionality of cascaded camouflaged logic gates <br/>

---

### Customizable Logic Gate Attack Pattern

Implement logic gate attack combination generation based on logic gate types shown in netlist <br/>

Example: <br/>
- Current algorithm generates all logic gate types for all camouflaged gates regardless of whether camouflaged gate is of that logic gate type <br/>
  - `User-input: 1 2 3 4 5 6` <br/>
  - User-input shown above will always generate logic gate combinations for all six logic gate types <br/>
- Proposed algorithm will generate logic gate types for camouflaged gates based on their logic gate types shown in netlist <br/>
  - `AND/XOR NOR/NAND OR/XNOR` <br/>
  - Logic gate types shown above will only generate logic gate combinations based on the valid logic gate types <br/>
  - In this example, the first logic gate will only be tested for AND and XOR logic gates, the second will be tested for NOR and NAND logic gates and the third will be tested for OR and XNOR logic gates <br/>

---

### CPU/GPU Processing Capability

Implementation of CPU Parallel Processing or GPU Processing to reduce the execution time <br/>
CPU excels in doing multiple tasks at the same time, while GPU excels in doing one task very quickly <br/>
