## Changelog : maestro (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des prélèvements, des analyses et des données associées, notamment pour les DAI et les RAI. Des corrections de bugs et des améliorations de l'interface utilisateur ont été apportées, ainsi que des optimisations techniques et l'ajout de nouvelles fonctionnalités pour faciliter le travail des agents de l'administration.

### Évolutions fonctionnelles
- Ajout d'une interface administrateur pour visualiser toutes les RAI [#898](https://github.com/betagouv/maestro/issues/898).
- Ajout d'une interface de configuration des laboratoires [#920](https://github.com/betagouv/maestro/issues/920).
- Synchronisation des modifications d'utilisateurs de Maestro avec Brevo [#840](https://github.com/betagouv/maestro/issues/840).
- Possibilité de dupliquer les prélèvements sur les environnements de tests [#842](https://github.com/betagouv/maestro/issues/842).
- Amélioration de l'affichage des prélèvements pour les administrateurs [#897](https://github.com/betagouv/maestro/issues/897).
- Ajout d'un filtre sur les prélèvements avec plusieurs exemplaires [#850](https://github.com/betagouv/maestro/issues/850).
- Correction de l'affichage des numéros d'exemplaires dans les prélèvements [#937](https://github.com/betagouv/maestro/issues/937).
- Gestion améliorée des agréments par type de plan [#832](https://github.com/betagouv/maestro/issues/832).
- Correction de l'affichage des dates et heures dans les exports DAI.
- Ajout de la possibilité de filtrer les prélèvements par donneur d'ordre (DAOA/DDPP) [#833](https://github.com/betagouv/maestro/issues/833).

### Évolutions techniques
- Mise à jour de nombreuses dépendances (React, Node.js, PostgreSQL, Express, S3, Docker, etc.).
- Amélioration de la gestion des erreurs et du typage avec Zod, affichant la valeur problématique en cas d'erreur [#820](https://github.com/betagouv/maestro/issues/820).
- Ajout d'un service OIDC local [#841](https://github.com/betagouv/maestro/issues/841).
- Refactor de la gestion des schémas et des coercions de données pour améliorer la robustesse et la flexibilité [#946](https://github.com/betagouv/maestro/issues/946).
- Amélioration de la gestion des erreurs de localstorage [#819](https://github.com/betagouv/maestro/issues/819).
- Ajout de sourcemaps pour faciliter le débogage en production [#821](https://github.com/betagouv/maestro/issues/821).
- Correction de la gestion des status après l'analyse des échantillons [#947](https://github.com/betagouv/maestro/issues/947).
- Correction de la gestion des identifiants de listes Brevo [#901](https://github.com/betagouv/maestro/issues/901).
- Correction de la duplication des document\_id [#938](https://github.com/betagouv/maestro/issues/938).
- Correction de la gestion des non quantifiables dans Cereco [#945](https://github.com/betagouv/maestro/issues/945).

### Autres changements
- Mise à jour de la documentation.
- Amélioration des tests unitaires et d'intégration.
- Nettoyage du code et refactoring de certains composants.
- Ajout de tests de non-régression pour la gestion des dates dans les exports XLS.
- Correction d'un problème de réversion involontaire d'une correction sur l'affichage d'un message d'alerte [#902](https://github.com/betagouv/maestro/issues/902).
- Ajout d'une table pour stocker toutes les RAI reçues [#870](https://github.com/betagouv/maestro/issues/870).
- Ajout d'une interface au S3 local [#889](https://github.com/betagouv/maestro/issues/889).
- Correction de la comparaison de dates [#813](https://github.com/betagouv/maestro/issues/813).
- Amélioration du cache Playwright [#814](https://github.com/betagouv/maestro/issues/814).
