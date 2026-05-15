## Changelog : api-engagement (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en matière de sécurité, notamment avec l'ajout de journaux d'audit et la sécurisation des webhooks Brevo. Des optimisations ont également été apportées à la recherche d'organisations et à la gestion des jobs, améliorant ainsi les performances globales. Enfin, des correctifs ont été déployés pour résoudre des problèmes d'affichage et de configuration.

### Évolutions fonctionnelles
- Ajout de journaux d'audit pour une meilleure traçabilité des actions sur l'API. [#1019](https://github.com/betagouv/api-engagement/issues/1019)
- Possibilité d'ajouter une clé API pour les annonceurs dans les paramètres de l'application. [#1015](https://github.com/betagouv/api-engagement/issues/1015)
- Activation des missions de service civique dans le job Grimpio. [#977](https://github.com/betagouv/api-engagement/issues/977)
- Correction de l'affichage des filtres et des onglets de modération dans l'application. [#975](https://github.com/betagouv/api-engagement/issues/975)
- Correction de l'alignement du sélecteur de date dans l'application pour une meilleure expérience utilisateur. [#976](https://github.com/betagouv/api-engagement/issues/976)
- Correction du problème de déconnexion lors d'erreurs réseau dans l'application. [#930](https://github.com/betagouv/api-engagement/issues/930)
- Correction de l'affichage de la page d'organisation désactivée. [#18512e0](https://github.com/betagouv/api-engagement/commit/18512e05c236849de0155903b109d34cd431817e)
- Affichage de l'URL sandbox de l'API dans l'exemple curl pour les broadcasters. [#1012](https://github.com/betagouv/api-engagement/issues/1012)

### Évolutions techniques
- Sécurisation des webhooks Brevo pour une meilleure protection contre les attaques. [#1026](https://github.com/betagouv/api-engagement/issues/1026)
- Suppression de la validation de l'adresse IP Brevo. [#1027](https://github.com/betagouv/api-engagement/issues/1027)
- Refactorisation du middleware de contrôle d'accès avec ajout de tests. [#1013](https://github.com/betagouv/api-engagement/issues/1013)
- Amélioration de la gestion des règles d'accès et des rapports. [#1017](https://github.com/betagouv/api-engagement/issues/1017)
- Refactorisation de l'exécution des agrégations du widget de manière séquentielle. [#966](https://github.com/betagouv/api-engagement/issues/966)
- Refactorisation de la gestion des missions avec exclusion de l'organisation publiant. [#965](https://github.com/betagouv/api-engagement/issues/965)
- Utilisation de `tsvector` pour la recherche d'organisations, améliorant les performances. [#950](https://github.com/betagouv/api-engagement/issues/950)
- Ajout de jobs de sauvegarde de la base de données RDB. [#955](https://github.com/betagouv/api-engagement/issues/955)
- Ajout de configuration Mockoon pour les tests. [#978](https://github.com/betagouv/api-engagement/issues/978)
- Ajout de limiteurs de débit pour les publishers et les IPs. [#932](https://github.com/betagouv/api-engagement/issues/932)
- Correction d'un problème de build des jobs. [#1018](https://github.com/betagouv/api-engagement/issues/1018)
- Déploiement de la spécification OpenAPI sur le CI. [#1014](https://github.com/betagouv/api-engagement/issues/1014)

### Autres changements
- Mise à jour de la version de `react-tooltip` dans l'application. [#984](https://github.com/betagouv/api-engagement/issues/984)
- Mise à jour de la version de `typescript` dans le widget et l'API. [#988](https://github.com/betagouv/api-engagement/issues/988), [#990](https://github.com/betagouv/api-engagement/issues/990)
- Mise à jour de la version de `uuid` dans l'API. [#991](https://github.com/betagouv/api-engagement/issues/991)
- Mise à jour de la version de `vite-plugin-svgr` dans l'application. [#986](https://github.com/betagouv/api-engagement/issues/986)
- Mise à jour des dépendances de développement. [#981](https://github.com/betagouv/api-engagement/issues/981), [#979](https://github.com/betagouv/api-engagement/issues/979)
- Mise à jour de l'action Scaleway. [#967](https://github.com/betagouv/api-engagement/issues/967)
- Mise à jour de l'action `actions/setup-node`. [#963](https://github.com/betagouv/api-engagement/issues/963)
- Mise à jour de l'action `orhun/git-cliff-action`. [#962](https://github.com/betagouv/api-engagement/issues/962)
- Amélioration du script de vérification des champs orphelins `stat_event` dans l'API.
- Publication des versions v1.5.1 et v1.5.0.
