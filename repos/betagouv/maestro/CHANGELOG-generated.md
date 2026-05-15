## Changelog : maestro (30 derniers jours, au 13 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la gestion des prélèvements et des analyses, notamment avec l'ajout d'une interface administrateur pour les RAI et la synchronisation des utilisateurs avec Brevo. De nombreuses mises à jour de dépendances et corrections de bugs ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'une interface administrateur pour visualiser toutes les RAI (Requêtes d'Analyse et d'Investigation) [#898](https://github.com/betagouv/maestro/issues/898).
- Synchronisation des utilisateurs de Maestro avec Brevo, facilitant la gestion des communications [#840](https://github.com/betagouv/maestro/issues/840).
- Possibilité de dupliquer les prélèvements en environnement de test [#842](https://github.com/betagouv/maestro/issues/842).
- Ajout d'un filtre sur les prélèvements avec plusieurs exemplaires [#850](https://github.com/betagouv/maestro/issues/850).
- Amélioration de l'affichage des prélèvements pour les administrateurs [#897](https://github.com/betagouv/maestro/issues/897).
- Ajout d'une table stockant toutes les RAI reçues [#870](https://github.com/betagouv/maestro/issues/870).
- Ajout d'une interface pour le S3 local [#889](https://github.com/betagouv/maestro/issues/889).
- Possibilité d'envoyer des DAI (Demandes d'Analyse Initiale) via SFTP [#698](https://github.com/betagouv/maestro/issues/698).
- Ajout de la gestion des prescriptions par abattoirs pour les préleveurs [#800](https://github.com/betagouv/maestro/issues/800).
- Correction de l'affichage des étiquettes pour inclure les analyses [#791](https://github.com/betagouv/maestro/issues/791).
- Correction de l'affichage des notes additionnelles sur les échantillons dans le suivi des prélèvements [#780](https://github.com/betagouv/maestro/issues/780).

### Évolutions techniques
- Mise en place d'un service OIDC local pour l'authentification [#841](https://github.com/betagouv/maestro/issues/841).
- Refactor de la gestion des dates pour améliorer la cohérence et la précision.
- Amélioration de la gestion des erreurs Zod avec affichage de la valeur problématique.
- Ajout de l'upload automatique des sourcemaps sur Sentry pour faciliter le débogage.
- Mise à jour de nombreuses dépendances (React, Node.js, PostgreSQL, Express, KnexJS, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- Amélioration du pipeline CI/CD avec ajout de cache pour Playwright.
- Suppression de code obsolète (exceljs) et ajout de tests de non-régression.

### Autres changements
- Correction de divers bugs et améliorations de l'expérience utilisateur.
- Mise à jour de la documentation.
- Correction d'erreurs mineures et amélioration de la lisibilité du code.
- Correction des identifiants de listes Brevo [#901](https://github.com/betagouv/maestro/issues/901).
- Ajout d'un message d'alerte pour la vérification des informations avant l'envoi des prélèvements [#902](https://github.com/betagouv/maestro/issues/902).
- Correction de l'affichage des laboratoires pour les administrateurs.
- Correction de l'affichage des numéros de prélèvements lors de la suppression d'un exemplaire [#823](https://github.com/betagouv/maestro/issues/823).
- Correction de l'affichage des plans de programmation validés par défaut pour DAOA [#769](https://github.com/betagouv/maestro/issues/769).
- Correction de l'affichage des agréments pour les laboratoires [#782](https://github.com/betagouv/maestro/issues/782).
- Correction de l'affichage des consignes de répartition et des notes [#796](https://github.com/betagouv/maestro/issues/796).
- Correction de l'affichage du champ saisie pour DAOA.
