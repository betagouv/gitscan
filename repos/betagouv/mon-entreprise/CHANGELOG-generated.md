## Changelog : mon-entreprise (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du simulateur pour les travailleurs frontaliers suisses, avec l'ajout d'un nouveau simulateur et de nombreuses corrections. Des améliorations ont également été apportées au comparateur de statuts, notamment au niveau de l'expérience utilisateur et de la précision des informations affichées. Enfin, des corrections et des mises à jour ont été apportées aux modèles de calcul et à la documentation.

### Évolutions fonctionnelles
- Ajout d'un nouveau simulateur pour les cotisations maladie des travailleurs frontaliers suisses. [#79fa6d7](https://github.com/betagouv/mon-entreprise/commit/79fa6d7)
- Amélioration de l'expérience utilisateur du comparateur de statuts : déplacement des cartes de statut, réduction des espacements, correction de l'affichage des réponses et des montants. [#e6f41de](https://github.com/betagouv/mon-entreprise/commit/e6f41de), [#e18d234](https://github.com/betagouv/mon-entreprise/commit/e18d234), [#45fb4c3](https://github.com/betagouv/mon-entreprise/commit/45fb4c3), [#1a989fd](https://github.com/betagouv/mon-entreprise/commit/1a989fd)
- Correction de l'application de la réforme de l'acre (critère = date de création de l'entreprise). [#9eaaca0](https://github.com/betagouv/mon-entreprise/commit/9eaaca0)
- Correction de la participation de la CPAM en cas d'exonérations. [#a77f57e](https://github.com/betagouv/mon-entreprise/commit/a77f57e)
- Correction de l'Acre non applicable en outre-mer. [#12f222f](https://github.com/betagouv/mon-entreprise/commit/12f222f)
- Ajout de la carte du statut AE au choix du statut. [#8883d77](https://github.com/betagouv/mon-entreprise/commit/8883d77)

### Évolutions techniques
- Refactor de l'API : dérivation des chemins du cache depuis les modèles, factorisation du découpage du chemin, réorganisation des middlewares. [#c056484](https://github.com/betagouv/mon-entreprise/commit/c056484), [#add7d30](https://github.com/betagouv/mon-entreprise/commit/add7d30), [#63e2851](https://github.com/betagouv/mon-entreprise/commit/63e2851)
- Amélioration de l'environnement de développement : adaptation du tracking, suppression du merge avec l'API Publicodes, gestion des variables d'environnement sous Vite. [#4446178](https://github.com/betagouv/mon-entreprise/commit/4446178), [#09c91d9](https://github.com/betagouv/mon-entreprise/commit/09c91d9), [#1a294df](https://github.com/betagouv/mon-entreprise/commit/1a294df)
- Refactor du code lié à l'i18n (internationalisation) pour une meilleure gestion des langues et des traductions. [#f0ecbf8](https://github.com/betagouv/mon-entreprise/commit/f0ecbf8), [#cbe771d](https://github.com/betagouv/mon-entreprise/commit/cbe771d), [#a51003b](https://github.com/betagouv/mon-entreprise/commit/a51003b)
- Refactor du design system pour améliorer la réutilisabilité des composants. [#812b767](https://github.com/betagouv/mon-entreprise/commit/812b767), [#583c8cf](https://github.com/betagouv/mon-entreprise/commit/583c8cf)

### Autres changements
- Mise à jour de la documentation sur la librairie de calcul. [#b4751ae](https://github.com/betagouv/mon-entreprise/commit/b4751ae)
- Mise à jour des paquets `modele-ti` et `modele-as`. [#2e78697](https://github.com/betagouv/mon-entreprise/commit/2e78697)
- Corrections de traductions et de clefs d'i18n. [#9aa5c22](https://github.com/betagouv/mon-entreprise/commit/9aa5c22)
- Ajout de tests unitaires. [#f4b163b](https://github.com/betagouv/mon-entreprise/commit/f4b163b)
- Corrections mineures de style et de layout.
- Correction d'un bug empêchant l'affichage correct des dates dans certains navigateurs. [#faa4c11](https://github.com/betagouv/mon-entreprise/commit/faa4c11)
