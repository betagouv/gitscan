# Synthèse d'activité : SocialGouv (du 25/07 au 01/08)

## Résumé de l'activité
L'activité de SocialGouv cette semaine est marquée par une forte dynamique autour de l'intégration de l'intelligence artificielle et de l'accessibilité numérique. Plusieurs projets renforcent leurs capacités d'analyse et d'automatisation via des modèles de langage ([iterion](/repos/SocialGouv/iterion), [repo-falcon](/repos/SocialGouv/repo-falcon), [claw-code-go](/repos/SocialGouv/claw-code-go)), tandis que l'accessibilité (RGAA) devient un standard transversal pour améliorer l'inclusion des usagers ([egapro](/repos/SocialGouv/egapro), [domifa](/repos/SocialGouv/domifa), [dsfr-mcp](/repos/SocialGouv/dsfr-mcp)).

Parallèlement, une modernisation profonde de l'infrastructure est en cours. L'organisation déploie des changements structurels importants, notamment par la migration vers de nouveaux outils de construction et de gestion de dépendances, visant à accroître la stabilité et la sécurité des services pour les utilisateurs finaux.

## Sécurité
- **Protection des données et de la vie privée** : Mise en place de la pseudonymisation des données personnelles (PII) et d'un coffre-fort chiffré AES-256-GCM ([doublure](/repos/SocialGouv/doublure)).
- **Contrôle des flux IA** : Implémentation de politiques de sécurité pour prévenir l'exfiltration de données vers des fournisseurs d'IA ([smart-allow](/repos/SocialGouv/smart-allow)).
- **Renforcement de l'authentification** : Migration vers l'authentification OIDC pour sécuriser les accès ([buildkit-operator](/repos/SocialGouv/buildkit-operator), [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example)) et implémentation du certificat client mTLS ([egapro](/repos/SocialGouv/egapro)).
- **Corrections de vulnérabilités** : Résolution de failles de sécurité sur plusieurs services ([archifiltre-mails](/repos/SocialGouv/archifiltre-mails), [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget)).

## Autres changements notables
- **Modernisation de l'infrastructure de build** : Migration massive des processus de construction vers `buildkit-operator` pour optimiser les déploiments ([srdt](/repos/SocialGouv/srdt), [domifa](/repos/SocialGouv/domifa), [code-du-travail-numerique](/repos/SocialGouv/code-du-travail-numerique), [cdtn-admin](/repos/SocialGouv/cdtn-admin)).
- **Optimisation de la gestion des dépendances** : Migration généralisée vers le gestionnaire de paquets `pnpm` pour améliorer la performance et la fiabilité ([revu](/repos/SocialGouv/revu), [matomo-next](/repos/SocialGouv/matomo-next), [jardinmental](/repos/SocialGouv/jardinmental), [enfants-du-spectacle](/repos/SocialGouv/enfants-du-spectacle)).
- **Évolutions majeures de l'analyse de code** : Avancées significatives dans la génération de graphes de connaissances et l'utilisation de modèles de langage locaux pour l'exploration de code ([repo-falcon](/repos/SocialGouv/repo-falcon), [claw-code-go](/repos/SocialGouv/claw-code-go)).

## Dépôts les plus actifs
- [buildkit-operator](/repos/SocialGouv/buildkit-operator) : Refonte majeure de l'infrastructure (sécurité OIDC, gestion du cache S3 et cycle de vie des builds).
- [domifa](/repos/SocialGouv/domifa) : Évolutions fonctionnelles importantes (RGAA, nouveaux contenus) et optimisations critiques du backend.
- [egapro](/repos/SocialGouv/egapro) : Refonte visuelle, amélioration de la précision des calculs et mise en conformité RGAA.
- [iterion](/repos/SocialGouv/iterion) : Développement massif de l'interface de gestion et intégration de capacités d'automatisation par IA.
- [repo-falcon](/repos/SocialGouv/repo-falcon) : Améliorations poussées de l'analyse de code et de l'intégration de modèles de langage.
- [helmdex](/repos/SocialGouv/helmdex) : Ajout de fonctionnalités avancées pour la gestion des catalogues et des versions Helm.
