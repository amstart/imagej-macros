#run("Save");
#run ("Jpeg...");
from ij.io import *;
from ij.plugin.frame import *;
from ij import IJ;

rm = RoiManager.getInstance()
imp = IJ.getImage(); 
roi = imp.getRoi();
sd = SaveDialog("specify", IJ.getDirectory("image"), ".roi");
RoiEncoder.save(roi, sd.getDirectory() + sd.getFileName()) ;
rm.addRoi(roi);
index = rm.getCount()-1;
rm.rename(index, sd.getFileName());