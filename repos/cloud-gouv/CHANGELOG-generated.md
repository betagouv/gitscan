# Synthèse d'activité : cloud-gouv (derniers 7 jours)

## Résumé de l'activité
L'organisation cloud-gouv a connu une semaine productive, marquée par des améliorations significatives en matière de sécurité et de fonctionnalités pour ses principaux projets. OpenBao a bénéficié de corrections de bugs critiques et de mises à jour de sécurité, tandis que le portail a renforcé sa sécurité avec l'ajout du support mTLS et de la redirection HTTP CONNECT. De nouveaux outils et charts Helm ont été ajoutés pour simplifier le déploiement d'applications Kubernetes, et securix a amélioré son expérience utilisateur et sa sécurité. L'initialisation du dépôt [common-helm-charts](/repos/cloud-gouv/common-helm-charts) marque le début d'une nouvelle initiative pour faciliter le déploiement d'applications sur Kubernetes.

## Sécurité
Plusieurs dépôts ont reçu des mises à jour axées sur la sécurité :

- **OpenBao** [openbao](/repos/cloud-gouv/openbao) a été mis à jour vers Go 1.25.7 et `go.opentelemetry.io/otel/sdk` pour corriger des vulnérabilités de sécurité (CVE-2025-68121 / GO-2026-4337, CVE-2026-24051 / GO-2026-4394 / GHSA-9h8m-3fm2-qjrq).
- **Securix** [securix](/repos/cloud-gouv/securix) a supprimé le mode développeur et corrigé un bug lié à l'acceptation de mots de passe hachés vides, renforçant ainsi la sécurité du système.
- **Portail** [portail](/repos/cloud-gouv/portail) a activé le support mTLS (mutual TLS) côté serveur pour une communication plus sécurisée.

## Autres changements notables
- **k8s-cluster-api-helm-charts** [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) a amélioré la gestion des clusters Kubernetes sur Openstack et Outscale, notamment avec des corrections pour CoreDNS et la prise en charge du multi-tenant sur Outscale.
- **dockerfiles** [dockerfiles](/repos/cloud-gouv/dockerfiles) a ajouté l'outil `kustomize` à l'image `k8s-tools` et mis à niveau les versions des outils inclus.
- **OpenBao** [openbao](/repos/cloud-gouv/openbao) a corrigé des problèmes liés à l'auto-déverrouillage, à la révocation de baux et à l'invalidation du cache PKI, améliorant ainsi sa robustesse et sa fiabilité.

## Dépôts les plus actifs
- **OpenBao** [openbao](/repos/cloud-gouv/openbao) : Nombreuses corrections de bugs et mises à jour de sécurité pour améliorer la robustesse et la sécurité du gestionnaire de secrets.
- **Portail** [portail](/repos/cloud-gouv/portail) : Ajout de fonctionnalités de sécurité importantes avec le support mTLS et la redirection HTTP CONNECT.
- **k8s-cluster-api-helm-charts** [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Améliorations de la gestion des clusters Kubernetes sur différentes plateformes cloud.
- **Securix** [securix](/repos/cloud-gouv/securix) : Corrections de bugs, améliorations de la configuration et ajout de nouvelles fonctionnalités pour une meilleure expérience utilisateur et une sécurité accrue.
- **dockerfiles** [dockerfiles](/repos/cloud-gouv/dockerfiles) : Mise à jour des outils inclus dans l'image `k8s-tools` pour faciliter le déploiement d'applications Kubernetes.
