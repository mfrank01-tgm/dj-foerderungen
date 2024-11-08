import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'k', 'M', 'B', 'T'][magnitude])

st.set_page_config(page_title='Corona Förderungen', initial_sidebar_state='collapsed')
st.write("*Dieser Text ist eine Rohversion und ist nicht als journalistisches Produkt zu verstehen. Es handelt sich hierbei um eine Übung im Rahmen eines Kurses.*")
# TODO: Muss ggf. als Frage umformuliert werden, falls sich die These nicht bestätigt
st.title('Vitamin B im Corona-Förderdschungel')

# Teaser
# TODO: Teaser in einen Satz umwandeln und den Rest in die Einleitung
st.write("**Haben Unternehmen von Politikern überdurchschnittlich hohe Corona-Förderungen bekommen?**")


# Einleitung
# TODO: Überarbeitung schon im Word, muss ggf. noch angepasst werden
st.write("""
Die staatlichen Corona-Förderungen kosteten Milliarden und waren für viele Betriebe während der Pandemie überlebenswichtig. 
    Doch auch einige Parlamentarier mit engen Verbindungen zur Wirtschaft oder eigenen Unternehmen profitierten von diesen Geldern.
    Das wirft kritische Fragen auf: Haben Politiker besonders hohe Fördersummen erhalten? 
    Wo verlaufen die Grenzen zwischen Eigeninteresse und öffentlicher Verantwortung? 
    In diesem Artikel nehmen wir die 8 Abgeordneten unter die Lupe, deren aktuelles oder ehemaliges Unternehmen Corona-Förderungen erhalten hat.""")


st.write("#### Betroffene Politiker")
st.write("""Wir konnten in unserer Datenanalyse aufzeigen, dass es 8 Parlamentier:innen gibt deren Unternehmen Förderungen erhielt. 
         Von der SPÖ die Abgeordneten Drozda, Keck, Köchl und Yildirim, bei der ÖVP die Abgeordneten Hörl, Minnich und Schmidhofer und 
         die Mandatare der Grünen Dziedzic und Schallmeiner. Wir haben genauere Analysen durchgeführt, wenn die Förderhöhe des Unternehmens stark vom
         Branchendurchschnitt abweicht.""")

# Selma Yildirim
st.write("#### Selma Yildirim und die Innsbrucker Soziale Dienste")
st.write("In der Branche Altenpflege gab es nur zwei Unternehmen, die Coronaförderungen erhalten haben. Eines davon beschäftigt die SPÖ-Abgeordnete Selma Yildirim im Aufsichtsrat. Summiert man alle Förderungen, die diese beiden Unternehmen bekommen haben, sieht man, dass das Unternehmen mit politischer Nähe eine höhere Summe bekommen hat.")
df_sy = pd.read_csv('app_data/selma_yildirim.csv')
# Sortieren damit höchste Förderung oben steht
df_sy = df_sy.sort_values('Beihilfeelement, in voller Höhe', ascending=True)
# Firma von Selma Yildirim farblich markieren
df_sy['color'] = df_sy['Name des Beihilfeempfängers'].apply(lambda x: 'Selma Yildirim <br>im Aufsichtsrat' if x == 'Innsbrucker Soziale<br> Dienste GmbH' else '')
fig_sy = px.bar(
    df_sy,
    x='Beihilfeelement, in voller Höhe',
    y='Name des Beihilfeempfängers',
    orientation='h',
    color='color',
    title='Die Corona-Förderungen für die Innsbrucker Soziale Dienste, in der Selma Yildirim <br>im Aufsichtsrat sitzt fällt höher aus (11%), als die des anderen Unternehmens derselben Branche',
    labels={'Beihilfeelement, in voller Höhe': 'Förderung in €', 'Name des Beihilfeempfängers': 'Förderempfänger in<br> der Altenpflegebranche'},
    color_discrete_map={'Innsbrucker Soziale<br> Dienste GmbH': 'red', '': 'grey'}
)
# Fußnote als Annotation hinzufügen
fig_sy.add_annotation(
    text="Quelle: transparenzportal.gv.at ",
    xref="paper", yref="paper",
    x=-0.4, y=-0.25,  # Positionierung der Fußnote unterhalb der Grafik
    showarrow=False,
    font=dict(size=12)#, color="gray")
)
st.plotly_chart(fig_sy)
st.write("Die geringe Anzahl geförderter Unternehmen in dieser wichtigen Branche wirft Fragen auf und hindert die Vergleichbarkeit. Es liefert aber trotzdem ein erstes Indiz, welches weitere Untersuchungen bekräftigt.")

