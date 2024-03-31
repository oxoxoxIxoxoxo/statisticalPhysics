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

* Zuordnung der Wahrscheinlichkeiten zu den einzelnen Elementen: Wahrscheinlichkeitsfunktion $P:\Omega \rightarrow [0,1]$

* Forderung an die Wahrscheinlichkeitsfunktion: $\sum_{\omega\in\Omega}P(\omega) = 1$

* Der Begriff der Wahrscheinlichkeit kann als empirisches Gesetz der großen Zahlen gedeutet werden, in dem sich ein bestimmter "Häufungswert" ermitteln lässt.

* Gegeben sei ein beliebig oft unter gleichen Bedingungen wiederholbares Experiment und $A\in\Omega$ ist ein Ausgang dieses Experiments. Weiters sei $H_{n}(A)$ die Anzahl der Ergebnisse von A bei n Durchführungen als absolute Häufigkeit und $h_{n}(A):=\frac{H_{n}(A)}{n}$ als relative Häufigkeit des Auftretens von A bei n Durchführungen gegeben. Dann zeigt die Folge der $h_{n}(A)$ ein "konvergentartiges" Verhalten.

* Man spricht von einem Laplace-Modell, wenn aufgrund von Symmetrien alle Ausgänge die gleiche Chance haben. Eines von n möglichen Ausgängen ist dann $\frac{1}{n}$ für alle dieser Ausgänge.

* Von einem Laplace Hilfsmodell spricht man, wenn sich die Wahrscheinlichkeiten kombinatorische ableiten lassen.

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
M_{X} = \{1,...,m \}\quad \text{und}\quad P(x)=\frac{1}{m}\quad\forall x\in M_{X}
$$

Dann gilt:

$$
\langle X\rangle = \frac{m+1}{2},\quad VX=\frac{m^2-1}{12}
$$

Anwendungen: Würfel, Zufallszahlen, Roulette, usw

### Alternativverteilung

* Definition: X heißt alternativverteilt, i.Z. $X\sim A_{\vartheta}$, wenn

$$
M_{X}=\{0,1 \}\quad\text{und}\quad P(1)=\vartheta,\quad P(0)=1-\vartheta
$$

Dann gilt:

$$
\langle X\rangle = \vartheta,\quad VX=\vartheta(1-\vartheta)
$$

Anwendungen, Münzwurf, Gut-Schlecht-Prüfungen, usw.

### Binomialverteilung

* Definition: X heißt binomialverteilt, i.Z. $X\sim B_{n,\vartheta}$, wenn

$$
M_{X}=\{0,1,...,n \}\quad\text{und}\quad P(x)=\binom{n}{x}\vartheta^x(1-\vartheta)^{n-x}
$$

Dann gilt:

$$
\langle X\rangle n\vartheta,\quad VX=n\vartheta(1-\vartheta)
$$

Anwendungen: Die Binomialverteilung kann als die Verteilung des Ziehens mit Zurücklegen angesehen werden, wobei aus einer Gesamtheit gezogen wird die sich im Verhältnis $\vartheta:1-\vartheta$ aus zwei Teilen zusammensetzt; z.B.: Anzahl von gewürfelten Sechsen, Auftreten einzelner Lottozahlen.

### Hypergeometrische Verteilung

* Definition: X heißt hypergeometrisch verteilt, i.Z. $X\sim H_{N,A,n}$, wenn

$$
M_{X}=\{k_{0},k_{0}+1,...,k_{1} \}\quad\text{und}\quad P(x)=\frac{\binom{A}{x}\binom{N-A}{n-x}}{\binom{N}{n}}
$$

wobei $k_{0}=max\{0,n-N+A\}$ und $k_{1} = min\{n,A \}$. Dann gilt

$$
\langle X\rangle = n\frac{A}{N},\quad VX=n\frac{A}{N}\big(1-\frac{A}{N} \big)\frac{N-n}{N-1}
$$

### Poissonverteilung

* Definition: X heißt poissonverteilt, i.Z. $X\sim P_{\lambda}$, wenn

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

* Definition: X heißt geometrische verteilt, i.Z. $X\sim G_{\vartheta}$, wenn

$$
M_{X} = \{1,2,3,... \}\quad\text{und}\quad P(x)=(1-\vartheta)^{x-1}\vartheta
$$

Dann gilt:

$$
\langle X\rangle = \frac{1}{\vartheta},\quad VX=\frac{1-\vartheta}{\vartheta^2}
$$


## Stetige Zufallsgrößen und Verteilungen

* Stetige Zufallsgrößen spielen in der Physik eine bedeutende Rolle. Um sie angeben zu können stellt man sich eine diskrete Zufallsgröße vor und lässt die Diskretisierung immer feiner werden. Der Grenzfall bildet eine stetige Funktion, die sogenannte "Dichtefunktion" f oder $\Phi$ mit folgenden Eigenschaften:

