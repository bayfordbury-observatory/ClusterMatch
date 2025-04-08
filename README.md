# Cluster Match

(Pre-requisites: Python >=3.7, Astropy, Numpy, Matplotlib)

To install pre-requisities run: 
`pip install astropy numpy matplotlib`

To install astropy on LRC computers run `C:\Python312\Scripts\pip install astropy` or `C:\Program Files\Python312\Scripts\pip install astropy`.

If using Spyder you can add parameters by clicking Run>Configuration per file, then entering the parameters (not including the script name itself) into the "Command line options" box in the "General Settings" section (be careful NOT to use the "Command line options" box in the "Console" section higher up).

Images will need to be plate-solved for these scripts (and APT) to run successfully. 

On the LRC computers, APT can be found at `C:\tools\APT_v3.0.8\APT_v3.0.8\APT.jar`.

You can download ClusterMatch from the [releases page.](https://github.com/bayfordbury-observatory/ClusterMatch/releases) Please send us any feedback or suggestions!

**Step 1:**

Download the UCAC4 stars covering the area around an input file:
If your files have spaces, don't forget to enclose the entire path in double quotes.

Use:

  `download.py <input file>`
  
e.g.

  `>> python download.py "NGC 457_B_15s_B2_T3_72939.fit"`

**Step 2:**

For each filter (V and B), match stars in the image to the UCAC4 stars, and estimate the zero point:

Use:

  `match-zp.py <catalog file> <APT source list> <output file name> <filter (V or B)>`
  
e.g.

 ` >> python match-zp.py "ngc 457_V_15s_B2_T3_72941-UCAC4.tbl" "NGC457-V-inst-mags.csv" "NGC457-V-cal-mags.csv" V`
  
  `>> python match-zp.py "ngc 457_V_15s_B2_T3_72941-UCAC4.tbl" "NGC457-B-inst-mags.csv" "NGC457-B-cal-mags.csv" B`
  
**Step 3:**

Match stars from the V and B files, and calculate B-V colour:
  
Use:

  `match-bv.py <B mag file> <V mag file> <output file>`
  
e.g.

  `>> python match-bv.py "NGC457-B-cal-mags.csv" "NGC457-V-cal-mags.csv" "NGC457-BV.csv"`
  
**Step 4:**

The CSV file can be opened in Excel or other software to plot the results.

You can make a basic plot of B-V colours against apparent V magnitudes to create an HR diagram:
  
Use:

  `plot.py <BV file>`
    
e.g.

   `>> python plot.py "NGC457-BV.csv"`