# Thomas Drozda
st.write("### Thomas Drozda und die Vereinigten Bühnen Wien")
st.write("Der SPÖ-Abgeordnete Thomas Drozda war bis 2016 der Generaldirektor der Vereinigten Bühnen Wien und war bis 2017 Bundesminister für Kunst und Kultur. Im Förder-Ranking in der Branche Kunst und Kultur ist sein ehemaliger Arbeitgeber an der Spitze und hat mit am meisten von den Förderungen profitiert, mit einer Gesamtsummer von 800.000€.")
df_td = pd.read_csv('./app_data/thomas_drozda.csv')
df_td['Name des Beihilfeempfängers'] = df_td['Name des Beihilfeempfängers'].replace("Vereinigte B�hnen Wien GmbH", "Vereinigte Bühnen Wien GmbH")
# Sortieren damit höchste Förderung oben steht
df_td = df_td.sort_values('Beihilfeelement, in voller Höhe', ascending=True)
# Durchschnitt berechnen
mean_value = df_td['Beihilfeelement, in voller Höhe'].mean()
# Firma von Thomas Drozda farblich markieren
df_td['color'] = df_td['Name des Beihilfeempfängers'].apply(lambda x: 'Generaldirektor <br>Thomas Drozda' if x == 'Vereinigte Bühnen Wien GmbH' else '')
fig_td = px.bar(
    df_td,
    x='Beihilfeelement, in voller Höhe',
    y='Name des Beihilfeempfängers',
    orientation='h',
    color='color',
    title='Die Vereinigeten Bühnen Wien mit SPÖ Generaldirektor Thomas Drozda haben <br>überdurchschnittlich (34%) hohe Förderungen während Corona erhalten',
    labels={'Beihilfeelement, in voller Höhe': 'Förderung in €', 'Name des Beihilfeempfängers': 'Förderempfänger in<br> der Kunst'},
    color_discrete_map={'Vereinigte Bühnen Wien GmbH': 'red', '': 'grey'}
)
# Durchschnittslinie hinzufügen
fig_td.add_shape(
    type="line",
    x0=mean_value, x1=mean_value,
    y0=-0.5, y1=len(df_td['Name des Beihilfeempfängers']) - 0.5,  # Länge der Linie über alle Balken
    line=dict(color="black", width=2),
    name="Durchschnitt"
)
# Annotation für den Durchschnittswert hinzufügen
fig_td.add_annotation(
    x=mean_value, 
    y=-0.8,  # Position der Annotation am unteren Rand
    text=f"Durchschnitt: {human_format(mean_value)}",
    showarrow=False,
    font=dict(color="black")
)
# Fußnote als Annotation hinzufügen
fig_td.add_annotation(
    text="Quelle: transparenzportal.gv.at ",
    xref="paper", yref="paper",
    x=-0.85, y=-0.25,  # Positionierung der Fußnote unterhalb der Grafik
    showarrow=False,
    font=dict(size=12)# color="gray")
)
st.plotly_chart(fig_td)
st.write("Angesichts der Bedeutung der Kulturbranche und der zahlreichen betroffenen Künstler und deren Vereine ist es wichtige, diese nicht im Stich zu lassen. Es ist jedoch Fakt, dass jene Unternehmen in Kunst und Kultur, mit politischer Nähe am meisten von diesen Förderungen profitiert haben.")


# TODO: Franz Hörl
st.write("### Franz Hörl und das Skilift-Zentrum-Gerlos")

