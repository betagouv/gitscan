## Changelog : recommandations-collaboratives (30 derniers jours, au 6 novembre 2026)

### Résumé
Les évolutions de ce mois se concentrent sur l'amélioration de l'expérience utilisateur, notamment via une gestion plus intuitive des formulaires et des fichiers, ainsi que sur la robustesse technique du projet. L'outil est désormais plus fluide grâce à une meilleure gestion des erreurs et des indicateurs visuels, tout en renforçant sa sécurité et ses performances par la localisation de services tiers auparavant dépendants de CDN externes.

### Évolutions fonctionnelles
- **Gestion documentaire** : Ajout de la prévisualisation des fichiers et de la possibilité de les ouvrir dans un nouvel onglet.
- **Expérience utilisateur & Formulaires** :
    - Amélioration de la clarté des formulaires avec l'ajout d'indicateurs visuels pour les champs obligatoires [#2552](https://github.com/betagouv/recommandations-collaboratives/pull/2552).
    - Optimisation de la gestion des erreurs de saisie (validation des mots de passe, formulaires de conseiller et d'onboarding).
    - Ajout d'indicateurs de chargement lors de l'envoi de messages pour améliorer le retour utilisateur.
    - Correction de la gestion des ressources liées aux tâches.
- **Gestion des utilisateurs (CRM)** : Amélioration de la visibilité des membres d'une organisation (ajout de badges pour les conseillers, tri des comptes supprimés et comptage des comptes actifs uniquement).
- **Adaptation au mode embarqué** : Simplification de l'interface en masquant certains champs (contact, fichiers) lorsque l'outil est utilisé en mode intégré [#2513](https://github.com/betagouv/recommandations-collaboratives/pull/2513).
- **Cartographie** : Ajout d'un nouveau champ de mapping pour les coordonnées GPS.

### Évolutions techniques
- **Architecture & Plugins** : Mise en place d'un système de "hooks" permettant d'implémenter des filtres de périmètre via des plugins [#2480](https://github.com/betagouv/recommandations-collaboratives/pull/2480).
- **Gestion des erreurs** : Implémentation de pages d'erreur personnalisées (404 et 500) pour une navigation plus cohérente [#2177](https://github.com/betagouv/recommandations-collaboratives/pull/2177).
- **Optimisation et Sécurité** : Migration de services tiers (Leaflet, Sentry, Crisp) du format CDN vers une gestion locale via les dépendances du projet pour améliorer la performance et la sécurité [#2409](https://github.com/betagouv/recommandations-collaboratives/pull/2409), [#2506](https://github.com/betagouv/recommandations-collaboratives/pull/2506), [#2507](https://github.com/betagouv/recommandations-collaboratives/pull/2507).
- **API & Backend** : Correction de la gestion des erreurs 404 sur l'API et sécurisation des accès aux endpoints de suppression de tâches.

### Autres changements
- **Documentation** : Mise à jour de la documentation technique concernant le fonctionnement du module de données (DS) et les conditions des challenges.
