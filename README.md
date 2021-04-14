## Use Gsheets to import CSV file to view first vehicle image

## **PURPOSE**
#### Review first image of incoming inventory from a third-party to ensure no overlays were received. This is easier than copying an pasting every link manually to review every first image on the inbound file. The code was used to prevent double overlays on the vehicle images since we apply seperate overlays created by our design team.

#### Only did it for the first image of every vehicle for minimal loading time on Gsheets and since Dealerships primarily use overlays on the first image as an industry standard.

## **DEFAULTS**
#### Default file name for inventory file: default-inventory.csv
#### Must contain the following headers: 'Dealer ID', 'Stock Number', 'VIN', 'Images'
