# Synthèse d'activité : incubateur-ademe (du 16 mai 2026 au 16 juin 2026)

## Résumé de l'activité
L'activité récente de l'organisation incubateur-ademe a été riche et diversifiée, avec des améliorations significatives sur plusieurs projets.  Plusieurs dépôts ont bénéficié d'améliorations de l'expérience utilisateur, notamment [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) et [benefriches](/repos/incubateur-ademe/benefriches), avec l'ajout de nouvelles fonctionnalités et la correction de bugs.  Des efforts importants ont été consacrés à la modernisation technique, avec des migrations vers TypeScript ([dsfr-override](/repos/incubateur-ademe/dsfr-override), [tacct-legacy-nextjs](/repos/incubateur-ademe/tacct-legacy-nextjs)) et des mises à jour de dépendances majeures (n8n, Node.js).  L'accent a également été mis sur la sécurité, avec des corrections pour prévenir les injections SQL et les IDOR dans [territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions) et l'ajout de scans de secrets ([benefriches](/repos/incubateur-ademe/benefriches)).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction de vulnérabilités et prévention des injections SQL et IDOR dans [territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions).
- Ajout d'un scan de secrets avec Talisman dans [benefriches](/repos/incubateur-ademe/benefriches).

## Autres changements notables
- Migration vers TypeScript dans [dsfr-override](/repos/incubateur-ademe/dsfr-override) et [tacct-legacy-nextjs](/repos/incubateur-ademe/tacct-legacy-nextjs) pour une meilleure maintenabilité.
- Mise à jour majeure de n8n vers la version 2 dans [n8n-scalingo](/repos/incubateur-ademe/n8n-scalingo).
- Refonte de l'infrastructure de déploiement pour [plusfraisautravail](/repos/incubateur-ademe/plusfraisautravail) vers Scaleway et OpenTofu.
- Intégration de l'authentification FGP dans [grafana](/repos/incubateur-ademe/grafana) pour une gestion centralisée des accès.
- Migration de l'application Pacoupa vers l'application FCU ([pacoupa](/repos/incubateur-ademe/pacoupa)).

## Dépôts les plus actifs
- [tacct-legacy-nextjs](/repos/incubateur-ademe/tacct-legacy-nextjs) : Développement initial de l'application avec authentification, pages et chiffrement.
- [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) : Améliorations de l'interface utilisateur et intégration d'un système d'enquête.
- [benefriches](/repos/incubateur-ademe/benefriches) : Ajout de documentation, refonte de l'interface de comparaison d'impacts et améliorations de la sécurité.
- [nosgestesclimat-app](/repos/incubateur-ademe/nosgestesclimat-app) : Ajout d'un mode "scolaire" et refonte du système de déploiement.
- [quefairedemesobjets](/repos/incubateur-ademe/quefairedemesobjets) : Amélioration de l'accessibilité et correction de bugs.
