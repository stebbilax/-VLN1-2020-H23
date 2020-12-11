# VLN1-2020-H23
### Execution Instructions
* Navigate to the `src` folder.
* Execute `main.py` with your python installation.

### Layer and File Hierarchy
* Presentation (Presentation Layer) \
├ Menu    (Menu System) \
├ Operations  (TUI to Logic operations) \
└ UserInterface   (TUI Logic and Menu initialization (UIAPI))
* Logic \
├ LogicAPI (API bridge between layers) \
├ SearchAPI (Provides search services extended by the logicAPI) \
└ SearchManager (Search logic)
* Data \
├ DataAPI (API bridge to the logic layer) \
├ CSV_Manager (Manages interactions with the CSV database) \
└ ID_Manager (Manages unique ID assignment and maintenance)

### Models
* Contract
* Customer
* Destination
* Employee
* Enums
* Vehicle_Type
* Vehicle


### util in data
*Populate_all: - calls dummy.py and adds dummy data to csv file\
└ To run this go to command prompt: python Data\util\populate_all.py