$$
f: M_{X}\rightarrow \mathbb{R}^{+}, \text{integrierbar}
$$

$$
\int_{M_{X}}f(x)dx = 1
$$

$$
P(\{x\in M_{X}:a\leq x \leq b \}) = \int_{a}^{b}f(x)dx
$$

* Bemerkung: Da die Wahrscheinlichkeit einer stetigen Verteilung durch ein Integral definiert ist, kann man einem einzelnen Punkt keine Wahrscheinlichkeit mehr zuordnen, sondern nur mehr einem Intervall.

* Definition: Sei X eine stetige (oder diskrete) Zufallsgröße, dann ist die Verteilungsfunktion $F(\xi):= P(\{x\in M_{X}: x\leq\xi \}) \quad \forall \xi \in\mathbb{R}$

Ist X diskret, so ist $F(x)=\sum_{x_{i}\leq x}P(x_{i})$ eine Treppenfunktion.

Ist X stetig, so ist F eine stetige Funktion mit:

$$
F'(x) = f(x), F(x)=\int_{-\infty}^{x} f(t)dt \text{und es gilt} P(\{x\in M_{X}:a\leq x\leq b \})=F(b)-F(a)
$$

### Lage und Streuparameter

* $\alpha$-Fraktil $x_{\alpha}$: $F(x_{\alpha})=\alpha$

Sonderfälle:

- 0.5-Fraktil (Median)
- 0.25-Fraktil (unteres Quartil)
- 0.75-Fraktil (oberes Quartil)

* Erwartungswert $\langle X\rangle$: In Verallgemeinerung zum diskreten Fall gilt:

$$
\langle X\rangle = \int_{M_{X}} xf(x)dx
$$

bzw. für die Funktion einer Zufallsgröße

$$
\langle g(X)\rangle = \int_{M_{X}} g(x)f(x)dx
$$

* Varianz $ VX =\sigma^2$: Sie ist ebenfalls analog zum diskreten Fall definiert durch

$$
VX = \int_{M_{X}} (x-\langle X\rangle)^2f(x)dx
$$

Ihre positive Wurzel $+\sqrt{VX}=\sigma$ heiß Standardabweichung. Es gilt weiterhin der Verschiebungssatz.

### Stetige Gleichverteilung

* Definition: X heißt stetig gleichverteilt auf $[a, b]$ i.Z. $X\sim S_{a,b}$, wenn

$$
M_{X}=[a,b] \quad \text{und}\quad f(x)=\frac{1}{b-a}\quad \forall x\in M_{X}
$$

Dann gilt:

$$
\langle X\rangle = \frac{a+b}{2},\quad VX=\frac{(b-a)^2}{12}
$$

Anwendungen: Kontinuierliche Zufallszahlen, usw.

### Exponentialverteilung

* Definition: X heißt exponentialverteilt, i.Z. $X\sim E_{x_{\lambda}}$, wenn

$$
M_{X}=\mathbb{R}^{+} \quad \text{und}\quad f(x)=\lambda exp(-\lambda x)
$$

Dann gilt:

$$
\langle X\rangle =\frac{1}{\lambda},\quad VX=\frac{1}{\lambda^2}
$$

Es besteht folgender Zusammenhang zur Poisson-Verteilung:
Ist die Anzahl von Ereignissen in einem Zeitintervall der Länge t verteilt nach $P_{\lambda t}$, so ist die Zeit zwischen den Ereignissen verteilt nach $E_{x_{\lambda}}$

Anwendungen: Lebensdauern, Zerfallszeiten (Radio-Carbon-Datierung), Wartezeiten

### Normalverteilung

* Definition: X heißt standard-normalverteilt, i.Z. $X\sim N(0,1)$, wenn

$$
M_{X}=\mathbb{R}\quad \text{und}\quad f(x)=\frac{1}{\sqrt{2π}}exp(-\frac{(x-\mu)^2}{2\sigma^2})
$$

Anwendungen: Die Normalverteilung tritt immer dann auf, wenn sich eine Zufallsgröße aus einer Summe vieler unabhängiger Einflussgrößen ergibt. Z.B.: Messfehler, Abmessungen von Bauteilen, Länge von Grashalmen auf einem Feld, usw. Aber auch z.B. die Antreffwahrscheinlichkeitsdichte $|\psi(x,t)|^2$ eines Teilchens in der Quantenmechanik ist eine Normalverteilung.

# Statistische Tests

## Hypothesen und Tests

## Der Chi-Quadrat-Test

## Der Run-Test

# Messfehler

# Zufallsgeneratoren
