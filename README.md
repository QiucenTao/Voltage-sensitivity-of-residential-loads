# Dataset of Power-to-Voltage Sensitivity of Residential Loads v2.0.0
updated: 22.12.2023

version v1.0.0 updated on 01.11.2023 can be found [here](https://github.com/QiucenTao/Voltage-sensitivity-of-residential-loads/tree/branch-v1.0.0)

## What's new in v2.0.0:


Here we provide a dataset of time-varying voltage sensitivity of common residential loads. The results are based on experiments on actual loads under realistic operation. The loads under test, their brand and model, and the specific operating mode selected for testing are provided in Table I. 

The voltage sensitivity of a load is calculated every 15 seconds during the operation and the minimum, maximum, and average values and the respective operating power are provided in Table II. Kpv and Kqv represent the active power and reactive power-to-voltage sensitivity respectively. The table provides information on e.g. the range of the voltage sensitivity and the sensitivity impact of each load on the power system, according to the power consumption.

The dataset of sensitivity profiles can be found in the "Sensitivity Dataset" folder. Detailed explanations of the sensitivity profiles of each load are provided in the "Individual Loads" folder.

### Table I. List of Loads Under Test
| Load                   | Brand and Model       | Tested Operating Mode                                | 
|------------------------|------------------------|------------------------------------------------------|
| Condenser cloth dryer  | Miele T 8687 C         | Gentle cycle                                         |
| Cooker hood            | IKEA <sup>b</sup>      | Extraction level: medium                             |
| Dishwasher             | Miele G 1834 SCI       | Quick wash 40°C                                      |
| Electric hot plate     | Clatronic EKP 3582     | Maximum power level                                  |
| Fan                    | BaseTech VE-5985BT     | Maximum power level with head shaking                |
| Freezer                | Liebherr GN 3056-29    | Set temperature -20°C                                |
| Fridge                 | Bosch KG KIRR18A       | Maximum cooling level                                |
| Hair dryer             | Impuls SL-805          | Maximum wind level, medium heat level                |
| Halogen ceiling light set | --<sup>a</sup>      | Lights on                                            |
| Induction stove        | Miele KM 5955          | Maximum power level                                  |
| Laptop charger         | TOSHIBA PA3755U-1ACA   | As power supply                                      |
| LED ceiling light      | --<sup>a</sup>         | Light on                                             |
| Microwave oven         | Renkforce MM720Ca7-PM  | Cook mode power level 4                              |
| Monitor                | Samsung BX2240         | Monitor on                                           |
| Oil radiator           | Clatronic RA 3735      | Set temperature 24°C                                 |
| Oven                   | Miele H5681BL          | Top and bottom heating, set temperature 280°C        |
| Toaster                | Severin AT 2586L       | Maximum power level                                  |
| Vacuum cleaner         | Siemens VBBS607V00     | Smooth surface cleaning mode                         |
| Washing machine        | Miele 3985 WPS         | Cotton wash 1000rpm                                  |
| Water kettle           | Clatronic WKS 3692     | Cook 1.5L water                                      |



<sup>a</sup> No information available  
<sup>b</sup> Model number not available

### Table II. Overview of Load Voltage Sensitivity Results
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
| Laptop charger             |  0.00    | 0.00      | 0.00      |  0.71    | 0.80      | 0.89      |    65     |    66      |  67       |     30    |     31      |     31    |    585 s     |
| LED ceiling light          |  0.00    | 0.00      | 0.00      |  0.00    | 0.00      | 0.00      |    58     |    61      |  65       |     13    |     13      |     13    |    855 s     |
| Microwave oven             |  1.15    | 1.19      | 1.22      |  2.95    | 3.15      | 3.26      |    1150   |    1168    |  1186     |     454   |     478     |     502   |    135 s     |
| Monitor                    |  0.12    | 0.19      | 0.34      |  0.31    | 0.65      | 0.88      |    26     |    27      |  28       |     52    |     55      |     57    |    1050 s    |
| Oil radiator               |  1.98    | 1.98      | 1.98      |  0.00    | 0.00      | 0.00      |    1490   |    1494    |  1499     |     11    |     12      |     12    |    2085 s    |
| Oven                       |  1.73    | 1.92      | 1.98      |  1.54    | 2.69      | 3.04      |    52     |    2128    |  3621     |     22    |     40      |     55    |    720 s     |
| Toaster                    |  1.98    | 1.98      | 1.98      |  0.00    | 0.00      | 0.00      |    735    |    736     |  738      |     9     |     9       |     10    |    75 s      |
| Vacuum cleaner             |  4.75    | 4.88      | 5.06      |  3.46    | 3.63      | 3.85      |    325    |    336     |  340      |     396   |     413     |     418   |    285 s     |
| Washing machine            |  0.00    | 0.08      | 2.06      |  0.00    | 0.06      | 1.76      |    8      |    181     |  2142     |     19    |     107     |     664   |    4305 s    |
| Water kettle               |  1.98    | 1.98      |  1.99    | 1.99      | 1.99      |    2      |    1870   |    1873    |  1879     |     133   |     134     |     135   |    255 s     |






