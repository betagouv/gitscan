# Synthèse d'activité : SocialGouv (derniers 7 jours)

## Résumé de l'activité
L'organisation SocialGouv a connu une semaine riche en activités, avec des mises à jour touchant de nombreux dépôts. L'accent a été mis sur l'amélioration de la sécurité (correction de vulnérabilités dans [archifiltre-docs](/repos/SocialGouv/archifiltre-docs) et [archifiltre-mails](/repos/SocialGouv/archifiltre-mails)), la modernisation des technologies (migration vers pnpm dans [cdtn-admin](/repos/SocialGouv/cdtn-admin), [domifa](/repos/SocialGouv/domifa), [revu](/repos/SocialGouv/revu) et [token-bureau](/repos/SocialGouv/token-bureau)), et l'ajout de nouvelles fonctionnalités, notamment dans [cdtn-admin](/repos/SocialGouv/cdtn-admin), [domifa](/repos/SocialGouv/domifa), [egapro](/repos/SocialGouv/egapro), [graal](/repos/SocialGouv/graal), [matomo-next](/repos/SocialGouv/matomo-next), [vao](/repos/SocialGouv/vao) et [questions-ecrites](/repos/SocialGouv/questions-ecrites). Plusieurs projets ont également progressé dans l'automatisation de leurs processus de développement et de déploiement.

## Sécurité
Plusieurs dépôts ont bénéficié de correctifs de sécurité :

- Correction d'une vulnérabilité de sécurité dans [archifiltre-docs](/repos/SocialGouv/archifiltre-docs).
- Correction d'une vulnérabilité de sécurité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails).
- Amélioration de la sécurité des API dans [srdt](/repos/SocialGouv/srdt).
- Correction de vulnérabilités de sécurité dans les dépendances de [revu](/repos/SocialGouv/revu).

## Autres changements notables
Plusieurs changements techniques majeurs ont été effectués :

- Migration vers pnpm dans plusieurs dépôts ([cdtn-admin](/repos/SocialGouv/cdtn-admin), [domifa](/repos/SocialGouv/domifa), [revu](/repos/SocialGouv/revu), [token-bureau](/repos/SocialGouv/token-bureau)) pour une meilleure gestion des dépendances.
- Mise à jour de technologies clés dans [cdtn-admin](/repos/SocialGouv/cdtn-admin) (Next.js, React, React-DSFR).
- Intégration de *feature flags* dans [vao](/repos/SocialGouv/vao) pour une gestion plus flexible des fonctionnalités.
- Refactorisation du code et amélioration de l'architecture dans [questions-ecrites](/repos/SocialGouv/questions-ecrites).
- Mise en place d'un cluster PostgreSQL dans [srdt](/repos/SocialGouv/srdt).

## Dépôts les plus actifs
Voici une liste des dépôts les plus actifs de la semaine :

- [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Corrections de bugs, amélioration de la gestion des alertes et modernisation des technologies.
- [domifa](/repos/SocialGouv/domifa) : Corrections de bugs, ajout de nouvelles fonctionnalités (envoi de SMS) et amélioration de la surveillance.
- [egapro](/repos/SocialGouv/egapro) : Ajout de nouvelles fonctionnalités (génération de déclaration PDF, parcours seconde déclaration) et amélioration des tests.
- [graal](/repos/SocialGouv/graal) : Amélioration de la gestion des configurations et de l'interface utilisateur.
- [vao](/repos/SocialGouv/vao) : Corrections de bugs, ajout de *feature flags* et intégration avec le stockage S3.
- [questions-ecrites](/repos/SocialGouv/questions-ecrites) : Intégration de modèles de langage (LLM) et refactorisation du code.
- [revu](/repos/SocialGouv/revu) : Corrections de bugs et migration vers pnpm.
- [matomo-next](/repos/SocialGouv/matomo-next) : Ajout d'un proxy pour contourner les bloqueurs de publicités et implémentation des tests A/B.
