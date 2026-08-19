## Changelog : complements-alimentaires (30 derniers jours, au 18 août 2026)

### Résumé
Ce mois a été marqué par une modernisation majeure de l'interface utilisateur avec la transition vers l'outil de build Vite. Parallèlement, plusieurs correctifs ont été apportés pour fiabiliser l'export de données (PDF, Excel) et améliorer la navigation, notamment en résolvant des erreurs d'accès (404) et en simplifiant la gestion des filtres pour les administrateurs et les utilisateurs.

### Évolutions fonctionnelles
- **Amélioration des filtres** : possibilité de supprimer les filtres actifs dans le tableau des entreprises (vue contrôle) et sur la liste des compléments alimentaires [#3066](https://github.com/betagouv/complements-alimentaires/pull/3066).
- **Corrections de navigation et d'affichage** :
    - Résolution d'une erreur 404 survenant lors de la consultation d'une déclaration sans déclarant [#3071](https://github.com/betagouv/complements-alimentaires/pull/3071).
    - Correction du filtre de statut [#3072](https://github.com/betagouv/complements-alimentaires/pull/3072).
    - Optimisation de l'affichage : masquage des tableaux vides pour les substances non actives et affichage ciblé des substances des ingrédients.
- **Fiabilisation des exports et formulaires** :
    - Correction des certificats PDF [#3034](https://github.com/betagouv/complements-alimentaires/pull/3034).
    - Correction de l'URL de téléchargement des fichiers Excel [#3064](https://github.com/betagouv/complements-alimentaires/pull/3064).
    - Correction du composant de création d'entreprise [#3063](https://github.com/betagouv/complements-alimentaires/pull/3063).

### Évolutions techniques
- **Modernisation du frontend** : migration de l'architecture vers **Vite** [#3050](https://github.com/betagouv/complements-alimentaires/pull/3050) et mise en place d'un nouveau workflow CI/CD pour le build frontend.
- **Refactorisation de l'API** : centralisation des appels API via une fonction dédiée (`createFetch`) et utilisation de variables d'environnement pour la gestion des URLs.
- **Optimisation de l'infrastructure** :
    - Amélioration de l'image Docker (nettoyage et ajout d'un fichier d'exemple pour les variables d'environnement).
    - Gestion optimisée des fichiers statiques et ajout d'un fichier `.htaccess`.
    - Maintenance du dossier `dist` dans le versionnage pour assurer la disponibilité des builds.

### Autres changements
- **Nettoyage du code** : suppression de bibliothèques obsolètes, de fichiers de configuration inutilisés (`python.json`) et de tags de template non utilisés.
- **Documentation et configuration** : mise à jour du README et déplacement du fichier `robots.txt`.
