# Synthèse d'activité : cloud-gouv (du 29/04 au 02/06)

## Résumé de l'activité
L'activité récente de l'organisation cloud-gouv s'est concentrée sur l'amélioration de la sécurité, de la stabilité et de la flexibilité de ses différents projets. Des efforts significatifs ont été déployés pour corriger des vulnérabilités dans [openbao](/repos/cloud-gouv/openbao) et renforcer la sécurité de [securix](/repos/cloud-gouv/securix).  Des améliorations ont également été apportées aux charts Helm pour faciliter le déploiement et la gestion d'applications sur Kubernetes, notamment via [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) et [common-helm-charts](/repos/cloud-gouv/common-helm-charts). L'ajout de Go à l'image Docker de GitLab Runner ([dockerfiles](/repos/cloud-gouv/dockerfiles)) simplifie l'exécution de pipelines nécessitant cet environnement.

## Sécurité
Plusieurs correctifs de sécurité ont été déployés :
- Correction d'une vulnérabilité de sécurité dans Go (CVE-2025-68121 / GO-2026-4337) dans [openbao](/repos/cloud-gouv/openbao).
- Correction de vulnérabilités de sécurité dans `go.opentelemetry.io/otel/sdk` (CVE-2026-24051 / GO-2026-4394 / GHSA-9h8m-3fm2-qjrq) dans [openbao](/repos/cloud-gouv/openbao).
- Renforcement de la sécurité de [securix](/repos/cloud-gouv/securix) avec la désactivation optionnelle de KWallet.

## Autres changements notables
- Refonte des dépendances dans [portail](/repos/cloud-gouv/portail) pour une meilleure compatibilité.
- Amélioration de l'idempotence de l'installateur de [securix](/repos/cloud-gouv/securix).
- Ajout d'un fichier README initial pour [securix-infra-reference-implementation](/repos/cloud-gouv/securix-infra-reference-implementation) pour faciliter la compréhension du projet.
- Refactorisation des tableaux de bord Grafana dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts) pour une meilleure gestion des données.

## Dépôts les plus actifs
- [openbao](/repos/cloud-gouv/openbao) : Correction de bugs et mises à jour de sécurité pour améliorer la stabilité et la sécurité de la gestion des baux.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Amélioration des charts Helm pour une meilleure gestion des secrets, des tableaux de bord Grafana et une configuration plus flexible.
- [securix](/repos/cloud-gouv/securix) : Améliorations de la sécurité, de la robustesse de l'installateur et de la conformité aux recommandations ANSSI.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Mises à jour pour assurer la compatibilité avec les dernières versions de Cluster API et correction de problèmes liés aux versions d'API.
