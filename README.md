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
| Induction stove        | Miele KM 5955          | Maximum power level                                  |
| Water kettle           | Clatronic WKS 3692     | Cook 1.5L water                                      |
| Oven                   | Miele H5681BL          | Top and bottom heating, set temperature 280°C        |
| Hair dryer             | Impuls SL-805          | Maximum wind level, medium heat level                |
| Microwave oven         | Renkforce MM720Ca7-PM  | Cook mode power level 4                              |
| Toaster                | Severin AT 2586L       | Maximum power level                                  |
| Dishwasher             | Miele G 1834 SCI       | Quick wash 40°C                                      |
| Halogen ceiling lights | --                     | Lights on                                            |
| Vacuum cleaner         | Siemens VBBS607V00     | Smooth surface cleaning mode                         |
| Washing machine        | Miele 3985 WPS         | Cotton wash 1000rpm                                  |
| Freezer                | Liebherr GN 3056-29    | Set temperature -20°C                                |
| Laptop charger         | TOSHIBA PA3755U-1ACA   | As power supply                                      |
| LED light              | --                     | Light on                                             |
| Fridge                 | Bosch KG KIRR18A       | Maximum cooling level                                |
| Monitor                | Samsung BX2240         | Monitor on                                           |
| Oil radiator           | Clatronic RA 3735      | Set temperature 24°C                                 |

### Overview of Load Voltage Sensitivity Results
|  Load                      |           |    Kpv    |           |          |    Kqv    |           |           |   P0 (W)   |           |           |   Q0 (var)  |           |  Data Length |
|----------------------------|-----------|-----------|-----------|----------|-----------|-----------|-----------|------------|-----------|-----------|-------------|-----------|--------------|
|                            | **min**   | **mean**  | **max**   | **min**  | **mean**  |  **max**  | **min**   | **mean**   | **max**   | **min**   |   **mean**  |  **max**  |              |
| Apartment                  |  0.00     | 0.87      | 1.98      |  0.00    | 1.15      | 1.91      |  31       |    1399    |  5876     |    265    |   386       |   716     |   5 hour     |
| Apartment with aggregated Heater|  0.00   | 1.48    | 1.98      |  0.00    | 1.15   | 1.91        |    5 hour     |
| Cloth dryer                |  1.10    | 1.73      | 2.01      |  0.00    | 0.53      | 1.30      |    6960 s      |
| Cooker hood                |  2.19    | 2.21      | 2.22      |  2.76    | 2.77      | 2.79      |    750 s       |
| Dishwasher                 |  0.00    | 0.55      | 1.94      |  0.00    | 1.01      | 2.79      |    2340 s      |
|  Electric hot plate        |  1.98    | 1.99      | 2.00      |  0.00    | 0.00      | 0.00      |     765 s      |
|  Fan                       |  1.92    | 1.95      | 1.98      |  0.00    | 0.00      | 0.00      |     780 s      |
|  Freezer                   |  0.20    | 0.30      | 0.50      |  0.00    | 0.00      | 0.00      |     3780 s     |
|  Fridge                    |  0.34    | 0.88      | 1.72      |  0.58    | 1.18      | 1.78      |     4409 s     |
|  Hair dryer                |  1.99    | 1.99      | 1.99      |  0.00    | 0.00      | 0.00      |  1188       |  1191   |  1194    | 15     |      15         |      16       |        605 s      |
