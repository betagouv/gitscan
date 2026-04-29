## Changelog : dsfr-design-md (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, le projet a fait un bond en avant significatif en intégrant une couverture complète des tokens DSFR (Design System de l'État Français) et en créant des catalogues visuels pour faciliter l'exploration et l'utilisation de ces éléments. L'objectif est de permettre aux agents de l'administration de générer des interfaces conformes aux standards gouvernementaux de manière plus efficace.

### Évolutions fonctionnelles
- **Intégration complète des tokens DSFR :** Couverture complète des tokens interactifs du DSFR.
- **Catalogues visuels :** Ajout de catalogues visuels `preview.html` et `preview-dark.html` pour une meilleure visualisation des couleurs et des composants.
- **Représentation des couleurs :** Amélioration de la représentation des couleurs, alignée sur la documentation DSFR, avec une présentation en grille à 3 cartes par ligne et des explications claires.
- **Espacement :** Implémentation de l'espacement tel que défini dans la documentation DSFR, incluant une échelle complète et des aperçus verticaux et horizontaux.
- **Typographie :** Intégration des styles de titres, titres alternatifs et corps de texte définis par le DSFR.
- **Cartes :** Adoption des visuels de cartes DSFR (contenu inséré, suppression des pilules hexagonales, utilisation de RGB/HSL).
- **Formes :** Correction de l'affichage des rayons de pilule, désormais représentés comme des stades horizontaux.

### Évolutions techniques
- **Restructuration des tokens de décision :** Refactorisation de la structure des tokens de décision pour une meilleure organisation et génération (~75 tokens).
- **Audit CSS :** Audits CSS approfondis des couleurs du système (ordre, espaces) et de la palette de gris (drift, espaces, états) pour garantir la conformité et la cohérence.
- **Amélioration de l'affichage des décisions :** Affichage uniquement de la colonne de thème pertinente dans les fichiers de prévisualisation.
- **Expansion des familles de couleurs :** Extension de 17 familles de couleurs illustratives à une palette complète de 6 nuances.

### Autres changements
- **Documentation :** Traduction du fichier README en français pour une meilleure accessibilité.
- **Initialisation du dépôt :** Initialisation du dépôt avec un fichier `.gitignore` et linting du fichier `DESIGN.md`.
- **Documentation du projet :** Ajout d'une documentation expliquant la portée du projet et les mises en garde concernant l'utilisation du DSFR.
