## Changelog : mle-back (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la recherche de logements, l'ajout de nouvelles sources de données (Campus et Toits, Cardinal Campus, SAIEM Dragouignan), et l'intégration de statistiques et de suivi via Matomo. Des améliorations ont également été apportées à l'export des données, à la gestion des prix et des images, ainsi qu'à la notification des utilisateurs.

### Évolutions fonctionnelles
- Ajout de la source de logements "Campus et Toits" [#873263d](https://github.com/betagouv/mle-back/commit/873263d).
- Ajout de la source de logements "Cardinal Campus" [#fbef5a3](https://github.com/betagouv/mle-back/commit/fbef5a3).
- Ajout de la source de logements "SAIEM Dragouignan" [#3574821](https://github.com/betagouv/mle-back/commit/3574821).
- Amélioration du filtre de recherche avec l'ajout de prix minimum et maximum [#38b7682](https://github.com/betagouv/mle-back/commit/38b7682).
- L'export des logements au format Excel inclut désormais les informations de disponibilité [#c831251](https://github.com/betagouv/mle-back/commit/c831251).
- L'export des logements est désormais disponible via un lien de téléchargement [#eba8e5b](https://github.com/betagouv/mle-back/commit/eba8e5b).
- Ajout de la possibilité d'importer les prix du CROUS via une commande spécifique [#d37f968](https://github.com/betagouv/mle-back/commit/d37f968).
- Amélioration du classement des logements dans les résultats de recherche [#c0949ff](https://github.com/betagouv/mle-back/commit/c0949ff).
- Ajout de la gestion des notifications (en production et en staging) avec l'historisation des modifications [#08edd43](https://github.com/betagouv/mle-back/commit/08edd43).
- Ajout de la date de dernière connexion pour les utilisateurs [#08edd43](https://github.com/betagouv/mle-back/commit/08edd43).

### Évolutions techniques
- Intégration de Matomo pour le suivi des événements et des statistiques [#3e99f65](https://github.com/betagouv/mle-back/commit/3e99f65).
- Amélioration significative de la recherche avec l'utilisation de FTS (Full Text Search) et un fallback vers trigram [#0d6bff9](https://github.com/betagouv/mle-back/commit/0d6bff9).
- Refonte du service de gestion des villes [#6f4a589](https://github.com/betagouv/mle-back/commit/6f4a589).
- Amélioration de la gestion des images lors de la création d'un logement [#f5c2c71](https://github.com/betagouv/mle-back/commit/f5c2c71).
- Utilisation d'un geolocator mocké pour les tests [#f6e23d5](https://github.com/betagouv/mle-back/commit/f6e23d5).
- Mise à jour de Ruff (linter) vers la version 0.15.0 [#c30f750](https://github.com/betagouv/mle-back/commit/c30f750).
- Mise à jour de Sentry SDK vers les versions 2.51.0 et 2.52.0 [#c4dc15f](https://github.com/betagouv/mle-back/commit/c4dc15f) et [#3574821](https://github.com/betagouv/mle-back/commit/3574821).

### Autres changements
- Correction de bugs liés aux migrations de la base de données [#3eaba48](https://github.com/betagouv/mle-back/commit/3eaba48), [#ab00dfa](https://github.com/betagouv/mle-back/commit/ab00dfa), [#873263d](https://github.com/betagouv/mle-back/commit/873263d).
- Correction d'un problème d'URL pour les images [#ea50a3e](https://github.com/betagouv/mle-back/commit/ea50a3e).
- Correction d'un bug dans les tests [#ad874ef](https://github.com/betagouv/mle-back/commit/ad874ef), [#4b4faa0](https://github.com/betagouv/mle-back/commit/4b4faa0), [#242af63](https://github.com/betagouv/mle-back/commit/242af63).
- Ajout de variables d'environnement pour Matomo [#a32c2e9](https://github.com/betagouv/mle-back/commit/a32c2e9), [#07f0cf4](https://github.com/betagouv/mle-back/commit/07f0cf4).
- Amélioration de la gestion des erreurs et ajout de logs [#58021e7](https://github.com/betagouv/mle-back/commit/58021e7).
- Correction d'un problème avec les slugs [#76d2139](https://github.com/betagouv/mle-back/commit/76d2139).
- Ajout de champs manquants aux serializers [#d0ebafc](https://github.com/betagouv/mle-back/commit/d0ebafc).
- Correction de la gestion des prix minimum et maximum [#d86b071](https://github.com/betagouv/mle-back/commit/d86b071), [#79f1202](https://github.com/betagouv/mle-back/commit/79f1202).
- Ajout d'une référence externe pour faciliter l'intégration avec les APIs externes [#d4bc45d](https://github.com/betagouv/mle-back/commit/d4bc45d).
- Correction d'un problème avec l'encodage UTF-8 [#f955c00](https://github.com/betagouv/mle-back/commit/f955c00).
- Correction d'un bug dans la requête POST de Matomo [#f283f18](https://github.com/betagouv/mle-back/commit/f283f18).
