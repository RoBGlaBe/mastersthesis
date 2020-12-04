import os





se_files = ["source", "tagging", "g2", "width", "rate"]
kr_files = ["source", "tagging", "lce", "e-lifetime", "scint-inhomo", "scint-gain", "eng-scale", "bg"]



def content(filename):
    return (
        "\n\n\n"
        "\subsection{" + filename + "}\n"
        "\label{ssec:" + filename+ "}\n"
        "\n\n"
                    )

def write_se_files():
    for idx, fn in enumerate(se_files):
        with open(f"{idx+1}{fn}.tex", "w") as f:
            f.write(content(fn))


def write_kr_files():
    for idx, fn in enumerate(kr_files):
        with open(f"{idx+1}{fn}.tex", "w") as f:
            f.write(content(fn))


def write_analysis_base():
    with open(f"alt_analysis.tex", "w") as f:
        f.write("\chapter{Analysis}")
        f.write("\n")
        f.write("\label{chap:Analysis}")
        f.write("\n")
        f.write("\n")
        f.write("")
        f.write("Analysis Chap.-Intro")
        f.write("\n")
        f.write("\n")


        f.write("\section{Single Electrons}\n")
        f.write("\label{sec:SE}\n\n\n")

        for idx, fn in enumerate(se_files):
            name = f"{idx+1}{fn}"
            f.write("\input{Chapters/sub/SingleElectrons/" + name + "}")
            f.write("\n")
            f.write("\\newpage")
            f.write("\n")

        f.write("\n")
        f.write("\section{Krypton}\n")
        f.write("\label{sec:Kr}\n\n\n")

        for idx, fn in enumerate(kr_files):
            name = f"{idx+1}{fn}"
            f.write("\input{Chapters/sub/Krypton/" + name + "}")
            f.write("\n")
            f.write("\\newpage")
            f.write("\n")

write_analysis_base()
