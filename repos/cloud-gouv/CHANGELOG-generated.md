# Synthèse d'activité : cloud-gouv (du 19/06 au 26/06)

## Résumé de l'activité
L'activité récente de l'organisation cloud-gouv s'est concentrée sur l'amélioration de la sécurité, de l'observabilité et de la flexibilité de ses projets. Des corrections de vulnérabilités ont été apportées à [openbao](/repos/cloud-gouv/openbao) et des logs structurés ont été implémentés dans [portail](/repos/cloud-gouv/portail) pour faciliter le débogage et le monitoring.  Plusieurs dépôts ont également bénéficié de mises à jour de versions et de corrections de bugs, notamment [securix](/repos/cloud-gouv/securix), [dockerfiles](/repos/cloud-gouv/dockerfiles) et [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).

## Sécurité
Plusieurs améliorations de sécurité ont été apportées :
- Correction de vulnérabilités dans `go.opentelemetry.io/otel/sdk` et Go dans [openbao](/repos/cloud-gouv/openbao).
- Désactivation de KWallet pour renforcer la sécurité dans [securix](/repos/cloud-gouv/securix).

## Autres changements notables
- Implémentation de logs structurés au format JSON dans [portail](/repos/cloud-gouv/portail) pour une meilleure observabilité.
- Mise à jour de `clusterctl` dans [dockerfiles](/repos/cloud-gouv/dockerfiles) vers la version 1.13.1.
- Refactorisation des tableaux de bord Grafana dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts) pour une meilleure gestion des données.
- Correction de problèmes liés aux versions d'API pour les ressources OpenStack dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).

## Dépôts les plus actifs
- [portail](/repos/cloud-gouv/portail) : Améliorations significatives de l'observabilité, de la flexibilité et de la gestion des backends.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et mises à jour de sécurité pour une meilleure stabilité et protection.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Amélioration de la gestion des secrets, des tableaux de bord Grafana et de la configuration des charts Helm.
- [securix](/repos/cloud-gouv/securix) : Améliorations de la localisation, correction de bugs liés au démarrage sécurisé et à l'installateur.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) : Mise à jour des versions des outils inclus dans les images Docker.
