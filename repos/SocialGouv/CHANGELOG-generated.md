# Synthèse d'activité : SocialGouv (du 20/09 au 26/09)

## Résumé de l'activité
L'activité récente de SocialGouv est portée par deux axes majeurs : l'intégration poussée de l'intelligence artificielle et la consolidation des infrastructures. L'organisation déploie des agents spécialisés et des outils de recherche juridique et de compréhension de code de plus en plus précis dans [srdt](/repos/SocialGouv/srdt), [iterion](/repos/SocialGouv/iterion) et [claw-code-go](/repos/SocialGouv/claw-code-go).

Parallèlement, un effort important est consacré à la sécurité des données et à la conformité, avec des avancées notables sur l'accessibilité (RGAA) dans [egapro](/repos/SocialGouv/egapro) et la protection contre l'exfiltration de données vers les IA dans [smart-allow](/repos/SocialGouv/smart-allow). Enfin, la période est marquée par des migrations d'infrastructure critiques et l'annonce de la fermeture prochaine de certains services comme [recosante](/repos/SocialGouv/recosante) et [nos1000jours-landing](/repos/SocialGouv/nos1000jours-landing).

## Sécurité
- **Protection des données et confidentialité** : Mise en place de la pseudonymisation automatique des données sensibles (PII) et d'un coffre-fort chiffré dans [doublure](/repos/SocialGouv/doublure), et déploiement de politiques contre l'exfiltration de données vers des fournisseurs d'IA externes dans [smart-allow](/repos/SocialGouv/smart-allow).
- **Authentification et accès** : Renforcement de la sécurité via l'adoption d'OIDC dans [buildkit-operator](/repos/SocialGouv/buildkit-operator) et [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example), implémentation de la double authentification (2FA) pour l'administration dans [egapro](/repos/SocialGouv/egapro), et durcissement des politiques de gestion des mots de passe dans [domifa](/repos/SocialGouv/domifa).
- **Corrections de vulnérabilités** : Résolution de failles de sécurité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails) et protection contre les injections (path traversal, shell injection) dans [helmdex](/repos/SocialGouv/helmdex).
- **Infrastructure** : Suppression des utilisateurs PostgreSQL statiques pour renforcer la sécurité dans [vao](/repos/SocialGouv/vao).

## Autres changements notables
- **Migrations d'infrastructure** : Bascule complète du stockage objet vers SeaweedFS dans [infra-apps](/repos/SocialGouv/infra-apps) et migration majeure vers Nuxt v4 dans [vao](/repos/SocialGouv/vao).
- **Évolutions produits et outils** : Lancement d'une application desktop et web pour [helmdex](/repos/SocialGouv/helmdex), refonte majeure du langage de domaine (DSL) dans [iterion](/repos/SocialGouv/iterion), et mise en service du réconciliateur de données Metabase dans [metabase-datasource-sync](/repos/SocialGouv/metabase-datasource-sync).
- **Accessibilité et conformité** : Améliorations massives de la conformité RGAA dans [egapro](/repos/SocialGouv/egapro) et introduction de nouveaux formats de rapports d'audit dans [ultra11y](/repos/SocialGouv/ultra11y).

## Dépôts les plus actifs
- [vao](/repos/SocialGouv/vao) : Avancées sur la gestion de l'hébergement et migrations techniques majeures.
- [srdt](/repos/SocialGouv/srdt) : Optimisation de l'IA juridique et de l'expérience utilisateur.
- [infra-apps](/repos/SocialGouv/infra-apps) : Migration de stockage et sécurisation de l'infrastructure.
- [egapro](/repos/SocialGouv/egapro) : Mise en conformité RGAA et renforcement de la sécurité administrative.
- [iterion](/repos/SocialGouv/iterion) : Développement de nouveaux agents IA et refonte du DSL.
- [claw-code-go](/repos/SocialGouv/claw-code-go) : Extension du support des modèles d'IA et fiabilisation de l'exécution.
- [domifa](/repos/SocialGouv/domifa) : Refonte de l'interface et gestion de la sécurité des comptes.
