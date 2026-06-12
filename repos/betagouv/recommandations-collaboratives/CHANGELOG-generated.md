## Changelog : recommandations-collaboratives (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur, notamment la refonte de la page de résultats du CRM, l'ajout de filtres pour les projets, et des corrections de bugs liés à l'affichage et aux permissions. Des améliorations de sécurité et des mises à jour de dépendances ont également été apportées.

### Évolutions fonctionnelles
- **CRM :** Refonte de la page de résultats du CRM avec affichage de l'organisation, du statut, de la commune, de la date et des informations sur l'utilisateur. Ajout d'un état vide pour une meilleure expérience utilisateur. [#2152](https://github.com/betagouv/recommandations-collaboratives/issues/2152)
- **Filtres projets :** Ajout d'un filtre "Mes projets" sur la page de la carte, permettant de visualiser uniquement les projets de l'utilisateur actuel. [#2140](https://github.com/betagouv/recommandations-collaboratives/issues/2140)
- **Gestion des utilisateurs :** Correction d'un bug empêchant la mise à jour des informations de l'utilisateur dans le CRM. [#2183](https://github.com/betagouv/recommandations-collaboratives/issues/2183)
- **Formulaire de contact :** Le formulaire de contact sur la page d'accueil est désormais uniquement accessible aux utilisateurs authentifiés. [#2153](https://github.com/betagouv/recommandations-collaboratives/issues/2153)
- **Gestion des droits :** Correction des droits d'accès pour l'éditeur de contact dans le CRM.
- **Export CSV :** Amélioration de l'export CSV avec l'ajout de badges et la correction de certains comportements.
- **Interface utilisateur :** Amélioration de l'affichage des statistiques et de la pagination.

### Évolutions techniques
- **Sécurité :**
    - Mise à jour de `pyjwt` vers la version 2.13.0 pour corriger des vulnérabilités.
    - Intégration de `uv` pour la gestion des dépendances et l'audit de sécurité.
    - Ajout de `gitleaks` au pre-commit pour détecter les secrets exposés.
- **Dépendances :** Mises à jour de plusieurs dépendances (uv, shell-quote, js-cookie, systeminformation, idna) pour bénéficier des dernières corrections et améliorations.
- **Tests :**
    - Ajout de tests pour le filtre "Mes projets".
    - Refactorisation des tests frontend pour éviter l'introduction de complexité.
    - Ajout d'une commande pour lancer tous les tests.
- **Refactoring :**
    - Nettoyage du code et suppression de code mort.
    - Amélioration de la structure du code pour une meilleure lisibilité et maintenabilité.
- **CI/CD :** Mise à jour de la configuration CI pour intégrer `uv`.

### Autres changements
- **Documentation :** Mise à jour de la documentation sur les webhooks.
- **Corrections diverses :** Correction de bugs mineurs liés à l'affichage, aux permissions et au comportement de certains composants.
- **Améliorations de l'interface :** Ajustements de style et d'accessibilité.
- **Génération de rapports :** Ajout de la possibilité d'exporter des données au format CSV.
