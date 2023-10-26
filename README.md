Jeg begynte med å ta testene fra oblig 2. Det gikk greit men når jeg begynte å commite changesan så merket jeg at testene ikke fungerte lenger. Prøvde å finne ut hva det var i noen dager men fant ikke svaret.

Jeg lagde så hele prosjektet på nytt med hjelp av noen medstudenter. Jeg hadde 1 mye bedre test som tester funkskjonen min og gikk lett inn i github med actions. Det jeg gjordet var at jeg lagde et repository som heter Oblig3_retry som jeg la de to filene mine i. Jeg lagde så en requirements.txt fordi det sto i oblig 2 som jeg skrev pytest i. Jeg lagde så en workflows mappe for å "gi signal" til github at nå kan jeg begynne med actions. Jeg begynte med actions og kom ikke langt. Så fikk jeg vite om "https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python" som hjalp meg veldig med actions delen av oppgaven. 

Teknisk så brukte jeg youtube videoer for å vite hvordan man gjør de forskjellige tingene. Med de nye testene så måtte jeg skrive python pip install. 

Man lager en yml fil i filstruktur som github kjenner igjen og aktiveres når det er en "push" til "main" branchen. Dette betyr at hver gang noen pusher endringer til hovedgrenen i repoet, vil dette workflowet bli utløst.

Job: Denne jobben heter "test" og kjører på en Ubuntu-maskin med den nyeste versjonen av Ubuntu.

checkout: Dette trinnet bruker GitHub Actions' innebygde handling actions/checkout@v2 for å trekke inn koden fra Git-repositoriet i workflowets arbeidsområde.

Sett opp Python: Dette trinnet bruker også en innebygd GitHub Actions-handling, actions/setup-python@v2, for å installere Python 3.9.13 på arbeidsmaskinen.

Installer avhengigheter: Dette trinnet bruker kommandoen pip install -r requirements.txt for å installere Python-avhengigheter som er definert i en fil kalt "requirements.txt". 

Deretter kjør Pytest: Dette trinnet bruker kommandoen pytest --junitxml=pytest_report.xml for å kjøre Pytest-testene. Pytest er et populært rammeverk for å kjøre Python-tester. Det genererer også en JUnit XML-testrapport kalt "pytest_report.xml". Denne rapporten kan brukes senere for å analysere resultatene av testene.

Sett output (output name "report"): Dette trinnet bruker echo-kommandoen sammen med ::set-output for å informere GitHub Actions om plasseringen av JUnit XML-testrapporten. Denne informasjonen kan brukes senere i workflowen

Last opp testrapport: Til slutt bruker dette trinnet GitHub Actions-håndlingen jeg har gjort slik at man kan laste ned pytest rapport osv

