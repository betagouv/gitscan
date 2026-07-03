## Changelog : passemarche (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des lots dans les marchés publics, avec notamment la possibilité de gérer des listes de lots plus longues, de modifier le type de lots et de configurer les pièces justificatives associées. Des corrections et améliorations de l'expérience utilisateur ont également été apportées, ainsi que des optimisations techniques et des mises à jour de dépendances.

### Évolutions fonctionnelles
- **Gestion des lots :**
    - Possibilité de gérer des listes de lots plus longues grâce à un affichage "collapsible" (plié/déplié). [#419](https://github.com/datagouv/passemarche/pull/419)
    - Possibilité de modifier le type de lots existants. [#416](https://github.com/datagouv/passemarche/pull/416)
    - Configuration des pièces justificatives requises pour un marché. [#404](https://github.com/datagouv/passemarche/pull/404) et [#413](https://github.com/datagouv/passemarche/pull/413)
    - Affichage du type de chaque lot dans l'annexe PDF générée. [#420](https://github.com/datagouv/passemarche/pull/420)
- **Candidature :**
    - Possibilité de re-candidater à un marché avant la date limite. [#438](https://github.com/datagouv/passemarche/pull/438)
    - Amélioration de l'expérience utilisateur lors de la candidature à des lots de types différents. [#405](https://github.com/datagouv/passemarche/pull/405)
- **Interface utilisateur :**
    - Ajout d'icônes pour les différents types de marchés (travaux, services, fournitures). [#415](https://github.com/datagouv/passemarche/pull/415) et [#420](https://github.com/datagouv/passemarche/pull/420)
    - Amélioration de l'affichage des noms des lots. [#434](https://github.com/datagouv/passemarche/pull/434)
    - Correction de l'affichage des badges de type de marché. [#418](https://github.com/datagouv/passemarche/pull/418)
- **Administration :**
    - Possibilité de modifier la date limite de dépôt des offres (DLRO) via l'API. [#426](https://github.com/datagouv/passemarche/pull/426)

### Évolutions techniques
- **Infrastructure :**
    - Ajout de la gem `aws-sdk-s3` pour l'utilisation de S3 Active Storage en environnement sandbox. [#444](https://github.com/datagouv/passemarche/pull/444)
- **Architecture :**
    - Refonte de la gestion des étapes du wizard candidat pour les acheteurs. [#407](https://github.com/datagouv/passemarche/pull/407)
    - Extraction de helpers pour centraliser la création de marchés et de candidatures. [#407](https://github.com/datagouv/passemarche/pull/407)
    - Utilisation de Stimulus pour le comportement "collapsible" des listes de lots. [#419](https://github.com/datagouv/passemarche/pull/419)
- **Tests :**
    - Ajout de tests RSpec et Cucumber pour les nouvelles fonctionnalités.
    - Ajout de tests pour la modification du type de lots. [#416](https://github.com/datagouv/passemarche/pull/416)
    - Ajout de tests pour la mise à jour de la DLRO via l'API. [#426](https://github.com/datagouv/passemarche/pull/426)

### Autres changements
- Documentation du script de seed pour créer un marché de test avec 1000 lots. [#423](https://github.com/datagouv/passemarche/pull/423)
- Documentation de la re-candidature et du blocage de la deadline. [#426](https://github.com/datagouv/passemarche/pull/426)
- Correction de l'affichage d'un message d'information dans Lookbook. [#435](https://github.com/datagouv/passemarche/pull/435)
- Correction de l'ordre des sous-catégories dans le wizard candidat pour les marchés hétérogènes. [#405](https://github.com/datagouv/passemarche/pull/405)
- Correction d'un problème de chargement de l'API lors du seed de 1000 lots. [#441](https://github.com/datagouv/passemarche/pull/441)
- Mise à jour de plusieurs dépendances (rubyzip, selenium-webdriver, doorkeeper, faraday, bootsnap, view_component, sentry-rails, shoulda-matchers, pagy).
