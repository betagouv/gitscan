# Synthèse d'activité : SocialGouv (du 01/09 au 31/10/2026)

## Résumé de l'activité
L'activité de l'organisation est marquée par une accélération majeure de l'intégration de l'intelligence artificielle, avec des avancées significatives sur les capacités d'analyse, de génération de code et de recherche juridique via [iterion](/repos/SocialGouv/iterion), [claw-code-go](/repos/SocialGouv/claw-code-go) et [srdt](/repos/SocialGouv/srdt). Parallèlement, une modernisation profonde des infrastructures est en cours, notamment avec la migration vers de nouveaux systèmes de stockage et l'adoption généralisée de nouveaux gestionnaires de paquets pour stabiliser les environnements de production.

On note également une phase de gestion du cycle de vie des services, avec l'annonce de la fermeture prochaine de plusieurs applications ([recosante](/repos/SocialGouv/recosante), [nos1000jours-landing](/repos/SocialGouv/nos1000jours-landing), [fce](/repos/SocialGouv/fce)). L'accent est mis sur l'accessibilité (RGAA) et la fiabilité des données pour les utilisateurs finaux.

## Sécurité
- Renforcement de la protection des données sensibles par la pseudonymisation automatique et le chiffrement AES-256 dans [doublure](/repos/SocialGouv/doublure).
- Mise en place de politiques de sécurité contre l'exfiltration de données vers des fournisseurs d'IA dans [smart-allow](/repos/SocialGouv/smart-allow).
- Durcissement de l'authentification via le passage à l'OIDC dans [buildkit-operator](/repos/SocialGouv/buildkit-operator) et [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example).
- Amélioration de la sécurité des comptes usagers (gestion des mots de passe et historique) dans [domifa](/repos/SocialGouv/domifa).
- Protection contre les injections et les attaques CSRF/CSP dans [helmdex](/repos/SocialGouv/helmdex) et [egapro](/repos/SocialGouv/egapro).
- Suppression des utilisateurs de base de données statiques pour renforcer la sécurité dans [vao](/repos/SocialGouv/vao).
- Correction de vulnérabilités de sécurité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails) et [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget).

## Autres changements notables
- **Infrastructure et Stockage** : Migration massive de l'infrastructure de stockage de MinIO vers SeaweedFS dans [infra-apps](/repos/SocialGouv/infra-apps).
- **Intelligence Artificielle** : Évolutions majeures des capacités avec le support de nouveaux modèles (GPT-6, Opus 5.5) dans [claw-code-go](/repos/SocialGouv/claw-code-go) et [iterion](/repos/SocialGouv/iterion), ainsi que l'optimisation de la recherche vectorielle via pgvector dans [questions-ecrites](/repos/SocialGouv/questions-ecrites).
- **Modernisation technique** : Passage à Nuxt v4 dans [vao](/repos/SocialGouv/vao) et adoption généralisée de `pnpm` pour la gestion des dépendances ([matomo-next](/repos/SocialGouv/matomo-next), [jardinmental](/repos/SocialGouv/jardinmental), [enfants-du-spectacle](/repos/SocialGouv/enfants-du-spectacle)).
- **Développement d'outils** : Lancement de nouveaux projets comme [git-ai-trace](/repos/SocialGouv/git-ai-trace) pour le suivi de la collaboration humain-IA et [metabase-datasource-sync](/repos/SocialGouv/metabase-datasource-sync) pour la synchronisation de données.

## Dépôts les plus actifs
- [vao](/repos/SocialGouv/vao) : Travaux intensifs sur la gestion de l'hébergement, la création de sites et la migration technique majeure.
- [srdt](/repos/SocialGouv/srdt) : Amélioration continue de la précision de l'IA juridique et de l'expérience utilisateur.
- [iterion](/repos/SocialGouv/iterion) : Développement de fonctionnalités avancées de supervision, de sécurité et de routage IA.
- [infra-apps](/repos/SocialGouv/infra-apps) : Migration de stockage et optimisation des capacités de calcul (runners).
- [claw-code-go](/repos/SocialGouv/claw-code-go) : Extension du support des modèles d'IA et fiabilisation de l'exécution de commandes.
- [domifa](/repos/SocialGouv/domifa) : Refonte de l'interface et gestion renforcée des bénéficiaires et de la sécurité.
- [kube-image-keeper](/repos/SocialGouv/kube-image-keeper) : Améliorations de la flexibilité du mirroring d'images et de la documentation.
