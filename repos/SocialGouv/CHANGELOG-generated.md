# Synthèse d'activité : SocialGouv (du 01/09 au 10/09)

## Résumé de l'activité
L'activité récente de SocialGouv est marquée par une intégration massive de l'intelligence artificielle pour enrichir les capacités d'analyse, d'audit et d'extraction de données ([iterion](/repos/SocialGouv/iterion), [ultra11y](/repos/SocialGouv/ultra11y), [questions-ecrites](/repos/SocialGouv/questions-ecrites), [dsfr-mcp](/repos/SocialGouv/dsfr-mcp)). L'organisation poursuit la modernisation de ses outils avec le lancement d'applications desktop ([helmdex](/repos/SocialGouv/helmdex)) et l'amélioration de la visualisation de données ([cm2d](/repos/SocialGouv/cm2d)). 

Parallèlement, une transition vers des infrastructures plus robustes et isolées est en cours ([infra-apps](/repos/SocialGouv/infra-apps), [buildkit-operator](/repos/SocialGouv/buildkit-operator)), tandis que plusieurs services annoncent leur fermeture prochaine auprès des utilisateurs ([recosante](/repos/SocialGouv/recosante), [nos1000jours-landing](/repos/SocialGouv/nos1000jours-landing), [fce](/repos/SocialGouv/fce)).

## Sécurité
- Correction de vulnérabilités critiques (injection SQL, contournement OAuth) sur Metabase ([infra-apps](/repos/SocialGouv/infra-apps)).
- Renforcement de la protection des données sensibles via la pseudonymisation automatique (PII) et la lutte contre l'exfiltration de données vers des IA externes ([doublure](/repos/SocialGouv/doublure), [smart-allow](/repos/SocialGouv/smart-allow)).
- Migration vers une authentification plus robuste basée sur OIDC ([buildkit-operator](/repos/SocialGouv/buildkit-operator), [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example)).
- Corrections de sécurité sur les outils d'archivage ([archifiltre-mails](/repos/SocialGouv/archifiltre-mails), [archifiltre-docs](/repos/SocialGouv/archifiltre-docs)).

## Autres changements notables
- Migration massive vers le gestionnaire de paquets `pnpm` pour stabiliser les environnements et améliorer les performances ([matomo-next](/repos/SocialGouv/matomo-next), [jardinmental](/repos/SocialGouv/jardinmental), [enfants-du-spectacle](/repos/SocialGouv/enfants-du-spectacle)).
- Transition des services de build vers l'architecture `buildkit-operator` ([infra-apps](/repos/SocialGouv/infra-apps), [srdt](/repos/SocialGouv/srdt), [cdtn-admin](/repos/SocialGouv/cdtn-admin)).
- Évolutions technologiques majeures : passage à Nuxt v4 ([vao](/repos/SocialGouv/vao)), migration vers le modèle d'IA Albert ([questions-ecrites](/repos/SocialGouv/questions-ecrites)), et refonte de l'API via tRPC/Zod ([egapro](/repos/SocialGouv/egapro)).

## Dépôts les plus actifs
- [vao](/repos/SocialGouv/vao) : Modernisation de l'infrastructure et développement du module d'hébergement.
- [ultra11y](/repos/SocialGouv/ultra11y) : Amélioration de la précision des audits d'accessibilité par l'IA.
- [iterion](/repos/SocialGouv/iterion) : Extension des capacités d'analyse et renforcement de la résilience.
- [domifa](/repos/SocialGouv/domifa) : Optimisation de l'expérience utilisateur et de la performance de traitement.
- [buildkit-operator](/repos/SocialGouv/buildkit-operator) : Sécurisation et fiabilisation du cycle de vie des builds.
- [egapro](/repos/SocialGouv/egapro) : Lancement de l'observatoire et amélioration des parcours de déclaration.
