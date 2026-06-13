# Synthèse d'activité : proconnect-gouv (du 22 mai 2026 au 12 juin 2026)

## Résumé de l'activité
L'activité récente de l'organisation proconnect-gouv s'est concentrée sur l'amélioration de la sécurité, la correction de bugs et l'ajout de nouvelles fonctionnalités, notamment dans les domaines de l'authentification, de la gestion des utilisateurs et de la validation de données. Plusieurs dépôts ont bénéficié de mises à jour significatives, comme [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) avec des améliorations de la modération et de la migration des emails, et [hyyypertool](/repos/proconnect-gouv/hyyypertool) avec des ajouts d'informations utilisateur et des optimisations de sécurité. La librairie [class-validator](/repos/proconnect-gouv/class-validator) a également été enrichie de nouveaux validateurs pour une validation de données plus complète.

## Sécurité
Plusieurs dépôts ont reçu des mises à jour axées sur la sécurité :
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) a implémenté une limitation de débit (rate limiting) basée sur l'adresse IP.
- [class-validator](/repos/proconnect-gouv/class-validator) a corrigé des vulnérabilités de dépendances.
- [federation](/repos/proconnect-gouv/federation) a bénéficié de mises à jour de l'infrastructure avec Node 24.16.

## Autres changements notables
- Migration de [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect) vers un runtime Bun natif pour améliorer les performances.
- Refactorisation de la documentation eIDAS dans [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires).
- Remplacement de `resolveMx` par une requête DNS-over-HTTPS dans le validateur d'email de [federation](/repos/proconnect-gouv/federation).

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Amélioration de la modération, migration des emails et optimisations de la base de données.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Ajout d'informations utilisateur, amélioration de l'interface et renforcement de la sécurité.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs et correction de vulnérabilités.
- [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect) : Correction de bugs d'authentification et migration vers Bun.
- [federation](/repos/proconnect-gouv/federation) : Amélioration de l'autocomplétion des mots de passe et mises à jour de l'infrastructure.
