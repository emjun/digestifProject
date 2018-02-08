# Author: Eunice Jun
# What does this do?: Loads the full conclusion pages and blocks into the DB.
# ----------

import django
import csv

from digestif.models import ConclusionPage
from digestif.models import Block


# Create and load all the conclusion pages to the DB first
f_cp = open('digestif/static/digestif/conclusionPages.csv');
reader_cp = csv.reader(f_cp, delimiter='|');

f_blocks = open('digestif/static/digestif/blocks.csv');
reader_blocks = csv.reader(f_blocks, delimiter='|') # use | as delimiter because body text on conclusion pages use commas

def populate():
    # {load static}
    # Create and load all the conclusion pages to the DB first
    # f_cp = open({% static 'digestif/conclusionPages.csv' %})
    # reader_cp = csv.reader(f_cp)

    for row in reader_cp:

        # Read content from TXT file that contains all the content for the conclusion page
        f_content = open('digestif/static/digestif/content/full/' + row[4], "r")
        cp_content = f_content.read().splitlines() #strip all new lines
        # cp_content.replace("\n", "")
        # print(cp_content)
        content_string = ""
        for i in cp_content:
            content_string += i

        cp = ConclusionPage(
            cp_id = 'cp_' + row[0],
            platform = row[1],
            study = row[2],
            full_page = 'full/' + row[3],
            content = content_string
        )

        cp.save()

    # Create all the Blocks
    # While creating, update the conclusion pages to point to the Blocks

    # Read a CSV file row by row
    for row_blocks in reader_blocks:
        # row[0] is the cp_id name for the ConclusionPage
        cp_blocks = ConclusionPage.objects.get(pk='cp_' + row_blocks[0])

        # Use the elements in the columns of each row to construct a Block instance
        block = Block(
            # block_id = 'block_' + cp.cp_id + '_' + row[1],
            block_type = row_blocks[1],
            path_name = row_blocks[2],
            # block_layout = row[3],
            content = row_blocks[3],
            cp = cp_blocks)
            # benefits = row[4],        )

        block.save()
        cp_blocks.blocks.add(block)


        # What happens if a conclusion page does not have all the blocks??
        # What does querying for it do? How should we go about taking care of these cases?
