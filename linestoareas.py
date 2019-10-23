from ij import IJ
from  ij.gui import GenericDialog, YesNoCancelDialog;
from ij.plugin.frame import RoiManager
from ij.macro import Functions

rm = RoiManager.getInstance()
imp = IJ.getImage()
path = IJ.getDirectory("image");
name = imp.getTitle()[0:2]
newimp = IJ.getImage()
rm.runCommand(newimp, "Show All")
for x in range(0,rm.getCount()):
	rm.select(newimp, x);
	IJ.run("Line to Area");
	IJ.run("Measure");
	# rm.setSelectedIndexes(range(rm.getCount()));
	# rm.runCommand(newimp, "Combine");
