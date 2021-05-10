package com.bls_tool.controller;

import net.minidev.json.JSONArray;
import net.minidev.json.JSONObject;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/urteil")
public class UrteilController {

    @GetMapping
    public String urteil() {
        JSONObject result = new JSONObject();
        result.put("gericht", "BVerfG");
        result.put("entscheidungsdatum", "05.05.2021");
        JSONArray aktenzeichen = new JSONArray();
        aktenzeichen.add("1 BvR 781/21");
        aktenzeichen.add("1 BvR 805/2");
        aktenzeichen.add("1 BvR 820/21");
        aktenzeichen.add("1 BvR 854/21");
        aktenzeichen.add("1 BvR 889/21");
        result.put("aktenzeichen", aktenzeichen);

        result.put("ecli", "ECLI:DE:BVerfG:2021:rs20210505.1bvr078121");
        result.put("dokumenttyp", "Ablehnung einstweilige Anordnung");
        JSONArray normen = new JSONArray();
        normen.add("Art 2 Abs 1 GG");
        normen.add("Art 3 Abs 3 S 2 GG");
        normen.add("Art 6 Abs 1 GG");
        normen.add("Art 12 Abs 1 GG");
        normen.add("Art 77 Abs 2 GG");
        normen.add("Art 104a Abs 4 GG");
        normen.add("§ 32 Abs 1 BVerfGG");
        normen.add("§ 32 Abs 2 S 2 BVerfGG");
        normen.add("Art 1 Nr 2 EpiBevSchG 4");
        normen.add("§ 28a Abs 2 S 1 Nr 2 IfSG");
        normen.add("§ 28b Abs 1 S 1 Nr 2 IfSG vom 22.04.2021");
        normen.add("§ 28b Abs 1 S 1 Nr 2 Buchst b IfSG vom 22.04.2021");
        normen.add("§ 28b Abs 1 S 1 Nr 2 Buchst c IfSG vom 22.04.2021");
        normen.add("§ 28b Abs 1 S 1 Nr 2 Buchst d IfSG vom 22.04.2021");
        normen.add("§ 28b Abs 1 S 1 Nr 2 Buchst f IfSG vom 22.04.2021");
        normen.add("§ 28b Abs 3 S 1 IfSG vom 22.04.2021");
        normen.add("§ 56 Abs 1a IfSG vom 29.03.2021, § 73 Abs 1a Nr 11c IfSG vom 22.04.2021");
        result.put("normen", normen);
        result.put("Kurztext", "Eilanträge gegen bundesrechtliche nächtliche Ausgangsbeschränkung (§ 28b Abs 1 S 1 Nr 2 IfSG idF vom 22.04.2021) erfolglos - angegriffene Normen weder formell noch materiell offensichtlich verfassungswidrig - Folgenabwägung\n" + "\n");
        result.put("Langtext", "    Eilanträge gegen bundesrechtliche nächtliche Ausgangsbeschränkung (§ 28b Abs 1 S 1 Nr 2 IfSG idF vom 22.04.2021) erfolglos - angegriffene Normen weder formell noch materiell offensichtlich verfassungswidrig - Folgenabwägung\n" +
                "\n" +
                "Tenor\n" +
                "\n" +
                "    Die Anträge auf Erlass einer einstweiligen Anordnung werden abgelehnt.\n" +
                "\n" +
                "Gründe\n" +
                "\n" +
                "    A.\n" +
                "\n" +
                "1\n" +
                "\n" +
                "    Die Beschwerdeführenden wenden sich gegen § 28b Abs. 1 Satz 1 Nr. 2 und gegen § 73 Abs. 1a Nr. 11c des Infektionsschutzgesetzes (IfSG) in der Fassung des am 23. April 2021 in Kraft getretenen Vierten Gesetzes zum Schutz der Bevölkerung bei einer epidemischen Lage von nationaler Tragweite vom 22. April 2021 (BGBl I S. 802). Mit ihren Anträgen auf Erlass einer einstweiligen Anordnung begehren sie, die Regelungen über Ausgangsbeschränkungen vorläufig außer Kraft zu setzen.\n" +
                "\n" +
                "    I.\n" +
                "\n" +
                "2\n" +
                "\n" +
                "    Durch Artikel 1 Nr. 2 des genannten Gesetzes vom 22. April 2021 wurde unter anderem § 28b Abs. 1 Satz 1 Nr. 2 IfSG mit einer Regelung über nächtliche Ausgangsbeschränkungen in das Infektionsschutzgesetz eingefügt. § 28b IfSG enthält folgende für den Gegenstand dieser Verfahren bedeutsame Bestimmungen:\n" +
                "\n" +
                "    § 28b\n" +
                "\n" +
                "    Bundesweit einheitliche Schutzmaßnahmen zur Verhinderung der Verbreitung der Coronavirus-Krankheit-2019 (COVID-19) bei besonderem Infektionsgeschehen, Verordnungsermächtigung\n" +
                "\n" +
                "    (1) Überschreitet in einem Landkreis oder einer kreisfreien Stadt an drei aufeinander folgenden Tagen die durch das Robert Koch-Institut veröffentlichte Anzahl der Neuinfektionen mit dem Coronavirus SARS-CoV-2 je 100 000 Einwohner innerhalb von sieben Tagen (Sieben-Tage-Inzidenz) den Schwellenwert von 100, so gelten dort ab dem übernächsten Tag die folgenden Maßnahmen:\n" +
                "\n" +
                "    1. private Zusammenkünfte im öffentlichen oder privaten Raum sind nur gestattet, wenn an ihnen höchstens die Angehörigen eines Haushalts und eine weitere Person einschließlich der zu ihrem Haushalt gehörenden Kinder bis zur Vollendung des 14. Lebensjahres teilnehmen; Zusammenkünfte, die ausschließlich zwischen den Angehörigen desselben Haushalts, ausschließlich zwischen Ehe- oder Lebenspartnerinnen und -partnern, oder ausschließlich in Wahrnehmung eines Sorge- oder Umgangsrechts oder im Rahmen von Veranstaltungen bis 30 Personen bei Todesfällen stattfinden, bleiben unberührt;\n" +
                "\n" +
                "    2. der Aufenthalt von Personen außerhalb einer Wohnung oder einer Unterkunft und dem jeweils dazugehörigen befriedeten Besitztum ist von 22 Uhr bis 5 Uhr des Folgetags untersagt; dies gilt nicht für Aufenthalte, die folgenden Zwecken dienen:\n" +
                "\n" +
                "    a) der Abwendung einer Gefahr für Leib, Leben oder Eigentum, insbesondere eines medizinischen oder veterinärmedizinischen Notfalls oder anderer medizinisch unaufschiebbarer Behandlungen,\n" +
                "\n" +
                "    b) der Berufsausübung im Sinne des Artikels 12 Absatz 1 des Grundgesetzes, soweit diese nicht gesondert eingeschränkt ist, der Ausübung des Dienstes oder des Mandats, der Berichterstattung durch Vertreterinnen und Vertreter von Presse, Rundfunk, Film und anderer Medien,\n" +
                "\n" +
                "    c) der Wahrnehmung des Sorge- oder Umgangsrechts,\n" +
                "\n" +
                "    d) der unaufschiebbaren Betreuung unterstützungsbedürftiger Personen oder Minderjähriger oder der Begleitung Sterbender,\n" +
                "\n" +
                "    e) der Versorgung von Tieren,\n" +
                "\n" +
                "    f) aus ähnlich gewichtigen oder unabweisbaren Zwecken oder\n" +
                "\n" +
                "    g) zwischen 22 und 24 Uhr der im Freien stattfindenden allein ausgeübten körperlichen Bewegung, nicht jedoch in Sportanlagen;\n" +
                "\n" +
                "    3. - 10. …\n" +
                "\n" +
                "    (2) Unterschreitet in einem Landkreis oder einer kreisfreien Stadt ab dem Tag nach dem Eintreten der Maßnahmen des Absatzes 1 an fünf aufeinander folgenden Werktagen die Sieben-Tage-Inzidenz den Schwellenwert von 100, so treten an dem übernächsten Tag die Maßnahmen des Absatzes 1 außer Kraft. Sonn- und Feiertage unterbrechen nicht die Zählung der nach Satz 1 maßgeblichen Tage. …\n" +
                "\n" +
                "    (3) - (9) …\n" +
                "\n" +
                "    (10) Diese Vorschrift gilt nur für die Dauer der Feststellung einer epidemischen Lage von nationaler Tragweite nach § 5 Absatz 1 Satz 1 durch den Deutschen Bundestag, längstens jedoch bis zum Ablauf des 30. Juni 2021. …\n" +
                "\n" +
                "    (11) …\n" +
                "\n" +
                "3\n" +
                "\n" +
                "    Zugleich ist in § 73 Abs. 1a IfSG als Nummer 11c eine Regelung eingefügt worden, die den Aufenthalt außerhalb einer Wohnung, einer Unterkunft oder des jeweils dazugehörigen befriedeten Besitztums entgegen § 28b Abs. 1 Satz 1 Nr. 2 erster Halbsatz IfSG als Ordnungswidrigkeit statuiert. Der Gesetzgeber hat in § 28c IfSG zudem eine Verordnungsermächtigung geschaffen, um die Anwendbarkeit dieser Maßnahmen auf Personen, bei denen von einer Immunisierung auszugehen ist, abweichend zu regeln.\n" +
                "\n" +
                "    II.\n" +
                "\n" +
                "4\n" +
                "\n" +
                "    1. Die Beschwerdeführenden im Verfahren 1 BvR 781/21 leben in Rheinland-Pfalz. Der Beschwerdeführer zu 1), der mit der Beschwerdeführerin zu 2) verheiratet ist, und der Beschwerdeführer zu 3) sind als Abgeordnete des Landtags gewählt. Sie leben im …kreis (Rheinland-Pfalz).\n" +
                "\n" +
                "5\n" +
                "\n" +
                "    2. Die Mehrzahl der Beschwerdeführenden im Verfahren 1 BvR 805/21 lebt in Berlin. Die Beschwerdeführerin zu 1) ist Mitglied des Deutschen Bundestags, vier weitere Beschwerdeführende sind Mitglieder des Abgeordnetenhauses von Berlin und gehören dort unterschiedlichen Fraktionen an. Sie weisen, ebenso wie die Beschwerdeführerin zu 1), auf die erheblichen Schwierigkeiten der Organisation ihres Alltags hin, die ihre Ursachen auch in mit dem Abgeordnetenmandat verbundenen Arbeitszeiten bis in die Abendstunden und die Nacht haben. Vor allem bei Alleinerziehenden könnten bislang praktizierte Modelle der Kinderbetreuung wegen der Ausgangsbeschränkung nicht mehr weitergeführt werden. Diese beschränke aber auch die Möglichkeit von Besuchen bei nahen Angehörigen, etwa den bereits vollständig geimpften Eltern. Zudem könne wegen der zeitlichen Belastungen durch die Abgeordnetentätigkeit der Kontakt zu pflegebedürftigen Angehörigen wie im Fall des Beschwerdeführers zu 4) erst in den Nachtstunden erfolgen. Es würden auch die ohnehin zeitlich begrenzten Möglichkeiten für sonstige soziale Kontakte durch die Ausgangsbeschränkung weiter vermindert.\n" +
                "\n" +
                "6\n" +
                "\n" +
                "    Die Beschwerdeführerin zu 6) und der Beschwerdeführer zu 10) sind ein Paar und leben in circa 30 Fahrminuten voneinander entfernten Orten in Baden-Württemberg. Die berufliche Tätigkeit beider bringt Arbeitszeiten bis gegen 20 oder 21 Uhr mit sich. Aufgrund der Ausgangsbeschränkung sind die zeitlichen Möglichkeiten, einander zu besuchen und etwa gemeinsame Spaziergänge, auch mit der Tochter der Beschwerdeführerin zu 6), zu unternehmen, eingeschränkt.\n" +
                "\n" +
                "7\n" +
                "\n" +
                "    Der im juristischen Vorbereitungsdienst befindliche Beschwerdeführer zu 3) lebt in Sachsen-Anhalt. Etwa die Hälfte seiner Freizeit verbringt er mit künstlerischem Fotografieren, wozu er auch von seinem Wohnort entfernte Orte mehrmals im Jahr spätabends oder nachts aufsucht.\n" +
                "\n" +
                "8\n" +
                "\n" +
                "    3. Der Beschwerdeführer im Verfahren 1 BvR 820/21 leidet unter psychischen Erkrankungen, die seine Interaktionsfähigkeit mit anderen Menschen stark einschränken. Er arbeitet seit März 2020 von seiner Wohnung aus und hat seitdem fast keinen Kontakt zu anderen Menschen mehr. Um mit der Isolation während der Pandemie zurecht zu kommen, geht er spazieren. Da er durch andere Menschen einem Bedrohungsgefühl ausgesetzt ist, kann er dies erst in den Abendstunden tun.\n" +
                "\n" +
                "9\n" +
                "\n" +
                "    4. Der Beschwerdeführer im Verfahren 1 BvR 854/21 ist als Rechtsanwalt in Nordrhein-Westfalen tätig. Er arbeitet häufig bis 22 Uhr und geht dann auch nach 24 Uhr noch spazieren. Einrichtungen, in denen er Zerstreuung finden könnte, sind geschlossen. Freunde zu treffen ist ihm nach 22 Uhr nicht mehr möglich. Deshalb hat er Sorge zu vereinsamen.\n" +
                "\n" +
                "10\n" +
                "\n" +
                "    5. Die Beschwerdeführer im Verfahren 1 BvR 889/21 leben beide in M. und sind dort als Taxifahrer tätig. Der Beschwerdeführer zu 1) arbeitet teilweise auch in Nachtschichten, die erst nach Mitternacht enden. Die Ausgangsbeschränkung mache soziale Kontakte für ihn unmöglich. Der Beschwerdeführer zu 2) ist verheiratet und Vater von zwei Kindern. Seine Eltern und seine Schwiegereltern wohnen in verschiedenen Orten außerhalb von M. Die Besuche bei ihnen müssten nun an die Ausgangsbeschränkung angepasst werden, was wegen seiner Arbeitszeiten als Taxifahrer nicht leichtfalle.\n" +
                "\n" +
                "    III.\n" +
                "\n" +
                "11\n" +
                "\n" +
                "    Die Beschwerdeführenden machen mit ihren Verfassungsbeschwerden im Wesentlichen geltend, dass durch die nach § 73 Abs. 1a Nr. 11c IfSG bußgeldbewehrte Regelung von Ausgangsbeschränkungen in § 28b Abs. 1 Satz 1 Nr. 2 IfSG erhebliche Eingriffe in ihre Grundrechte erfolgten, die verfassungsrechtlich nicht gerechtfertigt seien. Soweit die Ausgangsbeschränkung eine Freiheitsbeschränkung und damit einen Eingriff in die Freiheit der Person aus Art. 2 Abs. 2 Satz 2 GG enthalte, sei dieser Eingriff bereits deshalb unzulässig, weil eine solche Freiheitsbeschränkung nach Art. 2 Abs. 2 Satz 3 und Art. 104 Abs. 1 Satz 1 GG nur auf Grund eines Gesetzes, nicht aber durch ein Gesetz erfolgen dürfe. Hierdurch werde zudem der Rechtsschutz der Beschwerdeführenden in unzulässiger Weise verkürzt. Eine Überprüfung der Maßnahmen vor den Verwaltungsgerichten sei nicht möglich, zumal es auch keine Umsetzungsakte durch die Verwaltung gebe, die dann verwaltungsgerichtlicher Kontrolle unterzogen werden könnten.\n" +
                "\n" +
                "12\n" +
                "\n" +
                "    Die angegriffene gesetzliche Regelung genüge dem Grundsatz der Verhältnismäßigkeit nicht. Aus den vom Gesetzgeber zur Begründung des Gesetzes herangezogenen Studien könne nicht darauf geschlossen werden, dass nächtliche Ausgangsbeschränkungen geeignet seien, zu einer erheblichen Reduzierung von Kontakten zu führen und so den Zielen der gesetzlichen Regelung zu dienen, weil die Studien in wesentlichen Teilen nur auf Schätzungen beruhten, sich auf ausländische, nicht auf Deutschland übertragbare Verhältnisse bezögen oder mit der Mobilität Umstände bewerteten, die keine sicheren Rückschlüsse auf die Auswirkungen auf das Infektionsgeschehen zuließen. Die Sieben-Tage-Inzidenz sei jedenfalls für sich genommen kein hinreichender Indikator für das tatsächliche Infektionsgeschehen. Die Regelung verbiete auch den Aufenthalt im Freien alleine oder mit dem eigenen Hausstand, obwohl hiervon keine erkennbare Infektionsgefahr ausgehe.\n" +
                "\n" +
                "13\n" +
                "\n" +
                "    Soweit die Eignung zur Erreichung der Zwecke des Gesetzes noch zu bejahen sei, sei die Regelung jedenfalls nicht erforderlich. Es stünden mildere, die Grundrechte weniger einschränkende, aber gleich wirksame Mittel zur Verfügung. Um Engpässe im Gesundheitswesen zu verhindern, sei es ausreichend, diese durch landes- oder kommunalrechtliche Regelungen lediglich in den Regionen anzuordnen, in denen solche Engpässe konkret drohten. Ferner könne durch die Regelung von Kontaktbeschränkungen und Maßnahmen zur Kontaktreduzierung in der Arbeitswelt eine Verringerung der Kontakte erreicht werden, wodurch die Grundrechte der Betroffenen weniger schwer beeinträchtigt würden als durch Ausgangsbeschränkungen.\n" +
                "\n" +
                "14\n" +
                "\n" +
                "    Die Regelung sei auch unzumutbar. Es liege ein sehr schwerwiegender Grundrechtseingriff vor, dem allenfalls ein geringer Nutzen der Maßnahme gegenüberstehe. Die zur Wahrung der Verhältnismäßigkeit erforderliche Begrenzung der Maßnahme erfolge lediglich durch die Inzidenz, nicht aber durch eine zeitliche Begrenzung der Dauer der Ausgangsbeschränkung. Aufgrund der Schwere des Eingriffs in die Grundrechte komme die Ausgangsbeschränkung nur als ultima ratio in Betracht. Anders als in § 28a Abs. 2 Nr. 2 IfSG habe der Gesetzgeber diese Voraussetzung aber nicht in die angegriffene Regelung übernommen. Die Ausgangsbeschränkungen gälten auch dann, wenn nicht alle anderen möglichen Maßnahmen des Infektionsschutzes ausgeschöpft seien. Die Formulierung lasse auch nicht hinreichend erkennen, welches Verhalten im Einzelnen verboten und mit Bußgeld bewehrt sei. Dem Bestimmtheitsgebot aus Art. 103 Abs. 2 GG werde damit nicht entsprochen.\n" +
                "\n" +
                "15\n" +
                "\n" +
                "    Die Beschwerdeführenden halten den Erlass einer einstweiligen Anordnung zur Abwehr schwerer Nachteile für erforderlich. Sie tragen in den Verfahren 1 BvR 781/21, 1 BvR 805/21 und 1 BvR 889/21 vor, die Verfassungsbeschwerden seien offensichtlich begründet, so dass die einstweilige Anordnung schon deswegen erlassen werden müsse. Jedenfalls gebiete die vorzunehmende Folgenabwägung den Erlass der einstweiligen Anordnung. Erginge diese nicht, bestünden die schweren Grundrechtseingriffe und die damit verbundenen erheblichen Belastungen fort. Würde die einstweilige Anordnung erlassen und die angegriffene Regelung außer Kraft gesetzt, so hätte dies nach Ansicht der Beschwerdeführenden nur geringe nachteilige Auswirkungen. Der Zweck des Gesetzes würde nur in geringem Maße beeinträchtigt, weil die Ausgangsbeschränkungen ohnehin nur eine geringe Wirksamkeit hätten. Außerdem bestünden die von Ländern und Kommunen erlassenen Regelungen des Infektionsschutzes fort oder könnten von diesen erlassen werden.\n" +
                "\n" +
                "    IV.\n" +
                "\n" +
                "16\n" +
                "\n" +
                "    Der Senat hat nach § 32 Abs. 2 Satz 2 BVerfGG aufgrund der besonderen Dringlichkeit davon abgesehen, Gelegenheit zur Stellungnahme zu geben.\n" +
                "\n" +
                "    B.\n" +
                "\n" +
                "17\n" +
                "\n" +
                "    Die Anträge, § 28b Abs. 1 Satz 1 Nr. 2 und § 73 Abs. 1a Nr. 11c IfSG im Wege der einstweiligen Anordnung vorläufig außer Kraft zu setzen, bleiben ohne Erfolg. Die nach § 32 Abs. 1 BVerfGG dafür erforderlichen Voraussetzungen (I) liegen nicht vor (II).\n" +
                "\n" +
                "    I.\n" +
                "\n" +
                "18\n" +
                "\n" +
                "    Nach § 32 Abs. 1 BVerfGG kann das Bundesverfassungsgericht einen Zustand durch einstweilige Anordnung vorläufig regeln, wenn dies zur Abwehr schwerer Nachteile, zur Verhinderung drohender Gewalt oder aus einem anderen wichtigen Grund zum gemeinen Wohl dringend geboten ist.\n" +
                "\n" +
                "19\n" +
                "\n" +
                "    Bei der Entscheidung über die einstweilige Anordnung haben die Gründe, die für die Verfassungswidrigkeit der angegriffenen Maßnahmen vorgetragen werden, grundsätzlich außer Betracht zu bleiben, es sei denn, die in der Hauptsache begehrte Feststellung oder der in der Hauptsache gestellte Antrag erwiesen sich als von vornherein unzulässig oder offensichtlich unbegründet (vgl. BVerfGE 140, 99 <106 Rn. 11>; 143, 65 <87 Rn. 35>; stRspr). Bei offenem Ausgang des Hauptsacheverfahrens muss das Bundesverfassungsgericht im Rahmen einer Folgenabwägung die Nachteile abwägen, die einträten, wenn eine einstweilige Anordnung nicht erginge, der Antrag aber in der Hauptsache Erfolg hätte, gegenüber den Nachteilen, die entstünden, wenn die begehrte einstweilige Anordnung erlassen würde, dem Antrag in der Hauptsache aber der Erfolg zu versagen wäre (vgl. BVerfGE 140, 99 <106 Rn. 11>; 143, 65 <87 Rn. 35>; BVerfG, Beschluss des Zweiten Senats vom 15. April 2021 - 2 BvR 547/21 -, Rn. 73 jeweils m.w.N.; stRspr).\n" +
                "\n" +
                "20\n" +
                "\n" +
                "    Wegen der häufig weittragenden Folgen einer einstweiligen Anordnung ist regelmäßig ein strenger Maßstab anzulegen (vgl. BVerfGE 132, 195 <232 Rn. 86>; 143, 65 <87 Rn. 34>; BVerfG, Beschluss des Zweiten Senats vom 15. April 2021 - 2 BvR 547/21 -, Rn. 67; stRspr). Wird die Aussetzung des Vollzugs eines Gesetzes begehrt, gelten dafür besonders hohe Hürden (vgl. BVerfGE 140, 99 <106 f. Rn. 12>; stRspr). Denn das Bundesverfassungsgericht darf von seiner Befugnis, den Vollzug eines Gesetzes auszusetzen oder bereits das Inkrafttreten eines Gesetzes vorläufig zu unterbinden, nur mit größter Zurückhaltung Gebrauch machen, weil dies einen erheblichen Eingriff in die originäre Zuständigkeit des Gesetzgebers darstellt (vgl. BVerfGE 140, 99 <106 f. Rn. 12>; BVerfG, Beschluss des Zweiten Senats vom 15. April 2021 - 2 BvR 547/21 -, Rn. 67). Die Erheblichkeit dieses Eingriffs folgt aus dem Umstand, dass durch eine solche einstweilige Anordnung das angegriffene Gesetz allgemein und nicht nur in der Beziehung zu den Antragstellenden außer Vollzug gesetzt wird. Deshalb sind in die Folgenabwägung auch die Auswirkungen auf sämtliche von dem Gesetz Betroffenen einzubeziehen und nicht nur diejenigen für die Antragstellenden selbst (vgl. BVerfGE 122, 342 <362>; 140, 99 <107 Rn. 12>). Müssen die für eine vorläufige Regelung sprechenden Gründe schon im Regelfall so schwer wiegen, dass sie den Erlass einer einstweiligen Anordnung unabdingbar machen, so müssen sie, wenn beantragt ist, den Vollzug eines Gesetzes auszusetzen, darüber hinaus besonderes Gewicht haben (vgl. BVerfGE 122, 342 <361 f.>; 140, 99 <107 Rn. 12>; BVerfG, Beschluss des Zweiten Senats vom 15. April 2021 - 2 BvR 547/21 -, Rn. 67 m.w.N.; stRspr). Insoweit ist von entscheidender Bedeutung, ob die Nachteile irreversibel oder auch nur sehr erschwert revidierbar sind (vgl. BVerfGE 118, 111 <123>; 140, 211 <219 f. Rn. 13>; stRspr), um das Aussetzungsinteresse durchschlagen zu lassen. Stehen die jeweiligen Nachteile der abzuwägenden Folgenkonstellationen einander in etwa gleichgewichtig gegenüber, verbietet es die aus der Gewaltenteilung (Art. 20 Abs. 2 Satz 2 GG) notwendige Zurückhaltung des Bundesverfassungsgerichts, das angegriffene Gesetz auszusetzen, bevor geklärt ist, ob es mit dem Grundgesetz vereinbar ist (vgl. BVerfGE 108, 45 <51>; 140, 99 <106 f. Rn. 12>). Das Bundesverfassungsgericht setzt ein Gesetz also nur dann nach § 32 BVerfGG vorläufig außer Vollzug, wenn die Gründe für den Erlass der einstweiligen Anordnung überwiegen.\n" +
                "\n" +
                "    II.\n" +
                "\n" +
                "21\n" +
                "\n" +
                "    Gemessen an diesen strengen Anforderungen haben die zulässigen Anträge auf Erlass einer einstweiligen Anordnung keinen Erfolg. Die zugrunde liegenden Verfassungsbeschwerden sind zwar weder von vornherein unzulässig noch offensichtlich unbegründet (1). Ungeachtet der Frage, ob dies für sich genommen hier ausreichend wäre, sind sie allerdings auch nicht offensichtlich begründet (2). Die gebotene Folgenabwägung ergibt, dass die Nachteile, die einträten, wenn eine einstweilige Anordnung nicht erginge, der Antrag aber in der Hauptsache Erfolg hätte, nicht gegenüber den Nachteilen überwiegen, die entstünden, wenn die begehrte einstweilige Anordnung erlassen würde, dem Antrag in der Hauptsache aber der Erfolg zu versagen wäre (3).\n" +
                "\n" +
                "22\n" +
                "\n" +
                "    1. Die Verfassungsbeschwerden in den Hauptsacheverfahren sind weder von vornherein unzulässig, insbesondere wahren sie den Grundsatz der Subsidiarität (a), noch sind sie offensichtlich unbegründet (b).\n" +
                "\n" +
                "23\n" +
                "\n" +
                "    a) Die Beschwerden sind als Rechtssatzverfassungsbeschwerden (vgl. § 93 Abs. 3 BVerfGG) nicht von vornherein unzulässig. Den durch die angegriffenen Vorschriften selbst, gegenwärtig und unmittelbar betroffenen Beschwerdeführenden (aa) fehlt weder das allgemeine Rechtsschutzbedürfnis (bb) noch sind sie aus Gründen der Subsidiarität gehalten, vorab fachgerichtlichen Rechtsschutz (vgl. § 90 Abs. 2 Satz 2 BVerfGG) in Anspruch zu nehmen (cc).\n" +
                "\n" +
                "24\n" +
                "\n" +
                "    aa) Die Beschwerdeführenden sind durch die mit ihren Verfassungsbeschwerden angegriffene Regelung überwiegend selbst, gegenwärtig und unmittelbar betroffen (vgl. zu diesen Voraussetzungen BVerfGE 140, 42 <57 ff. Rn. 55 ff.>). Nach § 28b Abs. 1 Satz 1 Nr. 2 IfSG gilt die nächtliche Ausgangsbeschränkung bei Erreichen des Schwellenwertes an drei aufeinander folgenden Tagen in jedem betroffenen Landkreis und jeder betroffenen kreisfreien Stadt (vgl. auch § 28b Abs. 8 IfSG) unmittelbar ohne weiteren Vollzugsakt. Bei Vorliegen der Voraussetzungen erfasst die Regelung die Beschwerdeführenden an jedem Ort, den sie aufsuchen. Demnach sind die Beschwerdeführenden beinahe sämtlich dadurch gegenwärtig betroffen, dass sie entweder in Landkreisen oder kreisfreien Städten leben, in denen bereits zum Zeitpunkt der Erhebung ihrer Verfassungsbeschwerden die Maßnahme des § 28b Abs. 1 Satz 1 Nr. 2 IfSG galt, oder ‒ wie die Beschwerdeführenden zu V. ‒ vortragen, sich an solchen Orten aufzuhalten. Entsprechendes gilt hinsichtlich des Beschwerdeführers zu I. 3), der seine Verfassungsbeschwerde bereits am Tag der Verkündung des Gesetzes erhoben hat, da die Geltung der Maßnahme zu diesem Zeitpunkt gemäß § 77 Abs. 6 Satz 2 IfSG bereits klar abzusehen war (vgl. BVerfGE 140, 42 <58 Rn. 59> m.w.N.). Inwiefern auch die Beschwerdeführenden zu I. 1) und 2) angesichts des dynamischen Infektionsgeschehens schon zum maßgeblichen Zeitpunkt der Erhebung ihrer Verfassungsbeschwerde (vgl. BVerfGE 140, 42 <58 Rn. 58>) gegenwärtig betroffen waren, obwohl die Maßnahme des § 28b Abs. 1 Satz 1 Nr. 2 IfSG damals noch nicht galt und sie auch nicht vortragen, Orte aufzusuchen, an denen dies der Fall war, kann hier dahinstehen, da die Anträge aufgrund der gebotenen Folgenabwägung ohne Erfolg bleiben (vgl. BVerfGE 125, 385 <393>; 126, 158 <168>).\n" +
                "\n" +
                "25\n" +
                "\n" +
                "    bb) Das allgemeine Rechtsschutzbedürfnis fehlt auch nicht bei denjenigen Beschwerdeführenden, die in Bundesländern leben, in denen durch Landesverordnungsrecht ‒ durch § 28b Abs. 5 IfSG gestattet ‒ möglicherweise sogar strengere Ausgangsbeschränkungen als diejenigen nach § 28b Abs. 1 Satz 1 Nr. 2 IfSG gelten. Zwar würde die vorläufige Außervollzugsetzung der bundesrechtlichen Ausgangsbeschränkung nicht die auf Grundlage des Landesrechts weiterhin bestehenden Grundrechtseingriffe beseitigen. Jedoch führt das nicht zum Wegfall des Rechtsschutzbedürfnisses für Verfassungsbeschwerden gegen die bundesrechtliche Regelung. Der verfassungsgerichtliche Schutz drohte leerzulaufen, wenn Betroffenen in Verfahren gegen die Ausgangsbeschränkung nach § 28b Abs. 1 Satz 1 Nr. 2 IfSG das Fortbestehen einer landesrechtlichen Regelung entgegengehalten werden könnte, ihnen aber folgerichtig zugleich statthafter Rechtsschutz nach § 47 Abs. 1 Nr. 2 VwGO, gegebenenfalls in Verbindung mit § 47 Abs. 6 VwGO, mit der Erwägung versagt werden könnte, es mangele dafür wegen der fortbestehenden bundesrechtlichen Regelung der Ausgangsbeschränkung am Rechtsschutzbedürfnis. Dieses bleibt daher für die verschiedenen Rechtsbehelfe gegen die auf unterschiedlichen Rechtsgrundlagen beruhenden Ausgangsbeschränkungen jeweils erhalten (vgl. OVG Mecklenburg-Vorpommern, Beschluss vom 23. April 2021 - 1 KM 221/21 OVG -, juris, Rn. 29).\n" +
                "\n" +
                "26\n" +
                "\n" +
                "    cc) Die bereits erhobenen Verfassungsbeschwerden sind nicht deshalb von vornherein unzulässig, weil die Beschwerdeführenden keinen fachgerichtlichen Rechtsschutz in Anspruch genommen haben. Zwar ist die Möglichkeit einer negativen Feststellungsklage (vgl. § 43 Abs. 1 VwGO) nicht von vornherein ausgeschlossen. Wirft die Beurteilung einer Norm aber allein spezifisch verfassungsrechtliche Fragen auf, die das Bundesverfassungsgericht zu beantworten hat, ohne dass von einer vorausgegangenen fachgerichtlichen Prüfung verbesserte Entscheidungsgrundlagen zu erwarten wären, bedarf es einer vorangehenden fachgerichtlichen Entscheidung nicht (vgl. BVerfGE 143, 246 <322 Rn. 211>; 150, 309 <327 Rn. 44>; stRspr). So liegt es hier.\n" +
                "\n" +
                "27\n" +
                "\n" +
                "    b) Die mit den Eilanträgen zugleich erhobenen Verfassungsbeschwerden sind nicht offensichtlich unbegründet. Es ist offen, ob die angegriffenen Regelungen ‒ etwa hinsichtlich der formellen Anforderungen an das Gesetzgebungsverfahren betreffend die Mitwirkung des Bundesrats und der Verhältnismäßigkeit der Ausgangsbeschränkung ‒ mit der Verfassung vereinbar sind (vgl. zu verfassungsrechtlichen Bedenken unter anderem Wissenschaftliche Dienste des Deutschen Bundestags, WD 3 - 3000 - 083/21, S. 7 ff. m.w.N.; Guckelberger, NVwZ - Extra 9a/2020, S. 1 <11>; Kießling, NJW 2021, S. 178 <183>).\n" +
                "\n" +
                "28\n" +
                "\n" +
                "    2. Die danach grundsätzlich maßgebliche Folgenabwägung muss nicht deshalb von vornherein entfallen oder aber den Erlass der einstweiligen Anordnung geboten erscheinen lassen, weil sich die bereits erhobenen Verfassungsbeschwerden als offensichtlich begründet erwiesen.\n" +
                "\n" +
                "29\n" +
                "\n" +
                "    a) Zwar bleiben bei der hier allein zu treffenden Eilentscheidung außer in den Konstellationen von vornherein unzulässiger oder offensichtlich unbegründeter Verfassungsbeschwerden die für die Verfassungswidrigkeit des angegriffenen Hoheitsakts angeführten Gründe grundsätzlich außer Betracht (vgl. BVerfGE 143, 65 <87 Rn. 35> m.w.N.; stRspr). Jedoch ist nicht ausgeschlossen, dass ein Antrag auf Erlass einer einstweiligen Anordnung Erfolg hat, weil die dazugehörige Verfassungsbeschwerde offensichtlich begründet ist (vgl. BVerfGE 104, 23 <28>; 108, 34 <43>). Jedenfalls müssen erkennbare Erfolgsaussichten in bestimmten Konstellationen bei der Entscheidung über den Erlass einer einstweiligen Anordnung berücksichtigt werden, wenn ein Abwarten den Grundrechtsschutz mit hoher Wahrscheinlichkeit vereitelte (vgl. BVerfGE 111, 147 <153>).\n" +
                "\n" +
                "30\n" +
                "\n" +
                "    b) Ungeachtet dessen erweisen sich die angegriffenen Regelungen hier jedenfalls weder aus formellen (aa) noch aus materiellen Gründen (bb) als offensichtlich verfassungswidrig.\n" +
                "\n" +
                "31\n" +
                "\n" +
                "    aa) Eine offensichtliche formelle Verfassungswidrigkeit folgt nicht aus dem Umstand, dass der Bundesrat in seiner Sitzung vom 22. April 2021 dem Vierten Gesetz zum Schutz der Bevölkerung bei einer epidemischen Lage von nationaler Tragweite nicht zugestimmt, sondern lediglich den Beschluss gefasst hat, nicht nach Art. 77 Abs. 2 GG den Vermittlungsausschuss anzurufen (vgl. Stenografischer Bericht der 1003. Sitzung des Bundesrats vom 22. April 2021, S. 167). Das macht das Gesetz nicht offensichtlich verfassungswidrig. Die Notwendigkeit einer Zustimmung des Bundesrats für das Zustandekommen (Art. 78 GG) des genannten Gesetzes liegt jedenfalls nicht auf der Hand. Es bedarf näherer Klärung, ob vorliegend wegen der in § 28b Abs. 3 Satz 1 IfSG vorgesehenen Testungen von Schüler- und Lehrerschaft bei Durchführung von Präsenzunterricht die tatbestandlichen Voraussetzungen von Art. 104a Abs. 4 GG erfüllt sind. Die Beantwortung der damit verbundenen Fragen ist derzeit jedenfalls als offen einzustufen.\n" +
                "\n" +
                "32\n" +
                "\n" +
                "    Ebenso wenig liegt ein aus Art. 104a Abs. 4 GG folgendes Zustimmungserfordernis wegen der in § 56 Abs. 1a IfSG enthaltenen Entschädigungsregelungen etwa für die Fälle von Schulschließungen oder der Aufhebung der Präsenzpflicht (vgl. § 56 Abs. 1a Satz 1 Nr. 1 IfSG) auf der Hand. Die genannte Vorschrift hat ihre aktuelle Fassung bereits durch das Gesetz zur Fortgeltung der die epidemische Lage von nationaler Tragweite betreffenden Regelungen vom 29. März 2021 (BGBl I S. 370) erhalten und war nicht Bestandteil des § 28b IfSG einführenden Gesetzes. Ob die Einfügung von § 28b IfSG in das Infektionsschutzgesetz bestehenden zustimmungsbedürftigen Vorschriften eine wesentlich andere Bedeutung und Tragweite verleiht und deshalb selbst die Zustimmungsbedürftigkeit des Änderungsgesetzes auslöst, wirft ebenfalls Fragen auf, die näherer Prüfung bedürfen.\n" +
                "\n" +
                "33\n" +
                "\n" +
                "    bb) Die Ausgangsbeschränkung nach § 28b Abs. 1 Satz 1 Nr. 2 IfSG ist auch nicht offensichtlich materiell verfassungswidrig. Es liegt nicht eindeutig und unzweifelhaft auf der Hand, dass sie zur Bekämpfung der Pandemie unter Berücksichtigung des Einschätzungsspielraums des demokratischen Gesetzgebers offensichtlich nicht geeignet, nicht erforderlich oder unangemessen wäre (1). Das gilt auch im Hinblick auf die Anknüpfung an den Inzidenzwert von 100 (2).\n" +
                "\n" +
                "34\n" +
                "\n" +
                "    (1) (a) Ausweislich der Begründung des Gesetzentwurfs verfolgt der Gesetzgeber mit dem Vierten Gesetz zum Schutz der Bevölkerung bei einer epidemischen Lage von nationaler Tragweite in Erfüllung seiner verfassungsrechtlichen Schutzpflicht das Ziel, Leben und Gesundheit zu schützen sowie die Funktionsfähigkeit des Gesundheitssystems als überragend gewichtigem Gemeingut und damit zugleich die bestmögliche Krankheitsversorgung sicherzustellen (vgl. BTDrucks 19/28444, S. 1 und 8). Dazu bedarf es Maßnahmen, um eine exponentielle Verbreitung des Virus zu verhindern, vor allem auch diejenige von Virusvarianten, die die bisherigen Impferfolge in Frage stellen können (vgl. BTDrucks 19/28444, S. 8 und 10). Dieses Ziel soll durch effektive Maßnahmen zur Reduzierung von zwischenmenschlichen Kontakten erreicht werden (vgl. BTDrucks 19/28444, S. 8). Die hier angegriffene Ausgangsbeschränkung nach § 28b Abs. 1 Satz 1 Nr. 2 IfSG dient dabei nach den Vorstellungen des Gesetzgebers insbesondere der Kontrolle und Beförderung der Einhaltung der allgemeinen Kontaktregelungen (vgl. BTDrucks 19/28444, S. 12). Sie dient damit einem grundsätzlich legitimen Zweck.\n" +
                "\n" +
                "35\n" +
                "\n" +
                "    (b) Der Gesetzgeber betrachtet die Beschränkung des Aufenthalts im öffentlichen Raum als ein Mittel, um bisher in den Abendstunden stattfindende private Zusammenkünfte auch im privaten Raum zu begrenzen. Privaten Zusammenkünften komme ein erhebliches Infektionsrisiko zu. Gerade bei privaten Zusammenkünften würden die allgemeinen Regeln zur Vermeidung von Infektionen (Abstands- und Lüftungsregeln sowie das Tragen von Masken) weniger zuverlässig eingehalten als etwa bei beruflichen Kontakten am Tage (vgl. BTDrucks 19/28444, S. 12). Dass die nächtlichen Ausgangsbeschränkungen als Flankierung der Kontaktbeschränkungen dazu beitragen können, private Zusammenkünfte zu reduzieren, ist nicht offensichtlich unplausibel. Die Anreise zu und die Abreise von privaten Zusammenkünften erfolgt normalerweise über den öffentlichen Raum. Ist ein Aufenthalt dort untersagt, sind Anreisen zu nächtlichen privaten Zusammenkünften nicht möglich. Abreisen müssen frühzeitig erfolgen, so dass Zusammenkünfte eher enden. Dass private Zusammenkünfte, statt sie frühzeitig zu beenden, in derart großer Zahl bis in den nächsten Tag ausgedehnt und die Kontakte so erst recht intensiviert würden, dass der Gesetzeszweck konterkariert würde, ist nicht sehr wahrscheinlich. Jedenfalls ist der vom Gesetzgeber erwartete Effekt, dass die Ausdehnung privater Zusammenkünfte durch die Ausgangsbeschränkung reduziert wird, nicht offensichtlich unplausibel. Es kommt hinzu, dass sich die Einhaltung der flankierenden Ausgangsbeschränkung grundrechtsschonender kontrollieren lässt als die Beschränkung privater Zusammenkünfte in privaten Räumen an sich. Denn unmittelbar ließe sich die Kontaktbeschränkung in privaten Räumen nur kontrollieren, indem die Behörden in diese eindrängen.\n" +
                "\n" +
                "36\n" +
                "\n" +
                "    Ob die hier angegriffene nächtliche Ausgangsbeschränkung geeignet ist, um ihr Ziel zu erreichen, ist fachwissenschaftlich umstritten. Ihre fehlende Eignung ist nicht evident. Zum einen ist ohnehin grundsätzlich nicht in jedem Fall erforderlich, dass der Gesetzgeber seine Einschätzung auf wissenschaftliche Studien stützen kann oder im Gesetzgebungsverfahren darauf gestützt hat. Eine selbständige, von den Anforderungen an die materielle Verfassungsmäßigkeit des Gesetzes unabhängige Sachaufklärungspflicht folgt aus dem Grundgesetz nicht (BVerfGE 143, 246 <343 Rn. 273>). Das Grundgesetz schreibt grundsätzlich auch nicht vor, was, wie und wann genau im Gesetzgebungsverfahren zu begründen ist (vgl. BVerfGE 143, 246 <345 Rn. 279>; BVerfG, Beschluss des Ersten Senats vom 24. März 2021 - 1 BvR 2656/18 u.a. -, Rn. 241). Zum anderen ist zu berücksichtigen, dass der Gesetzgeber in der Beurteilung der Eignung einer Regelung über eine Einschätzungsprärogative verfügt, die sich sowohl auf die Einschätzung und Bewertung der tatsächlichen Verhältnisse erstreckt als auch auf die etwa erforderliche Prognose und die Wahl der Mittel, um seine Ziele zu erreichen (vgl. BVerfGE 152, 68 <130 f. Rn. 166> m.w.N.). Für die Eignung reicht bereits die Möglichkeit der Zweckerreichung aus (vgl. BVerfGE 126, 112 <144>; stRspr).\n" +
                "\n" +
                "37\n" +
                "\n" +
                "    Hier hat der Gesetzgeber nicht ins Blaue hinein geregelt, sondern sich auf wissenschaftliche Untersuchungen über die Wirkungen von nächtlichen Ausgangssperren in verschiedenen Staaten gestützt (siehe BTDrucks 19/28444, S. 12). Wie aussagekräftig diese im Einzelnen sind, ist hier nicht zu beurteilen. Jedenfalls liegen auf das Inland bezogene Untersuchungen vor, die nächtlichen Ausgangsperren eine senkende Wirkung auf die Ansteckungshäufigkeit ausweislich der Reproduktionszahl (\"R-Wert\") beimessen (vgl. Sachverständiger Nagel, Anhörung des Ausschusses für Gesundheit des Deutschen Bundestags, 19. Wahlperiode, Protokoll der 154. Sitzung vom 16. April 2021, S. 13; Nagel u.a., MODUS-COVID Bericht vom 19. März 2021, S. 4).\n" +
                "\n" +
                "38\n" +
                "\n" +
                "    (c) Für die Beurteilung der Erforderlichkeit einer gesetzlichen Regelung kommt dem Gesetzgeber ebenfalls ein Spielraum zu (vgl. BVerfGE 149, 86 <120 Rn. 94> m.w.N.). Unter Berücksichtigung dessen fehlt es der durch § 28b Abs. 1 Satz 1 Nr. 2 IfSG angeordneten Ausgangsbeschränkung auch nicht offensichtlich an der Erforderlichkeit. Andere Mittel, die eine effektive Kontrolle vorhandener Kontaktbeschränkungen und darüber eine Reduktion der Ansteckungsrate ebenso wirksam gewährleisteten, aber weniger intensiv in Grundrechte eingriffen, liegen nicht derart auf der Hand, dass bereits im einstweiligen Anordnungsverfahren von offensichtlich fehlender Erforderlichkeit auszugehen wäre. So dürfte etwa die Kontrolle von Beschränkungen privater Kontakte unmittelbar im privaten Raum kaum weniger eingriffsintensiv sein als eine nächtliche Ausgangsbeschränkung.\n" +
                "\n" +
                "39\n" +
                "\n" +
                "    (d) Eine offensichtliche Unangemessenheit solcher Ausgangsbeschränkungen als solcher kann ebenfalls nicht erkannt werden. Den in der Rechtsprechung einiger Oberverwaltungsgerichte angelegten Maßstäben für verhältnismäßige Ausgangsbeschränkungen auf landesrechtlicher Grundlage (vgl. Bayerischer VGH, Beschluss vom 12. Januar 2021 - 20 NE 20.2933 -, juris, Rn. 42; Niedersächsisches OVG, Beschluss vom 6. April 2021 - 13 ME 166/21 -, juris, Rn. 28 m.w.N.) kommt hier schon wegen der in § 28b Abs. 1 Satz 1 Nr. 2 IfSG einerseits und § 28a Abs. 2 Satz 1 Nr. 2 IfSG andererseits unterschiedlichen Voraussetzungen von Ausgangsbeschränkungen keine unmittelbare Bedeutung zu. In den Hauptsacheverfahren über die Verfassungsbeschwerden wird die Verhältnismäßigkeit der hier angegriffenen gesetzlichen Regelung über die Ausgangsbeschränkung eingehender Prüfung bedürfen.\n" +
                "\n" +
                "40\n" +
                "\n" +
                "    (2) Die Ausgangsbeschränkung in § 28b Abs. 1 Satz 1 Nr. 2 IfSG ist auch nicht deshalb offensichtlich ungeeignet, weil ihre Geltung an eine auf Landkreise und kreisfreie Städte bezogene Sieben-Tage-Inzidenz gebunden ist. Der Gesetzgeber sieht die Sieben-Tage-Inzidenz ohne klar ersichtliches Überschreiten seiner Einschätzungsprärogative als geeigneten Indikator für das Infektionsgeschehen an. Aus einer zunehmenden Zahl von Neuinfektionen, die die Inzidenz abbildet, könne geschlossen werden, dass mit dem auf den spezifischen Umständen der vorliegenden Pandemie beruhenden erheblichen zeitlichen Abstand die Belastung des Gesundheitssystems und die Zahl der Todesfälle steigen würden (vgl. BTDrucks 19/28444, S. 9). Diese Annahme ist ebenso wenig von vornherein unplausibel (zum Kriterium vgl. BVerfGE 152, 28 <128 Rn. 159>) wie die Einschätzung, dass die Sieben-Tage-Inzidenz als wochentagsbedingte Schwankungen ausmittelnder Wert einen tagesaktuell vorhandenen und einfach nachvollziehbaren Indikator darstellt (vgl. BTDrucks 19/28444, S. 9).\n" +
                "\n" +
                "41\n" +
                "\n" +
                "    Das Abstellen auf den Schwellenwert von 100 führt ebenfalls nicht zu einer offensichtlichen Ungeeignetheit der angegriffenen nächtlichen Ausgangsbeschränkung als Mittel, private Zusammenkünfte im privaten Raum in den Abend- und Nachtstunden zu begrenzen. Der Gesetzgeber geht davon aus, dass bei einer solchen Inzidenz eine Überlastung des Gesundheitswesens droht, die sich auch in der Verschiebung ansonsten planbarer Behandlungen bei anderen Erkrankungen ausdrückt (vgl. BTDrucks 19/28444, S. 9). Wegen der entsprechenden Erfahrungen in früheren Phasen der Pandemie hat das eine nachvollziehbare Grundlage. Das gilt auch für die weitere Annahme, dass ab dem Schwellenwert von 100 die Eindämmung des Infektionsgeschehens durch Kontaktnachverfolgung endgültig nicht mehr möglich ist.\n" +
                "\n" +
                "42\n" +
                "\n" +
                "    3. Über die Anträge auf Erlass einer einstweiligen Anordnung ist demnach nach Maßgabe einer Folgenabwägung zu entscheiden. Diese ergibt nach den strengen Anforderungen an das vorläufige Außervollzugsetzen eines Gesetzes, dass die Nachteile, die zu erwarten wären, wenn die einstweilige Anordnung nicht erginge, der Antrag aber in der Hauptsache Erfolg hätte, nicht gegenüber jenen Nachteilen überwiegen, die einträten, wenn die beantragte einstweilige Anordnung erlassen würde, dem Antrag in der Hauptsache aber der Erfolg zu versagen wäre.\n" +
                "\n" +
                "43\n" +
                "\n" +
                "    a) Erginge die einstweilige Anordnung nicht, erwiesen sich aber die Verfassungsbeschwerden später als begründet, sind die Nachteile aus der Fortgeltung der Ausgangsbeschränkung aus § 28b Abs. 1 Satz 1 Nr. 2 IfSG von erheblichem Gewicht. Dieses wird durch die Bußgeldbewehrung in § 73 Abs. 1a Nr. 11c IfSG noch verstärkt.\n" +
                "\n" +
                "44\n" +
                "\n" +
                "    aa) Die nächtliche Ausgangsbeschränkung greift tief in die Lebensverhältnisse ein. Ihre Wirkungen schränken nicht allein die Möglichkeiten ein, sich nach den eigenen Vorstellungen grundsätzlich jederzeit außerhalb einer Wohnung oder Unterkunft und des dazugehörigen befriedeten Besitztums aufzuhalten und im öffentlichen Raum unterschiedlichsten Aktivitäten nachzugehen. Vielmehr bewirkt sie erhebliche Veränderungen im Alltag zahlreicher Betroffener, die an ihrer bisherigen Lebensgestaltung während der Geltungsdauer der Ausgangsbeschränkung nicht mehr unverändert festhalten können. Das betrifft, wie sich unter anderem an den Darlegungen der Beschwerdeführenden zeigt, die gesamte Breite von Lebensentwürfen. Die Folgen der Ausgangsbeschränkung wirken sich auf nahezu sämtliche Bereiche privater, familiärer und sozialer Kontakte ebenso wie auf die zeitliche Gestaltung der Arbeitszeiten aus. Wollen Betroffene unter den Bedingungen einer nächtlichen Ausgangsbeschränkung in dem bisherigen Umfang neben den aus Amt oder Beruf resultierenden zeitlichen Bindungen ihre sozialen, insbesondere familiären Kontakte aufrechterhalten, geht dies mit nicht unerheblichen Belastungen einher. Bei etwa wegen Alter oder Erkrankung ohnehin bereits verletzlichen Betroffenen kann die Ausgangsbeschränkung vorhandene Beeinträchtigungen mit nicht unerheblichen Auswirkungen auf die psychische und physische Gesundheit weiter verstärken, weil vorhandene Kontakte auch wegen der Ausgangsbeschränkung nicht mehr in dem bisherigen Umfang möglich sind. Eine besondere verfassungsrechtliche Herausforderung kann die angegriffene Ausgangsbeschränkung auch für Personen bedeuten, bei denen von einer Immunisierung gegen das Coronavirus SARS-CoV-2 auszugehen ist (§ 28c Satz 1 IfSG), wenn es so ist, dass sie für das Infektionsgeschehen nicht maßgeblich sind.\n" +
                "\n" +
                "45\n" +
                "\n" +
                "    Solchen Konsequenzen der nach der derzeitigen Rechtslage bis längstens 30. Juni 2021 (§ 28b Abs. 10 IfSG) geltenden bundesrechtlichen Ausgangsbeschränkung wirkt das Gesetz allerdings durch einen Teil der Ausnahmeregelungen in § 28b Abs. 1 Satz 1 Nr. 2 IfSG entgegen, was die Folgen der Fortgeltung der Ausgangsbeschränkung abmildert. So belässt die Ausnahme in Satz 1 Nr. 2 Buchstabe b) der genannten Vorschrift Möglichkeiten der zeitlichen Gestaltung der Berufstätigkeit auch während des der Ausgangsbeschränkung unterfallenden Zeitraums. In Verbindung mit den Ausnahmen für die Wahrnehmung des Sorge- und Umgangsrechts und die Betreuung Unterstützungsbedürftiger nach Buchstaben c) und d) bleiben Optionen erhalten, die auch unter den Bedingungen der Pandemie eine gewisse individuell bestimmte Gestaltung etwa der Vereinbarkeit von beruflicher Tätigkeit sowie der Betreuung von aus unterschiedlichen Gründen unterstützungsbedürftigen Personen ermöglichen. Weiteren Belastungen wird durch die Anwendung der Ausnahmeregelung in § 28b Abs. 1 Satz 1 Nr. 2 Buchstabe f) IfSG unter Berücksichtigung vor allem des Schutzes von Ehe und Familie (Art. 6 Abs. 1 GG) sowie der Rechte von Menschen mit Behinderung (Art. 3 Abs. 3 Satz 2 GG) begegnet werden können.\n" +
                "\n" +
                "46\n" +
                "\n" +
                "    bb) Die Einschränkungen privater Lebensgestaltung durch die Ausgangsbeschränkung außerhalb der Ausnahmetatbestände reichen dennoch weit. Sie beziehen selbst das Verlassen der eigenen Wohnung oder der eigenen Unterkunft zur Wahrnehmung nach § 28b Abs. 1 Satz 1 Nr. 1 IfSG gestatteter familiärer Kontakte ein, soweit die Familienangehörigen nicht ohnehin in einem Haushalt leben oder die Voraussetzungen von § 28b Abs. 1 Satz 1 Nr. 2 Buchstaben c) oder d) IfSG vorliegen.\n" +
                "\n" +
                "47\n" +
                "\n" +
                "    Die mit der Ausgangsbeschränkung unmittelbar oder mittelbar verbundenen Beschränkungen der Ausübung unterschiedlicher Freiheiten können von den Betroffenen nicht außerhalb des von der Beschränkung erfassten Zeitraums oder nach dem Ende der Geltungsdauer der angegriffenen Regelung kompensiert werden. Die Möglichkeit der Wahrnehmung von Freiheiten während der Geltung der Ausgangsbeschränkung ist insofern unwiederbringlich verloren. Das erweist sich als erhebliche Belastung, die bei Ausbleiben einer einstweiligen Anordnung entweder bis zu einer Feststellung der Verfassungswidrigkeit in den Hauptsacheverfahren oder bis zum Ende der derzeitigen Geltungsdauer der Regelung (§ 28b Abs. 10 IfSG) anhält.\n" +
                "\n" +
                "48\n" +
                "\n" +
                "    cc) Allerdings ist auch der von der Ausgangsbeschränkung erfasste Zeitraum bei der Beurteilung der von ihr ausgehenden Belastungen in den Blick zu nehmen. Derzeit lässt sich davon ausgehen, dass die Mobilitätsrate unter Einschluss beruflich veranlassten Aufenthalts außerhalb der eigenen Wohnung im von der Regelung erfassten Zeitraum bei etwas mehr als 7% und jedenfalls unter 10% liegt (vgl. Report vom 31. März 2021 des COVID-19 Mobility Project, eines Forschungsprojekts von Wissenschaftlerinnen und Wissenschaftlern der Projektgruppe \"Epidemiologische Modellierung von Infektionskrankheiten\" am Robert Koch-Institut und der Forschungsgruppe \"Komplexe Systeme (ROCS)\" des Instituts für Theoretische Biologie und des Integrativen Forschungsinstitut für die Biowissenschaften (IRI Life Sciences) der Humboldt-Universität zu Berlin, abgerufen unter https://www.covid-19-mobility.org/reports/mobility-curfew/ am 5. Mai 2021). Die Ausgangsbeschränkung fällt damit in einen Zeitraum, in dem nach den bisherigen Verhaltensmustern Aktivitäten außerhalb einer Wohnung oder Unterkunft keine ganz erhebliche quantitative Bedeutung haben. Sie betrifft den Zeitraum von 22 Uhr bis 5 Uhr und lässt körperliche Bewegung im öffentlichen Raum noch bis 24 Uhr zu. Der Gesetzgeber hat die Beschränkung auf die regelmäßigen Ruhens- und Schlafenszeiten begrenzt (vgl. BTDrucks 19/28444, S. 12).\n" +
                "\n" +
                "49\n" +
                "\n" +
                "    Weiterhin ist bei den Folgen einer Fortgeltung der Ausgangsbeschränkung zu bedenken, dass deren Geltung an den Schwellenwert der Sieben-Tage-Inzidenz von 100 gekoppelt ist. Greifen die Maßnahmen zum Schutz vor der Ansteckung mit dem Virus und liegen die Voraussetzungen nach § 28b Abs. 2 Satz 1 IfSG vor, treten die Ausgangsbeschränkung ebenso wie die weiteren Schutzmaßnahmen aus § 28b Abs. 1 IfSG außer Kraft. Nach der für die Entscheidung über die Anträge auf Erlass einstweiliger Anordnungen maßgeblichen derzeitigen Rechtslage ist zudem die Geltungsdauer bis längstens zum 30. Juni 2021 begrenzt (§ 28b Abs. 10 IfSG). Ungeachtet der fehlenden Nachholbarkeit von während der Ausgangsbeschränkung nicht wahrnehmbaren Freiheiten (Rn. 47) mildern beide angesprochenen Umstände die von der hier fraglichen Ausgangsbeschränkung ausgehenden Belastungen.\n" +
                "\n" +
                "50\n" +
                "\n" +
                "    dd) Der Ordnungswidrigkeitentatbestand in § 73 Abs. 1a Nr. 11c IfSG stellt zwar eine zusätzliche Belastung dar, die fortbesteht, wenn die einstweilige Anordnung nicht ergeht, sich die Ausgangsbeschränkung und die darauf bezogene Ordnungswidrigkeit aber später als verfassungswidrig erwiesen. Das eigenständige Gewicht dieser Belastung könnte allerdings durch die Wiederaufnahmemöglichkeit nach § 79 BVerfGG gemildert werden, die zumindest nach einer im Einspruchsverfahren (§§ 67 ff. OWiG) erfolgten strafgerichtlichen Verurteilung (vgl. § 68 Abs. 1, § 71 OWiG) eröffnet sein könnte.\n" +
                "\n" +
                "51\n" +
                "\n" +
                "    b) Würde § 28b Abs. 1 Satz 1 Nr. 2 IfSG durch einstweilige Anordnung vorläufig außer Vollzug gesetzt, erwiese sich die Regelung aber später als verfassungsgemäß, entfiele die Ausgangsbeschränkung als bundeseinheitlich wirkende Maßnahme der Infektionsbekämpfung, was ebenfalls Nachteile von erheblichem Gewicht verursachen könnte.\n" +
                "\n" +
                "52\n" +
                "\n" +
                "    Damit stünde ein für die gesetzgeberische Gesamtkonzeption der Maßnahmen zur Infektionsbekämpfung nach § 28a und § 28b IfSG bedeutsames Instrument nicht mehr zur Verfügung. Die Ausgangsbeschränkung nach § 28b Abs. 1 Satz 1 Nr. 2 IfSG dient nach den Vorstellungen des Gesetzgebers der Kontrolle der vorhandenen allgemeinen Kontaktregelungen und soll die Bereitschaft zu deren Einhaltung fördern (Rn. 34). Von der nicht von vornherein unplausiblen Annahme ausgehend, dass gerade bei privaten Zusammenkünften in den von der Beschränkung erfassten Abend- und Nachtstunden die Einhaltung zur Eindämmung des Infektionsgeschehens unverzichtbarer Kontaktregeln weniger gesichert ist als zu den übrigen Tageszeiten, fehlte für die Dauer einer Außervollzugsetzung der Regelung ein im gesamten Bundesgebiet geltendes Kontrollinstrument. Dem kommt angesichts der nach wie vor absolut und relativ hohen Zahl von nachgewiesenen Neuinfektionen, der derzeit als gefährlich bewerteten Virusvarianten, den schweren Krankheitsverläufen und den Todesfällen erhebliche Bedeutung zu. Auch die Wirksamkeit bereits erfolgter Impfungen stünde in Frage.\n" +
                "\n" +
                "53\n" +
                "\n" +
                "    An der Beurteilung ändert auch der Umstand nichts, dass auf der Grundlage von § 28a Abs. 1 und 2 IfSG durch landesrechtliche Regelungen auch bei Außervollzugsetzung von § 28b Abs. 1 Satz 1 Nr. 2 IfSG weiterhin Ausgangsbeschränkungen angeordnet werden können. Wenn nämlich entsprechende Landesregelungen existieren, hilft es den Antragstellern ohnehin nicht, wenn der Vollzug der Bundesregelung ausgesetzt wird. Soweit hingegen keine Landesregelungen existieren, ist der Vollzug der Bundesregelung aber erforderlich, um die damit verfolgten Zwecke zu erreichen.\n" +
                "\n" +
                "54\n" +
                "\n" +
                "    Wirksame Maßnahmen zur Eindämmung der Pandemie erscheinen auch deshalb notwendig, weil die Auswirkungen hoher Infektionszahlen auf die Erfolge der derzeit stattfindenden Impfungen zu berücksichtigen sind. Nach den insoweit ebenfalls nachvollziehbaren Annahmen des Gesetzgebers kann eine zu große Zahl von Infizierten bei Kontakten mit noch nicht vollständig geimpften Personen die Entstehung von Virusvarianten mit verursachen, gegen die die vorhandenen und bereits verabreichten Impfstoffe weniger gut wirken (vgl. BTDrucks 19/28444, S. 10). Dem Wegfall von einheitlich geltenden und wirkenden Ausgangsbeschränkungen als Mittel zur Sicherung bestehender Kontaktbeschränkungen kommt auch insoweit erhebliche Bedeutung zu.\n" +
                "\n" +
                "55\n" +
                "\n" +
                "    c) Im einstweiligen Anordnungsverfahren ist dem Bundesverfassungsgericht lediglich eine summarische Prüfung der tatsächlichen Grundlagen möglich (vgl. BVerfGE 131, 47 <64>). Danach sind die Nachteile, die bei einer Außervollzugsetzung der angegriffenen Ausgangsbeschränkung einträten, die Regelung aber später als verfassungsgemäß erkannt würde, von erheblichem Gewicht. Trotz der ebenfalls nicht unerheblichen Belastungen für sämtliche von der Ausgangsbeschränkung Betroffenen überwiegen die damit verbundenen Nachteile nicht gegenüber denen einer Außervollzugsetzung. Zwar kann die während der Ausgangsbeschränkung nicht ausübbare Freiheitsbetätigung nicht nachgeholt werden und es wird auch verstärkten physischen und psychischen Belastungen der Infektionsschutzmaßnahmen nur mit erheblichem Aufwand entgegengewirkt werden können. Stünde aber bis zu einer Entscheidung in der Hauptsache die bundeseinheitliche Ausgangsbeschränkung als Instrument zur Sicherung und Kontrolle der aktuell dringend gebotenen Kontaktbeschränkungen nicht zur Verfügung, gingen damit erhebliche, wenn auch im Einzelnen nicht sicher prognostizierbare Infektionsrisiken einher. Zumindest auf der Grundlage der in diesem Verfahren zur Verfügung stehenden derzeitigen Tatsachengrundlage können bei insgesamt unzureichend wirkenden Maßnahmen zur Senkung der Anzahl der Infektionen die von der Impfung zu erwartenden Erfolge in Gefahr geraten (Rn. 54). Das könnte zur Erfüllung der staatlichen Schutzpflicht für Leben und Gesundheit der Menschen weitere Maßnahmen zur Eindämmung des Infektionsgeschehens notwendig werden lassen, die ihrerseits mit erneut weitgehenden Grundrechtsbeschränkungen verbunden wären.\n" +
                "\n" +
                "56\n" +
                "\n" +
                "    Da der Gesetzgeber die Wirkungen der mit der Ausgangsbeschränkung verbundenen Freiheitsbeeinträchtigungen zudem über Ausnahmetatbestände abgemildert hat und die Geltungsdauer der angegriffenen Regelung nach derzeitiger Rechtslage zeitlich relativ eng begrenzt ist, überwiegen die Nachteile für die Betroffenen ungeachtet der erheblichen Eingriffsintensität der Ausgangsbeschränkung nicht gegenüber den Nachteilen für einen wirksamen Infektionsschutz bei Aussetzen der Regelung in § 28b Abs. 1 Satz 1 Nr. 2 IfSG. Damit ist die einstweilige Anordnung nicht zu erlassen. Über die Frage, ob es einer einstweiligen Anordnung nach § 32 BVerfGG insoweit bedarf, als bei Personen von einer Immunisierung auszugehen ist, ist mit diesem Verfahren noch nicht entschieden. Hierfür bedürfte es weiterer Aufklärung.\n" +
                "\n");
        return result.toJSONString();
    }


}
