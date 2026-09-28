## Changelog : approbiom (30 derniers jours, au 25 septembre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec le développement d'un nouvel outil d'importation automatisée des données BCIB/BCIAT, simplifiant grandement la transformation de fichiers Excel complexes en données exploitables. Les capacités de visualisation cartographique ont été enrichies et l'interface utilisateur a été optimisée pour offrir une expérience plus fluide et compacte.

### Évolutions fonctionnelles
- **Importation de données (BCIB/BCIAT) :**
  - Mise en place d'un nouveau système d'importation pour les fichiers BCIB/BCIAT [#20](https://github.com/betagouv/approbiom/pull/20).
  - Amélioration de la robustesse de l'import : gestion des noms de feuilles non standards, détection automatique des départements et nettoyage des données de provenance [#19](https://github.com/betagouv/approbiom/pull/19).
  - Ajout de contrôles de validation pour vérifier la structure des fichiers et la cohérence des données après transformation [#22](https://github.com/betagouv/approbiom/pull/22).
  - Enrichissement des données exportées (ajout de champs tels que le PCI ou les certifications fournisseurs).
- **Cartographie et Visualisation :**
  - Amélioration de la carte de provenance : l'opacité des zones (polygones) varie désormais proportionnellement au tonnage.
  - Intégration du fond de carte "Plan IGN".
- **Interface Utilisateur (UI) :**
  - Ajout d'un filtre par statut de plan.
  - Optimisation de l'affichage pour une interface plus compacte et lisible.
  - Ajout d'une fonctionnalité permettant de copier l'URL des widgets directement depuis la page d'accueil.

### Évolutions techniques
- **Refactoring et Architecture :**
  - Réorganisation de la structure des composants React (création d'un dossier `hooks` et centralisation des composants).
  - Simplification du processus d'importation par la suppression de la logique Python au profit de solutions plus intégrées.
  - Renommage du référentiel géographique (`localization` devient `refrentiel-geo`).
- **Infrastructure et CI/CD :**
  - Correction et optimisation des pipelines de déploiement continu (CI/CD).
  - Nettoyage de l'infrastructure liée à Grist.

### Autres changements
- **Documentation :** Mise à jour du guide de développement et des templates ADR.
- **Maintenance :** Nettoyage du dépôt avec la suppression de plusieurs dossiers obsolètes (`script/import`, `insee`).
