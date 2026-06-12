## Changelog : passemarche (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Passe Marché se concentrent sur l'amélioration de l'expérience utilisateur lors de la sélection et de la configuration des lots, notamment pour les marchés hétérogènes. Des corrections et des ajustements ont été apportés pour une meilleure gestion des types de lots et des pièces justificatives. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- **Gestion des lots :** Amélioration de l'interface de sélection des lots avec une présentation en deux états (sélectionner/préparer) pour une meilleure clarté. [#391](https://github.com/datagouv/passemarche/pull/391)
- **Types de lots :** Affichage des types de lots reçus de la plateforme d'achat. [#383](https://github.com/datagouv/passemarche/pull/383)
- **Configuration des lots :** Possibilité de configurer les pièces justificatives pour un marché. [#413](https://github.com/datagouv/passemarche/pull/413)
- **Modification du type de lots :** Les utilisateurs peuvent maintenant modifier le type d'un ou plusieurs lots. [#416](https://github.com/datagouv/passemarche/pull/416)
- **Candidature à des lots de types différents :** Amélioration de la gestion des candidatures à des lots de types différents, avec affichage du type de chaque lot dans l'annexe PDF. [#420](https://github.com/datagouv/passemarche/pull/420)
- **Suppression de candidature :** Ajout de la fonctionnalité permettant de supprimer une candidature. [#377](https://github.com/datagouv/passemarche/pull/377)
- **Attestation candidat :** Ajustements de l'interface et du wording de l'attestation candidat pour les marchés avec plusieurs lots. [#392](https://github.com/datagouv/passemarche/pull/392) et [#382](https://github.com/datagouv/passemarche/pull/382)

### Évolutions techniques
- **Refactoring du code :** Extraction de composants et centralisation de la logique pour améliorer la maintenabilité et la lisibilité du code, notamment dans la gestion des étapes du wizard. [#407](https://github.com/datagouv/passemarche/pull/407)
- **Amélioration des tests :** Ajout et mise à jour des tests RSpec et Cucumber pour couvrir les nouvelles fonctionnalités et les corrections. [#415](https://github.com/datagouv/passemarche/pull/415) et [#414](https://github.com/datagouv/passemarche/pull/414)
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances (Doorkeeper, Solid Cable, View Component, Bootsnap, Pagy, Selenium-webdriver, Faraday, Thruster, Jbuilder) pour bénéficier des dernières corrections de sécurité et améliorations de performance.

### Autres changements
- **Icônes :** Ajout d'icônes pour les types de marché (fournitures, travaux, services) et amélioration de leur affichage. [#418](https://github.com/datagouv/passemarche/pull/418) et [#420](https://github.com/datagouv/passemarche/pull/420)
- **Documentation :** Mise à jour de la documentation interne et des fichiers i18n.
- **Améliorations UI/UX :** Ajustements de l'interface utilisateur et de l'expérience utilisateur pour une meilleure ergonomie.
