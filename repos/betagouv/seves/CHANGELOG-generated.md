## Changelog : seves (30 derniers jours, au 02 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Sèves se concentrent sur l'amélioration de l'interface utilisateur, notamment dans les modules SV (Surveillance Vétérinaire) et SSA (Surveillance Sanitaire Animale), avec l'introduction de nouveaux composants comme le treeselect et des améliorations de la gestion des cartes. Des corrections de bugs et des optimisations de performance ont également été apportées pour une meilleure expérience utilisateur et une plus grande fiabilité de l'application.

### Évolutions fonctionnelles
- Amélioration de l'affichage des sauts de ligne dans les commentaires des fiches Zone Délimitée et Détection dans SV [#41e51dc](https://github.com/betagouv/seves/commit/41e51dc).
- Correction d'une régression dans SSA concernant le formulaire de produit prêt à manger avec le nouveau treeselect [#c8bc916](https://github.com/betagouv/seves/commit/c8bc916).
- Ajout d'une carte pour visualiser les lieux lors de la création et de la consultation dans SV [#205a251](https://github.com/betagouv/seves/commit/205a251), [#eaafbf2](https://github.com/betagouv/seves/commit/eaafbf2).
- Implémentation d'un nouveau composant treeselect dans SSA pour une meilleure sélection des options [#fce56df](https://github.com/betagouv/seves/commit/fce56df).
- Ajout d'un panneau "éléments infestés" au formulaire SV [#8772c4e](https://github.com/betagouv/seves/commit/8772c4e), [#a4f8599](https://github.com/betagouv/seves/commit/a4f8599).
- Amélioration de l'affichage des blocs "lieux" et "prélèvements" sur la page de détails SV [#a4f8599](https://github.com/betagouv/seves/commit/a4f8599).
- Ajout d'une fonctionnalité d'exportation des données au format CSV pour les TIAC avec un format amélioré [#9185ac3](https://github.com/betagouv/seves/commit/9185ac3).
- Possibilité de passer une référence Maestro lors de la création pour faciliter l'identification [#f02247c](https://github.com/betagouv/seves/commit/f02247c).
- Ajout d'un webhook pour notifier Maestro [#3c50a2c](https://github.com/betagouv/seves/commit/3c50a2c).
- Amélioration de l'historique dans SV [#62b3d87](https://github.com/betagouv/seves/commit/62b3d87).
- Suppression de la limite de caractères sur le numéro RASFF dans SV [#57251bc](https://github.com/betagouv/seves/commit/57251bc).
- Suppression de la fonctionnalité de téléchargement en ZIP (feature flag supprimé) [#b9881ab](https://github.com/betagouv/seves/commit/b9881ab).
- Suppression de la fonctionnalité de rich text editor (feature flag supprimé) [#f8fe6ed](https://github.com/betagouv/seves/commit/f8fe6ed).

### Évolutions techniques
- Refactorisation de l'API de recherche d'espèces dans SV pour l'encapsuler dans un contrôleur Stimulus dédié [#1117f22](https://github.com/betagouv/seves/commit/1117f22).
- Amélioration des performances du bloc commun [#007ff4d](https://github.com/betagouv/seves/commit/007ff4d).
- Optimisation de la fiabilité de l'application account [#f951dac](https://github.com/betagouv/seves/commit/f951dac).
- Modification de l'approche de mise à jour dans SV [#c827b59](https://github.com/betagouv/seves/commit/c827b59).
- Nettoyage du code pour la fonction choice_js_fill [#0f59252](https://github.com/betagouv/seves/commit/0f59252).
- Modification de l'ordre par défaut des TIAC et Alim [#f384cd2](https://github.com/betagouv/seves/commit/f384cd2).
- Amélioration de la réutilisation du composant ChoiceJSPage [#35de83e](https://github.com/betagouv/seves/commit/35de83e).

### Autres changements
- Corrections de tests pour améliorer la fiabilité des tests SV [#583d0c7](https://github.com/betagouv/seves/commit/583d0c7), [#a14eb40](https://github.com/betagouv/seves/commit/a14eb40), [#29e1913](https://github.com/betagouv/seves/commit/29e1913), [#6c3a2d1](https://github.com/betagouv/seves/commit/6c3a2d1).
- Correction d'une vulnérabilité XSS potentielle avec le numéro de rappel conso [#306b5c1](https://github.com/betagouv/seves/commit/306b5c1).
- Suppression d'un avertissement dans les tests lié à django-widget-tweaks [#c457d59](https://github.com/betagouv/seves/commit/c457d59).
- Correction de l'affichage des types MIME EML [#7ce4ef8](https://github.com/betagouv/seves/commit/7ce4ef8).
- Amélioration de la couleur des niveaux d'accordéon dans le treeselect [#dade33b](https://github.com/betagouv/seves/commit/dade33b).
- Exclusion des documents de la structure MUS lors de l'envoi de notifications [#4c14041](https://github.com/betagouv/seves/commit/4c14041).
- Correction de l'affichage des dates de réception [#a9ed4a6](https://github.com/betagouv/seves/commit/a9ed4a6).
- Mise à jour de plusieurs dépendances : ruff, pytest-rerunfailures, pytest-playwright, sentry-sdk, idna, playwright, django-reversion, gunicorn, urllib3.
