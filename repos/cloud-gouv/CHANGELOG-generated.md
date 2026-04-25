# Synthèse d'activité : cloud-gouv (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation cloud-gouv s'est concentrée sur l'amélioration de la stabilité, la sécurité et la flexibilité de ses outils et services. Des progrès significatifs ont été réalisés dans la gestion des configurations Kubernetes avec [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts), l'automatisation des déploiements avec [common-helm-charts](/repos/cloud-gouv/common-helm-charts) et [dockerfiles](/repos/cloud-gouv/dockerfiles), ainsi que sur la sécurité du système d'exploitation avec [securix](/repos/cloud-gouv/securix). OpenBao ([openbao](/repos/cloud-gouv/openbao)) a bénéficié d'une attention particulière en matière de corrections de bugs et de mises à jour de sécurité. Le portail ([portail](/repos/cloud-gouv/portail)) a continué son développement avec des tests et des corrections de bugs.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- [openbao](/repos/cloud-gouv/openbao) a été mis à jour vers Go 1.25.7 et a bénéficié de mises à jour de dépendances pour corriger des vulnérabilités (CVE-2025-68121 / GO-2026-4337, CVE-2026-24051 / GO-2026-4394 / GHSA-9h8m-3fm2-qjrq).
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) permet désormais d'injecter des règles de sécurité supplémentaires (Security Groups) aux nœuds worker.

## Autres changements notables
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) a vu des améliorations dans la gestion des CIDR et des volumes snapshot.
- [securix](/repos/cloud-gouv/securix) a ajouté le support matériel pour le ThinkPad X13 Gen 1 AMD et a supprimé le module Openstack.
- [openbao](/repos/cloud-gouv/openbao) a corrigé des problèmes liés à l'auto-déverrouillage et à l'invalidation du cache PKI.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) a ajouté l'outil `kustomize` à l'image `k8s-tools`.

## Dépôts les plus actifs
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs, mises à jour de sécurité et améliorations de la gestion des baux.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Améliorations de la gestion des CIDR, des volumes snapshot et de la sécurité des nœuds worker.
- [securix](/repos/cloud-gouv/securix) : Ajout de support matériel et refactorisation de la configuration.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Amélioration de la flexibilité et de la stabilité des charts Helm.
