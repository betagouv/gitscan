## Changelog : envergo (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois a été marqué par un effort important sur la sécurisation de la plateforme (protection contre les failles XSS et renforcement des droits d'accès) et la modernisation de l'infrastructure de déploiement. Les performances ont été optimisées via de nouveaux mécanismes de cache et de préchargement de données, tandis que l'expérience utilisateur a été affinée, notamment sur la cartographie et l'affichage mobile.

### Évolutions fonctionnelles
- **Interface cartographique :** Amélioration de l'expérience utilisateur avec l'ajout d'infobulles sur la carte [#1232](https://github.com/MTES-MCT/envergo/pull/1232) et de nouveaux filtres par catégorie [#1231](https://github.com/MTES-MCT/envergo/pull/1231).
- **Expérience mobile :** Optimisation du style des filtres pour une meilleure utilisation sur petits écrans.
- **Identité visuelle :** Intégration du nouveau logo DN [#1233](https://github.com/MTES-MCT/envergo/pull/1233).
- **Simulations :** Évolutions apportées aux fonctionnalités de simulation (Nawalt) [#1243](https://github.com/MTES-MCT/envergo/pull/1243).
- **Corrections :** Résolution de problèmes lors de l'import des fichiers d'habitats [#1258](https://github.com/MTES-MCT/envergo/pull/1258).

### Évolutions techniques
- **Sécurité :** 
    - Correction de vulnérabilités XSS par l'échappement des données soumises par les utilisateurs [#1251](https://github.com/MTES-MCT/envergo/pull/1251).
    - Amélioration de l'API d'autorisation et gestion plus fine des accès [#1244](https://github.com/MTES-MCT/envergo/pull/1244).
    - Sécurisation de la base de données de statistiques [#1265](https://github.com/MTES-MCT/envergo/pull/1265).
- **Performance :** 
    - Optimisation des requêtes de données (HRU) [#1266](https://github.com/MTES-MCT/envergo/pull/1266).
    - Mise en place d'un cache pour les calculs de densité [#1238](https://github.com/MTES-MCT/envergo/pull/1238).
    - Implémentation du préchargement (prefetch) des zones.
- **Infrastructure & Déploiement :** 
    - Mise à jour majeure de la stack de déploiement (Scalingo) [#1252](https://github.com/MTES-MCT/envergo/pull/1252).
    - Migration vers un nouveau système de stockage pour les fichiers hébergés (S3) [#1253](https://github.com/MTES-MCT/envergo/pull/1253).
    - Mise à jour des dépendances système (GDAL) et de la version Node.js.
- **CI/CD & Données :** 
    - Ajout d'un contrôle automatique des migrations de base de données dans le pipeline CI pour éviter les erreurs de déploiement [#1259](https://github.com/MTES-MCT/envergo/pull/1259).
    - Automatisation du processus de synchronisation des données de production vers la base de statistiques.

### Autres changements
- **Documentation :** Mise à jour du README concernant les procédures d'anonymisation des données.
- **Maintenance :** Refactorisation de plusieurs modules pour améliorer la lisibilité et la maintenabilité du code.
