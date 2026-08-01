# Synthèse d'activité : cloud-gouv (du 23/07 au 30/07)

## Résumé de l'activité
L'organisation cloud-gouv a connu une semaine riche en activités, principalement axée sur la sécurité et la maintenance de ses outils. Des améliorations significatives ont été apportées à [openbao](/repos/cloud-gouv/openbao) avec des corrections de bugs et des mises à jour de sécurité critiques.  Les charts Helm ([k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) et [common-helm-charts](/repos/cloud-gouv/common-helm-charts)) ont également été mis à jour pour améliorer la compatibilité et ajouter de nouvelles fonctionnalités. L'initialisation de [playground-public](/repos/cloud-gouv/playground-public) marque le début d'un nouveau projet d'expérimentation. Enfin, [securix](/repos/cloud-gouv/securix) a bénéficié d'intégrations importantes pour la gestion centralisée et l'authentification renforcée.

## Sécurité
Plusieurs dépôts ont reçu des mises à jour de sécurité :

- [openbao](/repos/cloud-gouv/openbao) a été mis à jour vers Go 1.25.7 pour corriger une vulnérabilité (CVE-2025-68121 / GO-2026-4337) et a également mis à jour `go.opentelemetry.io/otel/sdk` pour corriger plusieurs vulnérabilités (CVE-2026-24051 / GO-2026-4394 / GHSA-9h8m-3fm2-qjrq).
- [securix](/repos/cloud-gouv/securix) a ajouté le support pour les puces de sécurité P14SG6 pour une authentification matérielle renforcée.

## Autres changements notables
- [securix](/repos/cloud-gouv/securix) a intégré le Portail pour une gestion centralisée du système et a amélioré la gestion des proxies via une API NetworkManager généralisée.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) a implémenté la gestion de versions individuelles pour chaque chart, offrant une plus grande flexibilité.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) a mis à jour les versions d'API pour assurer la compatibilité avec la dernière version de l'opérateur Cluster API.

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Intégration du Portail, support des puces P14SG6 et améliorations de la gestion des proxies.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs, mises à jour de sécurité et améliorations de la gestion des baux.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Ajout de fonctionnalités et corrections de bugs dans plusieurs charts, notamment `matrix` et `external-secrets`.
- [portail](/repos/cloud-gouv/portail) : Corrections de bugs liés à la gestion des connexions SOCKS5 et au support UDP.
