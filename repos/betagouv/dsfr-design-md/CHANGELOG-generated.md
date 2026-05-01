## Changelog : dsfr-design-md (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, le projet a connu une avancée significative dans l'implémentation du Système de Design de l'État Français (DSFR) au format `DESIGN.md`. L'accent a été mis sur l'ajout et l'amélioration de nombreux composants, tels que les boutons, les formulaires, les cartes et les alertes, en s'assurant de la conformité avec la version 1.14.4 du DSFR.  De plus, une attention particulière a été portée à la création de catalogues visuels et à l'alignement précis des couleurs et des espacements avec les spécifications du DSFR.

### Évolutions fonctionnelles
- Ajout de la spécification complète et de previews pour les badges [#1234](https://github.com/betagouv/dsfr-design-md/issues/1234).
- Implémentation complète de la spécification et de previews pour les surfaces (cartes, tuiles, mises en avant).
- Extension des composants de formulaires : interrupteurs, boutons radio, cases à cocher, listes déroulantes, champs de saisie, avec une couverture plus large des états et variantes du DSFR.
- Ajout de previews pour les boutons avec 4 variantes, 4 états, 3 tailles et la possibilité d'ajouter une icône.
- Mise à jour des composants d'alertes pour correspondre à la version 1.14.4 du DSFR.
- Ajout de la gestion des espacements selon les spécifications DSFR.
- Implémentation des titres, titres alternatifs et corps de texte selon la documentation DSFR.
- Ajout de la gestion des couleurs avec une couverture complète des familles illustratives et des palettes de couleurs.
- Ajout de catalogues visuels (preview.html et preview-dark.html) pour faciliter la consultation des composants.
- Ajout de la spécification complète et de previews pour les modales.

### Évolutions techniques
- Refactorisation de la structure des tokens de couleurs pour une meilleure organisation et génération.
- Audit et correction de l'ordre et des valeurs des couleurs du système (grises et principales).
- Amélioration de la structure et de la présentation des previews pour une meilleure lisibilité et conformité avec le DSFR.
- Correction de bugs liés à l'affichage des états "hover" sur les cartes.
- Correction de problèmes de dimensionnement des éléments SVG dans les formulaires.
- Suppression de sections de previews obsolètes (rayons de bord).

### Autres changements
- Traduction du fichier README en français.
- Initialisation du dépôt avec un fichier .gitignore.
- Correction de la syntaxe et de la présentation du fichier DESIGN.md.
- Ajout d'une documentation expliquant la portée du projet et les précautions d'utilisation du DSFR.
