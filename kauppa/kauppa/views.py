from django.http import HttpResponse

ETUSIVU_HTML = """
<html>
<body>
<H1>Kauppa</H1>
Data täältä 
<a href="/tuote/1">Tuotetta 1</a>
tai
<a href="/tuote/2">Tuotetta 2</a>

</body>
</html>
"""

TUOTESIVU_HTML = """
<html>
<body>
<H1>Kauppa</H1>
<h2>Tuote {}</h2>
<p>Nyt tarjouksessa. Osta heti!</p>
<p>Data täältä <a href="/">ETUSIVU</a></p>
</body>
</html>
"""

def etusivu(request):
    return HttpResponse(ETUSIVU_HTML)

def tuotesivu (request, tuote_id):
    return HttpResponse(TUOTESIVU_HTML.format(tuote_id))