## Changelog : euphrosyne (30 derniers jours)

### Résumé
Cette période a été marquée par des améliorations de la gestion des participations, notamment en termes de validation et d'édition. Des refactorings importants ont été effectués pour moderniser la gestion du stockage des fichiers, et plusieurs mises à jour de dépendances ont été appliquées pour assurer la sécurité et la stabilité de la plateforme. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la validation pour éviter de créer des participations sans employeur (#1772).
- Amélioration de l'interface d'édition des participations distantes (#1720).
- Implémentation de la logique d'exemption de l'employeur pour les participations (#1716).
- Ajout de la normalisation des noms de personnes et d'employeurs (capitalisation) (#1718).
- Ajout d'un lien vers un visualiseur HDF5 pour les données de run (#1735).
- Possibilité de filtrer les extensions de la table de fichiers (#1767).
- Correction d'un problème d'affichage des boutons "éditer" dans la table des participations distantes (#1720).

### Évolutions techniques
- Refactorisation de la gestion du stockage des fichiers avec l'utilisation de `BlobStorageClient` et `FileshareStorageClient` (#1706, #1709).
- Mise à jour de la version de Node.js vers la 24 et ajustement des exigences npm (#1770).
- Mise à jour de Django vers la version 6.0 et application de correctifs (#1736, #1733).
- Mise à jour de plusieurs dépendances npm et pip (voir section "Autres changements").
- Ajout de la configuration de Content Security Policy (CSP) (#1731).
- Augmentation du timeout pour les requêtes API dans les commandes `check_long_running_vms` et `check_project_data_availability`.

### Autres changements
- Mises à jour de dépendances :
    - `black` (25.11.0 -> 26.1.0) (#1739)
    - `ajv` (6.12.6 -> 6.14.0) (#1757)
    - `jsdom` (27.4.0 -> 28.1.0) (#1764)
    - `fast-xml-parser` (5.3.4 -> 5.3.6, 5.2.5 -> 5.3.4) (#1751, #1760)
    - `@azure/storage-blob` (12.29.1 -> 12.30.0, 12.30.0 -> 12.31.0) (#1711, #1763)
    - `@sentry/browser` (10.34.0 -> 10.36.0, 10.36.0 -> 10.37.0) (#1709, #1727)
    - `@typescript-eslint/eslint-plugin` (8.53.1, 8.54.0, 8.55.0) (#1708, #1741, #1745)
    - `@types/react` (19.2.8 -> 19.2.9, 19.2.10 -> 19.2.14) (#1710, #1753)
    - `vitest` (4.0.8 -> 4.0.17, 4.0.17 -> 4.0.18) (#1707, #1755)
    - `django-debug-toolbar` (6.0.0 -> 6.2.0) (#1762)
    - `social-auth-app-django` (5.5.1 -> 5.7.0) (#1725)
    - `css-loader` (7.1.2 -> 7.1.3, 7.1.3 -> 7.1.4) (#1730, #1765)
    - `css-minimizer-webpack-plugin` (7.0.2 -> 7.0.4) (#1743)
    - `prettier` (3.8.0 -> 3.8.1) (#1742)
    - `purgecss-webpack-plugin` (7.0.2 -> 8.0.0) (#1726)
    - `remixicon` (4.8.0 -> 4.9.0) (#1728)
    - `webpack` (5.104.1 -> 5.105.1) (#1754)
    - `glob` (13.0.0 -> 13.0.2) (#1756)
    - `drf-spectacular` (0.28.0 -> 0.29.0) (#1752)
    - `pillow` (12.0.0 -> 12.1.1) (#1759)
- Suppression temporaire de l'application H5web et restauration ultérieure avec une implémentation alternative pour la compatibilité avec React 19 (#1769).
- Correction de balises `div` non fermées dans les templates de run (#1771).
