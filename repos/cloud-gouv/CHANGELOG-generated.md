# Synthèse d'activité : cloud-gouv (du 24 avril au 09 juillet 2026)

## Résumé de l'activité
L'organisation cloud-gouv a connu une activité soutenue ces dernières semaines, avec des améliorations significatives apportées à plusieurs projets clés. Les efforts se sont concentrés sur la sécurité, notamment avec des mises à jour de dépendances dans [openbao](/repos/cloud-gouv/openbao) pour corriger des vulnérabilités. Des améliorations ont également été apportées à l'expérience utilisateur et à la gestion des infrastructures, avec des mises à jour de [portail](/repos/cloud-gouv/portail) pour un logging structuré et une gestion dynamique des backends, et des corrections pour assurer la compatibilité de [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) avec les dernières versions de Cluster API.  [securix](/repos/cloud-gouv/securix) a bénéficié d'améliorations de localisation et de corrections de bugs liés à la sécurité.

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité :

- Mise à jour de dépendances dans [openbao](/repos/cloud-gouv/openbao) pour corriger des vulnérabilités (CVE-2025-68121, GO-2026-4337, CVE-2026-24051, GO-2026-4394, GHSA-9h8m-3fm2-qjrq).
- Désactivation de KWallet dans [securix](/repos/cloud-gouv/securix) pour renforcer la sécurité.

## Autres changements notables
- Implémentation du logging structuré au format JSON dans [portail](/repos/cloud-gouv/portail) pour faciliter le débogage et la surveillance.
- Mise à jour de `clusterctl` dans [dockerfiles](/repos/cloud-gouv/dockerfiles) vers la version 1.13.1.
- Ajout de fonctionnalités et d'améliorations à plusieurs charts dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts), notamment pour Matrix, Coturn, pgbench et External Secrets.
- Correction d'un problème de démarrage sécurisé (Secure Boot) dans [securix](/repos/cloud-gouv/securix) pour l'ANSSI R3.

## Dépôts les plus actifs
- [portail](/repos/cloud-gouv/portail) : Amélioration du logging et de la gestion des backends dynamiques.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et mises à jour de sécurité.
- [securix](/repos/cloud-gouv/securix) : Améliorations de la localisation, corrections de bugs et renforcement de la sécurité.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Ajout de nouvelles fonctionnalités et améliorations à plusieurs charts Helm.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) : Mise à jour des outils et correction des sommes de contrôle.
