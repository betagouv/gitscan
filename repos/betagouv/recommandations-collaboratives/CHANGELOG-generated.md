## Changelog : recommandations-collaboratives (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'ajout d'un système de plugins pour étendre les fonctionnalités de Recoco, l'amélioration de l'authentification avec la suppression de Django Magicauth et l'implémentation d'une nouvelle méthode de connexion par code, ainsi que des corrections de bugs et des optimisations de sécurité. Des améliorations de l'interface utilisateur et des corrections de filtres ont également été apportées.

### Évolutions fonctionnelles
- **Plugins :** Ajout d'un système de plugins pour étendre les fonctionnalités de Recoco, incluant la découverte automatique des hooks et la possibilité d'ajouter des composants personnalisés à la conversation [#1986](https://github.com/betagouv/recommandations-collaboratives/pull/1986).
- **Authentification :**
    - Remplacement de Django Magicauth par une nouvelle méthode de connexion par code, avec une durée de validité accrue et une meilleure gestion des comptes sensibles [#2143](https://github.com/betagouv/recommandations-collaboratives/pull/2143).
    - Ajout d'une page de confirmation de code pour la connexion par code.
    - Amélioration de la sécurité de l'authentification avec la vérification du consentement aux cookies pour l'utilisation des magiclinks.
    - Ajout d'une page 403 personnalisée.
- **Interface utilisateur :**
    - Ajout d'un filtre pour afficher les projets sur la carte [#2144](https://github.com/betagouv/recommandations-collaboratives/pull/2144).
    - Amélioration de l'interface utilisateur pour la gestion des utilisateurs CRM [#2142](https://github.com/betagouv/recommandations-collaboratives/pull/2142).
    - Mise à jour du style de la mise en page et des couleurs principales.
- **Formulaires :**
    - Correction du formulaire de contact pour limiter son accès aux utilisateurs authentifiés [#2153](https://github.com/betagouv/recommandations-collaboratives/pull/2153).
    - Correction du formulaire de mise à jour des utilisateurs CRM pour permettre la saisie des noms et prénoms.

### Évolutions techniques
- **Dépendances :**
    - Mise à jour de plusieurs dépendances, notamment `uv`, `django`, `pyjwt`, `dompurify`, `vite`, `form-data`, `tar`, `@babel/core`, `bleach` et `tornado`.
    - Suppression de `requirements.txt` et passage à `uv` pour la gestion des dépendances.
    - Suppression des dépendances Django Magicauth.
- **CI/CD :**
    - Ajout de `uv` à l'environnement CI.
    - Mise à jour de la configuration de GitHub Actions pour l'audit des dépendances avec `uv-audit`.
- **Refactoring :**
    - Refactorisation du code lié à la gestion des projets pour préparer un nouveau lancement.
    - Suppression de code mort lié aux recommandations.
    - Amélioration de la robustesse des tests, notamment pour les documents.
    - Suppression de l'importation en ligne pour les plugins.
    - Utilisation de fixtures pour les tests.
- **Sécurité :**
    - Correction de failles de sécurité potentielles liées aux noms de schémas de plugins.
    - Mise à jour des dépendances pour corriger des vulnérabilités connues.
    - Ajout d'un hook pour détecter les exports multiples dans la même journée.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour l'installation des plugins.
- **Tests :** Ajout d'un nouveau test pour vérifier toutes les URLs.
- **Pre-commit :** Ajout de `gitleaks` au pre-commit pour détecter les secrets dans le code.
- **Divers :**
    - Correction de typos et amélioration de la lisibilité du code.
    - Suppression de code inutile.
    - Ajout de commentaires pour clarifier le fonctionnement de certains composants.
    - Mise à jour des statuts des projets dans l'API.
