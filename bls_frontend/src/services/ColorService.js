export const colorDictionary = {
    ['ablehnung einstweilige anordnung']: 'ablehnung-color',
    ['urteil']: 'urteil-color',
    ['teilurteil']: 'teilurteil-color',
    ['nichtannahmebeschluss']: 'nichtannahme-color',
    ['gegenstandswertfestsetzung im verfassungsgerichtlichen verfahren']: 'gegenstand-color',
    ['stattgebender kammerbeschluss']: 'kammerStatt-color',
    ['kammerbeschluss']: 'kammer-color',
    ['kammerbeschluss ohne begründung']: 'kammerOhne-color',
    ['beschluss']: 'beschluss-color',
    ['vorlagebeschluss']: 'vorlage-color',
    ['versäumnisurteil']: 'versaeumnis-color',
    ['einstweilige anordnung']: 'einstweilige-color',
    ['eugh-vorlage']: 'eugh-color',
};

/**
 * Service for generating and providing colors for the different types of verdict
 */
export class ColorService {
    constructor() {
        /**
         * Comment this line in to generate a new Color.
         * Copy generated output from the browser console into 'colors.css'.
         * Also create an entry in the above dictionary, where the key is your documenttype in lowercase letters
         * and the value is the generated colorclass name
         */
        //this.generateColor('vorlage', '220, 86, 58')
    }

    /**
     * Returns the name of the color class associated with a documenttype of a verdict
     * @param docType The documenttype of the verdict
     * @returns {string} The name of the color class
     */
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
            '.' + name + '-color div div div div button {\n' +
            '    background-color: rgba(' + rgb + ', 0.59);\n' +
            '}\n' +
            '\n' +
            '.' + name + '-color div div div div button:hover {\n' +
            '    background-color: rgba(' + rgb + ', 0.7);\n' +
            '}\n' +
            '\n' +
            '.' + name + '-color div div div div button:focus {\n' +
            '    background-color: rgba(' + rgb + ', 0.59);\n' +
            '    box-shadow: 0 0 0 3px rgba(' + rgb + ', 0.25) !important;\n' +
            '}\n' +
            '\n' +
            '.' + name + '-color div div div div button:active {\n' +
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