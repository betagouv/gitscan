## Changelog : euphrosyne (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à Euphrosyne au cours des 30 derniers jours. Les modifications incluent des mises à jour de sécurité, des corrections de bugs, des améliorations de l'interface utilisateur, l'ajout de nouvelles fonctionnalités comme le filtrage étendu des tables de données et la préparation pour la compatibilité avec Django 6. Des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité de filtrer les extensions dans les tables de fichiers ([#1767](https://github.com/betagouv/euphrosyne/pull/1767)).
- Intégration de liens vers un visualiseur HDF5 pour les données de run ([#1739](https://github.com/betagouv/euphrosyne/pull/1739)).
- Correction d'un bug empêchant la planification de runs sans employeur pour les participations sur site ([#1772](https://github.com/betagouv/euphrosyne/pull/1772)).
- Correction de l'affichage de balises `div` non fermées dans les templates de run ([#1771](https://github.com/betagouv/euphrosyne/pull/1771)).
- Ajout de la configuration de Sentry pour le frontend, permettant une meilleure surveillance des erreurs et des performances.
- Correction d'un bug lié à l'absence de l'ID de workflow dans Goodflag ([#1731](https://github.com/betagouv/euphrosyne/pull/1731)).

### Évolutions techniques
- Mise à jour de la version de Node.js à la version 24 et ajustement des exigences npm correspondantes ([#1770](https://github.com/betagouv/euphrosyne/pull/1770)).
- Préparation pour la migration vers Django 6, incluant des corrections et des ajustements nécessaires ([#1619](https://github.com/betagouv/euphrosyne/pull/1619)).
- Mise à jour de plusieurs dépendances npm et pip, notamment :
    - `react` et `@types/react`
    - `webpack`
    - `@typescript-eslint/eslint-plugin`
    - `jsdom`
    - `fast-xml-parser`
    - `rollup`
    - `css-loader`
    - `@azure/storage-blob`
    - `purgecss-webpack-plugin`
    - `remixicon`
    - `@sentry/browser`
    - `social-auth-app-django`
    - `django-debug-toolbar`
    - `sentry-sdk`
    - `drf-spectacular`
    - `brace-expansion`
- Correction de styles CSS spécifiques à Django pour assurer la compatibilité et une meilleure apparence.

### Autres changements
- Ajout de paramètres de Content Security Policy (CSP) et mise à jour de la documentation.
- Synchronisation du fichier `package.lock`.
- Suppression temporaire de l'application H5web et restauration ultérieure avec une version compatible React 19.
- Suppression du flag de fonctionnalité HDF5.
- Mise à jour de la documentation et des dépendances de développement.
