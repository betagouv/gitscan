# Synthèse d'activité : cloud-gouv (du 23/10 au 30/10)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par un renforcement significatif de la chaîne de déploiement et de l'automatisation DevOps. L'extension de la bibliothèque de conteneurs dans [dockerfiles](/repos/cloud-gouv/dockerfiles) et l'enrichissement du catalogue de déploiements via [common-helm-charts](/repos/cloud-gouv/common-helm-charts) permettent une mise en œuvre plus rapide, standardisée et sécurisée des services.

Parallèlement, l'organisation amorce le déploiement de plusieurs nouveaux services clés sur Kubernetes, notamment [openproject](/repos/cloud-gouv/openproject), [k8s-glpi](/repos/cloud-gouv/k8s-glpi) et [k8s-freescout](/repos/cloud-gouv/k8s-freescout). Ces évolutions visent à offrir une infrastructure plus robuste et automatisée, facilitant l'adoption de nouveaux outils de gestion et de collaboration par les utilisateurs finaux.

## Sécurité
- Correction de vulnérabilités (Go et OpenTelemetry) dans [openbao](/repos/cloud-gouv/openbao).
- Renforcement de la sécurité des workflows CI/CD via l'application de permissions restreintes par défaut dans [securix](/repos/cloud-gouv/securix).
- Amélioration de la gestion des clés de sécurité (Yubikey) dans [securix](/repos/cloud-gouv/securix).
- Intégration de l'outil d'analyse de vulnérabilités Grype dans [dockerfiles](/repos/cloud-gouv/dockerfiles).

## Autres changements notables
- **Expansion de l'outillage DevOps** : Amélioration de la gestion des déploiements avec OpenTofu et automatisation de la génération de SBOM (Software Bill of Materials) dans [dockerfiles](/repos/cloud-gouv/dockerfiles).
- **Mise à jour des infrastructures Kubernetes** : Adaptation des charts Helm pour assurer la compatibilité avec les nouveaux opérateurs et les environnements OpenStack dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).
- **Amélioration de la gouvernance et de la documentation** : Mise en place de la gestion des responsables de maintenance (`CODEOWNERS`) dans [portail](/repos/cloud-gouv/portail) et initialisation de la documentation pour plusieurs nouveaux projets comme [itsm-ng](/repos/cloud-gouv/itsm-ng) et [securix-infra-reference-implementation](/repos/cloud-gouv/securix-infra-reference-implementation).

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Amélioration de l'expérience de navigation web, de la sécurité des outils et de la stabilité système.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) : Extension majeure de la bibliothèque de conteneurs utilitaires et optimisation des pipelines CI/CD.
- [openbao](/repos/cloud-gouv/openbao) : Résolution de problèmes critiques liés au déverrouillage KMS et corrections de sécurité.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Enrichissement du catalogue de déploiements et amélioration du monitoring.