st.write("""
Eine genauere Analyse des Skigebiets Skilift-Zentrum-Gerlos zeigt, dass der ÖVP Politiker Franz Hörl Geschäftsführer ist. In einer Rangliste an 
Förderungsempfängern unter allen Seilbahnbetrieben Österreichs liegt das Unternehmen  am 16. Platz mit über sieben Millionen Euro 
an Förderungen. Eine weitere Recherche hat ergeben, dass der Betrieb in einem Umsatzranking der Branche von 2018/19 nur den 26. Rang 
belegt mit einem Umsatz von 17,7 Millionen Euro. Im Vergleich dazu erhält die Zauchensee Liftgesellschaft eine ähnliche Fördersumme 
von rund 7 Millionen Euro, erzielt jedoch einen deutlich höheren Umsatz von fast 25 Millionen Euro.
""")

# Step 1: Define the data
data = {
    "Seilbahnbetrieb": ["Skilift-Zentrum-Gerlos", "Skilift-Zentrum-Gerlos", 
                "Zauchsee Liftgesellschaft", "Zauchsee Liftgesellschaft"],
    "Category": ["Umsatz", "Förderungen", "Umsatz", "Förderungen"],
    "Höhe in Millionen": [17.71, 7.17, 24.87, 7.28],  # Amounts in millions
    "color": ["Geschäftsführer <br>Franz Hörl", "Geschäftsführer <br>Franz Hörl", "", ""]  # Mark Skilift-Zentrum-Gerlos for highlighting
}

# Create DataFrame
df = pd.DataFrame(data)

# Step 2: Set up color mapping for highlighting specific rows
color_discrete_map = {'Geschäftsführer <br>Franz Hörl': 'red', '': 'grey'}

# Step 4: Create traces for two subplots (one for each company)

# Filter data for each company
df_gerlos = df[df['Seilbahnbetrieb'] == 'Skilift-Zentrum-Gerlos']
df_zauchsee = df[df['Seilbahnbetrieb'] == 'Zauchsee Liftgesellschaft']

# Create Gerlos chart with red color for highlights
fig_gerlos = px.bar(df_gerlos, 
                    x="Category", 
                    y="Höhe in Millionen", 
                    color="color", 
                    color_discrete_map=color_discrete_map,
                    title="Skilift-Zentrum-Gerlos: Umsatz and Förderungen")

# Create Zauchsee chart with grey color
fig_zauchsee = px.bar(df_zauchsee, 
                      x="Category", 
                      y="Höhe in Millionen", 
                      color="color", 
                      color_discrete_map=color_discrete_map,
                      title="Zauchsee Liftgesellschaft: Umsatz and Förderungen")

# Step 5: Combine the two figures into subplots using plotly.subplots

# Create subplots: 1 row, 2 columns
fig = make_subplots(rows=1, cols=2, 
                    subplot_titles=("Skilift-Zentrum-Gerlos", "Zauchsee Liftgesellschaft"),
                    shared_yaxes=True)

# Add Gerlos figure to the first subplot
for trace in fig_gerlos.data:
    fig.add_trace(trace, row=1, col=1)

# Add Zauchsee figure to the second subplot
for trace in fig_zauchsee.data:
    fig.add_trace(trace, row=1, col=2)

# Update layout
fig.update_layout(
    title="Das Skilift-Zentrum-Gerlos mit Franz Hörl (ÖVP) als Geschäftsfürher erhält überdurchschnittlich <br>hohe Förderungen im Vergleich zum Umsatz in der Branche",
    showlegend=True,
    barmode='group',  # Group bars for each category
    xaxis_title="",
    yaxis_title="Höhe in Millionen €",
)

# Step 6: Add footnote as annotation (position it below the plot)
fig.add_annotation(
    text="Quelle: transparenzportal.gv.at, tai.at",
    xref="paper", yref="paper",
    x=-0.1, y=-0.17,  # Positioning the footnote below the figure
    showarrow=False,
    font=dict(size=12),#, color="gray"),
    align="center"  # Align the text to the center
)

# Step 6: Display the plot in Streamlit
st.plotly_chart(fig)
st.write("Da die Corona-Förderungen in dieser Branche vor allem den Umsatzeinbruch abfangen sollen, sollte das Unternehmen von Herrn Hörl im Vergleich mit anderen Skilift Unternehmen nicht so hohe Förderungen erhalten haben. Diese Diskrepanz wirft die Frage auf, nach welchen Kriterien die Fördermittel verteilt wurden und ob persönliche Verbindungen einen Einfluss hatten.")

