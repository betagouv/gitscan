## Changelog : nosgestesclimat (30 derniers jours, au 07/08/2026)

### Résumé
Ce mois-ci, le projet a progressé sur l'enrichissement des données de calcul (avion et véhicules) et l'amélioration de l'expérience utilisateur via de nouvelles notifications assistées par IA. Un travail important a également été réalisé pour stabiliser et sécuriser les processus de déploiement automatique (CI/CD).

### Évolutions fonctionnelles
- Ajout de nouvelles actions concernant le transport aérien.
- Mise à jour du script de calcul de l'empreinte carbone des véhicules.
- Introduction de notifications par IA avec une meilleure gestion de la mise en forme (sauts de ligne) [#2792](https://github.com/incubateur-ademe/nosgestesclimat/pull/2792).
- Correction d'un problème de double comptage pour les terminaux numériques [#2795](https://github.com/incubateur-ademe/nosgestesclimat/pull/2795).
- Correction de l'affichage des icônes via l'implémentation d'un namespace [#2796](https://github.com/incubateur-ademe/nosgestesclimat/pull/2796).

### Évolutions techniques
- Refonte et nettoyage des workflows GitHub Actions pour sécuriser les processus de déploiement et limiter l'usage d'actions externes.
- Optimisation du système de dispatching au sein du modèle.
- Intégration de Husky pour la gestion des hooks Git.
- Mise à jour de la version du projet vers la série 4.14.x (incluant la version 4.14.3 [#2806](https://github.com/incubateur-ademe/nosgestesclimat/pull/2806)).
