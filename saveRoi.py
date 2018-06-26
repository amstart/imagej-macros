#run("Save");
#run ("Jpeg...");
from ij.plugin.frame import RoiManager
from ij import IJ
from ij.io import SaveDialog
from ij.io import RoiEncoder
from ij.io import RoiDecoder
rm = RoiManager.getInstance()

imp = IJ.getImage();
roi = imp.getRoi();
rm.addRoi(roi);
sd = SaveDialog("specify", IJ.getDirectory("image"), ".roi");
path = sd.getDirectory() + sd.getFileName(); 
RoiEncoder.save(roi, path); 
