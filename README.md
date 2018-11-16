# HIV Hypermutant Tool Comparison

Final project for AS.410.712.81.SP17 Advanced Practical Computer Concepts for Bioinformatics at Johns Hopkins University. 

Website comparing results from two tools identifying HIV hypermutants: Hyperfreq and Hypermut.

## Background

Patients suppressed on antiretroviral therapy for years show persistence of proviruses of HIV-1 in peripheral blood mononuclear cells. However, many of these proviruses are defective and are considered “silent” with respect to HIV pathogenesis. Recently, Imamichi et al. identified defective viruses capable of transcribing HIV-RNA transcripts. Her results suggest that these defective proviruses are not silent as originally thought and may even actually play a role in HIV pathogenesis by activating host defense pathways. To better understand the population of the defective proviruses or hypermutants as they are referred, I used Hypermut and Hyperfreq. Hypermut is a commonly used tool available at www.hiv.lanl.gov for identifying HIV hypermutants from a list of sequences in fasta format. Hyperfreq is another tool that I came across when reviewing articles on HIV hypermutants. The paper from Matsen et al described Hyperfreq as a new method for finding hypermutants using a Bayesian method versus solely a Fisher exact test used in Hypermut. According to the authors, the Bayesian method is supposed to be an improvement on the statistical methods employed in Hypermut. Hyperfreq, which was published in 2014, is mentioned in only a handful of papers. None of these papers employed Hyperfreq in the context of HIV proviruses in human subjects. Additionally, none of my colleagues, who work with HIV extensively, know of Hyperfreq. Thus, for my final, I wanted to utilize Hyperfreq to see if it is comparable to Hypermut. Another aspect of my project was to then characterize these hypermutants, in particularly, their open reading frames. A question that could be answered if there are enough samples would be to look for any changes in the length of the open reading frames in hypermutants over time. As more mutations are introduced in the hypermutants, it’s possible that the open reading frames will become smaller. The smaller the open reading frame and the corresponding peptide, the easier it is for the peptide, and thus the defective provirus, to avoid detection by the cell’s defense system. 

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
[1] Imamichi, H., Dewar, R. L., Adelsberger, J. W., Rehm, C. A., O’Doherty, U., Paxinos, E. E., ... & Lane, H. C. (2016). Defective HIV-1 proviruses produce novel protein-coding RNA species in HIV-infected patients on combination antiretroviral therapy. Proceedings of the National Academy of Sciences, 113(31), 8783-8788

[2] Rose, PP and Korber, BT. 2000. Detecting hypermutations in viral sequences with an emphasis on G -> A hypermutation.Bioinformatics 16(4): 400-401

[3] Matsen IV, F. A., Small, C. T., Soliven, K., Engel, G. A., Feeroz, M. M., Wang, X., ... & Jones-Engel, L. (2014). A novel bayesian method for detection of APOBEC3-mediated hypermutation and its application to zoonotic transmission of simian foamy viruses. PLoS Comput Biol, 10(2), e1003493

