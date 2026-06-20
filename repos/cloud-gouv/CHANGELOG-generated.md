# Synthèse d'activité : cloud-gouv (du 18 mai au 18 juin 2026)

## Résumé de l'activité
L'activité récente de l'organisation cloud-gouv s'est concentrée sur l'amélioration de la sécurité, de l'observabilité et de la flexibilité de ses différents projets. Des correctifs de sécurité ont été appliqués à [openbao](/repos/cloud-gouv/openbao) pour corriger des vulnérabilités critiques. Les projets [portail](/repos/cloud-gouv/portail) et [common-helm-charts](/repos/cloud-gouv/common-helm-charts) ont bénéficié d'améliorations significatives en termes d'observabilité et de gestion de la configuration, offrant ainsi aux utilisateurs une meilleure visibilité et un contrôle accru sur leurs infrastructures. Des mises à jour de compatibilité et des corrections de bugs ont également été apportées à [securix](/repos/cloud-gouv/securix) et [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) pour assurer la stabilité et la conformité.

## Sécurité
Plusieurs correctifs de sécurité ont été déployés :
- [openbao](/repos/cloud-gouv/openbao) a été mis à jour vers Go 1.25.7 et des dépendances ont été mises à jour pour corriger des vulnérabilités (CVE-2025-68121, GO-2026-4337, CVE-2026-24051, GO-2026-4394, GHSA-9h8m-3fm2-qjrq).

## Autres changements notables
- [portail](/repos/cloud-gouv/portail) a introduit des logs structurés et la possibilité de mettre à jour dynamiquement les backends via l'API RPC, améliorant ainsi l'observabilité et la flexibilité.
- [securix](/repos/cloud-gouv/securix) a amélioré la compatibilité matérielle avec l'ajout de la prise en charge de Qemu/KVM et a corrigé des problèmes liés à la conformité ANSSI R3.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) a mis à jour `clusterctl` vers la version 1.13.1 et ajouté `golang` à l'image Docker des runners GitLab.

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Amélioration de la compatibilité matérielle et correction de bugs liés à la conformité ANSSI.
- [portail](/repos/cloud-gouv/portail) : Ajout de logs structurés et gestion dynamique des backends.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et mises à jour de sécurité.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Amélioration des charts Grafana, pgbench et Haproxy.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) : Mise à jour de `clusterctl` et ajout de `golang` aux runners GitLab.
