# Synthèse d'activité : cloud-gouv (du 19 juin 2026 au 26 juin 2026)

## Résumé de l'activité
L'activité récente de l'organisation cloud-gouv s'est concentrée sur l'amélioration de la sécurité, de la stabilité et de l'observabilité de ses projets. OpenBao a reçu des corrections de sécurité critiques et des améliorations de la robustesse. Le projet Portail a progressé sur l'observabilité et la flexibilité de la gestion des backends. Des améliorations significatives ont également été apportées aux charts Helm communs, notamment avec l'ajout de tableaux de bord Grafana pour Coturn et le monitoring de machines virtuelles, ainsi que des tests de performance pour PostgreSQL.  Plusieurs dépôts ont bénéficié de mises à jour de dépendances et de corrections de bugs pour assurer une meilleure expérience utilisateur.

## Sécurité
Plusieurs changements liés à la sécurité ont été déployés :

- Correction de vulnérabilités dans OpenBao ([openbao](/repos/cloud-gouv/openbao)) avec des mises à jour de `go.opentelemetry.io/otel/sdk` et de Go lui-même.
- Désactivation de KWallet dans Securix ([securix](/repos/cloud-gouv/securix)) pour renforcer la sécurité.

## Autres changements notables
- Intégration de tests de stress FIO aux benchmarks PostgreSQL dans les charts Helm communs ([common-helm-charts](/repos/cloud-gouv/common-helm-charts)).
- Refonte de la configuration des règles ACL dans le Portail ([portail](/repos/cloud-gouv/portail)) pour une meilleure flexibilité.
- Mise à jour de `clusterctl` dans les Dockerfiles ([dockerfiles](/repos/cloud-gouv/dockerfiles)) pour bénéficier des dernières fonctionnalités.
- Ajout de `golang` à l'image Docker `gitlab-runner` ([dockerfiles](/repos/cloud-gouv/dockerfiles)).

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Améliorations de la localisation, correction de bugs liés au démarrage sécurisé et à l'installateur.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de sécurité, améliorations de la stabilité et de la gestion des montages.
- [portail](/repos/cloud-gouv/portail) : Amélioration de l'observabilité, flexibilité de la gestion des backends et corrections de bugs.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Ajout de tableaux de bord Grafana et intégration de tests de performance pour PostgreSQL.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) : Mises à jour des versions des outils et corrections de sommes SHA.
