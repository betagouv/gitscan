## Changelog : chartsgouv (30 derniers jours, au 30 septembre 2026)

### Résumé
Ce mois a été marqué par le passage à la version majeure 2.0.0. Les évolutions principales concernent la mise en conformité avec la version 6.1 du Design Système de l'État (DSFR) et une amélioration de la compatibilité des déploiements via Helm avec les dernières versions d'Apache Superset.

### Évolutions fonctionnelles
- **Design Système :** Mise à jour de la configuration du thème pour s'aligner sur la version 6.1 du DSFR.
- **Déploiement :** Mise à jour des valeurs Helm pour garantir la compatibilité avec les versions les plus récentes d'Apache Superset.

### Évolutions techniques
- **Intégration Continue (CI) :**
    - Mise à jour du workflow de construction d'images ([#103](https://github.com/etalab-ia/chartsgouv/issues/103)).
    - Correction et amélioration de l'intégration du DSFR dans les pipelines ([#105](https://github.com/etalab-ia/chartsgouv/issues/105)).

### Autres changements
- **Maintenance :** Optimisation de la gestion des dépendances avec l'ajout d'une configuration Dependabot pour des mises à jour quotidiennes.
- **Documentation :** Nettoyage et application des règles de style (linting) sur la documentation.
