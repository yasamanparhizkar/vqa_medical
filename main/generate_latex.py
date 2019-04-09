LIST_QUESTION_BREAST = [
    "how many classes are there",
    "is there any benign class in the image",
    "is there any in situ class in the image",
    "is there any invasive class in the image",
    "what is the major class in the image",
    "what is the minor class in the image",
    "is benign in 64_64_32_32 location",
    "is invasive in 96_96_32_32 location",
]

LIST_QUESTION_TOOLS = [
    "how many tools are there",
    "is scissors in 64_32_32_32 location",
    "is irrigator in 64_96_32_32 location",
    "is grasper in 64_96_32_32 location"
    "is bipolar in 64_96_32_32 location"
    "is hook in 64_96_32_32 location"
    "is clipper in 64_96_32_32 location"
    "is specimenbag in 64_96_32_32 location"
    "is there any grasper in the image",
    "is there any bipolar in the image",
    "is there any hook in the image",
    "is there any scissors in the image",
    "is there any clipper in the image",
    "is there any irrigator in the image",
    "is there any specimenbag in the image",
]

LIST_QUESTION_IDRID = [
    "is there haemorrhages in the fundus",
    "is there microaneurysms in the fundus",
    "is there soft exudates in the fundus",
    "is there hard exudates in the fundus",
    "is hard exudates larger than soft exudates",
    "is haemorrhages smaller than microaneurysms",
    "is there haemorrhages in the region 32_32_16_16",
    "is there microaneurysms in the region 96_96_16_16",
]


BREAST = {
    "A02_idx-31344-39648_ps-8192-8192": "how many classes are there",
    "A03_idx-23568-14336_ps-4096-4096": "is invasive in 96_96_32_32 location",
    "A04_idx-22904-32351_ps-4096-4096": "what is the major class in the image",
    "A05_idx-35648-3248_ps-4096-4096": "is there any benign class in the image",
    "A10_idx-20000-2576_ps-4096-4096": "what is the minor class in the image",
    "A08_idx-34864-6672_ps-4096-4096": "is there any invasive class in the image",
}

TOOLS = {
    "v04_020125": "how many tools are there",
    "v04_020400": "is there any grasper in the image",
    "v05_056350": "how many tools are there",
    "v04_020200": "is there any specimenbag in the image",
    "v04_020300": "is there any irrigator in the image",
    "v06_070725": "is there any bipolar in the image",
}

IDRID = {
    "IDRiD_44": "is there hard exudates in the fundus",
    "IDRiD_46": "is there microaneurysms in the fundus",
    "IDRiD_47": "is there microaneurysms in the region 96_96_16_16",
    "IDRiD_51": "is there haemorrhages in the region 32_32_16_16",
    "IDRiD_53": "is there haemorrhages in the fundus",
    "IDRiD_49": "is there microaneurysms in the region 96_96_16_16",
}


file1 = open("temp/myfile.txt", "w")

top = ["\\begin{figure}[t] \n",
       "\\def\\subfigsize{0.19\\textwidth} \n",
       "\\def\\subfigverlabelsize{0.17\\textwidth} \n",
       "\\def\\scalefonesize{0.94} \n",
       "\\def\\scalefonesizetitle{0.85} \n",
       "\\centering"]

# bottom = 

for 

#     Question: - Answer:
#     \includegraphics[width=\subfigsize]{figures/gradcam/IDRiD_01_in.jpg}
#     \includegraphics[width=\subfigsize]{figures/gradcam/IDRiD_01_cnn.jpg}
#     \includegraphics[width=\subfigsize]{figures/gradcam/IDRiD_01_att_question_is-there-soft-exudates-in-the-fundus.jpg}
#     \includegraphics[width=\subfigsize]{figures/gradcam/IDRiD_01_att_question_is-there-soft-exudates-in-the-fundus.jpg}
#     \includegraphics[width=\subfigsize]{figures/gradcam/IDRiD_01_noatt_question_is-there-soft-exudates-in-the-fundus.jpg}\\


#     \begin{subfigure}{\subfigsize}
#         \centering
#         {\scalefont{\scalefonesizetitle} Input image\\~\\~}
#     \end{subfigure}
#     \begin{subfigure}{\subfigsize}
#         \centering
#         {\scalefont{\scalefonesizetitle}Grad-CAM of\\image model\\~}
#     \end{subfigure}
#     \begin{subfigure}{\subfigsize}
#         \centering
#         {\scalefont{\scalefonesizetitle}Grad-CAM of\\QC-MLB\\(attention)}
#     \end{subfigure}
#     \begin{subfigure}{\subfigsize}
#         \centering
#         {\scalefont{\scalefonesizetitle}Grad-CAM of\\QC-MLB\\(no attention)}
#     \end{subfigure}
#     \begin{subfigure}{\subfigsize}
#         \centering
#         {\scalefont{\scalefonesizetitle}Occlusion\\ Sensitivity\\~}
#     \end{subfigure}
#     \caption{IDRiD
#     }
#     \label{fig:gradcam}
# \end{figure}


file1.writelines(L)
file1.close()  # to change file access modes
