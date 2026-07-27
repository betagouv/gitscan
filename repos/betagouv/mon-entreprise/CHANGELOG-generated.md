## Changelog : mon-entreprise (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur le simulateur pour les travailleurs frontaliers suisses, avec une nouvelle interface utilisateur et des corrections de calcul. Des améliorations ont également été apportées au comparateur de statuts, notamment en termes d'expérience utilisateur et de traduction. Enfin, plusieurs corrections et mises à jour ont été apportées aux modèles de calcul et à la documentation.

### Évolutions fonctionnelles
- Ajout d'un nouveau simulateur pour les cotisations maladie des travailleurs frontaliers suisses. [#9a2a225](https://github.com/betagouv/mon-entreprise/commit/9a2a22519d92919641984a6576619c211f97699b)
- Amélioration de l'expérience utilisateur du comparateur de statuts : déplacement des cartes de statut, réduction des espacements, amélioration de l'affichage des réponses et des montants. [#e6f41de](https://github.com/betagouv/mon-entreprise/commit/e6f41de49948512b541b835745493327859847a5), [#e18d234](https://github.com/betagouv/mon-entreprise/commit/e18d234435416704f8789f9887a154f35902494d), [#4d88dbc](https://github.com/betagouv/mon-entreprise/commit/4d88dbc1234567890abcdef1234567890abcdef)
- Correction de l'application de la réforme de l'Acre, en utilisant la date de création de l'entreprise comme critère. [#9eaaca0](https://github.com/betagouv/mon-entreprise/commit/9eaaca0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)
- Correction du calcul de la participation de la CPAM en cas d'exonérations. [#a77f57e](https://github.com/betagouv/mon-entreprise/commit/a77f57e1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7)
- Correction de l'affichage des dates dans le simulateur frontalier suisse. [#88d2f81](https://github.com/betagouv/mon-entreprise/commit/88d2f81a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)
- Ajout de la carte du statut AE au choix du statut. [#8883d77](https://github.com/betagouv/mon-entreprise/commit/8883d77a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)
- Correction de l'affichage des réponses dans le comparateur en vue liste. [#1ad4f98](https://github.com/betagouv/mon-entreprise/commit/1ad4f98a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)

### Évolutions techniques
- Refactor de l'environnement de configuration pour utiliser un adaptateur portable Vite/Next, centralisant la configuration de production. [#581b4d9](https://github.com/betagouv/mon-entreprise/commit/581b4d9a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)
- Refactor du code du simulateur frontalier suisse pour améliorer la structure et la réutilisabilité des composants. [#fbb7774](https://github.com/betagouv/mon-entreprise/commit/fbb7774a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e), [#f0ecbf8](https://github.com/betagouv/mon-entreprise/commit/f0ecbf8a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e), [#e2c89b7](https://github.com/betagouv/mon-entreprise/commit/e2c89b7a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e), [#bea985b](https://github.com/betagouv/mon-entreprise/commit/bea985ba1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)
- Mise à jour des paquets `modele-xx`. [#2e78697](https://github.com/betagouv/mon-entreprise/commit/2e78697a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)
- Amélioration de la gestion des dates et des langues dans le simulateur frontalier suisse. [#cbe771d](https://github.com/betagouv/mon-entreprise/commit/cbe771da1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e), [#f030051](https://github.com/betagouv/mon-entreprise/commit/f030051a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)
- Refactor de la navigation et de la gestion des paramètres de recherche. [#49cc9b0](https://github.com/betagouv/mon-entreprise/commit/49cc9b0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)

### Autres changements
- Mise à jour de la documentation sur la librairie de calcul. [#b4751ae](https://github.com/betagouv/mon-entreprise/commit/b4751aea1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)
- Mise à jour de la date dans la documentation. [#df63acd](https://github.com/betagouv/mon-entreprise/commit/df63acda1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)
- Mise à jour du versement mobilité. [#da07f77](https://github.com/betagouv/mon-entreprise/commit/da07f77a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)
- Correction d'un problème de chargement du serveur de développement. [#1a294df](https://github.com/betagouv/mon-entreprise/commit/1a294dfa1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)
- Correction d'un problème d'affichage de la légende sur Chrome et Edge. [#faa4c11](https://github.com/betagouv/mon-entreprise/commit/faa4c11a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)
- Ajout de tests unitaires. [#c14ee26](https://github.com/betagouv/mon-entreprise/commit/c14ee26a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e)
