## Changelog : infra-apps (30 derniers jours, au 13 mai 2026)

### Résumé
Ce changelog résume les évolutions apportées au dépôt infra-apps au cours des 30 derniers jours. Les principales modifications concernent l'amélioration de la sécurité de Metabase avec l'ajout d'une authentification via OAuth2-proxy, des corrections et améliorations pour Huginn, ainsi que des avancées significatives concernant le déploiement et la configuration de Kuik et d'Elasticsearch.

### Évolutions fonctionnelles
- **Metabase:** Autorisation des routes d'intégration publiques via OAuth2-proxy, renforçant la sécurité d'accès aux données. [#a5dd034](https://github.com/SocialGouv/infra-apps/commit/a5dd034)
- **Huginn:** Correction du fonctionnement des nouveaux canaux. [#1f51bcd](https://github.com/SocialGouv/infra-apps/commit/1f51bcd), [#d21c1ec](https://github.com/SocialGouv/infra-apps/commit/d21c1ec)
- **Huginn:** Correction de la configuration des secrets. [#f33ab1e](https://github.com/SocialGouv/infra-apps/commit/f33ab1e)
- **Huginn:** Remplacement des URLs de flux RSS cassés. [#7bcda5a](https://github.com/SocialGouv/infra-apps/commit/7bcda5a)
- **Kuik:** Déploiement sur les environnements `ovh-prod` et `tools` avec désactivation initiale des webhooks via un sélecteur d'opt-in. [#a0be596](https://github.com/SocialGouv/infra-apps/commit/a0be596)
- **Elasticsearch:** Exposition d'Elasticsearch via Ingress pour faciliter l'accès. [#d9b04dd](https://github.com/SocialGouv/infra-apps/commit/d9b04dd)
- **Elasticsearch:** Déploiement sur l'environnement `ovh-dev` avec Kibana et authentification `fileRealm`. [#1b2d129](https://github.com/SocialGouv/infra-apps/commit/1b2d129)
- **Charon:** Mise à jour de l'image pour supporter la déconnexion initiée par le RP (Relying Party). [#96c97fe](https://github.com/SocialGouv/infra-apps/commit/96c97fe)

### Évolutions techniques
- **Metabase:** Adoption des CRDs Traefik pour la gestion du trafic. [#a7e5b61](https://github.com/SocialGouv/infra-apps/commit/a7e5b61)
- **Kuik:** Suppression du registre en cluster et routage via le proxy cache Harbor. [#c38516a](https://github.com/SocialGouv/infra-apps/commit/c38516a)
- **Kuik:** Ajout du champ `path` requis pour l'upstream docker.io. [#fd2cd91](https://github.com/SocialGouv/infra-apps/commit/fd2cd91)
- **Elasticsearch:** Correction pour permettre à `ingress-nginx` d'atteindre Elasticsearch, résolvant ainsi les erreurs 504. [#b5f83b8](https://github.com/SocialGouv/infra-apps/commit/b5f83b8)
- **Elasticsearch:** Ajout d'un helper `appset-env` manquant pour les overlays d'environnement. [#7285e23](https://github.com/SocialGouv/infra-apps/commit/7285e23)

### Autres changements
- **Documentation:** Ajout d'un document `CLAUDE.md` décrivant les patterns IaC (Infrastructure as Code) utilisés dans infra-apps. [#8b405b2](https://github.com/SocialGouv/infra-apps/commit/8b405b2)
- **Documentation Kuik:** Documentation de la limitation "Always-branch" sur les Kubernetes managés et lien vers l'issue upstream correspondante [#561](https://github.com/SocialGouv/infra-apps/commit/4e4295f). [#ca5b4f8](https://github.com/SocialGouv/infra-apps/commit/ca5b4f8)
- **Kuik:** Mise en pause du déploiement en production, avec une période de test d'une semaine sur `ovh-dev`. [#c86e11e](https://github.com/SocialGouv/infra-apps/commit/c86e11e)
- **Openebs-nfs:** Déploiement sur le cluster `tools`. [#a0c9505](https://github.com/SocialGouv/infra-apps/commit/a0c9505)
