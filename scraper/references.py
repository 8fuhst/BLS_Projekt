import re

# todo: Aktenzeichen von BSG und BFH, Unterschiedliche Aktenzeichen die aufs gleiche verweisen
aktenzeichenRegEx = re.compile("(((VGS|RiZ\\s?s?\\(R\\)|KZR|VRG|RiZ|EnRB|StbSt\\s?\\(B\\)|AnwZ\\s?\\(Brfg\\)|RiSt|PatAnwSt\\s?\\(R\\)|AnwZ\\s?\\(B\\)|PatAnwZ|EnVZ|AnwSt\\s?\\(B\\)|NotSt\\s?\\(Brfg\\)|KVZ|KZB|AR\\s?\\(Ri\\)|NotZ\\s?\\(Brfg\\)|RiSt\\s?\\(B\\)|AnwZ\\s?\\(P\\)|EnZB|RiSt\\s?\\(R\\)|NotSt\\s?\\(B\\)|AnwSt|WpSt\\s?\\(R\\)|KVR|AR\\s?\\(Kart\\)|EnZR|StbSt\\s?\\(R\\)|WpSt\\s?\\(B\\)|KZA|AR\\s?\\(Enw\\)|AnwSt\\s?\\(R\\)|KRB|RiZ\\s?\\(B\\)|PatAnwSt\\s?\\(B\\)|EnVR|AnwZ|NotZ|EnZA|AR)\\s\\d+/\\d+)|" \
            "((GSZ|LwZB|WpSt\\s?\\(B\\)|AnwZ|LwZR|KVZ|EnRB|PatAnwSt\\s?\\(B\\)|ARP|VGS|WpSt\\s?\\(R\\)|RiSt\\s?\\(B\\)|EnZA|KRB|AnwSt\\s?\\(R\\)|NotSt\\s?\\(Brfg\\)|EnVR|LwZA|ZB|AR\\s?\\(Vollz\\)|StB|ZR|AR\\s?\\(VS\\)|BJs|BLw|NotZ\\s?\\(Brfg\\)|RiZ\\s?\\(B\\)|PatAnwSt\\s?\\(R\\)|AK|RiZ|PatAnwZ|ARs|StbSt\\s?\\(R\\)|VRG|NotSt\\s?\\(B\\)|AR\\s?\\(Enw\\)|AR\\s?\\(VZ\\)|StE|KVR|AR\\s?\\(Ri\\)|AR|AnwSt|NotZ|StbSt\\s?\\(B\\)|StR|ZA|AnwZ\\s?\\(B\\)|EnZR|AR\\s?\\(Kart\\)|GSSt|AnwZ\\s?\\(P\\)|ZR\\s?\\(Ü\\)|AnwZ\\s?\\(Brfg\\)|KZB|BGns|KZR|RiSt|KZA|BAusl|AnwSt\\s?\\(B\\)|BGs|RiZ\\s?\\(R\\)|EnZB|RiSt\\s?\\(R\\)|ARZ|EnVZ)\\s\\d+/\\d+)|" \
            "([I+|IV|V|VI|VII|VIII|IX|X|XI|XII|1-6]+[a-z]?\\s[A-Za-z()]{2,20}\\s\\d+/\\d\\d))")

# paragraf = re.compile("§+ \d+[a-z]? (?:Abs\.|Nr\.|Satz|Halbsatz|Absatz|\d+[a-z]?|und(?: §)?|,(?: §)?| )*[A-Za-z]+")

test = ["(a) Dieser IV ZR 221/19 Umstand ist abweichend von der Rechtsauffassung der Kläger bei der Berechnung des steuerfreien Teils der Rente prognostisch bereits für das Streitjahr einzubeziehen. 4 AZR 339/17 Grund hierfür ist, dass die bis zum vorgenannten Zeitpunkt vom Kläger bezogene Teilaltersrente i.S. von § 42 Abs. 1 SGB VI weder sozialversicherungs- noch steuerrechtlich eine von der späteren Vollrente gesondert zu beurteilende Rente ist. Vielmehr handelt es sich um eine hinsichtlich der Rentenhöhe ins Ermessen des Berechtigten gestellte anteilige Altersrente in Gestalt einer \"quotierten Vollrente\" 2 BvR 721/21 (vgl. hierzu Urteil des Bundesarbeitsgerichts vom 22.09.2016 - 6 AZR 397/15, Neue Zeitschrift für Arbeitsrecht 2017, 398, Rz 20), die sich dann als sinnvoll erweisen kann, wenn der Berechtigte für Zeiten vor Beginn der Regelaltersgrenze Hinzuverdienstgrenzen ausschöpfen möchte (u.a. Gürtner in Kasseler Kommentar zum Sozialversicherungsrecht, § 42 SGB VI Rz 6). Demzufolge ist --auf Grundlage der Rentenwertverhältnisse des Streitjahres-- ab September 2013 ein monatlicher Rentenbetrag von ... € zu berücksichtigen."]


