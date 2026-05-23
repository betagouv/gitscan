# Synthèse d'activité : proconnect-gouv (du 07 mai au 16 mars 2026)

## Résumé de l'activité
L'activité récente de l'organisation proconnect-gouv s'est concentrée sur l'amélioration de la sécurité, la maintenance et l'ajout de nouvelles fonctionnalités à ses différents composants. Des efforts importants ont été déployés pour préparer la plateforme à la production et à la maintenance, notamment avec l'ajout d'une page de maintenance [proconnect-maintenance](/repos/proconnect-gouv/proconnect-maintenance) et l'implémentation d'un mode maintenance pour l'espace partenaires [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires).  Des améliorations significatives ont également été apportées à la validation des données et à l'expérience utilisateur, en particulier dans les composants `docteur-proconnect` [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect) et `federation` [federation](/repos/proconnect-gouv/federation). L'initialisation de nouveaux projets comme `proconnect-test-idp` [proconnect-test-idp](/repos/proconnect-gouv/proconnect-test-idp) et `mx-resolver` [mx-resolver](/repos/proconnect-gouv/mx-resolver) pose les bases pour de futurs développements.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction de vulnérabilités de dépendances dans [class-validator](/repos/proconnect-gouv/class-validator).
- Mise à jour des dépendances dans [proconnect-test-client](/repos/proconnect-gouv/proconnect-test-client) pour bénéficier des dernières corrections de bugs et améliorations de sécurité.
- Implémentation d'une limitation de débit par adresse IP dans [hyyypertool](/repos/proconnect-gouv/hyyypertool) pour renforcer la sécurité.

## Autres changements notables
- Migration des emails de MonComptePro vers un nouveau système dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Refonte de la validation d'email et amélioration de la configuration OIDC dans [federation](/repos/proconnect-gouv/federation).
- Rétrogradation de la version de Node dans les conteneurs Docker de [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) suite à des problèmes de compatibilité.
- Ajout de nouveaux validateurs (IBAN, ISO 639-1, ISO 3166-1, UUID) et d'une option de validation conditionnelle dans [class-validator](/repos/proconnect-gouv/class-validator).

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Amélioration de la sécurité, préparation de la migration des emails et ajustements pour la pré-production.
- [federation](/repos/proconnect-gouv/federation) : Amélioration de la sécurité, de la flexibilité et de la configuration OIDC.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Ajout d'un mode maintenance, amélioration de la documentation et correction de problèmes d'intégration.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs et correction de vulnérabilités de dépendances.
- [proconnect-test-client](/repos/proconnect-gouv/proconnect-test-client) : Mise à jour des dépendances pour améliorer la sécurité et la stabilité.
