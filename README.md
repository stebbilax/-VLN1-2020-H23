# VLN1-2020-H23
### Execution Instructions
* Navigate to the `src` folder.
* Execute `main.py` with your python installation.

### Authentication instructions
* Administrators can login with the username `admin`.
* A valid SSID can be located within the `employee.csv` document in the data files.
* Different employees have different access to menu's based on their employement titles.

### Layer and File Hierarchy
* Presentation (Presentation Layer) \
├ Menu    (Menu System) \
├ Operations (TUI to Logic operations) \
├ Display (Display methods for model data) \
├ InputVerifiers (Verifiers for input fields) \
└ UserInterface   (TUI Logic and Menu initialization (UIAPI))
* Logic \
├ LogicAPI (API bridge between layers) \
├ SearchAPI (Provides search services extended by the logicAPI) \
├ InvoiceManager (Manages invoice generation and operations) \
├ Enums (EnumManager, manages dynamic enums for airports, countries and employee titles) \
├ ReportGenerator
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
