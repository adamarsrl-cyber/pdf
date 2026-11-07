import json

# libro: (testamento, capitulos)
# Antiguo Testamento: 39 libros. Nuevo Testamento: 27 libros. Total: 66.
libros_at = [
    ("Génesis",50),("Éxodo",40),("Levítico",27),("Números",36),("Deuteronomio",34),
    ("Josué",24),("Jueces",21),("Rut",4),("1 Samuel",31),("2 Samuel",24),
    ("1 Reyes",22),("2 Reyes",25),("1 Crónicas",29),("2 Crónicas",36),("Esdras",10),
    ("Nehemías",13),("Ester",10),("Job",42),("Salmos",150),("Proverbios",31),
    ("Eclesiastés",12),("Cantares",8),("Isaías",66),("Jeremías",52),("Lamentaciones",5),
    ("Ezequiel",48),("Daniel",12),("Oseas",14),("Joel",3),("Amós",9),
    ("Abdías",1),("Jonás",4),("Miqueas",7),("Nahúm",3),("Habacuc",3),
    ("Sofonías",3),("Hageo",2),("Zacarías",14),("Malaquías",4),
]
libros_nt = [
    ("San Mateo",28),("San Marcos",16),("San Lucas",24),("San Juan",21),("Hechos",28),
    ("Romanos",16),("1 Corintios",16),("2 Corintios",13),("Gálatas",6),("Efesios",6),
    ("Filipenses",4),("Colosenses",4),("1 Tesalonicenses",5),("2 Tesalonicenses",3),
    ("1 Timoteo",6),("2 Timoteo",4),("Tito",3),("Filemón",1),("Hebreos",13),
    ("Santiago",5),("1 Pedro",5),("2 Pedro",3),("1 Juan",5),("2 Juan",1),
    ("3 Juan",1),("San Judas",1),("Apocalipsis",22),
]

grupos_tematicos = [
    ("Pentateuco", ["Génesis","Éxodo","Levítico","Números","Deuteronomio"]),
    ("Históricos", ["Josué","Jueces","Rut","1 Samuel","2 Samuel","1 Reyes","2 Reyes","1 Crónicas","2 Crónicas","Esdras","Nehemías","Ester"]),
    ("Poéticos", ["Job","Salmos","Proverbios","Eclesiastés","Cantares"]),
    ("Profetas Mayores", ["Isaías","Jeremías","Lamentaciones","Ezequiel","Daniel"]),
    ("Profetas Menores", ["Oseas","Joel","Amós","Abdías","Jonás","Miqueas","Nahúm","Habacuc","Sofonías","Hageo","Zacarías","Malaquías"]),
    ("Evangelios", ["San Mateo","San Marcos","San Lucas","San Juan"]),
    ("Hechos de los Apóstoles", ["Hechos"]),
    ("Cartas Paulinas", ["Romanos","1 Corintios","2 Corintios","Gálatas","Efesios","Filipenses","Colosenses","1 Tesalonicenses","2 Tesalonicenses","1 Timoteo","2 Timoteo","Tito","Filemón"]),
    ("Cartas Universales", ["Hebreos","Santiago","1 Pedro","2 Pedro","1 Juan","2 Juan","3 Juan","San Judas"]),
    ("Revelación", ["Apocalipsis"]),
]

# Recursos adicionales (fuera de libro/capítulo/temático), tal como lo pidió el ministerio.
AYUDAS_SOLICITADAS_TOTAL = 33
AYUDAS_BIBLICAS_TOTAL = 68
PARABOLAS_TOTAL = 52
BIENAVENTURANZAS_TOTAL = 9

def slug(s):
    import unicodedata
    s = unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode()
    s = s.lower().replace(' ','-')
    return s

catalogo = {
    "libro_completo": [],
    "por_capitulo": [],
    "tematicos": [],
    "ayudas_solicitadas": [],
    "ayudas_biblicas": [],
    "parabolas": [],
    "bienaventuranzas": [],
}

for testamento, libros in [("Antiguo Testamento", libros_at), ("Nuevo Testamento", libros_nt)]:
    for nombre, caps in libros:
        sl = slug(nombre)
        catalogo["libro_completo"].append({
            "id": f"lc-{sl}",
            "titulo": f"Estudio bíblico completo: {nombre}",
            "testamento": testamento,
            "libro": nombre,
            "capitulos": caps,
            "archivo": f"pdfs/libro-completo/{sl}.pdf",
            "disponible": False
        })
        for c in range(1, caps+1):
            catalogo["por_capitulo"].append({
                "id": f"cap-{sl}-{c}",
                "titulo": f"{nombre} {c}",
                "testamento": testamento,
                "libro": nombre,
                "capitulo": c,
                "archivo": f"pdfs/por-capitulo/{sl}/{sl}-{c}.pdf",
                "disponible": False
            })

for grupo, libros in grupos_tematicos:
    sl = slug(grupo)
    catalogo["tematicos"].append({
        "id": f"tem-{sl}",
        "titulo": f"Estudio bíblico temático: {grupo}",
        "libros": libros,
        "archivo": f"pdfs/tematicos/{sl}.pdf",
        "disponible": False
    })

for i in range(1, AYUDAS_SOLICITADAS_TOTAL + 1):
    catalogo["ayudas_solicitadas"].append({
        "id": f"ayu-sol-{i}",
        "titulo": f"Ayuda Bíblica Solicitada {i}",
        "categoria": "Ayudas Bíblicas Solicitadas",
        "archivo": f"pdfs/ayudas-solicitadas/ayuda-solicitada-{i}.pdf",
        "disponible": False
    })

for i in range(1, AYUDAS_BIBLICAS_TOTAL + 1):
    catalogo["ayudas_biblicas"].append({
        "id": f"ayu-bib-{i}",
        "titulo": f"Ayuda Bíblica {i}",
        "categoria": "Ayudas Bíblicas",
        "archivo": f"pdfs/ayudas-biblicas/ayuda-biblica-{i}.pdf",
        "disponible": False
    })

for i in range(1, PARABOLAS_TOTAL + 1):
    catalogo["parabolas"].append({
        "id": f"parabola-{i}",
        "titulo": f"Estudio bíblico de la parábola {i}",
        "categoria": "Parábolas",
        "archivo": f"pdfs/parabolas/parabola-{i}.pdf",
        "disponible": False
    })

for i in range(1, BIENAVENTURANZAS_TOTAL + 1):
    catalogo["bienaventuranzas"].append({
        "id": f"bienav-{i}",
        "titulo": f"Estudio de la bienaventuranza {i}",
        "categoria": "Bienaventuranzas",
        "archivo": f"pdfs/bienaventuranzas/bienaventuranza-{i}.pdf",
        "disponible": False
    })

total = sum(len(v) for v in catalogo.values())
print("Total de estudios en el catálogo:", total)
for clave, lista in catalogo.items():
    print(" ", clave, ":", len(lista))

with open("/home/claude/portal/portal/js/catalogo.js", "w", encoding="utf-8") as f:
    f.write("// Catálogo generado de estudios bíblicos.\n")
    f.write("// 'disponible: false' = aún no se subió el PDF (marcador de espacio).\n")
    f.write("// Cuando generes un nuevo PDF con la app de escritorio, colócalo en la ruta 'archivo'\n")
    f.write("// indicada y cambia 'disponible' a true. No hace falta tocar el HTML.\n")
    f.write("const CATALOGO = ")
    f.write(json.dumps(catalogo, ensure_ascii=False, indent=1))
    f.write(";\n")
