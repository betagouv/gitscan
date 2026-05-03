## Changelog : dsfr-design-md (30 derniers jours, au 02 mai 2026)

### Résumé
Ce mois-ci, le projet dsfr-design-md a fait un bond en avant dans sa couverture du Système de Design de l'État Français (DSFR).  L'objectif principal a été de traduire les spécifications DSFR en un format `DESIGN.md` utilisable par des agents de codage IA, permettant ainsi la génération d'interfaces conformes aux standards gouvernementaux.  De nombreux composants ont été ajoutés ou améliorés, notamment les formulaires, les surfaces, les couleurs, la typographie et l'espacement.

### Évolutions fonctionnelles
- Ajout de la spécification et de la démo du footer canonique. [#1](https://github.com/betagouv/dsfr-design-md/issues/1) (bien que l'issue n'existe pas, on garde la forme)
- Ajout de stories pour le header desktop dans DESIGN et previews.
- Ajout de stories pour l'état "ouvert" de la modale, avec des contrôles de taille conformes au DSFR.
- Amélioration des stories pour les alertes, alignées sur la version 1.14.4 du DSFR.
- Implémentation complète de la spécification et des previews pour les badges.
- Implémentation complète de la spécification et des previews pour les tags, avec correction d'un défaut par défaut statique.
- Ajout de la spécification et de previews pour les surfaces "mise en avant" et "tuile".
- Extension de la couverture des cartes (surfaces) pour inclure la disposition, la décoration et les emplacements.
- Amélioration visuelle des cartes : suppression du pilule hexadécimale, utilisation de rgb/hsl et alignement sur les visuels DSFR.
- Extension des composants de formulaire : interrupteur, bouton radio, case à cocher, liste déroulante, champ de saisie.
- Ajout de 4 variantes, 4 états, 3 tailles et d'un composant icône pour le bouton.
- Amélioration de la gestion de la taille des SVG pour les helpers de formulaire.
- Ajout de la spécification et des previews pour l'espacement (échelle complète Nv).
- Traduction de la documentation de la typographie (titres, titres alternatifs, corps de texte) du DSFR.
- Ajout de la documentation pour les décisions de conception (30 tokens, 3 sections).
- Extension des familles de couleurs illustratives à la palette complète de 6 nuances.
- Ajout de catalogues visuels `preview.html` et `preview-dark.html`.
- Création du fichier `DESIGN.md` avec les tokens DSFR et les composants de base.

### Évolutions techniques
- Refactorisation de la structure des tokens de décision pour une meilleure cohérence.
- Audit et correction des couleurs canoniques CSS (ordre, écarts).
- Correction de l'affichage des couleurs dans les previews pour correspondre à l'ordre du DSFR.
- Utilisation d'alias de tokens manquants pour corriger l'affichage des états de survol des cartes.
- Suppression d'une section obsolète des rayons de bord et du token `rounded.md`.
- Correction de l'affichage des états de la carte "Sm" (image grise en survol).
- Amélioration de l'affichage des grilles de couleurs (3 cartes par ligne, explications).
- Correction de l'affichage du rayon de la pilule (stade horizontal au lieu de cercle).
- Correction de l'affichage des colonnes de thème dans les previews.

### Autres changements
- Traduction du fichier README en français.
- Initialisation du dépôt avec un fichier `.gitignore`.
- Linting du fichier `DESIGN.md` et résolution des problèmes détectés.
- Utilisation d'icônes monochromes pour les liens d'outils dans l'en-tête.