test2 = ["I.","5","Das Berufungsgericht hat zur Begründung seiner in juris (Az. 3 U 2220/19) und unter BeckRS 2019, 33738 veröffentlichten Entscheidung, soweit für das Revisionsverfahren von Interesse, im Wesentlichen Folgendes ausgeführt:","6","Die Beklagte hafte nicht aus § 823 Abs. 2 BGB i.V.m. § 263 StGB. Der Kläger habe den Vorsatz der Beklagten bzw. eines verfassungsmäßigen Vertreters, für welchen er grundsätzlich beweisbelastet sei, nicht nachweisen können. Zwar habe der Kläger hinreichend konkret, schlüssig und substantiiert dargelegt und unter Beweis gestellt, dass der damalige Vorstandsvorsitzende der Beklagten vorsätzlich gehandelt habe. Doch habe der zunächst als Zeuge geladene Genannte unter Bezugnahme auf die gegen ihn laufenden Straf- und Ermittlungsverfahren zu Recht umfassend von seinem Zeugnisverweigerungsrecht nach § 384 Nr. 2 ZPO Gebrauch gemacht. Erleichterungen im Rahmen der sekundären Darlegungs- und Beweislast kämen dem Kläger unter den Umständen des Streitfalls nicht zugute. Die sekundäre Darlegungs- und Beweislast diene dazu, der darlegungs- und beweisbelasteten Partei darüber hinwegzuhelfen, dass sie den erforderlichen Vortrag aufgrund mangelnder Kenntnis nicht erbringen könne, während dies der anderen Partei möglich und zumutbar sei. Damit bedürfe es deren Anwendung nicht, wenn die darlegungspflichtige Partei wie im Streitfall in der Lage sei, die anspruchsbegründenden Tatsachen vorzutragen. Zweck der Annahme einer sekundären Darlegungslast sei es nicht, der Partei, die ihren ausreichenden Vortrag nicht beweisen könne, weitere Tatsachen in die Hand zu geben, welche einen erneuten und weiteren Vortrag zur Anspruchsbegründung ermöglichten. Abgesehen davon habe die Beklagte geltend gemacht, alles Zumutbare und Mögliche getan zu haben, um die tatsächlichen Geschehnisse aufzuklären. Ein Berufungsangriff hiergegen sei nicht erfolgt.","7","Ein Anspruch aus §§ 826, 31 BGB scheide aus, weil der geltend gemachte Schaden schon nicht vom Schutzzweck des § 826 BGB gedeckt werde. Es möge sein, dass verantwortliche Personen der Beklagten in Bezug auf Belange des Umweltschutzes sittenwidrig gehandelt hätten. Der hier geltend gemachte Schaden (Abschluss eines Kaufvertrags) liege aber außerhalb des Schutzbereichs des Gebots, das Fahrzeug nicht ohne gültige EG-Übereinstimmungsbescheinigung in den Verkehr zu bringen.","8","Nach der vorzunehmenden Gesamtwürdigung könne das Inverkehrbringen des Fahrzeugs mit der Umschaltlogik nicht als (konkludente) Täuschung durch positives Tun qualifiziert werden, zumal der Einsatz des Fahrzeugs mit der EG-Übereinstimmungsbescheinigung ohne Weiteres möglich gewesen sei und weiterhin sei. Eine Pflicht zur Aufklärung über den Einsatz der \"Schummelsoftware\" habe jedenfalls keine solche Schwere, als dass eine Aufklärung einem sittlichen Gebot entsprochen hätte. Erhebliche wertbildende Faktoren seien nicht verletzt. Der Kläger nutze das Fahrzeug seit dem Kauf legal und uneingeschränkt. Sittenwidriges Verhalten sei der Beklagten erst dann vorzuwerfen, wenn sie trotz positiver Kenntnis von der Chancenlosigkeit der Erhaltung der Betriebserlaubnis geschwiegen hätte, also in Kenntnis des Umstandes, dass eine Untersagung der Betriebserlaubnis unmittelbar bevorgestanden hätte. Dies sei weder geltend gemacht noch ersichtlich.","9","Unabhängig davon habe der Kläger den Beweis vorsätzlichen Handelns von Personen i.S.d. § 31 BGB nicht geführt und könne sich aus den zuvor genannten Gründen auch im Rahmen der §§ 826, 31 BGB nicht auf eine sekundäre Darlegungslast der Beklagten berufen.","10","Im Übrigen müsse sich der Vorsatz der Personen, deren Verhalten der Beklagten nach § 31 BGB zuzurechnen sei, darauf beziehen, dass das Kraftfahrzeug für den Kläger aufgrund der \"Schummelsoftware\" wertlos geworden sei. Eine etwa zu erwartende Belastung des Klägers wegen sich bei einem späteren Weiterverkauf ergebender Einbußen aufgrund eines geringeren Gebrauchtwagenpreises reiche dazu nicht aus.","II.","11","Diese Erwägungen halten der revisionsrechtlichen Überprüfung nicht stand. Mit der Begründung des Berufungsgerichts kann ein Schadensersatzanspruch des Klägers aus § 826 BGB wegen vorsätzlicher sittenwidriger Schädigung nicht verneint werden.","12","1. Entgegen der Auffassung des Berufungsgerichts ist das Verhalten der Beklagten im Verhältnis zum Kläger als sittenwidrig zu qualifizieren (vgl. im Einzelnen Senatsurteil vom 25. Mai 2020 - VI ZR 252/19, BGHZ 225, 316 Rn. 16 ff., 21, 23). Die Untersagung der Betriebserlaubnis des Fahrzeugs musste hierfür nicht unmittelbar bevorstehen. Es genügt, dass nicht feststand, welche der rechtlich möglichen und grundsätzlich auch die Vornahme einer Betriebsbeschränkung oder -untersagung nach § 5 Abs. 1 FZV umfassenden Maßnahmen die Behörden bei Aufdeckung der Verwendung der unzulässigen Abschalteinrichtung ergreifen würden. Auf das Bestehen einer Pflicht zur Aufklärung über die verwendete Software kommt es, anders als das Berufungsgericht meint, danach nicht mehr an (vgl. Senatsurteil vom 25. Mai 2020 - VI ZR 252/19, BGHZ 225, 316 Rn. 26).","13","2. Die Revision wendet sich weiter mit Erfolg gegen die Beurteilung des Berufungsgerichts, ein Anspruch aus § 826 BGB scheide bereits deshalb aus, weil der Kläger nicht habe beweisen können, dass der von ihm als Zeuge benannte damalige Vorstandsvorsitzende der Beklagten, dessen Handeln sich die Beklagte gemäß § 31 BGB zurechnen lassen müsste, den deliktischen Tatbestand verwirklicht habe.","14","a) Zwar trägt im Grundsatz derjenige, der einen Anspruch aus § 826 BGB geltend macht, die volle Darlegungs- und Beweislast für die anspruchsbegründenden Tatsachen. Bei der Inanspruchnahme einer juristischen Person hat der Anspruchsteller dementsprechend auch darzulegen und zu beweisen, dass ein verfassungsmäßig berufener Vertreter (§ 31 BGB) die objektiven und subjektiven Tatbestandsvoraussetzungen des § 826 BGB verwirklicht hat (vgl. Senatsurteile vom 26. Januar 2021 - VI ZR 405/19, ZIP 2021, 368 Rn. 15; vom 30. Juli 2020 - VI ZR 367/19, ZIP 2020, 1763 Rn. 15; vom 25. Mai 2020 - VI ZR 252/19, BGHZ 225, 316 Rn. 35).","15","Dieser Grundsatz erfährt aber eine Einschränkung, wenn die primär darlegungsbelastete Partei keine nähere Kenntnis von den maßgeblichen Umständen und auch keine Möglichkeit zur weiteren Sachaufklärung hat, während der Prozessgegner alle wesentlichen Tatsachen kennt und es ihm unschwer möglich und zumutbar ist, nähere Angaben zu machen. In diesem Fall trifft den Prozessgegner eine sekundäre Darlegungslast, im Rahmen derer es ihm auch obliegt, zumutbare Nachforschungen zu unternehmen. Genügt er seiner sekundären Darlegungslast nicht, gilt die Behauptung des Anspruchstellers nach § 138 Abs. 3 ZPO als zugestanden (vgl. Senatsurteile vom 26. Januar 2021 - VI ZR 405/19, ZIP 2021, 368 Rn. 16; vom 30. Juli 2020 - VI ZR 367/19, ZIP 2020, 1763 Rn. 16; vom 25. Mai 2020 - VI ZR 252/19, BGHZ 225, 316 Rn. 37 ff. mwN).","16","b) Nach diesen Grundsätzen traf die Beklagte die sekundäre Darlegungslast hinsichtlich der Frage, wer die Entscheidung über den Einsatz der unzulässigen Abschalteinrichtung bei ihr getroffen und ob ihr Vorstand hiervon Kenntnis hatte.","17","aa) Die Fragen, wer die Entscheidung über den Einsatz der unzulässigen Abschalteinrichtung bei der Beklagten getroffen und ob der Vorstand hiervon Kenntnis hatte, betreffen unternehmensinterne Abläufe und Entscheidungsprozesse, die sich der Kenntnis und dem Einblick des Klägers entziehen. Demgegenüber war der Beklagten Vortrag hierzu möglich und zumutbar (vgl. Senatsurteile vom 26. Januar 2021 - VI ZR 405/19, ZIP 2021, 368 Rn. 19; vom 30. Juli 2020 - VI ZR 367/19, ZIP 2020, 1763 Rn. 19; vom 25. Mai 2020 - VI ZR 252/19, BGHZ 225, 316 Rn. 39 ff.).","18","bb) Dem steht nicht entgegen, dass der Kläger seinen Vortrag hinsichtlich der Person des damaligen Vorstandsvorsitzenden der Beklagten soweit substantiieren konnte, dass sich das Berufungsgericht zunächst veranlasst sah, diesen als Zeugen zu laden.","19","Zum einen rügt die Revision mit Erfolg (§ 286 ZPO), dass sich der Vortrag des Klägers, der Vorstand der Beklagten habe über umfassende Kenntnis von dem Einsatz der unzulässigen Abschaltsoftware verfügt, erkennbar auf den gesamten Vorstand der Beklagten und nicht nur auf die Person ihres damaligen Vorstandsvorsitzenden bezog. Allein der Umstand, dass der damalige Vorstandsvorsitzende zunächst als Zeuge geladen wurde, bevor er sich auf sein Zeugnisverweigerungsrecht aus § 384 Nr. 2 ZPO berief und wieder abgeladen wurde, entbindet die Beklagte daher nicht von ihrer sekundären Darlegungslast hinsichtlich der Kenntnis des Vorstands im Übrigen.","20","Zum anderen wäre der außerhalb des maßgeblichen Geschehens stehende Geschädigte - folgte man der Ansicht des Berufungsgerichts - schutzlos gestellt, wenn er in Bezug auf eine der handelnden Personen ausreichende Anhaltspunkte für ein (möglicherweise) strafbares Verhalten vortragen kann, diese Person jedoch naturgemäß wegen der Gefahr einer strafrechtlichen Verfolgung als Zeuge nicht zur Verfügung steht (§ 384 Nr. 2 ZPO). Das ist mit der aus den verfassungsrechtlich geschützten Rechten auf ein faires Verfahren und auf effektiven Rechtsschutz folgenden Verpflichtung zu einer fairen Verteilung der Darlegungs- und Beweislasten (vgl. BVerfG NJW 2019, 1510 Rn. 12 ff.; BVerfG NJW 2000, 1483, 1484, juris Rn. 42) nicht zu vereinbaren und hat der Bundesgerichtshof auch in der Vergangenheit im Zusammenhang mit Sachverhalten, in denen von einer sekundären Darlegungslast ausgegangen wurde, nicht angenommen (vgl. etwa BGH, Urteil vom 18. Januar 2018 - I ZR 150/15, NJW 2018, 2412 Rn. 28; zum Ganzen Senatsurteil vom 25. Mai 2020 - VI ZR 252/19, BGHZ 225, 316 Rn. 42).","21","c) Mit der pauschalen Behauptung, alles Zumutbare und Mögliche getan zu haben, um die tatsächlichen Geschehnisse aufzuklären, hat die Beklagte dieser ihr obliegenden sekundären Darlegungslast erkennbar nicht genügt. Wie die Revision zu Recht rügt, bedurfte es insoweit - jenseits der Berufung auf eben die Grundsätze der sekundären Darlegungslast, die einen zentralen Berufungsangriff des Klägers darstellte - keiner näheren Ausführungen durch den Kläger, welche Aufklärungsschritte der Beklagten darüber hinaus noch zumutbar und möglich gewesen wären.","22","3. Mit der Begründung des Berufungsgerichts kann zudem der für einen Ersatzanspruch aus § 826 BGB erforderliche Schaden nicht verneint werden.","23","Ein Schaden im Sinne des § 826 BGB kann auch in einer auf dem sittenwidrigen Verhalten beruhenden Belastung mit einer ungewollten Verpflichtung liegen (Senatsurteile vom 26. Januar 2021 - VI ZR 405/19, ZIP 2021, 368 Rn. 21; vom 30. Juli 2020 - VI ZR 367/19, ZIP 2020, 1763 Rn. 21; vom 25. Mai 2020 - VI ZR 252/19, BGHZ 225, 316 Rn. 46 ff. mwN). Der vom Kläger geltend gemachte Schaden (Abschluss des ungewollten Kaufvertrags) liegt damit nicht außerhalb des Schutzzwecks des § 826 BGB. Auf den Schutzzweck des Gebots, das Fahrzeug nicht ohne gültige EG-Übereinstimmungsbescheinigung in den Verkehr zu bringen, kommt es im Rahmen des Schadensersatzanspruchs aus § 826 BGB entgegen der Auffassung des Berufungsgerichts nicht an (vgl. Senatsurteil vom 26. Januar 2021 - VI ZR 405/19, ZIP 2021, 368 Rn. 24; vom 30. Juli 2020 - VI ZR 367/19, ZIP 2020, 1763 Rn. 23 f.).","24","4. Rechtsfehlerhaft hat das Berufungsgericht schließlich angenommen, dass sich der Schädigungsvorsatz der nach § 31 BGB für die Beklagte handelnden Personen darauf beziehen müsse, dass das Kraftfahrzeug für den Kläger aufgrund der \"Schummelsoftware\" wertlos geworden sei. Da der Schaden des Käufers in dem Abschluss des ungewollten Kaufvertrags liegt, reichte es für die Annahme des hierauf bezogenen Vorsatzes aus, wenn den genannten Personen bewusst war, dass in Kenntnis des Risikos einer Betriebsbeschränkung oder -untersagung der betroffenen Fahrzeuge niemand - ohne einen erheblichen, dies berücksichtigenden Abschlag vom Kaufpreis - ein damit belastetes Fahrzeug erwerben würde (vgl. Senatsurteil vom 25. Mai 2020 - VI ZR 252/19, BGHZ 225, 316 Rn. 63).","III.","25","Die Sache ist schon deshalb nicht zur Entscheidung reif, weil das Berufungsgericht - von seinem Standpunkt aus konsequent - keine Feststellungen zum durchzuführenden Vorteilsausgleich getroffen hat. Das Berufungsurteil ist daher aufzuheben und die Sache zur neuen Verhandlung und Entscheidung an das Berufungsgericht zurückzuverweisen (§ 562 Abs. 1, § 563 Abs. 1 Satz 1 ZPO).","Seiters     ","        ","von Pentz     ","        ","Oehler","        ","Klein      ","        ","Böhm      ","        "]
# [[1, Aktenzeichen, Aktenzeichen], [2, Aktenzeichen], [3, Aktenzeichen], ...]
def find_reference(tag, text_array, outgoing_references_set):
    matches_dict = {}
    all_matches = []
    for index, text in enumerate(text_array):
        matches = re.findall(aktenzeichenRegEx, text)
        index_matches_list = []
        for match in matches:
            for entry in match:
                if entry != '':
                    index_matches_list.append(entry)
                    outgoing_references_set.add(entry)
        if len(index_matches_list) != 0: # todo frontend fragen ob die das wollen
            all_matches.append([str(index)] + list(set(index_matches_list)))
    matches_dict[tag] = all_matches
    return matches_dict, outgoing_references_set

# print(find_reference("test", test2))

'''
Wo befinden wir uns? Tenor, Gründe...
Wie wollen wir das speichern?

'''

'''
XI 21 BGH: [[II 14 BFG, reasons, 4], []], [IV 12 BSG...]]



Parent_aktenz $ child_aktenzeichen $ Fundort

ES Felder: [ID][Aktenzeichen][Liste ausgehend][Menge ausgehend][Menge eingehend][Summe eingehend]
aktenzeichen: (reasons: (1, ref, ref), (4, ref)), (tenor: (3, ref, ref) ...)

Offene Probleme:
Referenz auf Aktenzeichen, dass (noch) nicht in der Tabelle ist.
Einheitliche Formatierung der Aktenzeichen.
'''