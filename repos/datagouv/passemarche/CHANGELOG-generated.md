## Changelog : passemarche (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des lots, notamment pour les marchés hétérogènes, et sur l'expérience utilisateur. Des corrections et des ajustements ont été apportés pour fluidifier le processus de candidature et de configuration des lots, ainsi que pour améliorer l'affichage des informations. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la performance de l'application.

### Évolutions fonctionnelles
- **Gestion des lots :** Amélioration de la configuration des lots, avec la possibilité de modifier le type de lots et d'afficher les types de lots reçus de la plateforme d'achat. [#383](https://github.com/datagouv/passemarche/pull/383)
- **Interface de sélection des lots :** Refonte de l'interface de sélection des lots pour une meilleure expérience utilisateur, avec un affichage en deux états (sélectionner / préparer). [#391](https://github.com/datagouv/passemarche/pull/391)
- **Attestation candidat :** Ajustements de l'affichage de l'attestation candidat, notamment pour les marchés avec plusieurs lots. [#382](https://github.com/datagouv/passemarche/pull/382) et [#391](https://github.com/datagouv/passemarche/pull/391)
- **Suppression de candidature :** Implémentation de la fonctionnalité de suppression d'une candidature. [#377](https://github.com/datagouv/passemarche/pull/377)
- **API :** Ajout d'un endpoint pour mettre à jour la DLRO (Date Limite de Réponse) d'un marché via l'API. [#418](https://github.com/datagouv/passemarche/pull/418)
- **Types de lots :** Amélioration de l'affichage des types de lots, avec l'ajout d'icônes et de badges colorés. [#397](https://github.com/datagouv/passemarche/pull/397) et [#415](https://github.com/datagouv/passemarche/pull/415)

### Évolutions techniques
- **Refactoring :** Extraction de code pour améliorer la modularité et la maintenabilité, notamment dans la gestion des étapes du wizard et la création de marchés. [#407](https://github.com/datagouv/passemarche/pull/407)
- **Tests :** Ajout et mise à jour de tests RSpec et Cucumber pour couvrir les nouvelles fonctionnalités et les corrections de bugs. [#416](https://github.com/datagouv/passemarche/pull/416) et [#423](https://github.com/datagouv/passemarche/pull/423)
- **PaperTrail :** Activation de PaperTrail sur le modèle `PublicMarket` pour historiser les changements de deadline. [#537](https://github.com/datagouv/passemarche/pull/418)
- **Documentation :** Mise à jour de la documentation de l'API pour refléter les nouvelles fonctionnalités. [#418](https://github.com/datagouv/passemarche/pull/418) et [#539](https://github.com/datagouv/passemarche/pull/417)
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances (Doorkeeper, Solid Cable, View Component, Bootsnap, Pagy, Selenium-webdriver, Faraday, Thruster, Jbuilder, Sentry-rails, Rubyzip) pour bénéficier des dernières corrections de bugs et améliorations de sécurité.

### Autres changements
- **Améliorations de l'UX :** Ajustements de l'interface utilisateur, notamment pour l'affichage des badges de type de marché et la suppression d'éléments inutiles.
- **Nettoyage de code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **i18n :** Mise à jour des clés de traduction pour la nouvelle interface de sélection des lots.
