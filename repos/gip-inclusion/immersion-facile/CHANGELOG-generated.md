## Changelog : immersion-facile (30 derniers jours, au 29 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration de l'expérience utilisateur pour les bénéficiaires et les administrateurs, notamment avec un nouveau tableau de bord pour les bénéficiaires et des améliorations de la gestion des droits d'accès aux agences. Des corrections et des optimisations ont également été apportées à la gestion des conventions et des notifications.

### Évolutions fonctionnelles
- Ajout d'un bouton pour suivre l'intérêt des bénéficiaires [#794e446](https://github.com/gip-inclusion/immersion-facile/commit/794e446).
- Ajout d'un badge "à relancer" pour les conventions nécessitant une action [#111380f](https://github.com/gip-inclusion/immersion-facile/commit/111380f).
- Nouveau tableau de bord pour les bénéficiaires, incluant une liste des conventions, des onglets pour les discussions et un message de bienvenue personnalisé [#a7741dd](https://github.com/gip-inclusion/immersion-facile/commit/a7741dd), [#76c3ed5](https://github.com/gip-inclusion/immersion-facile/commit/76c3ed5), [#ab25ad7](https://github.com/gip-inclusion/immersion-facile/commit/ab25ad7).
- Affichage des informations supplémentaires de l'établissement dans les discussions [#5c1e655](https://github.com/gip-inclusion/immersion-facile/commit/5c1e655).
- Possibilité de supprimer les droits d'accès d'un utilisateur à une agence, avec confirmation modale [#84dbca2](https://github.com/gip-inclusion/immersion-facile/commit/84dbca2).
- Affichage de la date de naissance du bénéficiaire pour les administrateurs dans le détail de la convention [#e0bf5bd](https://github.com/gip-inclusion/immersion-facile/commit/e0bf5bd).
- Amélioration de l'affichage des statuts de convention pour les bénéficiaires [#3831a54](https://github.com/gip-inclusion/immersion-facile/commit/3831a54).
- Ajout d'un message d'aide lorsque l'utilisateur n'a aucune convention [#c043fa0](https://github.com/gip-inclusion/immersion-facile/commit/c043fa0).
- Affichage de la description des retours d'information dans la modale de diffusion [#021e4e6](https://github.com/gip-inclusion/immersion-facile/commit/021e4e6).
- Mise à jour des instructions d'erreur pour la date de naissance [#68a7750](https://github.com/gip-inclusion/immersion-facile/commit/68a7750).
- Mise à jour des CGU [#530e132](https://github.com/gip-inclusion/immersion-facile/commit/530e132).

### Évolutions techniques
- Refactor de l'accès utilisateur pour simplifier l'authentification et la gestion des rôles [#f6eeb5d](https://github.com/gip-inclusion/immersion-facile/commit/f6eeb5d), [#af2259e](https://github.com/gip-inclusion/immersion-facile/commit/af2259e), [#a354bc8](https://github.com/gip-inclusion/immersion-facile/commit/a354bc8), [#9b21ae4](https://github.com/gip-inclusion/immersion-facile/commit/9b21ae4).
- Ajout d'index manquants pour la table `notifications_sms` [#aabacc1](https://github.com/gip-inclusion/immersion-facile/commit/aabacc1).
- Refactor de la gestion des conventions pour améliorer les performances et la lisibilité du code [#3f64d47](https://github.com/gip-inclusion/immersion-facile/commit/3f64d47).
- Amélioration de la gestion des rappels pour les évaluations [#3afdb6b](https://github.com/gip-inclusion/immersion-facile/commit/3afdb6b).
- Mise en place d'une architecture "use case builder" pour simplifier la logique métier [#e10a9ff](https://github.com/gip-inclusion/immersion-facile/commit/e10a9ff), [#cfa1192](https://github.com/gip-inclusion/immersion-facile/commit/cfa1192), [#ce03bf4](https://github.com/gip-inclusion/immersion-facile/commit/ce03bf4), [#cae86de](https://github.com/gip-inclusion/immersion-facile/commit/cae86de), [#aba2565](https://github.com/gip-inclusion/immersion-facile/commit/aba2565), [#9cd2b05](https://github.com/gip-inclusion/immersion-facile/commit/9cd2b05), [#869c84a](https://github.com/gip-inclusion/immersion-facile/commit/869c84a), [#4cea1ec](https://github.com/gip-inclusion/immersion-facile/commit/4cea1ec), [#369a4d9](https://github.com/gip-inclusion/immersion-facile/commit/369a4d9), [#2baa720](https://github.com/gip-inclusion/immersion-facile/commit/2baa720).
- Suppression de la suppression de tâches cron pour la fermeture des agences inactives [#021e4e6](https://github.com/gip-inclusion/immersion-facile/commit/021e4e6).

### Autres changements
- Mise à jour de la documentation et des tests unitaires.
- Corrections de tests Playwright pour le tableau de bord de l'établissement [#8e05585](https://github.com/gip-inclusion/immersion-facile/commit/8e05585).
- Suppression de code inutilisé.
- Mise à jour des dépendances (immutable, vite, axios, dompurify, body-parser, brace-expansion, fast-uri, js-yaml).
- Amélioration de la gestion des erreurs et des messages d'information.
- Ajout de tests unitaires et d'intégration.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de tests pour la suppression d'un conseiller par convention [#21b5431](https://github.com/gip-inclusion/immersion-facile/commit/21b5431).
- Mise à jour des libellés et des textes dans l'interface utilisateur.
- Ajout de la possibilité de notifier les utilisateurs d'une agence en cas de bannissement d'un établissement [#54d9748](https://github.com/gip-inclusion/immersion-facile/commit/54d9748).
- Suppression de la version dupliquée des CGU [#4d3aad0](https://github.com/gip-inclusion/immersion-facile/commit/4d3aad0).
