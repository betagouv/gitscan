# Synthèse d'activité : SocialGouv (du 25/08 au 04/09)

## Résumé de l'activité
L'activité de SocialGouv est marquée par une accélération majeure sur l'intégration de l'intelligence artificielle et l'amélioration de l'accessibilité numérique. Les outils d'analyse de code et d'audit d'accessibilité ([ultra11y](/repos/SocialGouv/ultra11y), [repo-falcon](/repos/SocialGouv/repo-falcon), [iterion](/repos/SocialGouv/iterion)) gagnent en précision et en autonomie grâce à l'optimisation des modèles de langage et à l'introduction de nouveaux mécanismes de contrôle.

Parallèlement, une modernisation profonde des infrastructures est en cours, notamment via la généralisation de l'opérateur de build ([buildkit-operator](/repos/SocialGouv/buildkit-operator)) et la migration de nombreux projets vers de nouveaux gestionnaires de paquets pour plus de stabilité. Ces évolutions renforcent la fiabilité des services et améliorent l'expérience utilisateur globale ([domifa](/repos/SocialGouv/domifa), [egapro](/repos/SocialGouv/egapro)).

## Sécurité
- Renforcement de la protection des données sensibles (PII) par pseudonymisation et durcissement contre les fuites d'informations dans [doublure](/repos/SocialGouv/doublure).
- Correction de vulnérabilités critiques (injections SQL, contournement OAuth) sur [infra-apps](/repos/SocialGouv/infra-apps).
- Sécurisation des processus de build via la migration vers l'authentification OIDC dans [buildkit-operator](/repos/SocialGouv/buildkit-operator) et [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example).
- Mise en place de politiques de sécurité pour prévenir l'exfiltration de données vers des fournisseurs d'IA dans [smart-allow](/repos/SocialGouv/smart-allow).
- Durcissement de la sécurité contre les injections et le path traversal dans [helmdex](/repos/SocialGouv/helmdex).
- Sécurisation des appels vers SUIT par l'implémentation du certificat client mTLS dans [egapro](/repos/SocialGouv/egapro).
- Corrections de vulnérabilités et mises à jour de sécurité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails), [archifiltre-docs](/repos/SocialGouv/archifiltre-docs) et [crossplane-function-js](/repos/SocialGouv/crossplane-function-js).

## Autres changements notables
- **Modernisation de l'infrastructure de build** : Migration massive des services de construction vers `buildkit-operator` ([vao](/repos/SocialGouv/vao), [srdt](/repos/SocialGouv/srdt), [infra-apps](/repos/SocialGouv/infra-apps), [cdtn-admin](/repos/SocialGouv/cdtn-admin)).
- **Standardisation des outils de développement** : Migration de nombreux dépôts vers `pnpm` pour une meilleure gestion des dépendances ([revu](/repos/SocialGouv/revu), [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget), [matomo-next](/repos/SocialGouv/matomo-next), [jardinmental](/repos/SocialGouv/jardinmental), [enfants-du-spectacle](/repos/SocialGouv/enfants-du-spectacle)).
- **Évolutions majeures des frameworks et modèles** : Montée de version vers Angular 20 pour [domifa](/repos/SocialGouv/domifa), migration vers le modèle Albert pour [questions-ecrites](/repos/SocialGouv/questions-ecrites), et passage à Python 3.14/Django 5.2 pour [collecte-pro](/repos/SocialGouv/collecte-pro).
- **Déploiement GitOps** : Initialisation de nouvelles structures de déploiement automatisées pour [mesure-impact](/repos/SocialGouv/mesure-impact) et [mesure-impact-gitops](/repos/SocialGouv/mesure-impact-gitops).

## Dépôts les plus actifs
- [domifa](/repos/SocialGouv/domifa) : Migration vers Angular 20 et amélioration de l'autonomie des utilisateurs.
- [ultra11y](/repos/SocialGouv/ultra11y) : Optimisation des audits d'accessibilité par IA et renforcement de la CI.
- [buildkit-operator](/repos/SocialGouv/buildkit-operator) : Amélioration de la sécurité (OIDC) et de la gestion du cycle de vie des builds.
- [iterion](/repos/SocialGouv/iterion) : Introduction de mécanismes de repli entre modèles et amélioration de l'interface Studio.
- [questions-ecrites](/repos/SocialGouv/questions-ecrites) : Refonte de la base de données et amélioration de l'extraction de données du JO.
- [repo-falcon](/repos/SocialGouv/repo-falcon) : Avancées sur l'analyse de code et la génération de graphes de connaissances.
- [egapro](/repos/SocialGouv/egapro) : Refonte de l'interface utilisateur et fiabilisation des indicateurs.
- [vao](/repos/SocialGouv/vao) : Stabilisation du processus de premier agrément pour les DREETS.
- [kube-image-keeper](/repos/SocialGouv/kube-image-keeper) : Amélioration de la flexibilité du mirroring d'images.
- [cm2d](/repos/SocialGouv/cm2d) : Enrichissement de la visualisation de données avec la cartographie des DROM.
