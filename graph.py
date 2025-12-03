import graphviz
import re
from pathlib import Path

# --- Arborescence de fichiers ---
file_tree_text = """
Rout-Art/
├── Comment_regler_les_soucis_du_CMS.docx
├── README.md
├── app.py
├── cms
│   ├── CMS.md
│   ├── DOCUMENTATION.md
│   ├── README_CMS.md
│   ├── icon
│   │   ├── logo-routart.png
│   │   └── logo_routart.ico
│   ├── requirements.txt
│   └── source
│       ├── __init__.py
│       ├── build_exe.py
│       ├── config_manager.py
│       ├── git_manager.py
│       ├── html_manager.py
│       ├── logger.py
│       ├── rout_art_cms.py
│       ├── rout_art_cms.spec
│       └── server_manager.py
├── compile.bat
├── dependecies.bat
├── dist
│   └── Rout'Art CMS.exe
├── file_tree_stable.png
├── files
│   ├── moto
│   │   ├── 125cm3
│   │   │   └── programme_formation_125cm3.pdf
│   │   ├── a1
│   │   │   ├── parcours_formation_a1.pdf
│   │   │   └── programme_formation_a1.pdf
│   │   ├── a2
│   │   │   ├── enjeux_formation_a2.pdf
│   │   │   ├── parcours_formation_a2.pdf
│   │   │   └── programme_formation_a2.pdf
│   │   ├── a2_a
│   │   │   └── parcours_formation_a.pdf
│   │   └── am
│   │       ├── enjeux_formation_permis_am.pdf
│   │       └── programme_formation_permis_am.pdf
│   ├── reglement_interieur.docx
│   └── voiture
│       ├── auto
│       │   └── programme_auto_manuel.pdf
│       ├── enjeux_formation_permis_b.pdf
│       ├── parcours_formation_b.pdf
│       └── programme_formation_b.pdf
├── graph.py
├── icon
│   └── logo_routart_modern.png
├── images
│   ├── avatar
│   │   ├── avatar-emma.png
│   │   └── avatar-paul.png
│   ├── france-travail-sombre.png
│   ├── france-travail.png
│   ├── garantie-financiere.png
│   ├── hero-car-road.png
│   ├── icon-car.png
│   ├── icon-facebook.ico
│   ├── icon-instagram.png
│   ├── icon-moto.png
│   ├── logo_routart_modern.png
│   ├── moto
│   │   ├── am-bsr.png
│   │   ├── permis-a1-125.png
│   │   └── permis-a2.png
│   ├── permis-1e.png
│   ├── prepa_code.png
│   ├── remerciement
│   │   ├── avatar_jean-baptiste.png
│   │   ├── github_ico.svg
│   │   ├── github_ico_darkmode.svg
│   │   ├── linkedin_ico.png
│   │   ├── portfolio_ico.png
│   │   ├── portfolio_ico_darkmode.png
│   │   └── techno
│   │       ├── github_ico.svg
│   │       ├── github_ico_dark.svg
│   │       ├── html.png
│   │       ├── html_dark.png
│   │       └── python.png
│   └── voiture
│       ├── permis-b-accompagnee.png
│       ├── permis-b-automatique.png
│       └── permis-b-traditionnel.png
├── index.html
├── page
│   ├── code_de_la_route.html
│   ├── contact.html
│   ├── equipe.html
│   ├── financement.html
│   ├── formations.html
│   ├── garantie_financiere.html
│   ├── positionnement.html
│   ├── presse.html
│   ├── reclamation.html
│   ├── reglement.html
│   ├── remerciement.html
│   ├── resultat.html
│   ├── satisfaction.html
│   ├── tarifs.html
│   └── template.html
├── robots.txt
├── run.bat
├── script
│   ├── dark-mode.js
│   ├── financement.js
│   ├── formations.js
│   ├── remerciement.js
│   ├── script.js
│   └── tarifs.js
├── setup_git_safe.bat
├── sitemap.xml
└── style
    ├── README.md
    ├── code_de_la_route.css
    ├── contact.css
    ├── dark-mode.css
    ├── equipe.css
    ├── financement.css
    ├── formations.css
    ├── garantie_financiere.css
    ├── general.css
    ├── index.css
    ├── positionnement.css
    ├── presse.css
    ├── reclamation.css
    ├── reglement.css
    ├── remerciement.css
    ├── resultat.css
    ├── satisfaction.css
    ├── tarifs.css
    └── variables.css
"""


