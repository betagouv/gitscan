## Changelog : monitorfish (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur et à la gestion des données, notamment au niveau des contrôles, des signalements, des groupes de navires et des formulaires e-ISR. Des corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de l'application. Des optimisations de performance ont également été réalisées, en particulier pour les requêtes de données AIS.

### Évolutions fonctionnelles
- **Contrôles :**
    - Affichage des groupes prioritaires et des signalements de la marée sous la recherche navire.
    - Amélioration de l'affichage des tags de groupes et de signalements dans les formulaires de contrôle.
    - Correction de bugs liés à l'affichage des groupes de navires et des contrôles.
    - Ajout de la possibilité de suivre les contrôles faits sur des cibles prioritaires.
- **Signalements INN :**
    - Ajout d'un filtre "navire sans fiche" dans la liste des signalements "Outre-mer OP".
    - Amélioration du comportement du bouton "centrer sur la carte" dans la vue liste des signalements.
    - Correction de bugs liés à l'affichage et à la gestion des signalements.
- **Groupes de navires :**
    - Ajout d'une case "cibles prioritaires" au formulaire de création et de modification d'un groupe.
    - Possibilité de masquer l'affichage des groupes prioritaires pour les unités externes.
    - Amélioration de l'export CSV des groupes de navires.
- **Formulaires e-ISR :**
    - Mise à jour des champs facultatifs et des règles d'applicabilité.
    - Ajout des champs armateur.
    - Correction de bugs liés à l'affichage et à la logique des champs.
- **Autres :**
    - Correction de bugs liés à l'archivage automatique des alertes de position.
    - Amélioration de la gestion des poids des espèces dans les formulaires.
    - Correction de bugs liés aux missions, au rafraîchissement des préavis et aux avaries.

### Évolutions techniques
- **Performance :** Optimisation de la requête de dernières positions AIS pour améliorer les performances.
- **Linting :** Migration vers un linter hybride (OxLint) et mise à jour des règles ESLint pour améliorer la qualité du code.
- **Dépendances :** Mise à jour de plusieurs dépendances frontend (postcss).
- **Tests :** Ajout et amélioration des tests Cypress pour couvrir les nouvelles fonctionnalités et les corrections de bugs.
- **Architecture :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- **Scraper Legipeche :** Correction du scraper pour gérer les pages non visitées.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés.
- Corrections de commentaires obsolètes et ajout d'informations sur le box-sizing dans le fichier CONTRIBUTING.md.
- Suppression de fichiers de configuration inutiles (ktlint baseline).
- Amélioration des messages de progression dans le hook pré-push.
- Correction de divers bugs et améliorations mineures de l'interface utilisateur.
