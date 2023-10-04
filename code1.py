import os


def criaPasta(pasta):
    if os.path.exists(pasta)==False:
        os.makedirs(pasta)

origem = os.getcwd()+"/pastaA/"
pastaB = os.getcwd()+"/pastaB/"

criaPasta(origem)
criaPasta(pastaB)

dir_tree={
    "Imagens/":[".png", ".gif", ".jpeg", ".jpg"],
    "Sons/":[".mp3", ".mpeg", ".wav"],
    "Documentos/":[".pdf", ".doc", ".txt"]
}
