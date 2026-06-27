# Synthèse d'activité : proconnect-gouv (du 16 mars 2026 au 22 juin 2026)

## Résumé de l'activité
L'activité récente de l'organisation proconnect-gouv s'est concentrée sur l'amélioration de la sécurité, de la robustesse et de la fonctionnalité de ses différents services. Des progrès significatifs ont été réalisés sur [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) avec des améliorations de la gestion des ACR, de la limitation des tentatives de vérification par email et de la simplification de l'adhésion pour certaines organisations.  [hyyypertool](/repos/proconnect-gouv/hyyypertool) a bénéficié d'améliorations de sécurité et de nouvelles fonctionnalités pour la gestion des utilisateurs et des organisations. Plusieurs dépôts ont également reçu des mises à jour de dépendances pour maintenir la sécurité et la stabilité. L'initialisation de nouveaux projets comme [proconnect-test-idp](/repos/proconnect-gouv/proconnect-test-idp) et [mx-resolver](/repos/proconnect-gouv/mx-resolver) pose les bases pour de futurs développements.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Restriction des accès en écriture à la base de données aux rôles autorisés.
- [federation](/repos/proconnect-gouv/federation) : Suppression d'anciennes adresses IP et d'une exigence d'autorisation obsolète pour le scope `roles`.
- [class-validator](/repos/proconnect-gouv/class-validator) : Correction de vulnérabilités de dépendances.

## Autres changements notables
- Migration de [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect) vers un runtime Bun pour améliorer les performances.
- Préparation de la base de données de [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) pour la compatibilité avec PostgreSQL 17.
- Remplacement de `axios` par `fetch` dans [federation](/repos/proconnect-gouv/federation) pour améliorer les performances.
- Suppression de PM2 des images de production de [federation](/repos/proconnect-gouv/federation) pour simplifier le déploiement.

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Amélioration de la gestion des ACR, de la sécurité et de l'expérience utilisateur.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Ajout de fonctionnalités de sécurité, d'affichage d'informations et d'amélioration de l'interface utilisateur.
- [federation](/repos/proconnect-gouv/federation) : Amélioration de la recherche d'utilisateurs, de la gestion des collaborateurs et de la sécurité.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs et correction de vulnérabilités.
- [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect) : Correction de bugs d'authentification et migration vers Bun.
