## Changelog : slack2tchap (30 derniers jours, au 17 septembre 2026)

### Résumé
Le projet franchit une étape majeure avec le lancement de sa première version stable (V1.0.0). Cette phase initiale a permis d'instaurer les bases de la gestion des utilisateurs et d'introduire une architecture simplifiée ("stateless") permettant un déploiement plus facile et flexible.

### Évolutions fonctionnelles
- **Gestion des utilisateurs** : ajout des fonctionnalités de création et de gestion des comptes utilisateurs.
- **Manipulation des données** : implémentation des méthodes CRUD pour la gestion des ressources.

### Évolutions techniques
- **Architecture** : 
    - Introduction d'un mode "stateless" (sans état) pour optimiser l'utilisation de la passerelle [#1](https://github.com/betagouv/slack2tchap/pull/1).
    - Restructuration du projet en trois parties distinctes pour une meilleure modularité.
- **Déploiement et CI/CD** :
    - Ajout du support de déploiement sur Scalingo pour la version stateless [#2](https://github.com/betagouv/slack2tchap/pull/2).
    - Corrections de la chaîne d'intégration continue (CI) et des analyses de code.
- **Compatibilité** : mise à jour des interfaces de webhooks pour assurer une parfaite correspondance avec les standards de Slack [#3](https://github.com/betagouv/slack2tchap/pull/3).

### Autres changements
- Passage à la version 1.0.0.
