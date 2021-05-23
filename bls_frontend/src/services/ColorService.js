// TODO: Dictionary befullen
export const colorDictionary = {
    ['ablehnung einstweilige anordnung']: 'ablehnung-color',
    ['urteil']: 'urteil-color',
    // TODO: Farben aussuchen, generieren
    ['nichtannahmebeschluss']: '',
    ['gegenstandswertfestsetzung im verfassungsgerichtlichen verfahren']: '',
    ['stattgebender kammerbeschluss']: '',
    ['beschluss']: '',
};

export class ColorService {
    constructor() {
        //this.generateColor('urteil', '0, 136, 255')
    }

    colorClass(docType) {
        const key = docType.toLowerCase()
        if (colorDictionary[key]) {
            return colorDictionary[key]
        } else {
            return 'default-color'
        }
    }

    /**
     * Zum generieren der Farben der colors.css.
     * Muss bei Bedarf um neue Farbklassen erweitert werden.
     * Beispielaufruf im Konstruktor auskommentieren und Daten einfüllen.
     *
     * @param name String des namens
     * @param rgb String der Farbe in rgb im Format "r, g, b"
     */
    generateColor(name, rgb) {
        console.log('.' + name + '-color {\n' +
            '    border-color: rgba(' + rgb + ', 0.59);\n' +
            '}\n' +
            '\n' +
            '.' + name + '-color div div div div a {\n' +
            '    background-color: rgba(' + rgb + ', 0.59);\n' +
            '}\n' +
            '\n' +
            '.' + name + '-color div div div div a:hover {\n' +
            '    background-color: rgba(' + rgb + ', 0.7);\n' +
            '}\n' +
            '\n' +
            '.' + name + '-color div div div div a:focus {\n' +
            '    background-color: rgba(' + rgb + ', 0.59);\n' +
            '    box-shadow: 0 0 0 3px rgba(' + rgb + ', 0.25) !important;\n' +
            '}\n' +
            '\n' +
            '.' + name + '-color div div div div a:active {\n' +
            '    background-color: rgba(' + rgb + ', 0.85) !important;\n' +
            '}\n' +
            '\n' +
            '.' + name + '-color .card-footer {\n' +
            '    border-top: 1px solid rgba(' + rgb + ', 0.2);\n' +
            '}\n' +
            '\n' +
            '.' + name + '-color div div div div div span {\n' +
            '    background-color: rgba(' + rgb + ', 0.59);\n' +
            '}')
    }
}