# Synthèse d'activité : cloud-gouv (du 24 avril au 09 juillet 2026)

## Résumé de l'activité
L'activité récente de l'organisation cloud-gouv s'est concentrée sur l'amélioration de la sécurité, de l'observabilité et de la stabilité de ses différents projets. Des corrections de vulnérabilités ont été apportées à [openbao](/repos/cloud-gouv/openbao) et des améliorations significatives ont été faites au logging du [portail](/repos/cloud-gouv/portail).  Plusieurs dépôts ont également bénéficié de mises à jour de dépendances et de corrections de bugs pour améliorer leur fonctionnement et leur compatibilité, notamment [securix](/repos/cloud-gouv/securix), [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) et [dockerfiles](/repos/cloud-gouv/dockerfiles). Les charts Helm de [common-helm-charts](/repos/cloud-gouv/common-helm-charts) ont été enrichis de nouvelles fonctionnalités et améliorations.

## Sécurité
Plusieurs correctifs de sécurité ont été déployés :
- Mise à jour de `go.opentelemetry.io/otel/sdk` dans [openbao](/repos/cloud-gouv/openbao) pour corriger des vulnérabilités (CVE-2026-24051, GO-2026-4394, GHSA-9h8m-3fm2-qjrq).
- Mise à jour de Go vers la version 1.25.7 dans [openbao](/repos/cloud-gouv/openbao) pour corriger une vulnérabilité (CVE-2025-68121 / GO-2026-4337).
- Désactivation de KWallet dans [securix](/repos/cloud-gouv/securix) pour renforcer la sécurité.

## Autres changements notables
- Introduction de logs structurés au format JSON dans [portail](/repos/cloud-gouv/portail) pour faciliter le débogage et le monitoring.
- Mise à jour de `clusterctl` dans [dockerfiles](/repos/cloud-gouv/dockerfiles) vers la version 1.13.1.
- Suppression de la branche `disko-fork` dans [bureautix-example](/repos/cloud-gouv/bureautix-example) pour simplifier la gestion du code.

## Dépôts les plus actifs
- [openbao](/repos/cloud-gouv/openbao) : Correction de bugs, mises à jour de sécurité et améliorations de la robustesse.
- [portail](/repos/cloud-gouv/portail) : Amélioration de l'observabilité avec l'introduction de logs structurés.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Ajout de nouvelles fonctionnalités et améliorations aux charts Helm.
- [securix](/repos/cloud-gouv/securix) : Améliorations de la localisation, corrections de bugs liés au démarrage sécurisé et à l'installateur.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) : Mise à jour des outils inclus pour bénéficier des dernières fonctionnalités.
