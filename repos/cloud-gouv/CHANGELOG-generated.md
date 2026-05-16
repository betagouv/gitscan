# Synthèse d'activité : cloud-gouv (du 24 avril 2026 au 02 mai 2026)

## Résumé de l'activité
L'activité récente de l'organisation cloud-gouv s'est concentrée sur l'amélioration de la sécurité, la gestion des identités et l'optimisation des outils de déploiement Kubernetes. Des efforts significatifs ont été déployés pour renforcer la sécurité de l'authentification avec OpenBao et Securix, ainsi que pour faciliter la gestion des configurations Kubernetes avec les charts Helm et les outils associés. L'ajout de nouveaux charts et la correction de bugs dans les charts existants visent à simplifier le déploiement et la gestion des applications pour les utilisateurs.

## Sécurité
Plusieurs dépôts ont reçu des mises à jour axées sur la sécurité :
- [openbao](/repos/cloud-gouv/openbao) a été mis à jour vers Go 1.25.7 pour corriger une vulnérabilité de sécurité (CVE-2025-68121 / GO-2026-4337) et a également mis à jour des dépendances pour corriger d'autres vulnérabilités (CVE-2026-24051 / GO-2026-4394 / GHSA-9h8m-3fm2-qjrq).
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) a permis d'injecter des règles de sécurité supplémentaires (Security Groups) aux nœuds worker.

## Autres changements notables
- [securix](/repos/cloud-gouv/securix) a reçu des améliorations concernant l'expérience utilisateur et la gestion des clés YubiKey, notamment un outil de réinitialisation et de modification des utilisateurs.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) a implémenté un workflow de publication des charts au format OCI, facilitant leur distribution et leur utilisation.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) a vu des corrections et améliorations de la gestion des CIDR, des volumes snapshot, des secrets externes et des règles de sécurité pour les nœuds worker.

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Amélioration de l'expérience utilisateur et de la gestion des clés YubiKey.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et mises à jour de sécurité pour la gestion des secrets.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Ajout de nouveaux charts (pgbench-job) et améliorations de la publication et de la sécurité.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Améliorations de la gestion des configurations Kubernetes et de la sécurité des nœuds worker.
- [portail](/repos/cloud-gouv/portail) : Ajout du support des groupes supplémentaires pour l'authentification RPC.
