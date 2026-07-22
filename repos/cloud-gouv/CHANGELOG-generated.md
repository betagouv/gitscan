# Synthèse d'activité : cloud-gouv (du 05/07 au 16/07)

## Résumé de l'activité
L'organisation cloud-gouv a connu une activité soutenue cette semaine, avec des mises à jour significatives concernant la sécurité, l'infrastructure et les outils de gestion de cluster. Securix continue d'évoluer avec l'intégration d'un portail de gestion et le support de nouvelles architectures. OpenBao a bénéficié de mises à jour de sécurité importantes et d'améliorations de la robustesse. Les charts Helm pour Cluster API ont été mis à jour pour assurer la compatibilité avec les dernières versions de l'opérateur, et les charts communs ont vu l'ajout de nouvelles fonctionnalités et d'améliorations de la surveillance.

## Sécurité
Plusieurs dépôts ont reçu des corrections de sécurité :
- [openbao](/repos/cloud-gouv/openbao) a été mis à jour vers Go 1.25.7 et les dépendances `go.opentelemetry.io/otel/sdk` pour corriger des vulnérabilités (CVE-2025-68121 / GO-2026-4337, CVE-2026-24051 / GO-2026-4394 / GHSA-9h8m-3fm2-qjrq).

## Autres changements notables
- [securix](/repos/cloud-gouv/securix) intègre un portail pour la gestion centralisée des configurations et prépare le support de l'architecture x390.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) a été mis à jour pour assurer la compatibilité avec les dernières versions de l'opérateur Cluster API et pour corriger des problèmes liés aux versions d'API, notamment pour OpenStack.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) a vu l'ajout de fonctionnalités comme l'ajout d'annotations aux applications et External Secrets, l'intégration d'un fingerprint d'alerte pour Matrix, un tableau de bord pour Coturn et l'ajout d'Auditbeat.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) a mis à jour `clusterctl` vers la version 1.13.1.

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Intégration du Portail, amélioration de la gestion des réseaux et préparation du support de nouvelles architectures.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et mises à jour de sécurité pour une meilleure robustesse.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Ajout de nouvelles fonctionnalités et améliorations de la surveillance via l'intégration de nouveaux charts et la correction de bugs.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Mises à jour pour assurer la compatibilité avec les dernières versions de l'opérateur Cluster API.
