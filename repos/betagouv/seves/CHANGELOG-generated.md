## Changelog : seves (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Sèves se concentrent sur l'amélioration de l'interface utilisateur, la correction de bugs et l'ajout de nouvelles fonctionnalités, notamment dans le module SV (Surveillance Vétérinaire). Des améliorations de performance et de fiabilité ont également été apportées, ainsi que des corrections de sécurité.

### Évolutions fonctionnelles
- Amélioration de l'affichage des sauts de ligne dans les commentaires des fiches Zone Délimitée et Détection dans le module SV. [#41e51dc](https://github.com/betagouv/seves/commit/41e51dc)
- Correction d'une régression dans le formulaire EvenementProduit (SSA) concernant le champ produit prêt à manger avec le nouveau sélecteur arborescent. [#c8bc916](https://github.com/betagouv/seves/commit/c8bc916)
- Ajout de la possibilité de filtrer par structure sur la page d'administration via ChoiceJS. [#b31d352](https://github.com/betagouv/seves/commit/b31d352)
- Correction d'un problème avec le type MIME des fichiers EML. [#7ce4ef8](https://github.com/betagouv/seves/commit/7ce4ef8)
- Amélioration de l'affichage du label complet avec les catégories dans le bouton TreeSelect lors de la sélection d'un élément. [#71bf5c3](https://github.com/betagouv/seves/commit/71bf5c3)
- Ajout d'un panneau "éléments infestés" au formulaire SV, incluant l'affichage des lieux et prélèvements associés. [#a4f8599](https://github.com/betagouv/seves/commit/a4f8599) et [#8772c4e](https://github.com/betagouv/seves/commit/8772c4e)
- Possibilité de passer une référence Maestro lors de la création d'un événement, facilitant l'intégration. [#f02247c](https://github.com/betagouv/seves/commit/f02247c)
- Le nombre de personnes malades est maintenant obligatoire sur les TIAC (Troubles Immédiats Après Consommation). [#531e4a5](https://github.com/betagouv/seves/commit/531e4a5)
- Suppression de la limitation de 9 caractères pour le numéro RASFF dans le module SV. [#57251bc](https://github.com/betagouv/seves/commit/57251bc)
- Suppression du drapeau de fonctionnalité (feature flag) pour l'éditeur de texte enrichi. [#f8fe6ed](https://github.com/betagouv/seves/commit/f8fe6ed)
- Suppression du drapeau de fonctionnalité pour le téléchargement en ZIP. [#b9881ab](https://github.com/betagouv/seves/commit/b9881ab)

### Évolutions techniques
- Refactorisation de la recherche d'espèce dans le module SV pour utiliser un contrôleur Stimulus dédié. [#54c0ede](https://github.com/betagouv/seves/commit/54c0ede)
- Amélioration des performances du bloc commun. [#007ff4d](https://github.com/betagouv/seves/commit/007ff4d)
- Amélioration de la fiabilité de l'application account. [#f951dac](https://github.com/betagouv/seves/commit/f951dac)
- Correction d'une vulnérabilité XSS potentielle avec le numéro de rappel conso. [#306b5c1](https://github.com/betagouv/seves/commit/306b5c1)
- Adaptation des exports Europhyt dans le module SV. [#2cb9cc7](https://github.com/betagouv/seves/commit/2cb9cc7)
- Modification de l'API ChoiceJSPage pour la rendre réutilisable. [#35de83e](https://github.com/betagouv/seves/commit/35de83e)

### Autres changements
- Ajout d'un webhook pour notifier Maestro. [#3c50a2c](https://github.com/betagouv/seves/commit/3c50a2c)
- Mise à jour de l'URL de l'API BAN. [#5bf3107](https://github.com/betagouv/seves/commit/5bf3107)
- Suppression d'un avertissement dans les tests lié à django-widget-tweaks. [#c457d59](https://github.com/betagouv/seves/commit/c457d59)
- Diverses corrections et améliorations des tests pour augmenter leur fiabilité. [#583d0c7](https://github.com/betagouv/seves/commit/583d0c7), [#954a743](https://github.com/betagouv/seves/commit/954a743), [#34ff415](https://github.com/betagouv/seves/commit/34ff415), [#a14eb40](https://github.com/betagouv/seves/commit/a14eb40), [#8857987](https://github.com/betagouv/seves/commit/8857987)
- Mise à jour des dépendances : sentry-sdk, ruff, pytest-rerunfailures, pytest-playwright, gunicorn, urllib3, django, django-reversion, idna, playwright. (Ces mises à jour sont gérées par Dependabot et ne sont pas détaillées individuellement).
