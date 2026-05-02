## Changelog : zacharie (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, l'application Zacharie a bénéficié d'une série d'améliorations axées sur l'expérience utilisateur, notamment au niveau de la navigation, de l'affichage des données et de la gestion des fiches. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de l'application. Des travaux ont été réalisés sur les routes et l'authentification pour une meilleure gestion des accès.

### Évolutions fonctionnelles
- Ajout de la liste des lésions sur les fiches. [#331](https://github.com/betagouv/zacharie/issues/331)
- Amélioration de l'affichage des en-têtes des fiches chasseur et FEI/ETG. [#323](https://github.com/betagouv/zacharie/issues/323), [#319](https://github.com/betagouv/zacharie/issues/319), [#325](https://github.com/betagouv/zacharie/issues/325)
- Ajout d'un bouton de connexion pour les utilisateurs administrateurs.
- Implémentation d'un nouveau routage pour les chasseurs et administrateurs, incluant la gestion de la connexion.
- Possibilité d'afficher les carcasses même si elles appartiennent à un seul groupe. [#287](https://github.com/betagouv/zacharie/issues/287)
- Ajout d'un routage pour les SVI. [#296](https://github.com/betagouv/zacharie/issues/296)
- Amélioration de l'affichage des fiches envoyées. [#306](https://github.com/betagouv/zacharie/issues/306)
- Correction de l'affichage des fiches examinateur. [#305](https://github.com/betagouv/zacharie/issues/305)
- Correction de l'affichage des fiches. [#301](https://github.com/betagouv/zacharie/issues/301)
- Amélioration de l'interface utilisateur pour la création de fiches. [#311](https://github.com/betagouv/zacharie/issues/311)
- Amélioration du layout de l'administration. [#313](https://github.com/betagouv/zacharie/issues/313)
- Amélioration de l'interface utilisateur pour la liste des fiches. [#302](https://github.com/betagouv/zacharie/issues/302)

### Évolutions techniques
- Implémentation d'un système d'authentification avec un token Bearer pour les appels API. [#336](https://github.com/betagouv/zacharie/issues/336)
- Refonte des routes de l'application.
- Optimisation des images.
- Mise en place de tests E2E plus complets. [#315](https://github.com/betagouv/zacharie/issues/315)
- Utilisation de `npm ci` pour une installation plus propre et reproductible des dépendances. [#285](https://github.com/betagouv/zacharie/issues/285)
- Correction de la pagination des carcasses pour éviter une limite de 100 lignes. [#329](https://github.com/betagouv/zacharie/issues/329)
- Amélioration de la gestion des erreurs.
- Refactoring des routes. [#295](https://github.com/betagouv/zacharie/issues/295)

### Autres changements
- Correction de divers bugs d'interface utilisateur (wording, défilement, etc.). [#345](https://github.com/betagouv/zacharie/issues/345), [#344](https://github.com/betagouv/zacharie/issues/344), [#342](https://github.com/betagouv/zacharie/issues/342), [#335](https://github.com/betagouv/zacharie/issues/335), [#338](https://github.com/betagouv/zacharie/issues/338), [#337](https://github.com/betagouv/zacharie/issues/337), [#317](https://github.com/betagouv/zacharie/issues/317), [#316](https://github.com/betagouv/zacharie/issues/316), [#284](https://github.com/betagouv/zacharie/issues/284), [#292](https://github.com/betagouv/zacharie/issues/292), [#293](https://github.com/betagouv/zacharie/issues/293), [#291](https://github.com/betagouv/zacharie/issues/291), [#286](https://github.com/betagouv/zacharie/issues/286)
- Correction de la déconnexion. [#341](https://github.com/betagouv/zacharie/issues/341)
- Correction de la cloture automatique des circuits courts. [#343](https://github.com/betagouv/zacharie/issues/343)
- Mise à jour de la documentation E2E.
- Nettoyage des logs.
- Suppression d'une image volumineuse.
- Correction de l'initialisation du chemin dans l'application Expo.
- Ajout de la gestion hors ligne avec Expo. [#327](https://github.com/betagouv/zacharie/issues/327)
- Correction de messages d'erreur.
- Correction du chargement initial dans Expo.
- Correction de l'URL initiale dans Expo.
- Suppression de Claude.
- Correction du calcul du BPH. [#326](https://github.com/betagouv/zacharie/issues/326)
- Ajout de prettier pour formater le code. [#320](https://github.com/betagouv/zacharie/issues/320)
- Correction du chemin vers les carcasses.
