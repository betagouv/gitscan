# Synthèse d'activité : proconnect-gouv (du 05/05 au 18/06 2026)

## Résumé de l'activité
L'activité récente de l'organisation proconnect-gouv s'est concentrée sur l'amélioration de la sécurité, la correction de bugs et l'ajout de nouvelles fonctionnalités aux services existants. Plusieurs dépôts ont bénéficié de mises à jour pour supporter l'authentification multi-facteurs (MFA), simplifier l'inscription des utilisateurs, et améliorer la gestion des erreurs. L'accent a également été mis sur la modernisation de l'infrastructure et des dépendances, notamment avec l'adoption de Bun pour certains projets. Les améliorations apportées à [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) et [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) sont particulièrement notables, impactant directement l'expérience utilisateur et la sécurité des plateformes.

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité :
- Suppression d'anciennes adresses IP dans [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) pour améliorer la sécurité.
- Mise à jour de dépendances vulnérables dans [class-validator](/repos/proconnect-gouv/class-validator) pour corriger des failles de sécurité.
- Renforcement de l'authentification multi-facteurs (MFA) dans [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires).

## Autres changements notables
- Migration de la base de données MongoDB dans [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) vers "corev2" avec un nouvel utilisateur.
- Migration de l'application [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect) vers un runtime Bun natif sur l'environnement Scalingo-24 pour améliorer les performances.
- Refonte de l'interface d'administration de [federation](/repos/proconnect-gouv/federation) avec une nouvelle identité visuelle (ProConnect remplace FranceConnect).
- Préparation de la base de données [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) pour la compatibilité avec PostgreSQL 17.
- Suppression du proxy HTTP BridgeRie dans [federation](/repos/proconnect-gouv/federation).

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Amélioration de la validation des utilisateurs et ajout de nouvelles catégories juridiques.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Amélioration de la documentation eIDAS/ANSSI et renforcement de l'authentification MFA.
- [federation](/repos/proconnect-gouv/federation) : Refonte de l'interface d'administration et améliorations techniques de l'infrastructure.
- [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect) : Corrections de bugs liés à l'authentification OIDC et migration vers Bun.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs et correction de vulnérabilités.
