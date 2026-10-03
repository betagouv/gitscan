# Synthèse d'activité : SocialGouv (du 20/09 au 30/09)

## Résumé de l'activité
L'activité de l'organisation est marquée par une accélération majeure de l'intégration de l'intelligence artificielle et un renforcement de la robustesse des infrastructures. Les nouveaux agents spécialisés d' [iterion](/repos/SocialGouv/iterion) et les avancées de [srdt](/repos/SocialGouv/srdt) pour le traitement juridique illustrent cette tendance, tout comme l'élargissement du support des modèles de pointe dans [claw-code-go](/repos/SocialGouv/claw-code-go). Parallèlement, l'organisation maintient un effort soutenu sur l'accessibilité numérique avec des améliorations notables dans [ultra11y](/repos/SocialGouv/ultra11y) et [egapro](/repos/SocialGouv/egapro).

Une phase de transition est également visible avec l'annonce de la fermeture prochaine de plusieurs services ([recosante](/repos/SocialGouv/recosante), [nos1000jours-landing](/repos/SocialGouv/nos1000jours-landing), [fce](/repos/SocialGouv/fce)) et des migrations d'infrastructure critiques pour garantir la pérennité des plateformes actives.

## Sécurité
- **Protection des données et de la vie privée** : [doublure](/repos/SocialGouv/doublure) introduit la pseudonymisation des données personnelles et un coffre-fort chiffré (AES-256-GCM), tandis que [smart-allow](/repos/SocialGouv/smart-allow) met en place des politiques pour empêcher l'exfiltration de données vers des fournisseurs d'IA.
- **Authentification et contrôle d'accès** : [buildkit-operator](/repos/SocialGouv/buildkit-operator) et [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example) migrent vers une authentification exclusive via OIDC. [egapro](/repos/SocialGouv/egapro) renforce la sécurité de son espace administrateur par la double authentification.
- **Sécurisation des infrastructures** : [infra-apps](/repos/SocialGouv/infra-apps) a procédé à la rotation des clés JWT et au durcissement des déploiements par le pinning d'images. [archifiltre-mails](/repos/SocialGouv/archifiltre-mails) a corrigé une vulnérabilité de sécurité.

## Autres changements notables
- **Migrations technologiques majeures** : [vao](/repos/SocialGouv/vao) effectue une migration vers Nuxt v4 et Node 24, [collecte-pro](/repos/SocialGouv/collecte-pro) migre vers Python 3.14 et Django 5.2, et [infra-apps](/repos/SocialGouv/infra-apps) bascule son stockage objet de MinIO vers SeaweedFS.
- **Nouveaux outils et interfaces** : Lancement de l'application multi-surfaces [helmdex](/repos/SocialGouv/helmdex) et mise en service du réconciliateur de sources de données [metabase-datasource-sync](/repos/SocialGouv/metabase-datasource-sync).

## Dépôts les plus actifs
- [vao](/repos/SocialGouv/vao) : Évolutions importantes sur l'hébergement, la gestion des agréments et la migration vers Nuxt v4.
- [iterion](/repos/SocialGouv/iterion) : Déploiement de nouveaux agents IA spécialisés et refonte de la gestion Cloud.
- [infra-apps](/repos/SocialGouv/infra-apps) : Migration majeure du stockage et optimisation de la sécurité et des runners.
- [srdt](/repos/SocialGouv/srdt) : Amélioration de la précision juridique via l'intégration de la jurisprudence et optimisation du RAG.
- [claw-code-go](/repos/SocialGouv/claw-code-go) : Extension du support des modèles d'IA (GPT-6, Opus 5.5) et sécurisation de l'exécution des commandes.
- [ultra11y](/repos/SocialGouv/ultra11y) : Amélioration de la précision des audits d'accessibilité et nouveaux formats de rapports.
