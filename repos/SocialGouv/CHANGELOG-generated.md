# Synthèse d'activité : SocialGouv (du 01/08 au 28/08/2026)

## Résumé de l'activité
L'activité récente de SocialGouv est marquée par une intégration croissante de l'intelligence artificielle, tant dans les outils de développement avec [iterion](/repos/SocialGouv/iterion) que dans l'analyse de données avec [questions-ecrites](/repos/SocialGouv/questions-ecrites). Ces évolutions visent à automatiser des tâches complexes tout en garantissant une précision accrue des informations extraites des sources officielles.

Parallèlement, l'organisation poursuit la modernisation de ses infrastructures et la sécurisation de ses services, notamment par la migration vers de nouveaux standards de gestion de paquets et d'authentification, ainsi que par le renforcement de la protection des données sensibles.

## Sécurité
- Protection contre l'exfiltration de données vers des fournisseurs d'IA externes dans [smart-allow](/repos/SocialGouv/smart-allow).
- Protection et pseudonymisation automatique des données sensibles (PII) dans [doublure](/repos/SocialGouv/doublure).
- Migration vers une authentification basée exclusivement sur OIDC pour [buildkit-operator](/repos/SocialGouv/buildkit-operator) et [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example).
- Correction de vulnérabilités critiques (injection SQL, contournement OAuth) sur Metabase via [infra-apps](/repos/SocialGouv/infra-apps).
- Durcissement de la sécurité contre les injections et les conditions de concurrence dans [helmdex](/repos/SocialGouv/helmdex).
- Sécurisation des appels vers SUIT par l'implémentation du certificat client mTLS dans [egapro](/repos/SocialGouv/egapro).
- Correction de vulnérabilités de sécurité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails) et [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget).

## Autres changements notables
- Migration massive vers le gestionnaire de paquets `pnpm` pour améliorer la stabilité et la performance ([revu](/repos/SocialGouv/revu), [matomo-next](/repos/SocialGouv/matomo-next), [jardinmental](/repos/SocialGouv/jardinmental), [enfants-du-spectacle](/repos/SocialGouv/enfants-du-spectacle)).
- Consolidation de l'infrastructure de build via la migration vers [buildkit-operator](/repos/SocialGouv/buildkit-operator) ([vao](/repos/SocialGouv/vao), [srdt](/repos/SocialGouv/srdt), [infra-apps](/repos/SocialGouv/infra-apps), [cdtn-admin](/repos/SocialGouv/cdtn-admin)).
- Modernisation technologique majeure avec le passage à Angular 20 pour [domifa](/repos/SocialGouv/domifa) et l'adoption du modèle Albert pour l'IA dans [questions-ecrites](/repos/SocialGouv/questions-ecrites).
- Refonte technique de [smart-allow](/repos/SocialGouv/smart-allow) avec un portage du classificateur en Go pour optimiser les performances.
- Migration de l'environnement Python et Django pour [collecte-pro](/repos/SocialGouv/collecte-pro).

## Dépôts les plus actifs
- [vao](/repos/SocialGouv/vao) : Stabilisation du processus d'agrément pour les DREETS et améliorations du back-office.
- [domifa](/repos/SocialGouv/domifa) : Montée de version majeure vers Angular 20 et enrichissement de l'expérience utilisateur.
- [questions-ecrites](/repos/SocialGouv/questions-ecrites) : Optimisation de l'extraction de données du Journal Officiel via l'IA et refonte de la base de données.
- [iterion](/repos/SocialGouv/iterion) : Introduction de nouveaux agents IA et renforcement de la sécurité des sandboxes.
- [buildkit-operator](/repos/SocialGouv/buildkit-operator) : Amélioration de la gestion des ressources et de la flexibilité des builds.
- [cm2d](/repos/SocialGouv/cm2d) : Évolutions importantes de la cartographie (DROM) et de la granularité des données.
