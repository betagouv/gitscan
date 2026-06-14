## Changelog : recommandations-collaboratives (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau du CRM et de la gestion des projets. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de l'application. Des mises à jour de sécurité et des optimisations techniques ont également été réalisées.

### Évolutions fonctionnelles
- **CRM :** Refonte de l'affichage des résultats du CRM avec l'ajout d'informations sur l'organisation, la commune, la date, le statut et l'origine du portail. [#2152](https://github.com/betagouv/recommandations-collaboratives/issues/2152)
- **Filtres projets :** Ajout d'un filtre "Mes projets" sur la page de la carte, permettant aux utilisateurs de visualiser uniquement leurs propres projets. [#2140](https://github.com/betagouv/recommandations-collaboratives/issues/2140)
- **Gestion des comptes :** Correction d'un bug empêchant la création de compte si l'utilisateur n'était pas dans le processus d'accompagnement. [#2112](https://github.com/betagouv/recommandations-collaboratives/issues/2112)
- **Formulaire de contact :** Le formulaire de contact est désormais uniquement disponible pour les utilisateurs authentifiés. [#2153](https://github.com/betagouv/recommandations-collaboratives/issues/2153)
- **Gestion des droits :** Correction des droits d'accès pour l'éditeur de contact dans le CRM. [#2183](https://github.com/betagouv/recommandations-collaboratives/issues/2183)
- **Export CSV :** Amélioration de l'affichage des badges dans l'export CSV.
- **Interface utilisateur :** Amélioration de l'interface utilisateur, notamment au niveau de la sélection des activités et de l'affichage des informations.

### Évolutions techniques
- **Sécurité :**
    - Mise à jour de `pyjwt` vers la version 2.13.0 pour corriger des vulnérabilités. [#2169](https://github.com/betagouv/recommandations-collaboratives/issues/2169)
    - Mise à jour de `uv` et des dépendances associées pour corriger des problèmes de sécurité. [#2163](https://github.com/betagouv/recommandations-collaboratives/issues/2163)
    - Ajout de `gitleaks` au pre-commit pour détecter les secrets dans le code. [#2178](https://github.com/betagouv/recommandations-collaboratives/issues/2178)
- **Infrastructure :** Utilisation de `uv` pour la gestion des dépendances et l'audit de sécurité.
- **Tests :**
    - Ajout de tests E2E et refactorisation des tests existants. [#2043](https://github.com/betagouv/recommandations-collaboratives/issues/2043)
    - Ajout d'un nouveau test pour vérifier la redirection après la signature.
- **Refactoring :**
    - Refactorisation du code lié à la gestion des recommandations (reco).
    - Suppression de code mort et amélioration de la lisibilité du code.
    - Amélioration de la pagination.

### Autres changements
- **Documentation :** Ajout d'un lien vers la documentation.
- **Dépendances :** Mises à jour mineures de certaines dépendances (shell-quote, tmp, systeminformation).
- **Configuration :** Précision de la configuration pour la gestion des logs.
- **Corrections diverses :** Correction de bugs mineurs et améliorations de la qualité du code.
