# Synthèse d'activité : SocialGouv (du 01/09 au 22/09)

## Résumé de l'activité
L'activité récente de SocialGouv est marquée par une accélération majeure des capacités d'intelligence artificielle, tant pour l'automatisation de l'accessibilité avec [ultra11y](/repos/SocialGouv/ultra11y) que pour l'analyse de code et l'orchestration d'agents avec [repo-falcon](/repos/SocialGouv/repo-falcon), [iterion](/repos/SocialGouv/iterion) et [claw-code-go](/repos/SocialGouv/claw-code-go). Ces évolutions permettent de passer d'une simple détection à une capacité de proposition de corrections et d'analyse sémantique approfondie.

Parallèlement, l'organisation assure la pérennité de ses services par des migrations d'infrastructure critiques et une gestion rigoureuse du cycle de vie des produits, incluant l'annonce de fermetures prochaines pour [recosante](/repos/SocialGouv/recosante), [nos1000jours-landing](/repos/SocialGouv/nos1000jours-landing) et [fce](/repos/SocialGouv/fce). L'accent est mis sur la robustesse des plateformes de déploiement et la sécurisation des échanges de données avec les modèles d'IA.

## Sécurité
- **Protection des données et confidentialité** : Mise en place d'un coffre-fort chiffré (AES-256-GCM) et de mécanismes de protection des données sensibles (PII) avec [doublure](/repos/SocialGouv/doublure), ainsi que de politiques contre l'exfiltration de données vers des fournisseurs d'IA avec [smart-allow](/repos/SocialGouv/smart-allow).
- **Authentification et contrôle d'accès** : Migration vers une authentification basée sur OIDC pour [buildkit-operator](/repos/SocialGouv/buildkit-operator) et renforcement de la sécurité contre les injections (shell, path traversal) avec [helmdex](/repos/SocialGouv/helmdex).
- **Corrections de vulnérabilités** : Diverses corrections de sécurité ont été appliquées à [archifiltre-mails](/repos/SocialGouv/archifiltre-mails), [archifiltre-docs](/repos/SocialGouv/archifiltre-docs) et [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget).

## Autres changements notables
- **Migrations technologiques majeures** : Adoption massive de l'outil de gestion de paquets `pnpm` ([matomo-next](/repos/SocialGouv/matomo-next), [jardinmental](/repos/SocialGouv/jardinmental), [enfants-du-spectacle](/repos/SocialGouv/enfants-du-spectacle)) et migration vers Nuxt v4 et Node 24 pour [vao](/repos/SocialGouv/vao).
- **Infrastructure et déploiement** : Optimisation des chaînes de livraison via [buildkit-operator](/repos/SocialGouv/buildkit-operator), structuration multi-produits avec [mesure-impact](/repos/SocialGouv/mesure-impact) et stabilisation de la plateforme [infra-apps](/repos/SocialGouv/infra-apps).
- **Intelligence Artificielle et Données** : Refonte de l'intelligence d'extraction pour le Journal Officiel avec [questions-ecrites](/repos/SocialGouv/questions-ecrites) et création d'outils d'extraction de données d'accessibilité pour les assistants IA avec [dsfr-mcp](/repos/SocialGouv/dsfr-mcp).

## Dépôts les plus actifs
- [ultra11y](/repos/SocialGouv/ultra11y) : Avancées majeures dans l'automatisation des audits d'accessibilité RGAA et l'optimisation des coûts d'IA.
- [domifa](/repos/SocialGouv/domifa) : Améliorations significatives de l'expérience utilisateur, des performances et de l'infrastructure.
- [buildkit-operator](/repos/SocialGouv/buildkit-operator) : Renforcement de la sécurité (OIDC) et de la fiabilité des processus de build.
- [questions-ecrites](/repos/SocialGouv/questions-ecrites) : Refonte profonde de l'IA (modèle Albert) et de la base de données pour l'extraction de données.
- [iterion](/repos/SocialGouv/iterion) : Migration vers un nouveau DSL et stabilisation de la plateforme d'agents.
