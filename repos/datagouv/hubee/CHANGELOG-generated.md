## Changelog : hubee (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité, la modernisation de l'infrastructure et la préparation du nouveau portail V2. Des corrections de vulnérabilités ont été appliquées et le système de logs a été amélioré. L'intégration de Sentry permettra un meilleur suivi des erreurs en production.

### Évolutions fonctionnelles
- Le portail V2 commence à prendre forme avec l'intégration du socle DSFR, posant les bases de l'interface utilisateur. [#73](https://github.com/datagouv/hubee/pulls/73)
- Amélioration de la sécurité avec la gestion de `force_ssl` côté application et l'activation d'une Content Security Policy (CSP) minimale. [#87](https://github.com/datagouv/hubee/pulls/87)

### Évolutions techniques
- Les logs sont maintenant au format `logfmt`, recommandé par le CSIRT, facilitant leur analyse et leur exploitation. [#90](https://github.com/datagouv/hubee/pulls/90)
- La configuration de Renovate a été migrée pour en faire le seul robot de mise à jour du projet. [#92](https://github.com/datagouv/hubee/pulls/92)
- La connexion à la base de données PostgreSQL est maintenant configurée via des variables d'environnement en production, améliorant la sécurité et la flexibilité. [#94](https://github.com/datagouv/hubee/pulls/94)
- Intégration de Sentry pour le suivi des erreurs en production, permettant une détection et une résolution plus rapides des problèmes. [#81](https://github.com/datagouv/hubee/pulls/81)
- Mise à jour de l'image Docker Ruby. [#79](https://github.com/datagouv/hubee/pulls/79) et [#80](https://github.com/datagouv/hubee/pulls/80)
- Ajout d'un argument `bundler build-arg` pour la gem v1 dans le Dockerfile. [#93](https://github.com/datagouv/hubee/pulls/93)
- La CI est maintenant déclenchée chaque nuit à 5h UTC. [#85](https://github.com/datagouv/hubee/pulls/85)
- La CI GitHub est restreinte à l'analyse statique et à la sécurité. [#92](https://github.com/datagouv/hubee/pulls/92)

### Autres changements
- Ajout de la gem `hub-api-v1` (client API Hubee V1). [#82](https://github.com/datagouv/hubee/pulls/82)
- Suppression du devcontainer, car il n'était plus utilisé. [#82](https://github.com/datagouv/hubee/pulls/82)
- Correction de vulnérabilités (CVE) dans les dépendances (loofah, rails-html-sanitizer, crass). [#95](https://github.com/datagouv/hubee/pulls/95) et [#80](https://github.com/datagouv/hubee/pulls/80)
- Mise à jour de Renovate. [#92](https://github.com/datagouv/hubee/pulls/92)
- Mise à jour de l'action `actions/checkout` vers la version 7. [#76](https://github.com/datagouv/hubee/pulls/76)
- Mise à jour de la version de PostgreSQL dans le devcontainer. [#78](https://github.com/datagouv/hubee/pulls/78)
- Intégration de Renovate sur le portail V2. [#72](https://github.com/datagouv/hubee/pulls/72)
