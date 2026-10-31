# Synthèse d'activité : cloud-gouv (du 22/10 au 29/10)

## Résumé de l'activité
L'activité de l'organisation a été marquée par une forte dynamique d'expansion de l'écosystème Kubernetes. Plusieurs nouveaux projets ont été initialisés pour faciliter le déploiement de services clés comme [openproject](/repos/cloud-gouv/openproject), [k8s-glpi](/repos/cloud-gouv/k8s-glpi) et [k8s-freescout](/repos/cloud-gouv/k8s-freescout), offrant ainsi des bases prêtes à l'emploi pour les utilisateurs.

Parallèlement, l'organisation a renforcé ses capacités de déploiement et de gestion d'infrastructure. L'enrichissement du catalogue de déploiements via [common-helm-charts](/repos/cloud-gouv/common-helm-charts) et l'introduction de nouvelles images spécialisées dans [dockerfiles](/repos/cloud-gouv/dockerfiles) permettent une automatisation plus poussée et une meilleure traçabilité des composants logiciels utilisés par les clients finaux.

## Sécurité
- Renforcement de la sécurité des workflows de développement via l'application de permissions restreintes par défaut sur GitHub Actions dans [securix](/repos/cloud-gouv/securix).
- Amélioration de la robustesse de la gestion des secrets avec des correctifs critiques sur l'auto-déverrouillage KMS et la gestion des identités dans [openbao](/repos/cloud-gouv/openbao).
- Sécurisation des accès par une meilleure précision des règles d'accès (ACL) grâce à la normalisation des noms d'hôtes dans [portail](/repos/cloud-gouv/portail).

## Autres changements notables
- Évolution majeure de la gestion des paquets avec une migration structurelle et une compatibilité accrue avec les nouveaux compilateurs dans [nixpkgs](/repos/cloud-gouv/nixpkgs).
- Mise en conformité des outils de déploiement avec les dernières versions de l'opérateur Cluster API et des ressources OpenStack dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).
- Amélioration de la traçabilité logicielle avec l'intégration de la génération de SBOM (Software Bill of Materials) dans les nouvelles images OpenTofu de [dockerfiles](/repos/cloud-gouv/dockerfiles).

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Amélioration de l'expérience de navigation web et de la stabilité des outils de sécurité.
- [openbao](/repos/cloud-gouv/openbao) : Corrections importantes sur la gestion des secrets et la robustesse de l'infrastructure.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Extension du catalogue de composants et amélioration des capacités de monitoring.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Mise à jour majeure des versions d'API pour assurer la compatibilité infrastructurelle.
