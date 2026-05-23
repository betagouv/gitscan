# Synthèse d'activité : mission-apprentissage (du 2026-04-24 au 2026-05-23)

## Résumé de l'activité
L'organisation "mission-apprentissage" a connu une période d'activité soutenue, axée sur l'amélioration de la sécurité, de la performance et des fonctionnalités de ses différents outils. Des efforts importants ont été déployés pour renforcer la sécurité de l'infrastructure, notamment avec la migration vers SOPS pour la gestion des secrets et la correction de vulnérabilités critiques.  Plusieurs applications ont bénéficié d'améliorations fonctionnelles, comme l'ajout d'un classificateur de contacts dans [tableaudebord-lab](/repos/mission-apprentissage/tableaudebord-lab) et de nouvelles fonctionnalités sur [labonnealternance](/repos/mission-apprentissage/labonnealternance) et [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas), visant à améliorer l'expérience utilisateur et l'efficacité des processus. La surveillance de l'état des services a été renforcée avec des mises à jour régulières via [upptime](/repos/mission-apprentissage/upptime).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- Correction d'une vulnérabilité critique affectant la gestion des fragments TCP (Dirty Frag et Fragnesia) dans [infra](/repos/mission-apprentissage/infra).
- Migration de l'outil de scan de secrets de Talisman vers Gitleaks dans [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas).
- Épinglage de `handlebars` et `form-data` pour corriger des CVE critiques dans [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas).
- Configuration d'une autorité de certification pour l'authentification des membres d'une grappe MongoDB dans [mongodb](/repos/mission-apprentissage/mongodb).

## Autres changements notables
- Migration d'Ansible Vault vers SOPS pour une gestion des secrets plus sécurisée et flexible dans [infra](/repos/mission-apprentissage/infra).
- Mise à jour de Mongoose vers la version 9 et réécriture du plugin `diffHistory` dans [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage).
- Refactorisation des scripts de sauvegarde et de restauration de la base de données et mutualisation de code dans [mna-shared-bin](/repos/mission-apprentissage/mna-shared-bin).
- Remplacement de Mailhog par Mailpit pour les tests SMTP dans [voeux-affelnet](/repos/mission-apprentissage/voeux-affelnet).

## Dépôts les plus actifs
- [labonnealternance](/repos/mission-apprentissage/labonnealternance) : Amélioration continue de la plateforme avec de nouvelles fonctionnalités pour les candidats et les recruteurs, ainsi que des optimisations techniques.
- [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas) : Ajout de nouvelles fonctionnalités et corrections de bugs pour améliorer l'efficacité de la plateforme.
- [infra](/repos/mission-apprentissage/infra) : Améliorations significatives de la sécurité et de la gestion de l'infrastructure.
- [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage) : Corrections de bugs et améliorations techniques pour l'affichage et la synchronisation des données.
- [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) : Intégration d'un nouveau modèle d'apprentissage et amélioration du processus de CI/CD.
