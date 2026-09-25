## Changelog : catalogi (30 derniers jours, au 22 septembre 2026)

### Résumé
Les dernières évolutions se concentrent sur l'amélioration des capacités d'importation de données, notamment via de nouveaux outils en ligne de commande et une optimisation des imports massifs (notamment pour Zenodo). L'expérience de développement et l'utilisation de l'API sont également renforcées par une meilleure documentation et des tests plus robustes.

### Évolutions fonctionnelles
- Amélioration des processus d'importation massive, incluant des optimisations spécifiques pour Zenodo [#516](https://github.com/codegouvfr/catalogi/issues/516).
- Ajout de nouvelles fonctionnalités en ligne de commande (CLI) pour faciliter la gestion et la mise à jour des imports [#577](https://github.com/codegouvfr/catalogi/issues/577).
- Mise à disposition d'une documentation Swagger autonome pour l'export public v2.

### Évolutions techniques
- **API & Données :**
    - Optimisation des performances lors des imports massifs [#516](https://github.com/codegouvfr/catalogi/issues/516).
    - Correction de la gestion des préfixes de documentation derrière les proxys.
    - Renforcement de la conformité du schéma public par rapport aux types de logiciels originaux.
    - Correction de l'utilisation des identifiants (passage de `record id` à `conceptrecid`).
    - Ajout du champ `lastimport` sur les sources.
    - Correction de la gestion des déclarations d'exécutables et des URLs d'instance.
- **Tests & Qualité :**
    - Amélioration de la robustesse des tests de l'API (validation des schémas et nettoyage des données de test).
    - Isolation des données de test de la configuration de l'interface utilisateur par rapport aux migrations historiques.
- **Maintenance & Refactoring :**
    - Refactorisation du système de journalisation (timelog).

### Autres changements
- Réorganisation des migrations de base de données.
- Corrections mineures de configuration de build.
