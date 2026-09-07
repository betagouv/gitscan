## Changelog : recommandations-collaboratives (30 derniers jours, au 04/09/2026)

### Résumé
Cette période a été principalement consacrée au renforcement de la sécurité du logiciel et à l'optimisation de ses performances. Les outils d'administration (CRM) ont été améliorés pour offrir une meilleure visibilité sur les données, et la gestion des communications par email a été stabilisée pour garantir une expérience plus fiable.

### Évolutions fonctionnelles
- **Amélioration du CRM** : Refonte de la page d'administration du CRM [#2316](https://github.com/betagouv/recommandations-collaboratives/pull/2316) et correction de l'affichage des comptes de projets et de membres pour plus de cohérence.
- **Nouveaux outils de filtrage** : Ajout de filtres dans l'interface d'administration pour identifier plus facilement les utilisateurs supprimés et les organisations "mystérieuses" [#2343](https://github.com/betagouv/recommandations-collaboratives/pull/2343).
- **Optimisation des flux RSS** : Mise en place d'un système d'authentification pour les flux et filtrage automatique des ressources en mode "brouillon" pour ne proposer que du contenu publié [#2360](https://github.com/betagouv/recommandations-collaboratives/pull/2360).
- **Gestion des emails** : Amélioration de l'intégration avec Brevo (gestion du nom de l'expéditeur) et renforcement de la validation des adresses email [#2256](https://github.com/betagouv/recommandations-collaboratives/pull/2256).
- **Expérimentation** : Introduction d'une expérimentation liée à l'intelligence artificielle sur le frontend [#1939](https://github.com/betagouv/recommandations-collaboratives/pull/1939).

### Évolutions techniques
- **Sécurité renforcée** : 
    - Implémentation d'une politique de sécurité de contenu (CSP) pour protéger l'application tout en permettant l'usage d'outils tiers (Matomo, Crisp) [#2342](https://github.com/betagouv/recommandations-collaboratives/pull/2342).
    - Assainissement des données (sanitization) pour l'historique et les descriptions de projets afin de prévenir les failles d'injection [#2361](https://github.com/betagouv/recommandations-collaboratives/pull/2361).
    - Durcissement des contrôles de permissions sur les API et les flux de données.
- **Optimisation des performances** : Réduction massive des requêtes SQL inutiles (problème de N+1) via l'utilisation de `prefetch` sur les projets, les départements et les détails utilisateurs.
- **Fiabilité et tests** : Augmentation significative de la couverture de tests, particulièrement sur la gestion des droits d'accès et les permissions des utilisateurs (advisors vs members).

### Autres changements
- **Nettoyage du code** : Suppression de code mort et de variables inutilisées pour améliorer la maintenabilité.
- **Documentation** : Corrections de syntaxe dans les tutoriels.
