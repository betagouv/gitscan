# Synthèse d'activité : cloud-gouv (du 23/10 au 29/10/2026)

## Résumé de l'activité
L'activité de l'organisation est marquée par une forte dynamique d'expansion de l'écosystème de services cloud-native, avec l'initialisation de nouveaux projets ([openproject](/repos/cloud-gouv/openproject), [k8s-glpi](/repos/cloud-gouv/k8s-glpi), [k8s-freescout](/repos/cloud-gouv/k8s-freescout)) et l'enrichissement du catalogue de déploiements ([common-helm-charts](/repos/cloud-gouv/common-helm-charts)).

Parallèlement, un effort majeur est porté sur la fiabilisation et la sécurisation de l'infrastructure. Cela se traduit par le renforcement de la chaîne de production et de l'observabilité dans [dockerfiles](/repos/cloud-gouv/dockerfiles) et [securix](/repos/cloud-gouv/securix), ainsi que par des corrections de sécurité critiques et une amélioration de la gestion des accès dans [openbao](/repos/cloud-gouv/openbao) et [portail](/repos/cloud-gouv/portail).

## Sécurité
- Correction d'une vulnérabilité de sécurité (CVE-2025-68121) via la mise à jour de Go dans [openbao](/repos/cloud-gouv/openbao).
- Résolution de problèmes critiques liés à l'auto-déverrouillage KMS dans [openbao](/repos/cloud-gouv/openbao).
- Renforcement des permissions des GitHub Actions pour limiter les risques d'exploitation dans [securix](/repos/cloud-gouv/securix).
- Amélioration de la précision des règles d'accès (ACL) par la normalisation des noms d'hôtes dans [portail](/repos/cloud-gouv/portail).
- Intégration de nouveaux outils d'analyse de vulnérabilités (grype) et de validation de schémas dans [dockerfiles](/repos/cloud-gouv/dockerfiles).

## Autres changements notables
- Optimisation de la chaîne CI/CD et de la gestion des SBOM (Software Bill of Materials) avec l'ajout de nouveaux conteneurs de linting et d'analyse dans [dockerfiles](/repos/cloud-gouv/dockerfiles).
- Mise à jour majeure de la compatibilité avec l'opérateur Cluster API et les ressources OpenStack dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).
- Extension du catalogue de services avec l'ajout de nouveaux composants et l'amélioration du monitoring dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts).
- Amélioration de l'expérience de navigation web et introduction d'un système de télémétrie communautaire dans [securix](/repos/cloud-gouv/securix).

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Évolutions sur la navigation web, la connectivité réseau et la télémétrie.
- [openbao](/repos/cloud-gouv/openbao) : Corrections critiques sur le déverrouillage KMS, la gestion des baux et la sécurité.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) : Renforcement de la sécurité et de la qualité des pipelines de construction.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Extension du catalogue de services et amélioration du monitoring.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Mise à jour de la compatibilité pour les déploiements Kubernetes et OpenStack.
