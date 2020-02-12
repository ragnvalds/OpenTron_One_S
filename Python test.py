

from opentrons import robot, labware, instruments

plate = labware.load('96-flat', '1')
trough = labware.load('trough-12row', '2')

tiprack_1 = labware.load('tiprack-200ul', '3')
tiprack_2 = labware.load('tiprack-200ul', '4')

p100 = instruments.P100_Single(
    mount='left',
    tip_racks=[tiprack_2])

p100.transfer(100, plate.wells('A1'), plate.wells('B1'))
