## Changelog : sylvasan (30 derniers jours, au 16 juin 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'application mobile, notamment en termes de géolocalisation, d'affichage des cartes et de gestion des images. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, ainsi que des optimisations de performance et des mises à jour de dépendances. L'authentification via DSF a été améliorée et des fonctionnalités de filtrage et d'export des réponses ont été ajoutées.

### Évolutions fonctionnelles
- **Authentification :** Amélioration de l'authentification via DSF, avec affichage d'un spinner pendant la connexion et gestion des sessions après redémarrage. [#244](https://github.com/betagouv/sylvasan/pull/244)
- **Géolocalisation :** Ajout de la géolocalisation native dans le champ "MapField" sur l'application mobile, permettant de positionner la carte en touchant l'écran. [#350](https://github.com/betagouv/sylvasan/pull/350)
- **Images :** Ajout d'une galerie de visualisation des images, compression des images, et gestion du stockage local. [#314](https://github.com/betagouv/sylvasan/pull/314)
- **Export :** Implémentation de l'export des réponses. [#287](https://github.com/betagouv/sylvasan/pull/287)
- **Filtrage :** Ajout d'un filtre par enquête pour les réponses. [#317](https://github.com/betagouv/sylvasan/pull/317)
- **Affichage :** Affichage des coordonnées GPS dans l'application mobile. [#374](https://github.com/betagouv/sylvasan/pull/374)
- **Champs conditionnels :** Implémentation de champs conditionnels avec affichage et validation. [#286](https://github.com/betagouv/sylvasan/pull/286)
- **Vocabulaires :** Amélioration de l'affichage et de la gestion des vocabulaires. [#285](https://github.com/betagouv/sylvasan/pull/285)

### Évolutions techniques
- **Performance :** Améliorations de performance sur les réponses, notamment via le préchargement des images. [#370](https://github.com/betagouv/sylvasan/pull/370)
- **Infrastructure :** Mise à jour de nombreuses dépendances (Django, boto3, requests, etc.).
- **Architecture :** Utilisation de Django Storages pour la gestion des fichiers. [#282](https://github.com/betagouv/sylvasan/pull/282)
- **Tests :** Ajout de tests pour la sérialisation des organisations et des pôles.
- **CI/CD :** Mises à jour des workflows CI/CD.

### Autres changements
- Correction de coquilles et de bugs mineurs.
- Amélioration de la gestion des erreurs et des validations.
- Ajustements d'interface utilisateur (UI) sur le web et le mobile.
- Ajout d'icônes pour l'application Android.
- Suppression de code mort.
- Mise à jour de la documentation.
- Corrections de warnings Typescript.
- Ajout de spinners pour améliorer l'expérience utilisateur pendant les chargements.
- Amélioration de la gestion des erreurs de validation dans les formulaires.
- Ajout de messages de confirmation pour les suppressions.
- Correction de bugs liés à la hauteur des tabs dans le formulaire.
- Amélioration de la gestion des vocabulaires et des références.
- Mise à jour de la version de l'application Android (0.0.17).
- Ajout d'un bouton pour fermer la page de téléchargement de cartes.
- Suppression du message d'ETA dans le téléchargement de cartes.
- Ajout d'un modal de confirmation pour la suppression d'une page.
- Correction du bug de suppression d'options.
- Correction du bug de type de champ lors de l'édition.
- Ajout d'un autocomplete avec gestion des accents.
- Ajout de la possibilité de modifier les sous-champs.
- Ajout de la gestion des champs image.
- Correction de bugs liés à l'affichage des champs.
- Amélioration de la gestion des erreurs et des validations.
- Ajout de la pagination dans la vue réponses.
- Ajout de l'affichage des labels pour les vocabulaires web.
- Ajout de la possibilité de filtrer par enquête.
- Ajout de la gestion des conditions d'affichage pour les champs.
- Amélioration de la gestion des sessions et de l'authentification.
- Ajout de la gestion des erreurs et des validations.
- Correction de bugs liés à l'affichage des champs.
- Amélioration de la gestion des erreurs et des validations.
- Ajout de la pagination dans la vue réponses.
- Ajout de l'affichage des labels pour les vocabulaires web.
- Ajout de la possibilité de filtrer par enquête.
- Ajout de la gestion des conditions d'affichage pour les champs.
- Amélioration de la gestion des sessions et de l'authentification.
