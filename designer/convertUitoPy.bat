:: http://pyqt.sourceforge.net/Docs/PyQt5/designer.html
FOR /R . %%a IN (*.ui) DO pyuic5 -x %%a -i 0 -o ../ui/%%~na.py