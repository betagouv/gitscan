# Synthèse d'activité : cloud-gouv (du 07/10 au 21/10)

## Résumé de l'activité
L'organisation a connu une phase d'expansion importante avec l'initialisation de plusieurs nouveaux projets visant à faciliter le déploiement d'outils de gestion sur Kubernetes, notamment [openproject](/repos/cloud-gouv/openproject), [k8s-glpi](/repos/cloud-gouv/k8s-glpi) et [k8s-freescout](/repos/cloud-gouv/k8s-freescout). Cette dynamique renforce la capacité de l'organisation à proposer des solutions de gestion de parc et de services prêtes pour le cloud.

En parallèle, l'écosystème d'infrastructure et de déploiement s'est enrichi avec l'ajout de nouveaux composants dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts) et la création d'une image Docker optimisée pour OpenTofu dans [dockerfiles](/repos/cloud-gouv/dockerfiles). Ces évolutions permettent une meilleure automatisation et une gestion plus fine des environnements de production.

## Sécurité
- Correction de vulnérabilités via la mise à jour de Go et OpenTelemetry dans [openbao](/repos/cloud-gouv/openbao).
- Renforcement de la précision des règles de filtrage d'accès par la normalisation des noms d'hôtes dans [portail](/repos/cloud-gouv/portail).
- Amélioration de la fiabilité du déverrouillage automatique (KMS) et de la gestion du cache PKI dans [openbao](/repos/cloud-gouv/openbao).
- Optimisation de la sécurité des connexions IPsec via une meilleure gestion des noms de domaine dans [securix](/repos/cloud-gouv/securix).

## Autres changements notables
- Amélioration de la robustesse de [securix](/repos/cloud-gouv/securix), notamment sur la fiabilité des mises à jour automatiques et l'optimisation des performances CPU.
- Évolutions techniques majeures de [nixpkgs](/repos/cloud-gouv/nixpkgs) pour assurer la compatibilité avec GCC 15 et le support de nouvelles architectures.
- Mise à jour de la compatibilité des charts Helm pour l'opérateur Cluster API et les ressources OpenStack dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).
- Introduction de la génération de SBOM (Software Bill of Materials) dans les nouvelles images OpenTofu de [dockerfiles](/repos/cloud-gouv/dockerfiles).

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Améliorations de l'interface utilisateur, de la fiabilité système et des outils de gestion de clés.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Extension du catalogue de déploiements et optimisation du monitoring.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs critiques et mises à jour de sécurité.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Maintenance de la compatibilité des API pour les déploiements Kubernetes et OpenStack.
