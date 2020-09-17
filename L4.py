def main():
    europa_fil = open("europa.txt", "r")
    for line in europa_fil:
        dictionary_av_text = {}
        lista_av_text = line.split(",")
        for i in range(len(lista_av_text)):
            if i == 0:
                dictionary_av_text["namn"] = lista_av_text[i]
            elif i == 1:
                dictionary_av_text["yta"] = float(lista_av_text[i])
            elif i == 2:
                dictionary_av_text["befolkning"] = int(lista_av_text[i])
        land_info = Information(dictionary_av_text)
        dictionary_av_text["tathet"] = land_info.berakna_befolkningstathet()
        lista_av_land_info = land_info.lista_av_land_info()
        print(lista_av_land_info[0], 5*"", lista_av_land_info[1], 5*"", round(lista_av_land_info[2]), 5*"",
              lista_av_land_info[3], 5*"", "\n")
    europa_fil.close()


class Information:
    def __init__(self, dictionary):
        self.namn = dictionary["namn"]
        self.befolkning = dictionary["befolkning"]
        self.yta = dictionary["yta"]

    def berakna_befolkningstathet(self):
        self.tathet = round(float(self.befolkning)/float(self.yta), 1)
        return self.tathet

    def lista_av_land_info(self):
        lista_av_land_info = [self.namn, self.befolkning, self.yta, self.tathet]

        return lista_av_land_info













main()