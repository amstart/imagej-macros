#run("Save");
#run ("Jpeg...");
from ij import IJ 
from ij.plugin.frame import RoiManager;
from ij.io import SaveDialog
import os
imp = IJ.getImage(); 
#sd = SaveDialog("Specify", "", ".roi");
#IJ.saveAs(imp, "Selection", sd.getDirectory() + sd.getFileName() + ".roi"); 
