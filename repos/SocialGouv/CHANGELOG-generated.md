# Synthèse d'activité : SocialGouv (du 01/10 au 31/10/2026)

## Résumé de l'activité
L'activité de SocialGouv est marquée par une accélération majeure sur l'intégration de l'intelligence artificielle et le renforcement de la sécurité des données. Des avancées significatives ont été réalisées sur les outils d'assistance et d'analyse de code avec [iterion](/repos/SocialGouv/iterion), [claw-code-go](/repos/SocialGouv/claw-code-go) et [doublure](/repos/SocialGouv/doublure), offrant de nouvelles capacités de routage LLM, de génération de composants accessibles et de pseudonymisation automatique.

Parallèlement, l'organisation poursuit la modernisation de ses infrastructures (notamment via la migration vers SeaweedFS pour [infra-apps](/repos/SocialGouv/infra-apps)) et la gestion de la fin de vie de certains services comme [recosante](/repos/SocialGouv/recosante) ou [nos1000jours-landing](/repos/SocialGouv/nos1000jours-landing). L'accent est également mis sur la fiabilité des données juridiques et administratives à travers des cycles de mise à jour automatisés.

## Sécurité
- Renforcement de la protection des données sensibles via la pseudonymisation automatique (PII) et l'implémentation d'un coffre-fort chiffré en AES-256-GCM dans [doublure](/repos/SocialGouv/doublure).
- Amélioration de la sécurité applicative avec la mise en place de politiques de sécurité de contenu (CSP), du rate limiting et de la sécurisation des sessions dans [egapro](/repos/SocialGouv/egapro).
- Durcissement des politiques d'accès, de l'audit des comptes et de la gestion des mots de passe dans [domifa](/repos/SocialGouv/domifa).
- Migration vers une authentification basée exclusivement sur OIDC pour sécuriser les accès dans [buildkit-operator](/repos/SocialGouv/buildkit-operator) et [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example).
- Protection contre l'exfiltration de données vers des fournisseurs d'IA externes dans [smart-allow](/repos/SocialGouv/smart-allow).
- Correction de vulnérabilités de sécurité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails) et durcissement contre les injections dans [helmdex](/repos/SocialGouv/helmdex).

## Autres changements notables
- **Modernisation de l'infrastructure de stockage** : Migration massive du stockage d'objets de MinIO vers SeaweedFS pour [infra-apps](/repos/SocialGouv/infra-apps) et [iterion](/repos/SocialGouv/iterion).
- **Évolutions majeures de l'IA** : Extension du support des nouveaux modèles (GPT-6, Opus 5.5) dans [claw-code-go](/repos/SocialGouv/claw-code-go) et optimisation de la recherche vectorielle (HNSW) dans [questions-ecrites](/repos/SocialGouv/questions-ecrites).
- **Migrations technologiques** : Passage massif à la gestion de paquets `pnpm` pour stabiliser les dépendances ([revu](/repos/SocialGouv/revu), [matomo-next](/repos/SocialGouv/matomo-next), [jardinmental](/repos/SocialGouv/jardinmental)) et migration vers Nuxt v4 dans [vao](/repos/SocialGouv/vao).
- **Lancement de nouveaux outils** : Mise en service du réconciliateur de sources de données Metabase dans [metabase-datasource-sync](/repos/SocialGouv/metabase-datasource-sync).

## Dépôts les plus actifs
- [vao](/repos/SocialGouv/vao) : Déploiement de nouveaux parcours d'hébergement et migration technique majeure vers Nuxt v4.
- [iterion](/repos/SocialGouv/iterion) : Introduction de commandes slash, de nouveaux écrans d'administration et renforcement de la sécurité des sandboxes.
- [claw-code-go](/repos/SocialGouv/claw-code-go) : Élargissement du support des modèles d'IA et amélioration de la fiabilité de l'exécution des commandes.
- [domifa](/repos/SocialGouv/domifa) : Modernisation de l'interface utilisateur et déploiement d'un mode support pour l'assistance administrative.
- [buildkit-operator](/repos/SocialGouv/buildkit-operator) : Améliorations de la sécurité (OIDC) et de la gestion du cycle de vie des builds pour éviter les interruptions.
- [questions-ecrites](/repos/SocialGouv/questions-ecrites) : Optimisation des performances de recherche vectorielle et simplification de l'architecture avec pgvector.
