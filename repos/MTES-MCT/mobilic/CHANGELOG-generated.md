## Changelog : mobilic (30 derniers jours)

### Résumé
Les dernières mises à jour de mobilic se concentrent sur l'amélioration de l'interface d'administration, notamment la refonte du tableau des employés avec des fonctionnalités d'édition en ligne et de gestion des employés inactifs. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier sur les appareils mobiles. Enfin, des améliorations de sécurité ont été implémentées.

### Évolutions fonctionnelles
- Ajout d'une page de compatibilité/exigences système [#794](https://github.com/MTES-MCT/mobilic/pull/794).
- Refonte du tableau des employés dans l'administration avec édition en ligne et gestion des employés inactifs [#789](https://github.com/MTES-MCT/mobilic/pull/789).
- Ajout de badges indiquant le statut des employés inactifs dans l'administration.
- Possibilité de résilier plusieurs emplois en lot dans l'administration.
- Amélioration de la gestion des erreurs d'authentification et affichage de messages plus clairs [#810](https://github.com/MTES-MCT/mobilic/pull/810).
- Correction de l'affichage des saisies à valider dans le tiroir de la mission [#784](https://github.com/MTES-MCT/mobilic/pull/784).
- Correction de l'affichage des tags "mission en cours" et "mission à valider" dans l'en-tête [#77ca58ae](https://github.com/MTES-MCT/mobilic/commit/77ca58ae).
- Amélioration de l'optimisation du dropdown des employés inactifs [#549c3a1d](https://github.com/MTES-MCT/mobilic/commit/549c3a1d).
- Ajout d'une configuration minimale requise pour l'application [#803](https://github.com/MTES-MCT/mobilic/pull/803).

### Évolutions techniques
- Correction d'un problème de boucle infinie avec le cookie Ubika et le WAF en supprimant le cookie `x-ubika-data` [#808](https://github.com/MTES-MCT/mobilic/pull/808).
- Mise à jour de la configuration de webpack pour la compatibilité avec la version 5 [#799](https://github.com/MTES-MCT/mobilic/pull/799).
- Utilisation de HTTP/1.1 pour les requêtes API upstream afin de corriger des problèmes avec le proxy Ubika [#802](https://github.com/MTES-MCT/mobilic/pull/802).
- Refactorisation du code pour centraliser les styles DSFR dans les composants de filtre.
- Amélioration de la qualité du code et suppression de warnings ESLint.
- Utilisation de `useRef` pour optimiser la gestion de l'affichage des bannières.
- Correction de problèmes de typographie et d'affichage sur les appareils mobiles.
- Mise à jour de la configuration de `browserslist` pour la compatibilité.

### Autres changements
- Correction de l'importation des fichiers CSS dans le playground [#0e8d6cec](https://github.com/MTES-MCT/mobilic/commit/0e8d6cec).
- Mise à jour de la configuration CSP pour autoriser le domaine geoplatform [#fcf3c291](https://github.com/MTES-MCT/mobilic/commit/fcf3c291).
- Correction d'une vulnérabilité potentielle dans l'expression régulière [#6673dfd7](https://github.com/MTES-MCT/mobilic/commit/6673dfd7).
- Correction de vulnérabilités de sécurité avec `snyk-bot` [#c1d63a3b](https://github.com/MTES-MCT/mobilic/pull/791).
- Suppression de commentaires inutiles [#bb39784b](https://github.com/MTES-MCT/mobilic/commit/bb39784b).
