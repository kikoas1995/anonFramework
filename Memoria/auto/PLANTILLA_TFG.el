(TeX-add-style-hook
 "PLANTILLA_TFG"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("book" "a4paper" "11pt" "twoside" "openright" "titlepage")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("geometry" "a4paper" "left=1in" "right=1in" "top=0.6in") ("inputenc" "utf8") ("fontenc" "T1") ("babel" "english" "spanish") ("xy" "all") ("xcolor" "table" "xcdraw")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "portada"
    "primera_pag"
    "resumen"
    "agradecimientos"
    "cap_intro"
    "cap_estadodelarte"
    "cap_sistemadesarrollado"
    "cap_experimentos"
    "cap_conclusiones"
    "glosario"
    "anexo_manualuso"
    "anexo_manualprogramador"
    "book"
    "bk11"
    "geometry"
    "inputenc"
    "fontenc"
    "amsmath"
    "amssymb"
    "float"
    "natbib"
    "changepage"
    "babel"
    "graphicx"
    "psfrag"
    "quotchap"
    "epsfig"
    "xy"
    "caption"
    "subcaption"
    "xcolor"
    "makeidx"
    "ifthen"
    "multicolpar"
    "multicol"
    "multirow"
    "url"
    "marvosym"
    "fancybox"
    "hyperref"
    "fancyhdr")
   (TeX-add-symbols
    '("commentswho" 2)
    '("doubtwho" 2)
    '("modifiedsout" 1)
    '("modified" 1)
    '("commented" 1)
    '("comments" 1)
    '("todo" 1)
    '("NOcaptionFigure" 2)
    '("captionFigure" 2)
    '("lsection" 1)
    "titulo"
    "autor"
    "director"
    "tutor"
    "vocal"
    "vocalsup"
    "presidente"
    "presidentesup"
    "fecha"
    "carrera")
   (LaTeX-add-labels
    "#2")
   (LaTeX-add-bibliographies
    "bibliografia")
   (LaTeX-add-lengths
    "salto"
    "resalto")
   (LaTeX-add-xcolor-definecolors
    "dgreen"))
 :latex)

