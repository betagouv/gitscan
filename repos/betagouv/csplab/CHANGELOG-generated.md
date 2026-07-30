## Changelog : csplab (30 derniers jours, au 29 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des recrutements, notamment l'ajout de rôles et de permissions pour un contrôle d'accès plus précis. Des améliorations ont également été apportées à l'ingestion de données, à la gestion des API et à l'interface utilisateur pour une expérience plus fluide et sécurisée.

### Évolutions fonctionnelles
- Ajout de la gestion des étapes d'un pipeline de recrutement, avec possibilité de réinitialisation et de consultation/mise à jour. [#1050](https://github.com/betagouv/csplab/issues/1050) et [#1048](https://github.com/betagouv/csplab/issues/1048)
- Mise en place du contrôle d'accès basé sur les rôles (RBAC) pour les agents selon leurs rôles sur un recrutement, ainsi que pour la création d'organismes. [#1054](https://github.com/betagouv/csplab/issues/1054), [#1025](https://github.com/betagouv/csplab/issues/1025) et [#1026](https://github.com/betagouv/csplab/issues/1026)
- Intégration de la gestion des coordonnées GPS des offres via l'API web. [#969](https://github.com/betagouv/csplab/issues/969)
- Ajout d'une limite quotidienne au débit de l'API key et d'une authentification API key sur la liste des offres. [#1061](https://github.com/betagouv/csplab/issues/1061) et [#1058](https://github.com/betagouv/csplab/issues/1058)
- Ajout de la possibilité de changer l'étape d'un recrutement par lot. [#948](https://github.com/betagouv/csplab/issues/948)
- Amélioration de l'interface utilisateur pour la gestion des recrutements avec l'ajout de filtres et d'une vue Kanban. [#916](https://github.com/betagouv/csplab/issues/916), [#900](https://github.com/betagouv/csplab/issues/900) et [#899](https://github.com/betagouv/csplab/issues/899)
- Ajout d'une guidance utilisateur pour les étapes du pipeline de recrutement. [#915](https://github.com/betagouv/csplab/issues/915)

### Évolutions techniques
- Ajout des en-têtes `X-RateLimit-Limit`, `X-RateLimit-Remaining` et `X-RateLimit-Reset` aux réponses de l'API. [#1068](https://github.com/betagouv/csplab/issues/1068)
- Refactorisation de l'extraction des données de recrutement pour utiliser l'interface `IPage`. [#1040](https://github.com/betagouv/csplab/issues/1040)
- Migration des composants frontend vers Pinia Colada pour une meilleure gestion de l'état. [#1011](https://github.com/betagouv/csplab/issues/1011) et [#983](https://github.com/betagouv/csplab/issues/983)
- Amélioration de la configuration des identifiants TalentSoft pour la rendre dynamique. [#892](https://github.com/betagouv/csplab/issues/892)
- Ajout d'un modèle admin readonly pour les snapshots de statistiques. [#894](https://github.com/betagouv/csplab/issues/894)
- Refactorisation de la gestion des étapes de recrutement. [#943](https://github.com/betagouv/csplab/issues/943) et [#886](https://github.com/betagouv/csplab/issues/886)
- Séparation de l'interface `IOffersRepository` en deux interfaces distinctes. [#887](https://github.com/betagouv/csplab/issues/887)

### Autres changements
- Amélioration des tests RBAC pour la gestion des organismes. [#1027](https://github.com/betagouv/csplab/issues/1027)
- Suppression du script de rebase automatique après approbation des PR. [#1059](https://github.com/betagouv/csplab/issues/1059)
- Mise à jour des dépendances de plusieurs modules (ocr, web, notebook, ingestion). [#952](https://github.com/betagouv/csplab/issues/952), [#951](https://github.com/betagouv/csplab/issues/951), [#950](https://github.com/betagouv/csplab/issues/950) et [#889](https://github.com/betagouv/csplab/issues/889)
- Correction de bugs divers liés à la gestion des niveaux d'études, des codes d'expérience, et de la sérialisation des dates. [#1049](https://github.com/betagouv/csplab/issues/1049), [#1046](https://github.com/betagouv/csplab/issues/1046) et [#888](https://github.com/betagouv/csplab/issues/888)
- Amélioration de la configuration et des outils de développement. [#1043](https://github.com/betagouv/csplab/issues/1043), [#1021](https://github.com/betagouv/csplab/issues/1021) et [#974](https://github.com/betagouv/csplab/issues/974)
- Ajout de documentation et de commentaires pour améliorer la lisibilité du code. [#958](https://github.com/betagouv/csplab/issues/958) et [#902](https://github.com/betagouv/csplab/issues/902)
