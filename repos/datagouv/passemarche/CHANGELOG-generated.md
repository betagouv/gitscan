## Changelog : passemarche (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des lots, notamment pour les marchés publics mono-types, avec une refonte de l'interface utilisateur et de la logique associée. Des ajustements ont également été apportés à l'authentification des candidats et à la configuration des URLs de redirection. Enfin, plusieurs mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- **Gestion des lots :** Refonte de la page de sélection des lots avec une présentation en deux états (sélectionner / préparer) [#391](https://github.com/datagouv/passemarche/pull/391).
- **Gestion des lots :** Affichage des types de lots reçus de la plateforme d'achat [#383](https://github.com/datagouv/passemarche/pull/383).
- **Gestion des lots :** Simplification de l'affichage des lots avec des tags et un tableau détaillé en annexe [#378](https://github.com/datagouv/passemarche/pull/378).
- **Authentification candidat :** Amélioration de la gestion des URLs de redirection après authentification pour l'acheteur et le candidat [#378](https://github.com/datagouv/passemarche/pull/378).
- **Suppression de candidature :** Ajout de la fonctionnalité permettant de supprimer une candidature [#377](https://github.com/datagouv/passemarche/pull/377).
- **Attestation candidat :** Ajustements de l'interface utilisateur pour l'attestation candidat, notamment pour les marchés avec plusieurs lots mono-types [#399](https://github.com/datagouv/passemarche/pull/399) et [#392](https://github.com/datagouv/passemarche/pull/392).

### Évolutions techniques
- **Refactoring authentification candidat :** Refactorisation de l'authentification des candidats pour améliorer la gestion du contexte de session [#376](https://github.com/datagouv/passemarche/pull/376).
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances, notamment Doorkeeper, Solid Cable, View Component, Bootsnap, Pagy, Faraday, Devise et Selenium-webdriver.

### Autres changements
- Amélioration de la documentation et des tests pour les nouvelles fonctionnalités.
- Corrections de bugs et améliorations de la performance.
- Ajustements de l'interface utilisateur et des traductions.
- Corrections de RuboCop offenses.
