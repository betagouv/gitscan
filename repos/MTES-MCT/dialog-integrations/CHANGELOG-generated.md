## Changelog : dialog-integrations (30 derniers jours, au 31 octobre 2026)

### Résumé
Ce mois a été marqué par une refonte majeure du moteur de validation des données et une restructuration profonde de l'architecture du projet. Ces changements visent à rendre l'intégration des arrêtés de circulation plus robuste, plus modulaire et plus précise, notamment grâce à un nouveau système de règles de contrôle. L'intégration des données de Paris a également été significativement améliorée.

### Évolutions fonctionnelles
- **Amélioration de l'intégration de Paris** : Mise en place de la version "Eudonet Paris v0" et corrections sur la recette de l'intégration [#37](https://github.com/MTES-MCT/dialog-integrations/issues/37) [#43](https://github.com/MTES-MCT/dialog-integrations/issues/43).
- **Nouveaux connecteurs de données** : Capacité de lecture unifiée pour les exports Opendatasoft et les couches ArcGIS.
- **Nouvelles règles de validation et de filtrage** :
    - Exclusion automatique des restrictions incomplètes (ex: sens uniques sans direction précisée).
    - Filtrage des données hors périmètre (ex: tonnages supérieurs à 44t, zones exclusivement réservées aux piétons ou cyclistes).
    - Gestion intelligente des réglementations temporaires (exclusion des dates expirées, des dates manquantes ou des durées anormalement longues).
- **Amélioration de l'intégration de Lyon** : Meilleure gestion des qualificatifs en texte libre et publication des vitesses en zones à trafic limité (ZTL).

### Évolutions techniques
- **Refonte du moteur de règles** : Transition d'un système de filtres vers un système de validateurs plus puissant avec une nouvelle architecture dédiée [#41](https://github.com/MTES-MCT/dialog-integrations/issues/41).
- **Modularisation du pipeline** : Restructuration de l'organisation du code pour séparer les étapes d'exécution (un fichier par étape) [#40](https://github.com/MTES-MCT/dialog-integrations/issues/40) et déplacement du moteur hors du répertoire des intégrations pour une meilleure séparation des responsabilités [#39](https://github.com/MTES-MCT/dialog-integrations/issues/39).
- **Sécurisation de la synchronisation** : Mise en place d'une synchronisation nocturne plus fiable incluant le gel par source et des contrôles communs [#38](https://github.com/MTES-MCT/dialog-integrations/issues/38).
- **Optimisation des transformations** : Mutualisation des fonctions de traitement (troncation de titres, gestion des périodes et des types de véhicules).

### Autres changements
- **Nettoyage du code** : Suppression de composants obsolètes (helpers DTO, anciens chemins de snapshots, modes de fichiers locaux) et simplification des messages de logs.
- **Amélioration de la documentation et des commentaires** : Clarification des commentaires de règles (utilisation de termes explicites au lieu de numéros internes) et standardisation de la terminologie (modèle canonique).
- **Maintenance CI/CD** : Retrait de l'intégration de Rennes dans le pipeline de tests continu.
