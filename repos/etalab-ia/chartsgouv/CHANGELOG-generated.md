## Changelog : chartsgouv (30 derniers jours, au 30/09/2026)

### Résumé
Le projet a franchi une étape majeure avec le passage à la version 2.0.0. Cette mise à jour simplifie la gestion du dépôt et assure une meilleure compatibilité avec les dernières versions du Design Système de l'État (DSFR) et d'Apache Superset.

### Évolutions fonctionnelles
- **Mise à jour du thème** : Actualisation de la configuration pour s'aligner sur la version 6.1 du DSFR.
- **Installation** : Mise à jour des valeurs Helm pour garantir la compatibilité avec les dernières versions de Superset.

### Évolutions techniques
- **Simplification de la gestion du projet** : Refonte de la stratégie de dépôt et du processus de publication ([#99](https://github.com/etalab-ia/chartsgouv/issues/99)).
- **Optimisation de la CI/CD** :
    - Amélioration de l'intégration du DSFR ([#105](https://github.com/etalab-ia/chartsgouv/issues/105)).
    - Mise à jour du workflow de construction d'images ([#103](https://github.com/etalab-ia/chartsgouv/issues/103)).
    - Renforcement des contrôles de qualité (linting) sur Docker ([#102](https://github.com/etalab-ia/chartsgouv/issues/102)), Helm ([#101](https://github.com/etalab-ia/chartsgouv/issues/101)) et les scripts Shell ([#100](https://github.com/etalab-ia/chartsgouv/issues/100)).

### Autres changements
- **Maintenance** : Configuration de Dependabot pour automatiser les mises à jour de dépendances.
- **Nettoyage** : Suppression de l'écosystème `uv` et application de règles de linting sur la documentation.
