## Changelog : aides-agri (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface d'administration, notamment l'export de données, la réutilisation des bases juridiques et la correction de bugs. La documentation a également été revue et mise à jour, incluant l'ajout d'informations sur la sécurité. Des mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- **Admin :** Possibilité de réutiliser les bases juridiques pour simplifier la création et la gestion des aides. [#616](https://github.com/betagouv/aides-agri/issues/616)
- **Admin :** Amélioration des exports CSV, avec l'ajout d'un champ pour faciliter l'export des données. [#607](https://github.com/betagouv/aides-agri/issues/607) et [#599](https://github.com/betagouv/aides-agri/issues/599)
- **Statistiques :** Amélioration de la lisibilité de la page des statistiques. [#585](https://github.com/betagouv/aides-agri/issues/585)
- **Fiche d'aide :** Correction d'un bug empêchant l'affichage du commentaire de la base juridique. [#569](https://github.com/betagouv/aides-agri/issues/569)
- **Notifications Admin :** Correction de deux erreurs concernant les notifications dans l'interface d'administration des aides. [#576](https://github.com/betagouv/aides-agri/issues/576)
- **Thème Transmission :** Ajout d'un nouvel icône pour le thème Transmission. [#573](https://github.com/betagouv/aides-agri/issues/573)

### Évolutions techniques
- **Documentation :** Mise à jour complète de la documentation, incluant l'architecture technique, les ADR (Architecture Decision Records) et les aspects de sécurité. [#605](https://github.com/betagouv/aides-agri/issues/605), [#604](https://github.com/betagouv/aides-agri/issues/604), [#603](https://github.com/betagouv/aides-agri/issues/603), [#602](https://github.com/betagouv/aides-agri/issues/602)
- **Performance :** Tentative d'amélioration des performances en dynamisant le nombre maximal de requêtes gérées par Gunicorn. [#578](https://github.com/betagouv/aides-agri/issues/578)
- **Dépendances :** Mises à jour de plusieurs dépendances, incluant Django, Ruff, Faker, Sentry, et d'autres, pour assurer la sécurité et la stabilité. (voir les PRs [#614](https://github.com/betagouv/aides-agri/issues/614), [#613](https://github.com/betagouv/aides-agri/issues/613), [#612](https://github.com/betagouv/aides-agri/issues/612), [#611](https://github.com/betagouv/aides-agri/issues/611), [#610](https://github.com/betagouv/aides-agri/issues/610), [#598](https://github.com/betagouv/aides-agri/issues/598), [#597](https://github.com/betagouv/aides-agri/issues/597), [#596](https://github.com/betagouv/aides-agri/issues/596), [#588](https://github.com/betagouv/aides-agri/issues/588), [#587](https://github.com/betagouv/aides-agri/issues/587), [#586](https://github.com/betagouv/aides-agri/issues/586), [#582](https://github.com/betagouv/aides-agri/issues/582), [#581](https://github.com/betagouv/aides-agri/issues/581), [#580](https://github.com/betagouv/aides-agri/issues/580), [#579](https://github.com/betagouv/aides-agri/issues/579), [#577](https://github.com/betagouv/aides-agri/issues/577), [#575](https://github.com/betagouv/aides-agri/issues/575), [#574](https://github.com/betagouv/aides-agri/issues/574), [#572](https://github.com/betagouv/aides-agri/issues/572), [#571](https://github.com/betagouv/aides-agri/issues/571), [#570](https://github.com/betagouv/aides-agri/issues/570), [#568](https://github.com/betagouv/aides-agri/issues/568), [#567](https://github.com/betagouv/aides-agri/issues/567), [#566](https://github.com/betagouv/aides-agri/issues/566), [#565](https://github.com/betagouv/aides-agri/issues/565), [#564](https://github.com/betagouv/aides-agri/issues/564))
- **DSFR Chart :** Mise à jour de la librairie `@gouvfr/dsfr-chart` à la version 2.1.1. [#589](https://github.com/betagouv/aides-agri/issues/589)

### Autres changements
- Correction d'un bug dans le script `aides_publish_illustrations_from_db`. [#600](https://github.com/betagouv/aides-agri/issues/600)
- Correction d'une typo dans la documentation. [#606](https://github.com/betagouv/aides-agri/issues/606)
