## Changelog : monitorfish (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, monitorfish a bénéficié d'améliorations significatives en termes de cartographie, de gestion des signalements et de correction de bugs. Des optimisations ont été apportées à l'affichage des données sur la carte, à la gestion des alertes et à la stabilité de l'application. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la performance du système.

### Évolutions fonctionnelles
- **Cartographie :**
    - Ajout de la ZEE SHOM et mise à jour de la ZEE monde pour une meilleure précision géographique. [#4922]
    - Correction de l'affichage des coordonnées lors de la modification d'un signalement.
    - Amélioration de la gestion des projections cartographiques pour éviter les problèmes d'affichage en dehors de la projection MERCATOR. [#4920]
    - Possibilité de supprimer automatiquement les anciens signalements IUU après 24 heures.
- **Signalements :**
    - Amélioration de l'interface utilisateur pour la création et la gestion des signalements. [#4924]
    - Correction de l'affichage des signalements sur la carte après leur création. [#4919]
    - Ajout de la possibilité de filtrer les navires par équipement VMS. [#4914]
    - Ajout de la possibilité de sélectionner la nationalité d'un navire inconnu. [#4993, #4989]
    - Ajout de trois nouvelles catégories d'infractions (NATINFs). [#4975]
- **Alertes :**
    - Correction d'un bug où deux alertes étaient affichées au lieu d'une seule. [#5028]
    - Ajout d'un bouton pour supprimer les alertes de position. [#5027]
- **Gestion des infractions :**
    - Possibilité de supprimer automatiquement les signalements IUU après une période définie.

### Évolutions techniques
- **Refactoring :**
    - Refactoring du composant carte avec des hooks pour une meilleure maintenabilité. [#5030]
    - Refactoring de la base de la carte avec des hooks.
- **Mises à jour de dépendances :**
    - Mise à jour de OpenLayers. [#5021]
    - Mises à jour de plusieurs dépendances frontend (ora, basic-ftp, vite, rollup, lodash, etc.).
    - Mises à jour de dépendances backend (testcontainers, cryptography, weasyprint, etc.).
- **CI/CD :**
    - Mise à jour de l'action Docker pour le build et le push. [#4957]
    - Mise à jour de l'action Docker pour la connexion. [#4958]
- **Tests :**
    - Correction de problèmes de race condition dans les fixtures de base de données des tests de pipeline. [#5023, #88a27ecf]
    - Amélioration de la stabilité des tests Cypress.
- **Architecture :**
    - Correction d'un bug lié à la gestion des time zones dans le parser ERS. [#4946]
    - Ajout de gestion des éléments de risque (zones fermées, VMS, PNO).

### Autres changements
- Correction de bugs divers liés à l'interface utilisateur et à l'affichage des données.
- Amélioration des performances de certaines requêtes SQL.
- Mise à jour de la documentation.
- Suppression de code mort.
- Ajout de tests unitaires et d'intégration.
- Configuration de dépendabot pour exclure Prefect des mises à jour automatiques.
- Correction de problèmes de linting.
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
- Correction de problèmes de typage.
- Ajout de feature flags.
- Mise à jour de la liste des pays.
- Correction de problèmes de marge blanche dans l'interface utilisateur.
