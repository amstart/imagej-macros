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
sd = SaveDialog("specify", IJ.getDirectory("image"), ".zip");
index = rm.getCount()-1;
path = sd.getDirectory() + sd.getFileName(); 
name = sd.getFileName();
rm.rename(index, name[0:-4]);
rm.deselect() ;
rm.runCommand("Save", path)
#ok = RoiEncoder.save(roi, path); 
