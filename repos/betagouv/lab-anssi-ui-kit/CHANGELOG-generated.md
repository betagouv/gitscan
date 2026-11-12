## Changelog : lab-anssi-ui-kit (30 derniers jours, au 09/11/2026)

### Résumé
Ce mois a été marqué par une étape majeure avec le passage à la version 2.0.0 du kit. Les utilisateurs bénéficient de nouveaux composants essentiels, notamment pour l'import de fichiers et la sélection complexe, ainsi que d'améliorations sur les filtres de catalogue. En coulisses, une refonte technique importante a été réalisée pour stabiliser l'utilisation des composants et moderniser l'environnement de développement et de publication.

### Évolutions fonctionnelles
- **Nouveaux composants** :
    - Ajout du composant `DsfrUpload` pour la gestion des téléchargements.
    - Ajout du composant `Combobox` pour des sélections enrichies.
- **Améliorations des composants existants** :
    - `DsfrCombobox` : ajout d'une largeur minimale personnalisable, amélioration du filtrage par légende de groupe et optimisation de la logique du bouton "Tout sélectionner".
    - `FiltresCatalogue` : ajout d'une nouvelle variation de liens et affinement des styles.
- **Corrections d'expérience utilisateur** :
    - `DsfrCombobox` : simplification de la logique d'ouverture/fermeture et suppression d'animations de collapse.
    - `DsfrTabs` : correction du fonctionnement de la propriété `activeTabIndex`.
    - `DsfrTagsGroup` et `DsfrRadiosGroup` : corrections de la gestion des clés et des valeurs par défaut.

### Évolutions techniques
- **Architecture et stabilité** :
    - Refonte de l'enregistrement des Web Components pour le rendre idempotent, évitant ainsi les doubles enregistrements des composants Lab ANSSI et DSFR.
    - Unification de l'extraction des métadonnées pour les Web Components.
    - Correction des cibles d'imports DSFR pour les composants `Card`, `User` et `Dropdown`.
- **Infrastructure et CI/CD** :
    - Modernisation de la chaîne de production avec le passage à Node.js v26 et pnpm v12.
    - Renforcement de la qualité logicielle via l'ajout de vérifications automatiques des types Svelte et TypeScript dans la CI.
    - Centralisation de la configuration de publication dans `publishConfig`.
- **Tests** :
    - Ajout de tests pour vérifier l'enregistrement idempotent et le bon fonctionnement du *tree-shaking*.
