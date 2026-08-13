## Changelog : zero-logement-vacant (30 derniers jours, au 11 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes importantes pour améliorer la gestion opérationnelle et l'accessibilité. Les utilisateurs peuvent désormais gérer des documents directement dans les campagnes, enregistrer des campagnes à partir de groupes de logements et utiliser un nouveau statut "Ne pas contacter" pour les propriétaires. Un effort majeur a également été porté sur la mise en conformité avec les normes d'accessibilité (RGAA). En coulisses, une refonte profonde de la gestion de la base de données a été réalisée pour garantir plus de robustesse et de performance.

### Évolutions fonctionnelles
- **Gestion des campagnes**
  - Possibilité d'enregistrer une campagne directement depuis un groupe de logements [#1918](https://github.com/MTES-MCT/zero-logement-vacant/pull/1918).
  - Ajout de la gestion documentaire au sein des campagnes (téléchargement, liste et suppression de documents) [#1919](https://github.com/MTES-MCT/zero-logement-vacant/pull/1919).
  - Automatisation du changement de statut des logements en fonction de la date d'envoi prévue des campagnes.
  - Ajout d'avertissements lors du report d'une campagne déjà envoyée pour éviter les erreurs de manipulation.
- **Gestion des propriétaires**
  - Introduction d'un statut global "Ne pas contacter" au niveau du propriétaire [#1836](https://github.com/MTES-MCT/zero-logement-vacant/pull/1836).
  - Exclusion automatique des propriétaires marqués "Ne pas contacter" lors des exports de données de logements.
- **Cartographie et Visualisation**
  - Amélioration de la carte des logements avec une meilleure gestion des projections et de l'affichage des points.
  - Nouvelle gestion de la visibilité des périmètres : possibilité d'afficher les contours et de maintenir les périmètres exclus visibles (en rouge) [#1884](https://github.com/MTES-MCT/zero-logement-vacant/pull/1884).
- **Accessibilité (RGAA)**
  - Mise en conformité avec plusieurs critères d'accessibilité numérique : amélioration de la structure des documents, validation des erreurs de formulaires, gestion des rôles de navigation (landmarks) et ajout de légendes aux tableaux.
- **Analyses et Statistiques**
  - Correction des indicateurs de calcul pour les critères LOVAC et le comptage des logements.
  - Amélioration de la stabilité et de la fluidité de l'affichage des tableaux de bord d'analyse.

### Évolutions techniques
- **Base de données et Backend**
  - Migration massive de l'outil de requête SQL de Knex vers Kysely pour l'ensemble des dépôts (repositories) et la gestion des transactions, améliorant la sécurité du typage.
  - Refactorisation des points de terminaison (endpoints) de gestion des logements vers une structure unifiée et typée `/housings`.
  - Activation de la compression des réponses de l'API pour optimiser les temps de chargement [#1925](https://github.com/MTES-MCT/zero-logement-vacant/pull/1925).
- **Outils et Infrastructure**
  - Création d'un nouvel outil en ligne de commande (CLI) dédié à la planification et à l'application de réparations de données (ZLV repair harness).
  - Optimisation des pipelines de données (Dagster) pour le calcul et la classification de la localisation des propriétaires.
  - Amélioration de la CI/CD : exécution parallèle des tests Playwright et Cypress, et renforcement de la sécurité des secrets dans les environnements de revue.
- **Frontend**
  - Amélioration de la gestion de la pagination dans les tableaux de données.
  - Renforcement de la résilience de l'interface face aux erreurs de chargement de fichiers (gestion des "stale chunks" de Vite).

### Autres changements
- Mise à jour approfondie de la documentation technique, incluant les méthodologies de test RGAA et les plans de migration de la base de données.
- Nettoyage général du code et suppression de fonctions obsolètes.