# Ralph Schallmeiner
st.write("### Ralph Schallmeiner und Conrad Electronic")
st.write("""Der Grünen-Abgeordnete Ralph Schallmeiner hat für Conrad gearbeitet. Das Unternehmen erhielt fast 1,5 Millionen Euro an 
         Coronaförderungen für seine österreichischen Niederlassungen. Angesichts der Marktmacht von Conrad stellt sich die Frage, 
         ob diese Förderhöhe gerechtfertigt ist oder ob kleinere Unternehmen benachteiligt wurden.""")


st.write("### Fazit")
st.write("""Alle Förderungen wurden laut Regierungsangaben nach transparenten Kriterien vergeben, basierend auf Umsatzverlusten und 
         wirtschaftlicher Notwendigkeit. 
         Ob Abgeordnete überdurchschnittlich hohe Förderungen erhalten haben, lässt sich nicht eindeutig belegen,
         dennoch zeigen die Daten Auffälligkeiten.
         Die Untersuchung zeigt die Bedeutung von Transparenz und Kontrolle bei der Vergabe staatlicher Mittel. 
         Es ist unerlässlich, dass solche Prozesse genau beobachtet und hinterfragt werden, 
         um das Vertrauen der Öffentlichkeit in die Politik zu stärken. """)

 

# Interviewleitfaden
st.write("""
## Interviewleitfaden für Abgeordnete zur Corona-Förderung

Um ein umfassendes Bild zu erhalten und mögliche Unklarheiten zu beseitigen, soll ein Interview mit den betroffenen Abgeordneten geführt werden. Der folgende Leitfaden dient dazu, gezielte Fragen zu stellen und tiefere Einblicke zu gewinnen. Die Fragen weichen je nach Abgeordeneten ab, um spezifische Aspekte der Branche und jeweiligen zugehörigen Partei besser zu beleuchten.

**Allgemeine Fragen**
- Wie bewerten Sie generell die Vergabe der Coronaförderungen in Ihrer Branche?
- Gab es aus Ihrer Sicht genügend Transparenz bei der Vergabe der Fördermittel?
- Waren Sie an der Konzeption des Gesetzespakets, welches die Fördermaßnahmen beschloss, direkt beteiligt?

**Spezifische Fragen an Selma Yildirim (SPÖ)**
- Ihr Unternehmen gehört zu den wenigen in der Altenpflegebranche, die Förderungen erhalten haben. Wie erklären Sie sich das?
- Sehen Sie einen möglichen Interessenskonflikt zwischen Ihrer politischen Tätigkeit und Ihrer Position in einem Pflegeheim?

**Spezifische Fragen an Thomas Drozda (SPÖ)**
- Die Vereinigten Bühnen Wien erhielten den größten Anteil der Förderungen in der Kulturbranche. Was waren die Kriterien für diese hohe Förderung?
- Sehen Sie einen möglichen Interessenskonflikt zwischen Ihrer politischen Tätigkeit und Ihrer Position bei den Vereinigten Bühnen Wien?

**Spezifische Fragen an Franz Hörl (ÖVP)**
- Ihr Betrieb erhielt eine hohe Förderung im Vergleich zu ähnlichen Unternehmen mit höherem Umsatz. Wie erklären Sie diese Diskrepanz?
- Sehen Sie einen möglichen Interessenskonflikt zwischen Ihrer politischen Tätigkeit und Ihrer Funktion als Geschäftsführer in einem Seilbahnbetrieb?

**Spezifische Fragen an Ralph Schallmeiner (GRÜNE)**
- Conrad erhielt erhebliche Fördermittel. Waren Sie in irgendeiner Form in den Antragsprozess involviert?
- Wie stellen Sie sicher, dass Ihre politische Tätigkeit und frühere berufliche Verbindungen getrennt bleiben?

**Abschlussfragen**
- Welche Maßnahmen halten Sie für notwendig, um Transparenz und Fairness bei zukünftigen Förderungen zu gewährleisten?
- Möchten Sie sonst noch etwas hinzufügen oder klarstellen?
""")