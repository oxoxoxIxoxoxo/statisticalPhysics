# Aufgaben in diesem Praktikum

## Messfehler

## Zufall

# Informationen, die einzuholen sind

* Wahrscheinlichkeitsrechung

* Die wichtigsten Verteilungstypen

* Messfehler

* Statistische Tests

* Zufall

* Libre Office

# Literatur

* Demtröder 1

* Physik im Experiment

* Skriptum "Fehlerrechnung

# Protokoll

* Verwendete Tabellen und Plots sind auszudrucken

# Theorie zum Praktikum

* Stochastische Prozesse in der Physik

* Beispiel: Quantenmechanik

* Behandlung von Messfehlern

* Gewisse Verteilungstypen

* Die Frage nach der Zufälligkeit eines Ereignisses

* Monte-Carlo Methode

* Pollard-$\rho$-Methode

* Glücksspiel-Branche

# Stochastik

* Ziel:

-> Ein mathematisches Modell zu finden, mit dem bestimmte Aussagen über den Ausgang des Experimentes getroffen werden können.

-> Alle möglichen Ausgänge des Experiments bilden die Grundmenge $\Omega$. Dabei gibt es diskrete (abzählbar unendlich) und kontinuierliche (überabzählbar unendlich) Ausgänge.

## Wahrscheinlichkeitsmodelle

* Zuordnung der Wahrscheinlichkeiten zu den einzelnen Elementen: Wahrscheinlichkeitsfunktion $P:\Omega \Rightarrow [0,1]$

* Forderung an die Wahrscheinlichkeitsfunktion: $\sum_{\omega\in\Omega}P(\omega) = 1

* Der Begriff der Wahrscheinlichkeit kann als empirisches Gesetz der großen Zahlen gedeutet werden, in dem sich ein bestimmter "Häufungswert" ermitteln lässt.

* Gegeben sei ein beliebig oft unter gleichen Bedingungen wiederholbares Experiment und $A\in\Omega$ ist ein Ausgang dieses Experiments. Weiters sei $H_{n}(A)$ die Anzahl der Ergebnisse von A bei n Durchführungen als absolute Häufigkeit und $h_{n}(A):=\frac{H_{n}(A)}{n}$ als relative Häufigkeit des Auftretens von A bei n Durchführungen gegeben. Dann zeigt die Folge der $h_{n}(A)$ ein "konvergentartiges" Verhalten.

* Man spricht von einem LaPlace-Modell, wenn aufgrund von Symmetrien alle Ausgänge die gleiche Chance haben. Eines von n möglichen Ausgängen ist dann $\frac{1}{n}$ für alle dieser Ausgänge.

* Von einem La Place Hilfsmodell spricht man, wenn sich die Wahrscheinlichkeiten kombinatorische ableiten lassen.

* Das Auftreten von mehreren Ereignissen ist bestimmt durch die Erweiterung der Wahrscheinlichkeitsfunktion mit: $P(E):=\sum_{\omega\in E}P(\omega)$. Somit erhält man eine neue Wahrscheinlichkeitsfunktion: $P:\cal{P}(\omega)\rightarrow [0,1]$, wobei $\cal{P}(\omega)$ die Potenzmenge, also die Menge aller Teilmengen von $\Omega$ bedeutet.

Außerdem gilt folgendes:
$$
P(\varnothing) = 0\quad P(\Omega) = 1
$$

$$
P(A\cup B) = P(A)+P(B) \quad\text{wenn}\quad A\cap B = \varnothing
$$

$$
A\subset B \Rightarrow P(A)\leq P(B)
$$

* Für Laplace-Modelle gilt folgendes:

$$
P(E) = \frac{|E|}{|\Omega|}
$$

was der klassischen Definition von "Anzahl der günstigen Ereignisse durch Anzahl der möglichen Ereignisse" entspricht.

* Bedingte Wahrscheinlichkeit:

Für das Eintreten eines Ereignisses A wird das Eintreten eines Ereignisses B als Voraussetzung angenommen. Es sind dann nur noch jene Ausgänge günstig, die sowohl in A als auch in B enthalten sind.

Ist B die Bedingung des Ereignisses A, so gilt für die bedingte Wahrscheinlichkeit $P(A|B)$, in Worten "P von A unter der Bedingung B":

$$
P(A|B) = \frac{P(A\cap B)}{P(B)}
$$

* Multiplikationstheorem:
Seien A und B, $A,B\subset\Omega$, zwei nicht notwendig unabhängige Ereignisse, so gilt:

$$
P(A\cap B)=P(A)\cdot P(B|A)=P(B)\cdot P(A|B)
$$

* Definition: 
Zwei Ereignisse A und B heißen voneinander unabhängig, wenn $P(A|B) = P(A)$ gilt.

* Satz von Bayes:
Bilden $H_{1}, H_{2}, ..., H_{n}$ gemeinsam die ganze Grundmenge $\Omega$, ohne zu überlappen und ist $A\subset\Omega$ ein beliebiges Ereignis, so gilt:

$$
P(H_{i}|A)=\frac{P(H_{i})P(A|H_{i})}{\sum_{j=1}^{n}P(H_{i})P(A|H_{i})}
$$

Man kann $P(H_{i})$ auch als Wahrscheinlichkeit vor und $P(H_{i}|A)$ als Wahrscheinlichkeit nach einer Beobachtung verstehen und spricht daher auch von a-priori und a-posteriori Wahrscheinlichkeiten.