def parse_tree_text(tree_text):
    lines = tree_text.strip().split('\n')
    if lines and 'Rout-Art tree' in lines[0]:
        lines = lines[2:]

    paths = []
    indent_map = {}

    for line in lines:
        clean_line = re.sub(r'[\s\t\n\r│├─└──]+', '', line).strip()
        if not clean_line:
            continue

        match = re.search(r'[a-zA-Z0-9._-]+', line)
        if not match:
            continue

        name = match.group(0)
        indent_index = match.start()

        parent_path = ''
        if indent_index > 0:
            parent_indent = max(
                [i for i in indent_map if i < indent_index] or [-1])
            if parent_indent != -1:
                parent_path = indent_map.get(parent_indent, '')

        current_path = Path(parent_path) / name
        paths.append(str(current_path))
        indent_map[indent_index] = str(current_path)

    return paths


def create_file_tree_graph(file_tree_text, output_filename="file_tree_stable"):
    paths = parse_tree_text(file_tree_text)

    dot = graphviz.Digraph(
        'FileTree',
        comment='Arborescence de fichiers Rout-Art',
        format='png',
        graph_attr={
            'rankdir': 'LR',
            'splines': 'polyline',  # <--- CHANGEMENT CRUCIAL : 'ortho' crashe, 'polyline' est stable
            'ranksep': '2.0',       # Espace horizontal large pour éviter les chevauchements
            'nodesep': '0.08',      # Espace vertical très serré
            'bgcolor': '#ffffff',
            'ordering': 'out',      # Garde l'ordre visuel des fichiers
            'concentrate': 'true',  # Fusionne les lignes
            'dpi': '300'
        },
        node_attr={
            'shape': 'plain',
            'fontname': 'Consolas',
            'fontsize': '10',
            'height': '0.2',
            'margin': '0.05'
        },
        edge_attr={
            'color': '#888888',
            'arrowhead': 'none',
            'penwidth': '1.0'
        }
    )

    root_name = 'Rout-Art'
    dot.node(root_name, label=root_name, shape='rect',
             style='filled,bold', fillcolor='#E3F2FD', fontname='Arial-Bold')

    added_edges = set()

    for path_str in paths:
        path = Path(path_str)
        parts = path.parts

        for i, part in enumerate(parts):
            child_node_path = "/".join(parts[:i+1])
            parent_node_path = "/".join(parts[:i]) if i > 0 else root_name

            is_folder = ('.' not in part)

            if is_folder:
                dot.node(child_node_path, label=part + "/", shape='rect', style='filled',
                         fillcolor='#F5F5F5', fontname='Arial-Bold', color='#CCCCCC')
            else:
                dot.node(child_node_path, label=part, fontcolor='#333333')

            edge_key = (parent_node_path, child_node_path)

            if edge_key not in added_edges:
                # Avec polyline, on peut enlever les contraintes strictes headport/tailport
                # pour laisser le moteur trouver le chemin le plus stable,
                # ou garder des contraintes légères.
                if parent_node_path == root_name and i == 0:
                    dot.edge(root_name, child_node_path)
                elif i > 0:
                    dot.edge(parent_node_path, child_node_path)

                added_edges.add(edge_key)

    try:
        dot.render(output_filename, view=False, cleanup=True)
        print(f"Graphique généré avec succès : {output_filename}.png")
    except graphviz.backend.ExecutableNotFound:
        print("Erreur : Graphviz non trouvé.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")


if __name__ == "__main__":
    create_file_tree_graph(file_tree_text)
