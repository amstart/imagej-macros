n = getNumber("How many divisions (e.g., 2 means quarters)?", 2);
notfirst = 0;
id = getImageID();
title = getTitle();
getLocationAndSize(locX, locY, sizeW, sizeH);
width = getWidth();
height = getHeight();
title = getTitle();
tileWidth = width / n;
tileHeight = height / n;
for (y = 0; y < n; y++) {
offsetY = y * height / n;
 for (x = 0; x < n; x++) {
offsetX = x * width / n;
selectImage(id);
 call("ij.gui.ImageWindow.setNextLocation", locX + offsetX, locY + offsetY);
tileTitle = title + " [" + x + "," + y + "]"; 
makeRectangle(offsetX, offsetY, tileWidth, tileHeight);
 run("Duplicate...", "title=&tileTitle");
   selectImage(tileTitle);
   print(notfirst);
   print(tileTitle);
   if (notfirst) {
      run("Concatenate...", "open image1=&firstimg image2=&tileTitle title=&firstimg");
   }
   else {
      firstimg = tileTitle;
      notfirst = 1;
   }
 hasrun = 1;
 print(tileTitle);
}
}
rename(title);
selectImage(id);
close(); 
