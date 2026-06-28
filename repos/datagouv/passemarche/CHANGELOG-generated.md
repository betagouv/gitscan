## Changelog : passemarche (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des lots, notamment pour les marchés publics proposant des lots de types différents. Des corrections et des améliorations UX ont été apportées pour faciliter la sélection et la configuration des lots, ainsi que la mise à jour des informations relatives aux marchés. Des ajustements ont également été faits pour améliorer la robustesse et la maintenance du code.

### Évolutions fonctionnelles
- **Gestion des lots hétérogènes :** Possibilité de candidater à des lots de types différents sur un même marché ([#405](https://github.com/datagouv/passemarche/pull/405), [#420](https://github.com/datagouv/passemarche/pull/420)).
- **Configuration des lots :** Amélioration de la configuration des pièces justificatives pour les marchés ([#404](https://github.com/datagouv/passemarche/pull/404), [#413](https://github.com/datagouv/passemarche/pull/413)).
- **Affichage des lots :** Affichage du type de chaque lot dans l'annexe PDF et dans les tags de la page de préparation ([#420](https://github.com/datagouv/passemarche/pull/420)).
- **Mise à jour de la DLRO :** Ajout d'une API pour mettre à jour la Date Limite de Réponse (DLRO) d'un marché ([#418](https://github.com/datagouv/passemarche/pull/418)).
- **Collapsible des listes de lots :** Implémentation d'un affichage collapsible pour les longues listes de lots, améliorant la lisibilité et l'ergonomie ([#419](https://github.com/datagouv/passemarche/pull/419)).
- **Amélioration de l'UX :** Correction de l'affichage des noms des lots et du nombre de lots sur la page de configuration ([#434](https://github.com/datagouv/passemarche/pull/434)).
- **Icônes de types de marché :** Ajout d'icônes pour les différents types de marché (travaux, services, fournitures) pour une meilleure identification visuelle ([#415](https://github.com/datagouv/passemarche/pull/415)).

### Évolutions techniques
- **Refactoring API :** Extraction de helpers et centralisation de la création de marchés/candidatures pour améliorer la maintenabilité du code ([#407](https://github.com/datagouv/passemarche/pull/407)).
- **Tests :** Ajout de tests RSpec et Cucumber pour les nouvelles fonctionnalités et corrections de bugs.
- **Documentation :** Mise à jour de la documentation de l'API et des scripts de seed.
- **Seed market :** Création d'un script pour générer un marché de test avec 1000 lots ([#421](https://github.com/datagouv/passemarche/pull/421)).
- **PaperTrail :** Activation de PaperTrail sur PublicMarket pour l'historisation des changements de deadline ([#537](https://github.com/datagouv/passemarche/pull/537)).

### Autres changements
- Mise à jour des dépendances : plusieurs dépendances ont été mises à jour vers leurs dernières versions stables (Doorkeeper, Selenium, Shoulda Matchers, Faraday, Bootsnap, Puma, Jbuilder, Sentry-rails, Rubyzip, View Component).
- Correction de bugs mineurs et améliorations de la qualité du code.
- Amélioration de l'affichage des badges de type de marché.
- Correction de la traduction manquante d'un badge.
