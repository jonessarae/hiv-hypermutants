# HIV Hypermutant Tool Comparison

Final project for AS.410.712.81.SP17 Advanced Practical Computer Concepts for Bioinformatics at Johns Hopkins University. 

Website comparing results from two tools identifying HIV hypermutants: Hyperfreq and Hypermut.

## Background

## Software/Scripts

## Usage

## MySQL Database Design

<img width="953" alt="diagram" src="https://user-images.githubusercontent.com/42072830/48634110-db631180-e992-11e8-9c8a-394e223da525.png">

## Website

As of 11/16/2018, the website, which is hosted on my school's server, is still working and can be accessed via the link below: 

http://bfx.eng.jhu.edu/sjone215/final/hyper_tool.html

Here are screenshots of the website if the above link is not working: 

### Main page
The user must enter a coded patient name (ex. LEOHIR) and select one of three options, "Hypermut", "Hyperfreq", and "Compare Both". For "Hypermut" and "Hyperfreq", the user can select an open reading frame (1,2,3) from a drop-down menu. 

<img width="1252" alt="main_page" src="https://user-images.githubusercontent.com/42072830/48634121-e28a1f80-e992-11e8-984b-f21378dc79a9.png">

### Results for "Hypermut" or "Hyperfreq" option
When either "Hypermut" or "Hyperfreq" is selected, the following results are displayed:
<ul>
  <li>Total number of sequences</li>
<li>Total number of hypermutants</li>
<li>Number of hypermutants by tissue type</li>
<li>All Predicted Hypermutants</li>
<li>Open Reading Frame Data for each Hypermutant</li>
</ul>
<img width="620" alt="by_tissue_type" src="https://user-images.githubusercontent.com/42072830/48634154-e9b12d80-e992-11e8-948f-df6543452db4.png">

<img width="586" alt="all_predicted" src="https://user-images.githubusercontent.com/42072830/48634158-eb7af100-e992-11e8-9560-0ed1761a9cc4.png">

<img width="743" alt="open_reading_frames" src="https://user-images.githubusercontent.com/42072830/48634165-f0d83b80-e992-11e8-9649-0ff945aa503a.png">

### Results for "Compare Both" option
<ul>
  <li>Total number of sequences</li>
<li>Total number of hypermutants in Hyperfreq</li>
<li>Total number of hypermutants in Hypermut</li>
<li>Number of matches</li>
<li>Fisher p-value</li>
<li>Hyperfreq and Hypermut Comparison</li>
</ul>
<img width="685" alt="comparison" src="https://user-images.githubusercontent.com/42072830/48634128-e6b63d00-e992-11e8-9f11-bcde22ba55ed.png">

## References
Imamichi, H., Dewar, R. L., Adelsberger, J. W., Rehm, C. A., O’Doherty, U., Paxinos, E. E., ... & Lane, H. C. (2016). Defective HIV-1 proviruses produce novel protein-coding RNA species in HIV-infected patients on combination antiretroviral therapy. Proceedings of the National Academy of Sciences, 113(31), 8783-8788

Matsen IV, F. A., Small, C. T., Soliven, K., Engel, G. A., Feeroz, M. M., Wang, X., ... & Jones-Engel, L. (2014). A novel bayesian method for detection of APOBEC3-mediated hypermutation and its application to zoonotic transmission of simian foamy viruses. PLoS Comput Biol, 10(2), e1003493

Rose, PP and Korber, BT. 2000. Detecting hypermutations in viral sequences with an emphasis on G -> A hypermutation.Bioinformatics 16(4): 400-401

