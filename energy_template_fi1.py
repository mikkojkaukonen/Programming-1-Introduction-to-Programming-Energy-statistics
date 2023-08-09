"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Energiatilasto
Name:       Mikko Kaukonen

Ohjelma joka kysyy kättäjältä energiankulutusarvoja ja tulostaa näiden
perusteella  logaritmisen histogrammin.
"""

def read_and_check_energy_consumption(energy_consumption_list):
    """
    Funtio joka kysyy käyttäjältä syötteenä enegriankulutuksen arvoja
    ja tallentaa ne parametrina saamaansa tyhjään listaan jonka palauttaa
    täytettynä käyttäjän syöttämillä luvuilla.

    :param energy_consumption_list:
        Tyhjä lista johon tallennetaan käyttäjän syöttämät arvot.
    :return:
        Listan täytettynä käyttäjän syöttämillä arvoilla
    """
    consumption_value_input = 0

    # Tarkastaa onko käyttäjän antama syöte funktion lopetuskäskynä toimiva
    # tyhjä rivi
    while consumption_value_input != "":
        consumption_value_input = input("Enter energy consumption (kWh): ")

        # Mikäli käyttäjän syöte ei ole lopetus komento muuttaa sen int
        # tyyppiseksi
        if consumption_value_input != "":
            consumption_value = int(consumption_value_input)

            # Mikäli käyttäjän syöttämä arvo on negatiivinen tulostaa
            # virheilmoituksen, muuten lisää arvon enrgiankulutuslistaan.
            if consumption_value < 0:
                print("You entered: ", consumption_value,"."
                    " Enter non-negative numbers only!", sep="")

            elif consumption_value >= 0:
                energy_consumption_list.append(consumption_value)


def calculate_largest_class_number(energy_consumption_list):
    """
    Etsii käyttäjänsyöttämästä energiankulutuslistasta suurimman arvon
    ja laskee tämän avulla suurimman luokan.

    :param energy_consumption_list: Ottaa parametrinä energiankulutuslistan
    :return: ja palauttaa suurimman tarvittavan energiakulutusluokan arvon
    """

    # Haetaan listan suurin arvo
    largest_number = max(energy_consumption_list)

    # Suurimman tarvittavan luokan muuttuja
    largest_class_number = 1

    # Suurin arvo jaetaan kymmenellä niin monta kertaa kun pystytään ja
    # kasvatetaan samalla suurimman luokan muuttujaa
    while largest_number > 0:

        largest_number = largest_number // 10

        if largest_number > 0:

            largest_class_number += 1

    return largest_class_number


def class_minimum_value(class_number):
    """
    Funktio saa parametrinä luokan arvon ja laskee tämän avulla luokan
    alarajan.
    :param class_number: Luokan arvo
    :return: Luokan alaraja
    """

    minimum_value = 10 ** class_number // 100 * 10

    return minimum_value


def class_maximum_value(class_number):
    """
    Funktio saa parametrinä luokan arvon ja laskee tämän avulla luokan
    ylärajan.
    :param class_number: Luokan arvo
    :return: Luokan yläraja
    """

    maximum_value = 10 ** class_number - 1

    return maximum_value


def specify_the_class(consumption_value):
    """
    Funktio joka selvittää käyttäjän syöttämältä listalta mihin luokkaan
    yksittäinen arvo kuuluu
    :param consumption_value:käyttäjän syöttämä energiankulutusarvo
    :return:Luokan numeron johon kyseinen arvo kuuluu
    """

    class_number = 1

    # Edellä olevia luokan yla- ja alarajat laskevia funktioita apuna käyttäen
    # tutkii mihin luokkaan arvo kuuluu.
    while True:
        if class_minimum_value(class_number) <= consumption_value <= \
                class_maximum_value(class_number):
            # Palauttaa luokan numeron.
            return class_number

        # mikäli arvo ei kuulu kyseiseen luokkaan kasvattaa luokkaa yhdellä
        # ja tutkii uudelleen kunnes oikea luokka löytyy.
        class_number += 1

def calculate_amounts_in_classess(energy_consumption_list):
    """
    Käy specify_the_class funktion avulla läpi käyttäjän syöttämän listan ja
    muodostaa uuden listan jossa kerrotaan montako arvoa kuhunkin luokkaan
    kuuluu.
    :param energy_consumption_list: Käyttäjän syöttämä energiankulutuslista
    :return: Lista joka kertoo montako arvoa kuhunkin energiankulutusluokkaan
    kuuluu
    """

    # Luodaan tyhjälista ja määritellään sen koko suurimman energiankulutus-
    # luokan avulla
    values_in_classess = [0] * calculate_largest_class_number\
        (energy_consumption_list)

    # Käydään energiankulutuslista läpi edelläolevan funktion avulla ja
    # lasketaan montako arvoa kuuluu mihinkin luokkaan.
    for consumption_value in energy_consumption_list:
        class_number = specify_the_class(consumption_value)
        values_in_classess[class_number-1] += 1

    return values_in_classess


def print_histogram(energy_consumption_list, amount_of_the_values_in_classes):
    """
    Funktio joka käy läpi values_in_classess listan ja tulostaa
    print_single_histogram_line funktion avulla histogrammit antaen tälle
    oikeat parametrit
    :param energy_consumption_list: käyttäjän syöttämä lista
    :param amount_of_the_values_in_classes: lista joka kertoo montako arvoa
    energy_consumption_list listalta kuuluu mihinkin luokkaan
    :return:
    """

    for i in range (len(amount_of_the_values_in_classes)):

            print_single_histogram_line(i+1, amount_of_the_values_in_classes[i],
                                    calculate_largest_class_number(
                                        energy_consumption_list))


def main():
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()

    energy_consumption_list = []

    read_and_check_energy_consumption(energy_consumption_list)

    if not energy_consumption_list:
        print("Nothing to print. Done.")
        return

    print_histogram(energy_consumption_list,
                    calculate_amounts_in_classess(energy_consumption_list))



"""
Tämä funktio oli valmiina harjoitustyön ohjelmakoodipohjassa.
Ei siis itse tehty!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
def print_single_histogram_line(class_number, count, largest_class_number):
    """
    Tämä on luultavasti projektin haastavin funktio, joten tässä se on
    valmiina.  Funktio tulostaa oikean muotoisen histogrammin rivin,
    kuhan kutsut sitä oikeilla parametrien arvoilla.

    :param class_number: int,
        Mitä kulutuskatergoriaa tulostettava rivi kuvaa (1, 2, 3, ...)
        Parametria <class_number> käytetään päättämään, mikä arvoväli
        (0-9, 10-99, 100-999, ...) riville tulostuu ennen diagrammin
        "*"-merkkejä.

    :param count: int,
        Kuinka monta "*"-merkkiä riville on tarpeen tulostaa, eli
        kuinka monta käyttäjän syöttämää arvoa kuuluu <class_number>-
        parametrin kuvaamalle välillä.

    :param largest_class_number: int,
        Mikä on kaikkein suurin kategorian numero.  Riippuu
        suurimmasta käyttäjän syöttämästä kulutusarvosta.
        Esimerkiksi jos suurin käyttäjän syöttämä luku
        oli 91827364 (8 numeromerkkiä) <largest_class_number>-parametrin
        arvon tulisi myös olla 8.  Parametrin arvoa käytetään
        määriteltäessä, kuinka monta välilyöntiä muiden kuin viimeisen
        histogrammin rivin eteen pitäisi tulostaa.
    """

    # <range_string>-muuttujaan talletetaan merkijonona rivin
    # histogrammissa kuvaama arvoväli. Esimerkiksi "1000-9999".
    # Apufunktiot class_minimum_value ja class_maximum_value
    # sinun on määriteltävä itse.

    min_value = class_minimum_value(class_number)
    max_value = class_maximum_value(class_number)
    range_string = f"{min_value}-{max_value}"


    # Kun histogrammin viimeinen rivi tulostetaa, kuinka monta
    # merkkiä leveä tulee <range_string> silloin olemaan.
    # Jos esimerkiksi <largest_class_number> on 7, tarkoittaisi
    # se, että arvoväliksi tulostetaan "1000000-9999999" eli
    # muuttujaan <largest_width> pitää tallentaa arvo 15.
    # Kaikkien arvovälien <range_string> tulostetaan tämän
    # levyisen kentän oikeaan laitaan.

    largest_width = 2 * largest_class_number + 1


    # Kaikki valmistelun on tehty, voidaan tulostaa rivi,
    # jonka alussa on oikea määrä välilyöntejä, niiden perässä
    # arvoväli ja lopulta oikea määrä "*"-merkkejä.
    # Merkki ">" seuraavassa f""-merkkijonossa tulostaa
    # <range_string>:in arvon tulostuskentän oikeaan laitaan
    # (täytevälilyönnit tulostetaan alkuun).

    print(f"{range_string:>{largest_width}}: {'*' * count}")


if __name__ == "__main__":
    main()
