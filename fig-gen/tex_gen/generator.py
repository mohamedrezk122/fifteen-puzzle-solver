import subprocess 
import os 



def generate_figure_tex_content(arr, tex_file):

    file_content = r"""
        \documentclass{article}
        \usepackage{tikz}
        \begin{document}
            \begin{tikzpicture}[thick]  
    """
    color = "blue"
    for i , row in enumerate(arr) :
        for j , entry in enumerate(row) :

            if entry == len(arr) * len(arr[0]) : 
                color = "white"
            elif entry % 2 == 0 : 
                color = "red" 
            else:
                color = "blue"

            file_content += rf"\node[fill={color}!20, minimum size=1cm, inner sep=0pt] at ({j},{i}) {{${entry}$}};"
            file_content += "\n"

    file_content += r"""
            \end{tikzpicture}
        \end{document}
    """

    with open(tex_file+".tex" , 'w') as file :
        file.write(file_content)




def compile_tex_file(file):

    subprocess.call(["pdflatex", file+".tex"], \
    stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)

    # return subprocess.getoutput(f"pdflatex {file}.tex")
def convert_pdf_to_svg(pdf_file, svg_file):
    subprocess.call(["pdf2svg", pdf_file+".pdf" , svg_file+".svg"], \
    stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)

    # return subprocess.getoutput(f"pdf2svg {pdf_file}.pdf {svg_file}.svg")
def generate_figure(arr , filename):

    file = "temp"
    generate_figure_tex_content(arr , file)
    compile_tex_file(file)
    convert_pdf_to_svg(file, filename)

arr = [ [1 ,2 , 3, 4],
        [5 , 6 , 7, 8],
        [9, 10, 11, 12],
        [13 , 14 , 15, 16]]
generate_figure(arr , "fig-1")