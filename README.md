# Dataset of Power-to-Voltage Sensitivity of Residential Loads
Here we provide a dataset of time-varying voltage sensitivity of common residential loads based on experiments on actual loads.

### List of Loads Under Test
| Load                   | Brand and Model       | Tested Operating Mode                                | 
|------------------------|------------------------|------------------------------------------------------|
| Condenser cloth dryer  | Miele T 8687 C         | Gentle cycle                                         |
| Cooker hood            | IKEA                   | Extraction level: medium                             |
| Dishwasher             | Miele G 1834 SCI       | Quick wash 40°C                                      |
| Electric hot plate     | Clatronic EKP 3582     | Maximum power level                                  |
| Fan                    | BaseTech VE-5985BT     | Maximum power level with head shaking                |
| Freezer                | Liebherr GN 3056-29    | Set temperature -20°C                                |
| Fridge                 | Bosch KG KIRR18A       | Maximum cooling level                                |
| Hair dryer             | Impuls SL-805          | Maximum wind level, medium heat level                |
| Halogen ceiling light set | --                  | Lights on                                            |
| Induction stove        | Miele KM 5955          | Maximum power level                                  |
| Water kettle           | Clatronic WKS 3692     | Cook 1.5L water                                      |
| Oven                   | Miele H5681BL          | Top and bottom heating, set temperature 280°C        |
| Microwave oven         | Renkforce MM720Ca7-PM  | Cook mode power level 4                              |
| Toaster                | Severin AT 2586L       | Maximum power level                                  |
| Dishwasher             | Miele G 1834 SCI       | Quick wash 40°C                                      |
| Vacuum cleaner         | Siemens VBBS607V00     | Smooth surface cleaning mode                         |
| Washing machine        | Miele 3985 WPS         | Cotton wash 1000rpm                                  |
| Laptop charger         | TOSHIBA PA3755U-1ACA   | As power supply                                      |
| LED light              | --                     | Light on                                             |
| Monitor                | Samsung BX2240         | Monitor on                                           |
| Oil radiator           | Clatronic RA 3735      | Set temperature 24°C                                 |

### Overview of Load Voltage Sensitivity Results
|  Load                      |          |    Kpv    |           |          |    Kqv    |           |           |   P0 (W)   |           |           |   Q0 (var)  |           |  Data Length |
|----------------------------|----------|-----------|-----------|----------|-----------|-----------|-----------|------------|-----------|-----------|-------------|-----------|--------------|
|                            | **min**  | **mean**  | **max**   | **min**  | **mean**  |  **max**  | **min**   | **mean**   | **max**   | **min**   |   **mean**  |  **max**  |              |
| Apartment                  |  0.00    | 0.87      | 1.98      |  0.00    | 1.15      | 1.91      |    32     |    1399    |  5876     |    265    |     386     |    716    |   5 hour     |
| Apartment with aggregated Heater|  0.00   | 1.48    | 1.98     |  -       |    -      |    -     |    32     |    2618    |  7368     |     -     |     -       |     -     |   5 hour     |
| Cloth dryer                |  1.10    | 1.73      | 2.01      |  0.00    | 0.53      | 1.30      |    97     |    1268    |  2777     |     25    |     56      |     76    |    6960 s    |
| Cooker hood                |  2.19    | 2.21      | 2.22      |  2.76    | 2.77      | 2.79      |    121    |    122     |  123      |     90    |     92      |     93    |    750 s     |
| Dishwasher                 |  0.00    | 0.55      | 1.94      |  0.00    | 1.01      | 2.79      |    8      |    557     |  2025     |     18    |     79      |     114   |    2340 s    |
| Electric hot plate         |  1.98    | 1.99      | 2.00      |  0.00    | 0.00      | 0.00      |    1449   |    1461    |  1470     |     12    |     12      |     13    |    765 s     |
| Fan                        |  1.92    | 1.95      | 1.98      |  0.00    | 0.00      | 0.00      |    39     |    40      |  42       |     2     |     2       |     3     |    780 s     |
| Freezer                    |  0.20    | 0.30      | 0.50      |  0.00    | 0.00      | 0.00      |    93     |    138     |  160      |     18    |     22      |     26    |    3780 s    |
| Fridge                     |  0.34    | 0.88      | 1.72      |  0.58    | 1.18      | 1.78      |    34     |    53      |  65       |     51    |     69      |     82    |    4395 s    |
| Hair dryer                 |  1.99    | 1.99      | 1.99      |  0.00    | 0.00      | 0.00      |    1188   |    1191    |  1194     |     15    |     15      |     16    |    165 s     |
| Halogen ceiling light set  |  0.00    | 0.00      | 0.00      |  1.78    | 1.79      | 1.81      |    541    |    548     |  553      |     112   |     113     |     114   |    300 s     |
| Induction stove            |  0.88    | 1.00      | 1.09      |  1.75    | 1.77      | 1.80      |    1926   |    1942    |  1964     |     274   |     285     |     290   |    600 s     |
