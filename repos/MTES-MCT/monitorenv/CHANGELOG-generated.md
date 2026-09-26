## Changelog : monitorenv (30 derniers jours, au 23 septembre 2026)

### Résumé
Ce mois-ci, les développements ont principalement porté sur l'amélioration des outils de gestion administrative (backoffice) et l'optimisation de l'expérience cartographique. Les utilisateurs bénéficieront d'une meilleure gestion des zones réglementaires, de nouvelles capacités de recherche (codes FAO) et d'une interface plus fluide et accessible. Les processus de récupération des données publiques ont également été renforcés pour garantir la fiabilité des informations affichées.

### Évolutions fonctionnelles
- **Administration et Backoffice** :
    - Mise en place de la première version du backoffice pour la gestion des zones réglementaires.
    - Ajout de la recherche par code FAO dans les étiquettes (tags).
    - Création d'une fonctionnalité d'importation d'utilisateurs basée sur le format CSV de Cerbere.
- **Cartographie et SIG** :
    - Amélioration de l'interaction sur la carte, notamment l'affichage des superpositions de zones pendant le dessin.
    - Optimisation de l'affichage des périodes de vigilance (affichage des jours de début et de fin pour les fréquences hebdomadaires).
- **Interface Utilisateur (UI/UX)** :
    - Amélioration de la navigation avec l'ajout d'un en-tête fixe (sticky header).
    - Optimisation de l'accessibilité (ajustement des contrastes de couleurs) et de la gestion du focus sur les éléments interactifs.
    - Corrections diverses sur le tableau de bord (tri des colonnes) et l'affichage des composants.
- **API et Données** :
    - Ajout de nouveaux endpoints pour la mise à jour des unités de ressources et l'intégration des contacts des unités de contrôle dans l'API publique des missions.

### Évolutions techniques
- **Optimisation de la cartographie (SIG)** :
    - Amélioration significative des performances de rendu des tuiles cartographiques via l'utilisation de `ST_asMVT` et la gestion du système de coordonnées 3857.
    - Optimisation des requêtes backend par l'intégration de la gestion de l'emprise (extent).
- **Pipelines de données** :
    - Mise à jour et fiabilisation des flux de données provenant d'Open Data et de data.gouv pour les zones réglementaires.
    - Ajout de logs de suivi pour les flux de données afin d'améliorer l'observabilité.
- **Infrastructure et API** :
    - Ajustements de l'infrastructure (ports de healthcheck, labels Portainer).
    - Amélioration de la robustesse de l'API (gestion des migrations de base de données, endpoints SSE et mapping JSON).
    - Optimisation de l'interface via la virtualisation des listes (code FAO) pour améliorer la fluidité.

### Autres changements
- **Configuration** : Ajout de la clé API Carto.
- **Nettoyage** : Suppression de messages d'avertissement inutiles et de paramètres de log obsolètes.
