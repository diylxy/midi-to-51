Midicsv.exe %1 out.csv
python midi-to-beep.py -f out.csv
rm out.csv