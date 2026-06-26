## Changelog : nitrates (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration significative de la calculatrice de nitrates, notamment en ajoutant des fonctionnalités de saisie de dates, de gestion des périodes et de visualisation des données. Des améliorations ont également été apportées à l'interface d'administration pour faciliter la configuration et la gestion des données.

### Évolutions fonctionnelles
- **Calculatrice de nitrates :**
    - Généralisation de l'absorption des bornes adjacentes à une date saisie. [#129](https://github.com/betagouv/nitrates/pull/129)
    - Dates désormais paramétrables via l'URL, permettant une bidirectionnalité et une absorption des bornes par la date sélectionnée.
    - Label des bornes de zone affiché comme jour métier, et non bord géométrique.
    - Rendu du calendrier amélioré avec une palette unifiée, des ticks et un masque.
    - Possibilité de saisir et de rendre des conditions de période dans la calculatrice.
    - Ajout d'un composant JavaScript pour un calendrier dynamique dans le simulateur.
    - Serialisation de la feuille de calculatrice et branche template pour un rendu dynamique.
    - Ajout du champ `label_court` dans les inputs requis pour la spécification du rendu du simulateur.
- **Interface d'administration :**
    - Amélioration de l'éditeur YAML avec un highlight et un scroll du bloc édité.
    - Possibilité de réorganiser les branches par drag & drop et ajout d'un log pour les erreurs d'ajout d'enfant.
    - Amélioration des performances et de l'UX lors de la sauvegarde dans l'administration.
    - Ajout de boutons "+Ajouter" et "Corbeille" pour les inputs requis de la calculatrice.
    - Formulaire d'administration pour la calculatrice avec des structures et un composant select pour les inputs requis.
- **Validation couvert :**
    - Ajout d'un snapshot de l'arbre actif de la base de données.
    - Implémentation d'une application de validation couvert avec seed, feuilles et CRUD admin.
    - Ajout d'un screenshot de la borne et d'un script pour l'attacher, avec un lien vers le viewer.

### Évolutions techniques
- **Tests :**
    - Skip de 6 tests upstream Envergo cassés en contexte fork.
    - Alignement du test colza type III sur l'arbre.
- **Développement :**
    - Implémentation d'un autoreload fiable via watchdog/inotify.
    - Aplatissement des couverts d'interculture dans la grammaire.
    - Capture des erreurs de parcours dans l'administration.
- **Refactoring :**
    - Amélioration de la grammaire de la calculatrice.

### Autres changements
- Snapshot de l'arbre Miro complet du 30 mai 2026.
- Documentation et nettoyage du code.
