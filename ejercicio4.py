import string

evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

#titulo = evaluar.split(" título: ")
texto = evaluar.split("resumen: ")
titulo = texto[0].split(" título: ")[1]
resumen = texto[1]
#resumen = evaluar.split(str(titulo[1]))

#print(texto)
#print(" ")
#print(titulo)
#print(" ")
#print(resumen)

print("El titulo esta ok." if len(titulo.split()) <= 10 else "El titulo NO esta ok.")

oraciones = resumen.split(".")
#print(len(oraciones))
#print(oraciones)
faciles = 0
aceptables = 0
dificiles = 0
muy_dificiles = 0

for oracion in oraciones:
    if len(oracion.split()) <= 12:
        faciles = faciles + 1
    elif len(oracion.split()) <= 17:
        aceptables = aceptables + 1
    elif len(oracion.split()) <= 25:
        dificiles = dificiles + 1
    elif len(oracion.split()) > 25:
        muy_dificiles = muy_dificiles + 1

print(f"Oraciones faciles: {faciles}, oraciones aceptables: {aceptables}, oraciones dificiles: {dificiles} y oraciones muy dificiles: {muy_dificiles}.")
