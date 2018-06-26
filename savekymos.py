from ij import IJ
from  ij.gui import GenericDialog;
from ij.plugin.frame import RoiManager

rm = RoiManager.getInstance()
imp = IJ.getImage()
if rm.getCount() > 1:
	rm.runCommand(imp, "Combine");
path = IJ.getDirectory("image");
path = path[0:path.find('\\MTs\\')]
name = imp.getTitle()[0:2]
if not name.isdigit():
	name = imp.getTitle()[0:1]
#name = int(''.join(filter(str.isdigit, name)))
IJ.run("Make Inverse");
IJ.run("Cut");
gd = GenericDialog("suffix");
gd.addStringField("suffix:","");
gd.showDialog();
suffix = gd.getNextString();
IJ.saveAs("Tiff", path + "\\MTs\\prepared\\" + name + suffix + ".tif");
rm.runCommand("Save", path + "\\MTs\\prepared\\" + name + suffix + ".zip")
IJ.run("Undo");
#ij.RUN("mAKE iNVERSE");
#ij.RUN("cUT");
#ij.SAVEaS("tIFF", PATH + "PREPARED\\" + NAME + "P.TIF");