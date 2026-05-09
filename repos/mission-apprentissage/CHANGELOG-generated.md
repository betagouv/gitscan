# Synthèse d'activité : mission-apprentissage (du 24/04 au 24/05)

## Résumé de l'activité
L'organisation mission-apprentissage a connu une période d'activité soutenue, axée sur l'amélioration de la sécurité, de la performance et des fonctionnalités de ses différentes plateformes. Des efforts importants ont été déployés pour renforcer la sécurité des données, notamment avec la migration vers SOPS pour la gestion des secrets et l'ajout d'une autorité de certification pour MongoDB [mongodb](/repos/mission-apprentissage/mongodb).  Les plateformes "La Bonne Alternance" [labonnealternance](/repos/mission-apprentissage/labonnealternance) et "Flux Retour CFAS" [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas) ont bénéficié de nouvelles fonctionnalités et d'optimisations pour améliorer l'expérience utilisateur et l'efficacité des services. L'infrastructure [infra](/repos/mission-apprentissage/infra) a également été renforcée avec des mises à jour de sécurité et une meilleure gestion des accès.

## Sécurité
Plusieurs changements ont été apportés pour améliorer la sécurité :
- Migration de la gestion des secrets d'Ansible Vault vers SOPS [infra](/repos/mission-apprentissage/infra).
- Ajout d'une autorité de certification pour l'authentification des membres d'un cluster MongoDB [mongodb](/repos/mission-apprentissage/mongodb).
- Correction de vulnérabilités de sécurité dans les dépendances Handlebars et form-data [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas).
- Mise à jour des images Docker de Nginx et ModSecurity-CRS pour bénéficier des dernières corrections de sécurité [infra](/repos/mission-apprentissage/infra).

## Autres changements notables
- Refactorisation générale du code et correction de scripts de sauvegarde/restauration dans [mna-shared-bin](/repos/mission-apprentissage/mna-shared-bin).
- Migration de la gestion des secrets d'Ansible Vault vers SOPS et amélioration du processus de CI/CD dans [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab).
- Mise à jour de Mongoose vers la version 9 et réécriture du plugin `diffHistory` dans [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage).

## Dépôts les plus actifs
- [labonnealternance](/repos/mission-apprentissage/labonnealternance) : Amélioration de la recherche d'alternances, intégration de nouveaux flux d'offres et ajout de pages SEO.
- [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas) : Ajout de nouvelles collaborations, intégration de Crisp pour le support utilisateur et enrichissement des exports utilisateurs.
- [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage) : Corrections d'affichage et de périmètre, ajout d'options de configuration et amélioration de la synchronisation avec Elasticsearch.
- [infra](/repos/mission-apprentissage/infra) : Amélioration de la sécurité et de la gestion des accès, migration vers SOPS et mises à jour de sécurité.
- [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) : Intégration d'un nouveau modèle d'apprentissage, amélioration du processus de CI/CD et correction de bugs.
