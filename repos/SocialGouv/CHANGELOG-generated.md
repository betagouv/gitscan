# Synthèse d'activité : SocialGouv (du 15/09 au 22/09)

## Résumé de l'activité
L'activité de l'organisation est marquée par une accélération majeure sur les outils d'intelligence artificielle et l'automatisation du développement, notamment avec les avancées sur [iterion](/repos/SocialGouv/iterion) et [claw-code-go](/repos/SocialGouv/claw-code-go). Parallèlement, un effort important est porté sur la fiabilisation des services publics et la gestion des données juridiques via des mises à jour régulières de [legi-data](/repos/SocialGouv/legi-data) et [egapro](/repos/SocialGouv/egapro).

On note également une phase de transition pour plusieurs services arrivant en fin de vie ([recosante](/repos/SocialGouv/recosante), [nos1000jours-landing](/repos/SocialGouv/nos1000jours-landing)) et une modernisation profonde des infrastructures pour soutenir la montée en charge des plateformes ([infra-apps](/repos/SocialGouv/infra-apps), [buildkit-operator](/repos/SocialGouv/buildkit-operator)).

## Sécurité
- Protection des données personnelles (PII) via la pseudonymisation automatique et le chiffrement AES-256-GCM dans [doublure](/repos/SocialGouv/doublure).
- Renforcement de la protection contre l'exfiltration de données vers les fournisseurs d'IA dans [smart-allow](/repos/SocialGouv/smart-allow).
- Durcissement de l'authentification par la migration vers le standard OIDC dans [buildkit-operator](/repos/SocialGouv/buildkit-operator) et [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example).
- Corrections de vulnérabilités et protection contre les injections (shell, path traversal) dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails) et [helmdex](/repos/SocialGouv/helmdex).
- Amélioration de la sécurité des sessions dans [vao](/repos/SocialGouv/vao).

## Autres changements notables
- **Modernisation des infrastructures** : Stabilisation des moteurs d'exécution et passage à une identité web officielle pour [infra-apps](/repos/SocialGouv/infra-apps), et renforcement de la fiabilité des processus de build dans [buildkit-operator](/repos/SocialGouv/buildkit-operator).
- **Migrations technologiques majeures** : Passage vers Nuxt v4 et Node 24 dans [vao](/repos/SocialGouv/vao), et migration vers des versions récentes de Python et Django dans [collecte-pro](/repos/SocialGouv/collecte-pro).
- **Optimisation des performances** : Amélioration de la recherche vectorielle (pgvector/HNSW) et simplification de l'architecture dans [questions-ecrites](/repos/SocialGouv/questions-ecrites).
- **Évolutions de l'IA** : Refonte de l'architecture des compétences IA dans [vao](/repos/SocialGouv/vao) et amélioration de la précision des audits via l'IA dans [ultra11y](/repos/SocialGouv/ultra11y).

## Dépôts les plus actifs
- [iterion](/repos/SocialGouv/iterion) : Expansion du catalogue d'agents spécialisés et refonte de l'interface Studio.
- [infra-apps](/repos/SocialGouv/infra-apps) : Stabilisation de la plateforme, gestion des ressources et transition vers iterion.cloud.
- [claw-code-go](/repos/SocialGouv/claw-code-go) : Support étendu des nouveaux modèles d'IA et sécurisation de l'exécution des commandes.
- [domifa](/repos/SocialGouv/domifa) : Amélioration du suivi des usagers, de l'interface de pilotage et de la sécurité des données.
- [egapro](/repos/SocialGouv/egapro) : Lancement de l'observatoire public et optimisation des parcours de déclaration.
- [buildkit-operator](/repos/SocialGouv/buildkit-operator) : Renforcement de la sécurité (OIDC) et de la fiabilité du cycle de vie des builds.
