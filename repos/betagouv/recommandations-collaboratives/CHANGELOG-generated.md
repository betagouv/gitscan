## Changelog : recommandations-collaboratives (30 derniers jours, au 28/08/2026)

### Résumé
Ce mois-ci, l'accent a été mis sur l'amélioration de l'expérience de gestion via une refonte visuelle du CRM et une meilleure précision des données affichées (comptages, noms d'organisations). La sécurité de l'application a été renforcée et les performances globales ont été optimisées pour garantir une navigation plus fluide et rapide.

### Évolutions fonctionnelles
- **Refonte de l'interface CRM** : Amélioration de l'affichage de la page d'accueil, des cartes d'administration (espacement et texte) et des cartes de projets pour inclure le nom de l'organisation. [#2282](https://github.com/betagouv/recommandations-collaboratives/pull/2282), [#2316](https://github.com/betagouv/recommandations-collaboratives/pull/2316)
- **Fiabilisation des données de gestion** : Correction du comptage des membres et des projets par organisation, et résolution des problèmes de troncature des noms d'organisations. [#2317](https://github.com/betagouv/recommandations-collaboratives/pull/2317)
- **Gestion des accès et inscriptions** : Correction des erreurs lors des demandes d'accès pour les conseillers dont le compte existe déjà ou est présent sur un autre site. [#2334](https://github.com/betagouv/recommandations-collaboratives/pull/2334)
- **Notifications et emails** : Amélioration de la configuration de l'expéditeur pour les emails (via Brevo) et correction des doublons de notifications de modération. [#2327](https://github.com/betagouv/recommandations-collaboratives/pull/2327), [#2335](https://github.com/betagouv/recommandations-collaboratives/pull/2335)

### Évolutions techniques
- **Sécurité** : Implémentation d'une politique de sécurité du contenu (CSP) pour renforcer la protection de l'application, notamment lors de son intégration dans d'autres interfaces. [#2330](https://github.com/betagouv/recommandations-collaboratives/pull/2330)
- **Optimisation des performances** : Réduction massive des requêtes à la base de données (problème de requêtes N+1) via l'utilisation de `prefetch` sur les modules projets, CRM et utilisateurs. [#2325](https://github.com/betagouv/recommandations-collaboratives/pull/2325)
- **Optimisation de la mémoire** : Mise en cache des permissions des utilisateurs pour accélérer les vérifications de droits.

### Autres changements
- **Nettoyage du code** : Suppression de code mort, de variables inutilisées et de l'ancienne configuration d'envoi d'emails.
- **Maintenance** : Mise à jour de la version du projet vers la v3.10.x.
