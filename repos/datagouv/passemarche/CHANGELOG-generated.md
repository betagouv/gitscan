## Changelog : passemarche (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Passe Marché se sont concentrées sur l'amélioration de l'expérience utilisateur lors de la configuration des lots, notamment pour les marchés hétérogènes (composés de différents types de lots). Des ajustements ont été apportés à l'interface pour faciliter la sélection et la configuration des lots, ainsi que l'affichage des informations relatives à chaque lot. Des corrections et des améliorations techniques ont également été apportées pour stabiliser l'application et mettre à jour les dépendances.

### Évolutions fonctionnelles
- **Gestion des lots :** Amélioration de l'interface de configuration des lots, avec la possibilité de modifier le type de lot [#416](https://github.com/datagouv/passemarche/issues/416).
- **Gestion des lots :** Ajout d'icônes pour identifier les types de lots (travaux, services, fournitures) [#415](https://github.com/datagouv/passemarche/issues/415), [#420](https://github.com/datagouv/passemarche/issues/420).
- **Gestion des lots :**  Refonte de la page de sélection des lots avec une présentation en deux états : sélection et préparation. Affichage des types de lots sélectionnés en temps réel [#398](https://github.com/datagouv/passemarche/issues/398).
- **Gestion des lots :** Amélioration de la gestion des marchés hétérogènes avec la possibilité de candidater à des lots de types différents [#420](https://github.com/datagouv/passemarche/issues/420).
- **Attestations candidat :** Ajustements de l'affichage de l'attestation candidat pour les candidatures multi-lots [#391](https://github.com/datagouv/passemarche/issues/391).
- **Suppression de candidature :** Implémentation de la fonctionnalité de suppression d'une candidature [#377](https://github.com/datagouv/passemarche/issues/377).
- **Types de lots :** Affichage des types de lots reçus de la plateforme d'achat [#383](https://github.com/datagouv/passemarche/issues/383).

### Évolutions techniques
- **Refactoring :** Extraction de code pour améliorer la modularité et la maintenabilité, notamment dans la gestion des étapes du wizard et la construction des marchés [#407](https://github.com/datagouv/passemarche/issues/407).
- **Tests :** Ajout et mise à jour de tests (RSpec, Cucumber) pour couvrir les nouvelles fonctionnalités et les corrections de bugs.
- **Mises à jour de dépendances :** Mise à jour de plusieurs dépendances (Doorkeeper, Solid Cable, View Component, Bootsnap, Pagy, Selenium-webdriver, Faraday, Thruster, Jbuilder) pour bénéficier des dernières corrections de sécurité et améliorations de performance.

### Autres changements
- **Documentation :** Amélioration de la documentation interne et des commentaires de code.
- **Configuration :** Uniformisation des tags lots pour une meilleure lisibilité et cohérence.
- **Interface utilisateur :** Améliorations mineures de l'interface utilisateur pour une meilleure expérience utilisateur.
