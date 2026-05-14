## Changelog : gestion-des-subventions-locales (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau des filtres de recherche, de la génération de documents (arrêtés et lettres) et de la gestion des simulations. Des optimisations ont également été apportées au proxy de l'API Demarches Simplifiées (DS) pour améliorer la performance et la sécurité. Enfin, des corrections de bugs et des améliorations techniques ont été implémentées pour stabiliser l'application.

### Évolutions fonctionnelles
- **Filtres de recherche améliorés :** Ajout d'une recherche floue sur l'intitulé, la raison sociale et le numéro de dossier dans les listes de projets, simulations et programmations [#701]. Le champ de recherche est maintenant réordonné après la réinitialisation des filtres.
- **Génération de documents :**
    - Amélioration significative du processus de génération d'arrêtés et de lettres, avec la possibilité de générer les deux types de documents simultanément et de choisir le format d'exportation.
    - Le parcours de génération de documents en masse a été déplacé dans une modale pour une meilleure expérience utilisateur [#697].
    - Possibilité de gérer les erreurs lors de la génération de documents.
    - Amélioration de la gestion des fichiers générés (nommage, caractères valides).
- **Simulations :**
    - Ajout de la possibilité de changer le statut de plusieurs simulations en masse.
    - Persistance de l'ordre de tri des listes de simulations en plus des filtres.
    - Correction d'un bug empêchant l'affichage correct des documents d'une autre dotation dans l'onglet Programmation.
    - Amélioration de la logique pour ne pas sélectionner les projets programmés sur des enveloppes antérieures lors de la création de simulations.
- **Proxy DS :**
    - Amélioration de la sécurité du proxy DS en limitant la portée des tokens d'autorisation à une démarche spécifique.
    - Ajout d'un proxy GraphQL pour l'API DS, filtré par les instructeurs.
    - Optimisation du proxy DS pour éviter les timeouts Scalingo en streamant un heartbeat.
- **Administration :**
    - Ajout d'une action dans l'interface d'administration pour récupérer un dossier depuis DN [#696].
    - Possibilité pour les utilisateurs DN de mettre à jour leur adresse email [#700].
- **FAQ :** Création d'une première version de la FAQ [#672].

### Évolutions techniques
- **Refactoring :** Plusieurs refactorings ont été effectués pour améliorer la qualité du code et la maintenabilité, notamment au niveau de la génération de documents et de la gestion des simulations.
- **Performance :**
    - Optimisation des requêtes GraphQL pour le proxy DS afin de réduire les timeouts.
    - Évaluation paresseuse des choix dans les FilterSet [#703] pour améliorer la performance des filtres.
- **Tests :**
    - Ajout de tests pour la tâche de nettoyage des projets programmés sur des enveloppes antérieures.
    - Empêchement des requêtes HTTP non mockées dans les tests pour une meilleure fiabilité.
    - Rendre `dotation_not_treated` déterministe pour stabiliser un test flaky [#660].
- **CI/CD :** Ajout d'une commande `just release-dry-run` pour prévisualiser un tag et ses notes de version [#680]. Exécution des tests sur les branches `hotfix/*` [#686].
- **Sécurité :** Stockage du hash des tokens du proxy DS au lieu du texte en clair.

### Autres changements
- Mise à jour de l'URL du script HeatmapSessionRecording de Matomo [#687].
- Correction de typos CSS [#690].
- Ajout de la librairie `django-query-counter` pour le profilage des requêtes.
- Amélioration de la mise en page des arrêtés et lettres.
- Validation de l'assiette avant l'acceptation d'une dotation.
- Suppression des logs verbeux de `fontTools` en production [#684].
- Ajout de liens vers les dossiers dans l'interface d'administration pour les documents.
- Suppression du Demandeur (doublon) pour ne conserver que le demandeur au niveau du dossier [#670].
- Mise à jour de l'enveloppe lorsqu'on modifie les montants des projets acceptés [#674].
- Utilisation des champs actifs d'une démarche DN [#668].
- Correction de l'affichage de la date de notification [#695].
- Suppression du `dotation_projet` des simulations hors-périmètre lorsque le périmètre du dossier a changé [#656].
- Ajout de la possibilité de fermer la modale "Vous ne faites pas partie du groupe d'instructeurs" [#690].
