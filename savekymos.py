from ij import IJ
from  ij.gui import GenericDialog, YesNoCancelDialog;
from ij.plugin.frame import RoiManager
from ij.macro import Functions

rm = RoiManager.getInstance()
imp = IJ.getImage()
path = IJ.getDirectory("image");
name = imp.getTitle()[0:2]
if not name.isdigit():
	name = imp.getTitle()[0:1]
#name = int(''.join(filter(str.isdigit, name)))
IJ.run("Select All");
IJ.run("Duplicate...", "check and close");
newimp = IJ.getImage()
rm.runCommand(newimp, "Show All")
if rm.getCount() > 1:
	rm.setSelectedIndexes(range(rm.getCount()));
	rm.runCommand(newimp, "Combine");
else:
	rm.select(newimp, 0);
IJ.run("Make Inverse");
IJ.run("Cut");
gd = GenericDialog("suffix");
gd.addStringField("suffix:","");
gd.showDialog();
suffix = gd.getNextString();
ync = YesNoCancelDialog(None, "coverage (yes) or intensity (no or cancel)", "coverage (yes) or intensity (no or cancel)");
if ync.yesPressed():
	IJ.saveAs("Tiff", path + "\\coverage\\" + name + suffix + ".tif");
else:
	IJ.saveAs("Tiff", path + "\\prepared\\" + name + suffix + ".tif");
#IJ.saveAs("Tiff", path + "\\MTs\\prepared\\" + name + suffix + ".tif");
#IJ.run("Undo");
#ij.RUN("mAKE iNVERSE");
#ij.RUN("cUT");
#ij.SAVEaS("tIFF", PATH + "PREPARED\\" + NAME + "P.TIF");
#rm.runCommand("Save", path + "\\MTs\\prepared\\" + name + suffix + ".zip")