## Changelog : dsfr-design-md (30 derniers jours, au 26 avril 2026)

### Résumé
Ce changelog fait état de la création et de la mise en place initiale du système de design DSFR au format `DESIGN.md`.  Le projet vise à fournir aux agents de codage IA un moyen de générer des interfaces utilisateur conformes aux standards gouvernementaux français.  Les travaux récents se concentrent sur la traduction en français, la création d'un catalogue visuel de prévisualisation et l'alignement précis sur les spécifications du DSFR.

### Évolutions fonctionnelles
- Ajout d'un catalogue visuel de prévisualisation (mode clair et sombre) pour faciliter l'exploration des composants et des couleurs du DSFR.
- Implémentation complète de la couverture des tokens interactifs du DSFR.
- Visualisation des couleurs du DSFR alignée sur la documentation officielle, avec une présentation en grille à 3 cartes par ligne et des explications.
- Amélioration de la présentation des cartes, notamment en adoptant les visuels DSFR (contenu imbriqué, suppression des pastilles hexagonales, utilisation de couleurs RGB/HSL).
- Correction de l'affichage du rayon des pastilles pour correspondre à un stade horizontal plutôt qu'un cercle.
- Ajustement de la largeur des cartes et de la disposition de la grille pour un affichage optimal du contenu.

### Évolutions techniques
- Initialisation du dépôt avec un fichier `.gitignore`.
- Création du fichier `DESIGN.md` contenant les tokens et composants principaux du DSFR.
- Correction de l'audit CSS canonique de la palette de gris (drift, gaps, états).
- Mise à jour pour correspondre à l'ordre des couleurs du DSFR et verrouillage de 3 cartes par ligne.

### Autres changements
- Traduction du fichier `README` en français pour une meilleure accessibilité.
- Nettoyage et linting du fichier `DESIGN.md` pour assurer la conformité aux standards de qualité du code.
- Ajout d'un fichier `README` expliquant la portée du projet et les mises en garde concernant l'utilisation du DSFR.
