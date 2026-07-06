## Changelog : portail-rse (30 derniers jours, au 03 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration significative de la fonctionnalité d'exportation des données VSME au format PowerPoint (pptx). De nombreuses corrections et refactorisations ont été apportées pour assurer un rendu précis et complet des informations, avec une attention particulière portée à la gestion des indicateurs, des tableaux et des données variables. Une fonctionnalité permettant aux utilisateurs de réinitialiser un indicateur VSME a également été ajoutée.

### Évolutions fonctionnelles
- Ajout de la possibilité pour les utilisateurs de réinitialiser un indicateur VSME. [#2a12381](https://github.com/betagouv/portail-rse/commit/2a12381)
- Amélioration de l'exportation au format PPTX :
    - Ajout de nombreux indicateurs et données à l'export PPTX.
    - Gestion améliorée des tableaux, y compris ceux avec des lignes variables.
    - Prise en charge de différents types de données (nombres entiers, booléens, etc.).
    - Suppression des diapositives non pertinentes en fonction de la pertinence des indicateurs.
    - Ajout d'une diapositive de couverture avec les informations de l'entreprise.
    - Centrage vertical du contenu des cellules dans les tableaux.
    - Gestion des unités d'affichage.
    - Amélioration de l'affichage de la couverture.
    - Ajout de liens de téléchargement pour les rapports PPTX.
- Ajout de logs pour les requêtes d'export xlsx et pptx pour faciliter le débogage. [260e6ff](https://github.com/betagouv/portail-rse/commit/260e6ff)

### Évolutions techniques
- Refactorisation importante du code d'exportation PPTX pour améliorer la lisibilité et la maintenabilité.
- Simplification des fonctions d'export PPTX.
- Renommage de variables et de fonctions pour une meilleure clarté.
- Suppression de code inutile et de conditions redondantes.
- Adaptation du modèle PPTX pour prendre en charge les nouvelles fonctionnalités.
- Déplacement de fichiers pour une meilleure organisation du projet.
- Correction de bugs liés à l'affichage des données dans les tableaux PPTX.
- Amélioration de la gestion des erreurs lors de l'exportation.

### Autres changements
- Mise à jour des dépendances : `cryptography`, `aiohttp`, `pyjwt`.
- Documentation : Complétion du diagramme overview. [46d3b7e](https://github.com/betagouv/portail-rse/commit/46d3b7e)
- Amélioration des boutons de téléchargement.
- Correction de l'alignement d'une image de fond sur une diapositive PPTX.
