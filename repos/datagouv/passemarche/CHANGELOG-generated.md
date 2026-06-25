## Changelog : passemarche (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Passe Marché se sont concentrées sur l'amélioration de l'expérience utilisateur concernant la gestion des lots, notamment pour les marchés avec de nombreux lots ou des lots de types différents. Des corrections et des ajustements ont été apportés pour faciliter la configuration des lots et l'affichage des informations, ainsi que des améliorations techniques et des mises à jour de dépendances.

### Évolutions fonctionnelles
- **Gestion des lots :** Amélioration de l'affichage des lots, notamment avec un affichage "collapsible" pour les listes de lots volumineuses [#419](https://github.com/datagouv/passemarche/pull/419).
- **Configuration des lots :** Refonte de l'interface de configuration des lots pour les acheteurs, avec une meilleure organisation et une présentation plus claire des types de lots [#434](https://github.com/datagouv/passemarche/pull/434), [#422](https://github.com/datagouv/passemarche/pull/422), [#398](https://github.com/datagouv/passemarche/pull/398).
- **Types de lots :** Possibilité de modifier le type de lots individuellement [#416](https://github.com/datagouv/passemarche/pull/416) et d'afficher le type de chaque lot dans les annexes PDF [#420](https://github.com/datagouv/passemarche/pull/420).
- **DLRO (Dépôt Légal des Réponses) :** Ajout d'une API pour mettre à jour la date limite de réponse (DLRO) d'un marché [#418](https://github.com/datagouv/passemarche/pull/418).
- **Améliorations UI :** Corrections d'affichage et d'espacement sur la page de sélection des lots et ajout d'icônes pour les types de marché [#415](https://github.com/datagouv/passemarche/pull/415), [#412](https://github.com/datagouv/passemarche/pull/412).

### Évolutions techniques
- **Refactoring :** Extraction de code pour améliorer la modularité et la maintenabilité, notamment dans la gestion des étapes du wizard et des helpers de formulaire [#407](https://github.com/datagouv/passemarche/pull/407).
- **Tests :** Ajout et mise à jour de tests RSpec et Cucumber pour couvrir les nouvelles fonctionnalités et les corrections [#431](https://github.com/datagouv/passemarche/pull/419), [#418](https://github.com/datagouv/passemarche/pull/418).
- **Documentation :** Mise à jour de la documentation de l'API et des scripts de seed [#435](https://github.com/datagouv/passemarche/pull/435), [#417](https://github.com/datagouv/passemarche/pull/417).
- **Seed :** Ajout d'un script pour créer un marché de test avec 1000 lots [#421](https://github.com/datagouv/passemarche/pull/421).

### Autres changements
- Mise à jour des dépendances : plusieurs dépendances ont été mises à jour vers leurs dernières versions stables (kamal, selenium-webdriver, shoulda-matchers, faraday, doorkeeper, actions/checkout, rubyzip, sentry-rails, bootsnap, view_component, pagy). Ces mises à jour visent à améliorer la sécurité et la performance de l'application.
