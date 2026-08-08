# Synthèse d'activité : SocialGouv (du 26/07 au 02/08)

## Résumé de l'activité
L'activité de SocialGouv est marquée par une accélération sur l'intégration de l'intelligence artificielle et l'amélioration de l'accessibilité numérique. Des projets comme [iterion](/repos/SocialGouv/iterion) et [repo-falcon](/repos/SocialGouv/repo-falcon) progressent sur l'automatisation des workflows et l'analyse de code assistée par IA, tandis que l'accessibilité (RGAA) devient un pilier central sur [domifa](/repos/SocialGouv/domifa), [egapro](/repos/SocialGouv/egapro) et [vao](/repos/SocialGouv/vao).

Parallèlement, l'organisation assure la mise à jour continue des données législatives et sociales ([legi-data](/repos/SocialGouv/legi-data), [fiches-vdd](/repos/SocialGouv/fiches-vdd)) et prépare la transition de certains services ([recosante](/repos/SocialGouv/recosante), [fce](/repos/SocialGouv/fce)).

## Sécurité
- Protection des données et de l'authentification :
    - Mise en place de politiques contre l'exfiltration de données vers des fournisseurs d'IA dans [smart-allow](/repos/SocialGouv/smart-allow).
    - Migration vers l'authentification OIDC pour sécuriser les accès dans [buildkit-operator](/repos/SocialGouv/buildkit-operator) et [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example).
    - Renforcement de la sécurité des services et des accès (rotation de clés, OAuth) dans [infra-apps](/repos/SocialGouv/infra-apps) et [da-manager](/repos/SocialGouv/da-manager).
    - Corrections de vulnérabilités dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails) et [archifiltre-docs](/repos/SocialGouv/archifiltre-docs).

## Autres changements notables
- Migrations technologiques et infrastructurelles :
    - Adoption généralisée de `pnpm` pour la gestion des dépendances ([revu](/repos/SocialGouv/revu), [matomo-next](/repos/SocialGouv/matomo-next), [jardinmental](/repos/SocialGouv/jardinmental), [enfants-du-spectacle](/repos/SocialGouv/enfants-du-spectacle)).
    - Migration vers `buildkit-operator` pour l'optimisation des processus de build ([vao](/repos/SocialGouv/vao), [srdt](/repos/SocialGouv/srdt), [egapro](/repos/SocialGouv/egapro), [domifa](/repos/SocialGouv/domifa), [cdtn-admin](/repos/SocialGouv/cdtn-admin)).
    - Montée de version majeure des frameworks ([domifa](/repos/SocialGouv/domifa) vers Angular 20, [collecte-pro](/repos/SocialGouv/collecte-pro) vers Python 3.14/Django 5.2).
    - Optimisation des pipelines CI/CD et de la distribution ([questions-ecrites](/repos/SocialGouv/questions-ecrites), [charon](/repos/SocialGouv/charon), [Veille_JO](/repos/SocialGouv/Veille_JO)).

## Dépôts les plus actifs
- [domifa](/repos/SocialGouv/domifa) : Migration majeure vers Angular 20 et enrichissement de l'expérience usagers.
- [iterion](/repos/SocialGouv/iterion) : Développement de l'interface de gestion des bots et des capacités d'IA.
- [egapro](/repos/SocialGouv/egapro) : Refonte du moteur d'étapes et amélioration de l'accessibilité.
- [buildkit-operator](/repos/SocialGouv/buildkit-operator) : Stabilisation de l'infrastructure et sécurisation des processus de build.
- [repo-falcon](/repos/SocialGouv/repo-falcon) : Avancées dans l'analyse de code et l'intégration de modèles de langage locaux.
