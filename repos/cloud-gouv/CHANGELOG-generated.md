# Synthèse d'activité : cloud-gouv (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité de la période est marquée par une montée en maturité significative des outils de gestion et de sécurité. L'organisation renforce ses capacités de surveillance, de documentation et de gestion des flux, notamment avec [portail](/repos/cloud-gouv/portail), tout en étendant son support matériel et ses capacités d'intégration avec [securix](/repos/cloud-gouv/securix).

Parallèlement, l'écosystème de déploiement s'enrichit grâce à l'expansion des catalogues de services ([common-helm-charts](/repos/cloud-gouv/common-helm-charts), [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts)) et à l'optimisation des images de conteneurs ([dockerfiles](/repos/cloud-gouv/dockerfiles)). L'initiation de nouveaux projets comme [openproject](/repos/cloud-gouv/openproject) et [playground-public](/repos/cloud-gouv/playground-public) témoigne également d'une dynamique d'expansion de l'offre et des environnements d'expérimentation.

## Sécurité
- [openbao](/repos/cloud-gouv/openbao) : Correction de vulnérabilités via la mise à jour de Go et d'OpenTelemetry, et résolution de problèmes liés aux montages de groupes d'identité.
- [securix](/repos/cloud-gouv/securix) : Ajout du support pour les puces de sécurité matérielles P14SG6 pour l'authentification.
- [portail](/repos/cloud-gouv/portail) : Mise en place de notifications automatiques en cas d'échec de la négociation TLS.

## Autres changements notables
- **Infrastructure et Déploiement** : Extension du catalogue de composants ([common-helm-charts](/repos/cloud-gouv/common-helm-charts)), optimisation de la taille des images Docker ([dockerfiles](/repos/cloud-gouv/dockerfiles)) et mise à jour de la compatibilité des charts Helm pour Cluster API ([k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts)).
- **Documentation et Standardisation** : Efforts majeurs de documentation multilingue et exhaustive ([portail](/repos/cloud-gouv/portail)) et initialisation de nouveaux dépôts de référence ([securix-infra-reference-implementation](/repos/cloud-gouv/securix-infra-reference-implementation), [itsm-ng](/repos/cloud-gouv/itsm-ng)).
- **Maintenance Système** : Mise à jour de logiciels majeurs et amélioration de la compatibilité avec le compilateur GCC 15 dans [nixpkgs](/repos/cloud-gouv/nixpkgs).

## Dépôts les plus actifs
- [portail](/repos/cloud-gouv/portail) : Amélioration majeure de la surveillance, de la gestion des logs et de la documentation.
- [openbao](/repos/cloud-gouv/openbao) : Travaux intensifs sur la correction de bugs critiques et la sécurité.
- [securix](/repos/cloud-gouv/securix) : Évolutions fonctionnelles liées à la gestion centralisée et au support matériel.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Enrichissement du catalogue de déploiement et optimisation du monitoring.
