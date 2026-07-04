# Synthèse d'activité : proconnect-gouv (du 28 avril 2026 au 2 juillet 2026)

## Résumé de l'activité
L'activité récente de l'organisation proconnect-gouv s'est concentrée sur l'amélioration de la sécurité, la correction de bugs et l'ajout de nouvelles fonctionnalités, notamment autour de l'authentification et de la gestion des utilisateurs. Plusieurs dépôts ont bénéficié de mises à jour pour supporter de nouveaux standards (eIDAS) et améliorer l'expérience utilisateur. L'équipe a également investi dans la modernisation de l'infrastructure et des dépendances pour assurer la stabilité et la performance des applications. Les dépôts [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) et [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) ont été particulièrement actifs.

## Sécurité
Plusieurs améliorations de sécurité ont été apportées :
- Restriction de l'accès en écriture à la base de données aux administrateurs et modérateurs dans [hyyypertool](/repos/proconnect-gouv/hyyypertool).
- Correction de vulnérabilités de dépendances dans [class-validator](/repos/proconnect-gouv/class-validator).

## Autres changements notables
- Migration du runtime vers Bun dans [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect) pour de meilleures performances.
- Mise à jour du schéma de la base de données pour la compatibilité avec PostgreSQL 17 dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Suppression de PM2 des images de production pour simplifier le déploiement dans [federation](/repos/proconnect-gouv/federation).
- Abaissement de la version de PostgreSQL à 16 pour alignement avec la production dans [federation](/repos/proconnect-gouv/federation).

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Amélioration de la gestion des utilisateurs, ajout de nouveaux niveaux d'ACR et correction de bugs.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Amélioration de la documentation eIDAS et correction de bugs liés à l'authentification.
- [federation](/repos/proconnect-gouv/federation) : Ajout de la gestion des collaborateurs et amélioration de l'interface d'administration.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs et correction de vulnérabilités.
- [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect) : Correction de bugs d'authentification et migration vers Bun.
