# import django
import csv

from digestif.models import ConclusionPage
from digestif.models import Block


{load static}
# Create and load all the conclusion pages to the DB first
f_cp = open({% static 'digestif/conclusionPages.csv' %})
reader_cp = csv.reader(f_cp)

for row in reader_cp:
    cp = ConclusionPage(
        cp_id = row[0]
        platform = row[1]
        study = row[2]
        full_page = row[3]
    )

    cp.save()

# Create all the Blocks
# While creating, update the conclusion pages to point to the Blocks
f = open({% static 'digestif/blocks.csv' %})
reader = csv.reader(f)
row_count = 0 # keeps track of the number of rows read for a particular group of Blocks on the same conclusion page

# Read a CSV file row by row
for row in reader:
    # row[0] is the cp_id name for the ConclusionPage
    cp = ConclusionPage.objects.get(pk=row[0])

    # Use the elements in the columns of each row to construct a Block instance
    block = Block(
        block_type = row[1],
        path_name = row[2],
        block_layout = row[3],
        content = {'heading' : row[4], 'body' : row[5]},
        benefits = row[6])
    )

    block.save()
    cp.blocks.add(block)

    # What happens if a conclusion page does not have all the blocks??
    # What does querying for it do? How should we go about taking care of these cases?
