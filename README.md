# Dataset of Power-to-Voltage Sensitivity of Residential Loads v1.0.0
updated: 01.11.2023

Here we provide a dataset of time-varying voltage sensitivity of common residential loads. The results are based on experiments on actual loads under realistic operation. The loads under test, their brand and model, and the specific operating mode selected for testing are provided in Table I. 

The voltage sensitivity of a load is calculated every 15 seconds during the operation and the minimum, maximum, and average values and the respective operating power are provided in Table II. Kpv and Kqv represent the active power and reactive power-to-voltage sensitivity respectively. The table provides information on e.g. the range of the voltage sensitivity and the sensitivity impact of each load on the power system, according to the power consumption.

The dataset of sensitivity profiles can be found in the "Sensitivity Dataset" folder. 

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
| Load                   | Kpv_mean  | P0_mean  | Kqv_mean  | Q0_mean   |
|------------------------|------|------|------|------|
| Oven                   | 1.60 | 1754 | 2.25 | 35   |
| Condenser dryer        | 1.70 | 1252 | 0.50 | 55   |
| Cooker hood            | 2.30 | 217  | 2.80 | 229  |
| Dishwasher             | 0.50 | 557  | 1.10 | 79   |
| Electric cook plat     | 1.98 | 1461 | 1.94 | 12   |
| Fan                    | 1.95 | 40   | 0.00 | 2    |
| Freezer                | 0.36 | 124  | 0.00 | 21   |
| Fridge                 | 0.87 | 53   | 1.17 | 69   |
| Hair dryer             | 1.99 | 1191 | 1.66 | 15   |
| Halogen ceiling lights | 0.00 | 548  | 1.79 | 113  |
| Induction stove        | 0.99 | 1942 | 1.77 | 285  |
| Laptop charger         | 0.00 | 66   | 0.80 | 31   |
| LED light              | 0.00 | 61   | 1.30 | 13   |
| Microwave oven         | 1.18 | 1168 | 3.14 | 478  |
| Monitor                | 0.18 | 27   | 0.65 | 55   |
| Toaster                | 1.98 | 736  | 0.00 | 9    |
| Vacuum cleaner         | 4.88 | 336  | 3.60 | 413  |
| Water kettle           | 1.98 | 1873 | 1.99 | 134  |
| Washing machine        | 0.07 | 176  | 0.00 | 104  |
| Oil radiator           | 1.98 | 1494 | 1.92 | 12   |











