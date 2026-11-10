from pyscript import document

#Non metals
#dictionary w information about non metals
# <!--Chemical Symbol, Atomic Number, Atomic Mass -->

nonmetals ={ "H": ("Hydrogen", 1, 1.008),
            "He": ("Helium", 2, 4.0026),
            "C": ("Carbon", 6, 12.011),
            "N": ("Nitrogen", 7, 14.007),
            "O": ("Oxygen", 8, 15.999),
            "F": ("Fluorine", 9, 18.998),
            "NE": ("Neon", 10, 20.180),
            "P": ("Phosphorus", 15, 30.974),
            "S": ("Sulfur", 16, 32.06),
            "CL": ("Chlorine", 17, 35.45),
            "AR": ("Argon", 18, 39.948),
            "SE": ("Selenium", 34, 78.971),
            "BR": ("Bromine", 35, 79.904),
            "KR": ("Krypton", 36, 83.798),
            "I": ("Iodine", 53, 126.90),
            "XE": ("Xenon", 54, 131.29),
            "RN": ("Radon", 86, 222),
            "OG": ("Oganesson", 118, 294),
}

#Create function to search element info
def search_element(e):
    # get the input from html
    Element1 = document.getElementById("element1").value.upper().strip()
    #retrieve info from dictionary
    result = nonmetals.get(Element1, ("Element not found", "", ""))
    #display of result
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]