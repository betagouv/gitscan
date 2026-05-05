## Changelog : dsfr-design-md (30 derniers jours, au 03 mai 2026)

### Résumé
Ce mois-ci, le projet a connu une avancée significative dans la formalisation du Système de Design de l'État Français au format `DESIGN.md`. L'objectif est de permettre aux agents de codage IA de générer des interfaces utilisateur conformes aux standards gouvernementaux.  Les efforts se sont concentrés sur l'ajout de composants, l'amélioration de la couverture des spécifications DSFR, et la création d'outils de prévisualisation pour faciliter l'adoption et la validation du design system.

### Évolutions fonctionnelles
- Ajout d'une démo et d'une couverture de spécification pour le pied de page (footer) [#1234](https://github.com/betagouv/dsfr-design-md/issues/1234).
- Implémentation des stories pour l'en-tête de bureau (header) dans DESIGN et les prévisualisations.
- Ajout de stories pour les états ouverts des modales avec des contrôles de taille conformes au DSFR.
- Extension des stories pour les alertes et alignement de la référence DSFR sur la version 1.14.4.
- Implémentation complète des spécifications et des prévisualisations pour les badges.
- Ajout de la spécification complète et de 4 prévisualisations pour les tags, avec correction d'un défaut par défaut statique.
- Implémentation complète des spécifications et de 2 prévisualisations pour la mise en avant (surfaces).
- Implémentation complète des spécifications et de 5 prévisualisations pour les tuiles (surfaces).
- Extension des cartes (surfaces) pour couvrir les axes de mise en page, de décoration et d'emplacements.
- Correction de problèmes de visibilité du survol des cartes (surfaces).
- Extension des cartes (surfaces) pour couvrir les 4 tailles de stories.
- Extension des interrupteurs (forms) pour couvrir toutes les stories DSFR.
- Extension des boutons radio (forms) pour refléter les cas à cocher et les boutons radio enrichis.
- Amélioration du dimensionnement des SVG d'aide pour s'appliquer à tous les champs, pas seulement aux champs de formulaire.
- Restructuration des groupes (forms) et extension du champ de saisie.
- Extension de la liste déroulante (forms) pour inclure les états et la variante d'aide.
- Correction de la stratégie d'entrée de date (forms) pour refléter la stratégie canonique du DSFR.
- Extension des boutons (button) pour couvrir 4 variantes, 4 états, 3 tailles et une composition d'icônes.
- Mise à jour de la typographie pour refléter la documentation DSFR sur les titres, titres alternatifs et corps de texte.
- Implémentation complète des tokens d'option interactifs du DSFR.

### Évolutions techniques
- Refactorisation de la structure des tokens de couleur pour une meilleure cohérence et génération automatique.
- Audit et correction de l'ordre et des lacunes des couleurs du système (CSS canonique).
- Audit et correction de la palette de gris (CSS canonique).
- Création de catalogues visuels `preview.html` et `preview-dark.html`.
- Initialisation du projet avec un fichier `.gitignore`.
- Ajout d'un fichier `DESIGN.md` avec les tokens DSFR et les composants de base.
- Correction de l'affichage des couleurs dans les prévisualisations pour correspondre aux visuels DSFR.
- Amélioration de la disposition de la grille de couleurs pour correspondre à la documentation DSFR.

### Autres changements
- Traduction du fichier README en français.
- Ajout d'une description du projet et des avertissements concernant l'utilisation du DSFR dans le fichier README.
- Suppression de la section de prévisualisation des rayons de bord (shapes) et du token arrondi obsolète.
- Amélioration de l'affichage des décisions (decisions) pour ne montrer que la colonne de thème pertinente par fichier de prévisualisation.
- Implémentation de la documentation DSFR pour les décisions (30 tokens, 3 sections).
- Extension des familles d'accent illustratif de couleurs à la palette complète de 6 nuances.
- Correction de l'affichage des pilules de rayon dans les prévisualisations.
- Correction de l'affichage des états dans les prévisualisations.
