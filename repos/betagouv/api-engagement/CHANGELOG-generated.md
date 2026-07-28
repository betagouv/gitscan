## Changelog : api-engagement (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la performance de l'API, notamment au niveau de la recherche de missions et de l'enrichissement des données.  Des corrections ont été apportées pour améliorer la fiabilité et la sécurité, ainsi que des améliorations d'accessibilité sur la plateforme. De nouvelles fonctionnalités ont été ajoutées pour la diffusion de missions et le suivi des événements.

### Évolutions fonctionnelles
- Ajout de la diffusion de missions et de l'affichage des documents associés dans l'application ([#1340](https://github.com/betagouv/api-engagement/issues/1340)).
- Amélioration du suivi des clics sur les missions en liant les identifiants de scoring utilisateur ([#1335](https://github.com/betagouv/api-engagement/issues/1335)).
- Ajout d'un bandeau de consentement pour les cookies ([#1329](https://github.com/betagouv/api-engagement/issues/1329)).
- Les diffuseurs peuvent désormais modérer leurs propres missions ([#1330](https://github.com/betagouv/api-engagement/issues/1330)).
- Ajout de pages légales et de liens de pied de page ([#1246](https://github.com/betagouv/api-engagement/issues/1246)).
- Ajout de la possibilité d'enregistrer l'adresse email pour la newsletter ([#1209](https://github.com/betagouv/api-engagement/issues/1209)).
- Ajout d'événements de vue de page pour le suivi analytique ([#1235](https://github.com/betagouv/api-engagement/issues/1235)).

### Évolutions techniques
- Refonte de la construction des jobs pour utiliser un publisher dédié ([#1343](https://github.com/betagouv/api-engagement/issues/1343)).
- Optimisation de la requête de recherche de missions ([#1345](https://github.com/betagouv/api-engagement/issues/1345), [#1322](https://github.com/betagouv/api-engagement/issues/1322)).
- Mise en place d'un service de diffusion de missions et reconstruction du job associé ([#1302](https://github.com/betagouv/api-engagement/issues/1302), [#1297](https://github.com/betagouv/api-engagement/issues/1297)).
- Amélioration de la performance du modèle analytique ([#1347](https://github.com/betagouv/api-engagement/issues/1347)).
- Utilisation de materialized views pour la diffusion des missions ([#1334](https://github.com/betagouv/api-engagement/issues/1334)).
- Correction d'une vulnérabilité potentielle de type SSRF lors de l'importation de fichiers XML ([#1303](https://github.com/betagouv/api-engagement/issues/1303)).
- Mise à jour des dépendances Docker et Node.js.
- Amélioration de la gestion des secrets pour l'API.

### Autres changements
- Corrections d'accessibilité (RGAA) sur la plateforme, notamment pour les contrastes, la navigation au clavier, les titres, les liens et les champs de formulaire ([#1286](https://github.com/betagouv/api-engagement/issues/1286), [#1287](https://github.com/betagouv/api-engagement/issues/1287), [#1288](https://github.com/betagouv/api-engagement/issues/1288), [#1289](https://github.com/betagouv/api-engagement/issues/1289), [#1290](https://github.com/betagouv/api-engagement/issues/1290), [#1291](https://github.com/betagouv/api-engagement/issues/1291), [#1292](https://github.com/betagouv/api-engagement/issues/1292), [#1293](https://github.com/betagouv/api-engagement/issues/1293), [#1294](https://github.com/betagouv/api-engagement/issues/1294), [#1295](https://github.com/betagouv/api-engagement/issues/1295), [#1296](https://github.com/betagouv/api-engagement/issues/1296)).
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour de la documentation.
- Suppression de workflows CI inutiles.
- Correction de problèmes de comptage des événements analytiques ([#1332](https://github.com/betagouv/api-engagement/issues/1332)).
- Restauration du préchargement des résultats des quiz ([#1344](https://github.com/betagouv/api-engagement/issues/1344)).
