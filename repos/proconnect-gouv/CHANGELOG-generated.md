# Synthèse d'activité : proconnect-gouv (du 01/10 au 14/10/2026)

## Résumé de l'activité
L'activité de cette période est marquée par un renforcement significatif de la sécurité des accès et de la protection des données pour les utilisateurs. Les efforts se sont concentrés sur l'amélioration de l'expérience de connexion (MFA, 2FA) et la fiabilité des informations collectées, notamment via l'intégration de nouvelles sources de données comme l'API RNE dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).

Parallèlement, l'organisation a lancé plusieurs nouveaux outils et services pour enrichir son écosystème, tels que le thème visuel [tailwindcss-dsfr-theme](/repos/proconnect-gouv/tailwindcss-dsfr-theme) et le service de résolution DNS [mx-resolver](/repos/proconnect-gouv/mx-resolver). L'expérience utilisateur a également été affinée avec des traductions et des améliorations d'interface dans [monitoring-pinger](/repos/proconnect-gouv/monitoring-pinger) et [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect).

## Sécurité
- Renforcement de l'authentification avec l'imposition du 2FA par organisation et la vérification du MFA dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) et [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires).
- Amélioration de la sécurité des accès via la restriction des rôles dans [federation](/repos/proconnect-gouv/federation) et l'application du principe de moindre privilège sur les scopes dans [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- Correction de vulnérabilités de dépendances dans [class-validator](/repos/proconnect-gouv/class-validator).

## Autres changements notables
- Refonte majeure de la suite de tests automatisés et optimisation de la CI/CD (sharding) pour [hyyypertool](/repos/proconnect-gouv/hyyypertool).
- Migration vers l'API RNE pour la gestion des informations d'organisation dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Initialisation de plusieurs nouveaux projets : [tailwindcss-dsfr-theme](/repos/proconnect-gouv/tailwindcss-dsfr-theme), [proconnect-test-idp](/repos/proconnect-gouv/proconnect-test-idp), [mx-resolver](/repos/proconnect-gouv/mx-resolver) et [bun-buildpack](/repos/proconnect-gouv/bun-buildpack).
- Amélioration des capacités de gestion des releases et de la lisibilité des logs de workflow dans [release-action](/repos/proconnect-gouv/release-action).

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Travaux intensifs sur la sécurité, la gestion des données et l'infrastructure.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Amélioration de la sécurité des comptes et mise à jour majeure de la documentation métier.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Stabilisation via une refonte des tests et optimisation des processus de déploiement.
- [release-action](/repos/proconnect-gouv/release-action) : Développement de nouvelles fonctionnalités de gestion de branches et de génération de changelogs.
