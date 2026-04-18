# Synthèse d'activité : cloud-gouv (derniers 7 jours)

## Résumé de l'activité
L'organisation cloud-gouv a connu une activité soutenue au cours des dernières semaines, avec des améliorations significatives apportées à plusieurs de ses projets. Les efforts se sont concentrés sur l'amélioration de la sécurité, notamment dans [openbao](/repos/cloud-gouv/openbao) avec des mises à jour de dépendances corrigeant des vulnérabilités critiques.  Des avancées ont également été réalisées dans la gestion des clusters Kubernetes avec [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts), offrant plus de flexibilité et de contrôle sur la configuration des nœuds et des volumes. Enfin, des corrections et des améliorations ont été apportées aux outils de déploiement et de gestion d'applications via [common-helm-charts](/repos/cloud-gouv/common-helm-charts) et [dockerfiles](/repos/cloud-gouv/dockerfiles).

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité :

- Correction de vulnérabilités dans les dépendances de [openbao](/repos/cloud-gouv/openbao) (Go 1.25.7 et `go.opentelemetry.io/otel/sdk`).
- Amélioration de la sécurité des nœuds worker via l'injection de règles de sécurité (Security Groups) dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).

## Autres changements notables
- Suppression du module Openstack dans [securix](/repos/cloud-gouv/securix).
- Introduction de la version 1 des règles d'accès (ACL) dans [portail](/repos/cloud-gouv/portail).
- Ajout de l'outil `kustomize` à l'image `k8s-tools` dans [dockerfiles](/repos/cloud-gouv/dockerfiles).
- Amélioration de la gestion des CIDR dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).

## Dépôts les plus actifs
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Amélioration de la gestion des clusters Kubernetes avec des corrections et des fonctionnalités pour la sécurité des nœuds, la gestion des volumes et des CIDR.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et mises à jour de sécurité pour le service de gestion des clés.
- [portail](/repos/cloud-gouv/portail) : Ajout de tests d'intégration et initialisation des nouvelles règles d'accès.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Ajout de fonctionnalités pour la personnalisation des charts Helm et corrections de bugs.
