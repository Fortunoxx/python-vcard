import qrcode

def export(fcn, exportFolder):
    # with open(fcn) as file:
    with open(fcn, encoding='utf8') as file:
        id = 0
        vcards = ""

        for line in file:
            line = line.strip()

            firstname, lastname, street, number, plz, city, birthdate, cellphone, email = line.split(";")
            day, month, year = birthdate.split(".")

            vcard = "BEGIN:VCARD" 
            vcard += f"\nVERSION:4.0"
            # vcard += f"\nVERSION:2.1"
            vcard += f"\nEMAIL;PREF=1:{email}"
            vcard += f"\nFN;CHARSET=UTF-8:{firstname} {lastname}"
            vcard += f"\nADR;CHARSET=UTF-8;HOME:;;{street} {number};{city};NRW;{plz};Germany"
            # vcard += f"\nADR;HOME:;;{street} {number};{city};NRW;{plz};Germany"
            # vcard += f"\nBDAY:{year}{month}{day}"
            vcard += f"\nBDAY;VALUE=DATE:{year}{month}{day}"
            vcard += f"\nTEL;TYPE=cell:{cellphone}"
            # vcard += f"\nEMAIL;TYPE=home:{email}"
            vcard += f"\nEND:VCARD"

            vcards += vcard + "\n"
            id += 1

            filename = f'{exportFolder}/{str(id)}-{firstname} {lastname}'
            with open(f'{filename}.vcf', 'w', encoding='utf8') as exportFile:
                exportFile.write(vcard)

            # Encoding data using make() function
            img = qrcode.make(vcard)
            img.save(f'{filename}.png')

        with open(f'{exportFolder}/all.vcf', 'w') as exportFile:
            exportFile.write(vcards)

export("data/data.csv", "export")
