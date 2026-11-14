# Synthèse d'activité : proconnect-gouv (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une forte dynamique d'innovation avec le lancement de plusieurs nouveaux outils destinés à simplifier le développement et l'intégration des standards de l'État, notamment via [tailwindcss-dsfr-theme](/repos/proconnect-gouv/tailwindcss-dsfr-theme), [mx-resolver](/repos/proconnect-gouv/mx-resolver) et le [bun-buildpack](/repos/proconnect-gouv/bun-buildpack). Ces nouveaux services permettent une mise en œuvre plus rapide et standardisée des projets tout en facilitant les environnements de test avec [proconnect-test-idp](/repos/proconnect-gouv/proconnect-test-idp).

Par ailleurs, des avancées majeures ont été réalisées pour renforcer la sécurité et la fiabilité des services existants. L'amélioration des processus d'authentification (MFA, mots de récupération) dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) et [federation](/repos/proconnect-gouv/federation), ainsi que la fiabilisation de la gestion des domaines dans [api-partenaires](/repos/proconnect-gouv/api-partenaires), garantissent une expérience utilisateur plus sécurisée et transparente.

## Sécurité
- Renforcement de la sécurité des comptes via l'introduction de mots de récupération, l'obligation du MFA et des notifications par email dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Sécurisation de la configuration de l'authentification LemonLDAP dans [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires).
- Amélioration de la sécurité de la fédération par la validation des noms de fournisseurs et la liaison des sessions OIDC dans [federation](/repos/proconnect-gouv/federation).
- Renforcement de la validation des domaines et application du principe de moindre privilège sur les rôles dans [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- Mise à jour des configurations `.well-known` pour l'alignement avec les standards d'authentification dans [proconnect-maintenance](/repos/proconnect-gouv/proconnect-maintenance).
- Correction de vulnérabilités de dépendances dans [class-validator](/repos/proconnect-gouv/class-validator).

## Autres changements notables
- **Modernisation des architectures et de l'observabilité** : Adoption de frameworks modernes (Hono) et de standards d'observabilité (OpenTelemetry, logs JSON) dans [proconnect-test-client](/repos/proconnect-gouv/proconnect-test-client) et [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- **Évolutions d'infrastructure et de CI/CD** : Migration vers Node.js 26 dans [federation](/repos/proconnect-gouv/federation), mise en place d'un preset Renovate partagé dans [renovate-config](/repos/proconnect-gouv/renovate-config) et optimisation des pipelines de qualité avec oxlint dans [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect).
- **Optimisation des outils de développement** : Amélioration de la gestion des releases et du nettoyage des branches avec [release-action](/repos/proconnect-gouv/release-action), et modernisation de la suite de tests via Buncept et le partitionnement dans [hyyypertool](/repos/proconnect-gouv/hyyypertool).

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Évolutions majeures sur la sécurité, l'expérience utilisateur et l'observabilité.
- [federation](/repos/proconnect-gouv/federation) : Ajout de fonctionnalités de statistiques, support multi-appareils et mises à jour d'infrastructure.
- [api-partenaires](/repos/proconnect-gouv/api-partenaires) : Renforcement de la validation des données et alignement sur les standards officiels.
- [release-action](/repos/proconnect-gouv/release-action) : Amélioration significative de la gestion des releases et de la lisibilité des changelogs.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Amélioration de la traçabilité et modernisation de la suite de tests.
