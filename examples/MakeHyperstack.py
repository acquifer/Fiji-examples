"""
From a directory, a well and subposition, this scripts list the image files and make a hyperstack for a selected well and subposition.
the following variables should be updated to match your local image dataset:
- inputDir
- selectedWell and selectedSubpositions
- listChannel, Zslice and Timepoint

NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/Fiji-examples
"""
from acquifer.im04         import FileUtils, MetadataParser
from acquifer.im04.plugins import Hyperstack_Maker

"""
# Use following imports for IM03
from acquifer.im03         import FileUtils, MetadataParser
from acquifer.im03.plugins import Hyperstack_Maker_IM03
"""
inputDir = r"C:\Users\Laurent Thomas\Documents\Acquifer\DataSet\Fish\Clicking_AppNote96"

# Select a single well and single subposition
selectedWell = ["A002"]
selectedSubpositions = [1] # first subposition
listChannel   = None # if None or [], all available channels will be displayed, same for other dimensions
listZslice    = None
listTimepoint = None

def printAligned(array):
	"""
	This function is designed to print each elements of an array on a new line.
	""" 
	for i in array:
		print i

listFiltered = FileUtils().getListImageFiles(inputDir, 
                                             selectedWell, 
                                             selectedSubpositions, 
                                             listChannel, 
                                             listZslice, 
                                             listTimepoint)
print "\nList files"
printAligned(listFiltered)

# Get metadatas
listInfos = FileUtils().getListImagesInfos(listFiltered)
print "\nImages metadata"
printAligned(listInfos)

# Make hyperstacks
hyperstack = Hyperstack_Maker().makeHyperStack(listInfos)
hyperstack.show()