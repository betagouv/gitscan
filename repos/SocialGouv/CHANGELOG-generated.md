# Synthèse d'activité : SocialGouv (du 22/04 au 22/05)

## Résumé de l'activité
L'activité récente de SocialGouv a été marquée par une forte concentration sur l'amélioration de la qualité des données, la sécurité et l'expérience utilisateur. Plusieurs projets ont bénéficié de mises à jour régulières de leurs données (legi-data, fiches-travail-data, fiches-vdd), assurant ainsi la pertinence des informations fournies. Des efforts significatifs ont également été déployés pour renforcer la sécurité de plusieurs applications (revu, archifiltre-mails, archifiltre-docs). Enfin, de nombreuses améliorations ont été apportées aux interfaces utilisateur (egapro, jardinmental, code-du-travail-numerique) et à l'automatisation des processus (token-bureau, repo-falcon, infra-apps). L'accent est mis sur la modernisation des outils et l'intégration de nouvelles technologies comme pnpm et l'utilisation de LLM.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- Correction d'une vulnérabilité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails).
- Correction d'une vulnérabilité et ajout de suivi d'événements dans [archifiltre-docs](/repos/SocialGouv/archifiltre-docs).
- Migration vers pnpm dans [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget) pour corriger des vulnérabilités.
- Amélioration de la sécurité et correction de vulnérabilités dans [claw-code-go](/repos/SocialGouv/claw-code-go).

## Autres changements notables
Plusieurs évolutions techniques majeures ont été réalisées :

- Migration vers pnpm dans plusieurs dépôts (revu, token-bureau, nos1000jours-blues-epds-pro, smart-allow, matomo-next) pour améliorer la gestion des dépendances.
- Intégration d'Elasticsearch dans [cdtn-admin](/repos/SocialGouv/cdtn-admin) pour améliorer la recherche.
- Refonte de l'interface utilisateur de [egapro](/repos/SocialGouv/egapro) avec le DSFR.
- Mise en place d'un système de journalisation avec OpenTelemetry dans [claw-code-go](/repos/SocialGouv/claw-code-go).
- Migration vers Python 3.14 et Django 5.2.13 dans [collecte-pro](/repos/SocialGouv/collecte-pro).
- Ajout d'un proxy de suivi côté serveur dans [matomo-next](/repos/SocialGouv/matomo-next) pour contourner les bloqueurs de publicités.

## Dépôts les plus actifs
- [vao](/repos/SocialGouv/vao) : Amélioration de la gestion des agréments, ajout de mails de confirmation et d'accessibilité RGAA.
- [token-bureau](/repos/SocialGouv/token-bureau) : Corrections de bugs liés à la migration vers pnpm et améliorations de la gestion des permissions.
- [srdt](/repos/SocialGouv/srdt) : Optimisation des performances et ajout de nouvelles fonctionnalités à l'assistant virtuel.
- [questions-ecrites](/repos/SocialGouv/questions-ecrites) : Intégration des questions écrites des Assemblées Nationale et du Sénat et extraction des réponses.
- [infra-apps](/repos/SocialGouv/infra-apps) : Déploiement d'Elasticsearch, Kuik et Huginn et amélioration de l'observabilité.
- [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Ajout de la gestion des actualités et migration vers Elasticsearch.
- [egapro](/repos/SocialGouv/egapro) : Refonte de l'interface utilisateur et ajout de fonctionnalités d'administration.
- [git-ai-trace](/repos/SocialGouv/git-ai-trace) : Initialisation du projet et ajout des premiers hooks Git pour le suivi de la collaboration IA/humain.