## Zufallsgrößen

* Ist $\Omega$ der Grundraum eines Wahrscheinlichkeitsmodells, dann heißt jede Funktion $X:\Omega\rightarrow \mathbb{R}$ eine Zufallsgröße.

## Erwartungswert und Varianz

* Definition: Ist X eine Zufallsgröße des Wahrscheinlichkeitsmodelles mit Grundraum $M_{X}$ und Wahrscheinlichkeitsverteilung $P$, so heißt

$$
\mu = \langle X\rangle = \sum_{x\in M_{X}}xP(x)
$$
der Erwartungswert von X.

* Definition: Ist X eine Zufallsgröße des Wahrscheinlichkeitsmodelles mit Grundraum $M_{X}$ und Wahrscheinlichkeitsverteilung P, so heißt

$$
\sigma_{X}^2 = VX=\sum_{x\in M_{X}}P(x)(x-\mu)^2
$$
die Varianz von X.

* Verschiebungssatz

$$
VX = \langle X^2\rangle-\langle X\rangle^2
$$

* Berechnung des Erwartungswertes:

Ist $f:\mathbb{R}\rightarrow\mathbb{R}$ und $X$ eine Zufallsgröße des Wahrscheinlichkeitsmodelles mit Grundraum $M_{X}$ und Wahrscheinlichkeitsverteilung P, dann ist

$$
\langle f(X)\rangle = \sum_{x\in M_{X}}f(x)P(x)
$$

## Diskrete Verteilungen

### Diskrete Gleichverteilung

* Definition: X heißt diskret gleichverteilt, in Zeichen $X ~D_{m}$, wenn

$$
M_{X} = \{1,...,m \}\quad \tect{und}\quad P(x)=\frac{1}{m}\quad\forall x\in M_{X}
$$
Dann gilt:

$$
\langle X\rangle = \frac{m+1}{2},\quad VX=\frac{m^2-1}{12}
$$
Anwendungen: Würfel, Zufallszahlen, Roulette, usw

### Alternativverteilung

* Definition: X heißt alternativverteilt, i.Z. XÃ_{\vartheta}, wenn

$$
M_{X}=\{0,1 \}\quad\text{und}\quad P(1)=\vartheta,\quad P(0)=1-\vartheta
$$
Dann gilt:

$$
\langle X\rangle = \vartheta,\quad VX=\vartheta(1-\vartheta)
$$
Anwendungen, Münzwurf, Gut-Schlecht-Prüfungen, usw.

### Binomialverteilung

* Definition: X heißt binomialverteilt, i.Z. $X~B_{n,\vartheta}$, wenn

$$
M_{X}=\{0,1,...,n \}\quad\text{und}\quad P(x)=\binom{n}{x}\vartheta^x(1-\vartheta)^{n-x}
$$
Dann gilt:

$$
\langle X\rangle n\vartheta,\quad VX=n\vartheta(1-\vartheta)
$$
Anwendungen: Die Binomialverteilung kann als die Verteilung des Ziehens mit Zurücklegen angesehen werden, wobei aus einer Gesamtheit gezogen wird die sich im Verhältnis $\vartheta:1-\vartheta$ aus zwei Teilen zusammensetzt; z.B.: Anzahl von gewürfelten Sechsen, Auftreten einzelner Lottozahlen.

### Hypergeometrische Verteilung

* Definition: X heißt hypergeometrisch verteilt, i.Z. $X~H_{N,A,n}$, wenn

$$
M_{X}=\{k_{0},k_{0}+1,...,k_{1} \}\quad\text{und}\quad P(x)=\frac{\binom{A}{x}\binom{N-A}{n-x}}{\binom{N}{n}}
$$
wobei $k_{0}=max\{0,n-N+A\}$ und $k_{1} = min\{n,A \}$. Dann gilt

$$
\langle X\rangle = n\frac{A}{N},\quad VX=n\frac{A}{N}\big(1-\frac{A}{N} \big)\frac{N-n}{N-1}
$$

### Poissonverteilung

* Definition: X heißt poissonverteilt, i.Z. $X~P_{\lambda}$, wenn

$$
M_{X} = \{0, 1, 2, 3, ... \}\quad\text{und}\quad P(x)=\frac{\lambda^x}{x!}exp(-\lambda)
$$
Dann gilt:

$$
\langle X\rangle = \lambda,\quad VX=\lambda
$$
Zur Verdeutlichung des Parameters $\lambda$:
Man erhält die Poissonverteilung auchaus einer Binomialverteilung für kleine $\vartheta$ und große n. Dann ist $\lambda = n\vartheta$. Ab $n\geq 30$ und $\vartheta\leq0.1$ ist dieser Übergtang für die meisten Anwendungen hinreichend genau.

### Geometrische Verteilung

* Definition: X heißt geometrische verteilt, i.Z. $X~G_{\vartheta}$, wenn

$$
M_{X} = \{1,2,3,... \}\quad\text{und}\quad P(x)=(1-\vartheta)^{x-1}\vartheta
$$
Dann gilt:

$$
\langle X\rangle = \frac{1}{\vartheta},\quad VX=\frac{1-\vartheta}{\vartheta^2}
$$


## Kontinuierliche Modelle