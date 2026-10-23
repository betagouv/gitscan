## Changelog : pitchou (30 derniers jours, au 21 octobre 2026)

### Résumé
Ce mois-ci, Pitchou a connu une évolution majeure axée sur l'enrichissement des données et la modernisation de son infrastructure. Les utilisateurs bénéficient de nouvelles capacités de gestion (personnes impliquées, porteurs de projet) et d'outils d'exportation de données plus complets. En parallèle, une mise à jour profonde des technologies de base a été effectuée pour garantir la performance et la pérennité de l'application.

### Évolutions fonctionnelles
- **Nouvelles capacités de gestion** :
    - Ajout de la gestion des personnes impliquées dans un dossier.
    - Structuration et gestion des porteurs de projet en base de données [#709].
    - Gestion des décisions requises, de l'UICN et possibilité de supprimer des pièces jointes [#705].
- **Export et données** :
    - Possibilité d'exporter les dossiers filtrés aux formats CSV et ODS [#710].
- **Améliorations de l'interface (UX/UI)** :
    - Optimisation de l'affichage pour rendre la saisie d'espèces responsive (adaptée aux mobiles/tablettes) [#706].
    - Ajustements ergonomiques des onglets de dossiers, de la pagination et des boutons d'action [#707].
- **Corrections** :
    - Clarification des imports de prescriptions et des conversions de surfaces [#714].
    - Correction d'une coquille sur les libellés de "perturbation" [#713].
    - Suppression des notifications redondantes concernant les champs obligatoires [#711].

### Évolutions techniques
- **Montée de version majeure des technologies de base** :
    - Passage à TypeScript 6 [#721].
    - Migration vers SvelteKit 3 [#724].
    - Mise à jour de Vitest et des tests de navigateur vers la v5 [#723].
- **Optimisation de l'infrastructure et du stockage** :
    - Implémentation de l'upload direct vers S3 pour les fichiers [#704].
- **Modernisation de la chaîne de développement (DevEx)** :
    - Remplacement de Prettier par oxfmt [#726] et ajout d'oxlint [#717] pour un formatage et un linting plus rapides.
    - Mise à jour des dépendances GitHub Actions [#725].
    - Ajout d'une option de capture locale d'e-mails pour le développement [#715].
- **Maintenance et nettoyage** :
    - Mise à jour de l'ensemble des dépendances compatibles [#720] et mise à jour de `json-schema-to-typescript` [#722].
    - Nettoyage du projet par la suppression de dépendances mineures [#719].
