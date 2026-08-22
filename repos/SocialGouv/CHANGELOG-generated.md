# Synthèse d'activité : SocialGouv (du 14/08 au 21/08)

## Résumé de l'activité
L'activité de cette période est marquée par une accélération majeure sur l'intégration de l'intelligence artificielle et l'amélioration de l'analyse de code, notamment avec les évolutions de [iterion](/repos/SocialGouv/iterion) et [repo-falcon](/repos/SocialGouv/repo-falcon). Parallèlement, l'organisation concentre ses efforts sur la fiabilité des données et la stabilisation des parcours utilisateurs critiques, comme pour [egapro](/repos/SocialGouv/egapro) et [vao](/repos/SocialGouv/vao).

L'infrastructure globale connaît une modernisation profonde, caractérisée par une migration massive vers le gestionnaire de paquets `pnpm` pour optimiser les déploiements et une centralisation des services de build via [buildkit-operator](/repos/SocialGouv/buildkit-operator).

## Sécurité
- **Protection des données et vie privée** : Mise en place d'une protection automatisée des données personnelles (PII) par pseudonymisation et d'un coffre-fort chiffré dans [doublure](/repos/SocialGouv/doublure), ainsi que de nouvelles politiques contre l'exfiltration de données vers des IA dans [smart-allow](/repos/SocialGouv/smart-allow).
- **Correction de vulnérabilités critiques** : Résolution de failles d'injection SQL et de contournement d'authentification sur [infra-apps](/repos/SocialGouv/infra-apps) (Metabase), et corrections de vulnérabilités dans [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget) et [archifiltre-mails](/repos/SocialGouv/archifiltre-mails).
- **Durcissement des accès et protocoles** : Migration vers une authentification exclusivement basée sur OIDC dans [buildkit-operator](/repos/SocialGouv/buildkit-operator) et sécurisation des appels via certificat mTLS dans [egapro](/repos/SocialGouv/egapro).
- **Sécurisation des interfaces** : Protection renforcée contre les injections de commandes et les traversées de chemin dans [helmdex](/repos/SocialGouv/helmdex).

## Autres changements notables
- **Modernisation des outils de build** : Migration généralisée vers `pnpm` pour améliorer la performance et la gestion des dépendances ([revu](/repos/SocialGouv/revu), [matomo-next](/repos/SocialGouv/matomo-next), [jardinmental](/repos/SocialGouv/jardinmental), [enfants-du-spectacle](/repos/SocialGouv/enfants-du-spectacle)).
- **Évolution de l'architecture et de l'observabilité** : Renforcement de l'isolation des processus par sandboxing et intégration de l'observabilité (Sentry) pour [iterion](/repos/SocialGouv/iterion) et [infra-apps](/repos/SocialGouv/infra-apps).
- **Mises à jour technologiques majeures** : Migration de la stack vers Angular 20 et Node 22 pour [domifa](/repos/SocialGouv/domifa), et mise en place d'une architecture de déploiement Kubernetes/Helm robuste pour [mesure-impact](/repos/SocialGouv/mesure-impact).

## Dépôts les plus actifs
- [egapro](/repos/SocialGouv/egapro) : Stabilisation intensive des parcours de déclaration et alignement sur les maquettes de design.
- [iterion](/repos/SocialGouv/iterion) : Avancées majeures sur l'orchestration d'agents IA et la gestion des ressources.
- [buildkit-operator](/repos/SocialGouv/buildkit-operator) : Renforcement de la sécurité, de la gestion du cycle de vie des builds et de la flexibilité de configuration.
- [vao](/repos/SocialGouv/vao) : Amélioration du processus de gestion des premiers agréments pour les utilisateurs DREETS.
- [repo-falcon](/repos/SocialGouv/repo-falcon) : Évolutions significatives sur l'analyse de code et la génération de graphes de connaissances.
- [doublure](/repos/SocialGouv/doublure) : Développement de fonctionnalités de protection de la confidentialité et de gestion des politiques de données.
