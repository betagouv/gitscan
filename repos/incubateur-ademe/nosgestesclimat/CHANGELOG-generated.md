## Changelog : nosgestesclimat (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment via des ajustements de traduction, des corrections de wording et l'ajout de nouvelles fonctionnalités comme un éditeur de situations et un outil de sauvegarde. Des optimisations techniques ont également été apportées, incluant des mises à jour de packages et des corrections de workflows.

### Évolutions fonctionnelles
- **Traduction et Wording :** Améliorations significatives des traductions et du wording dans plusieurs sections de l'application, notamment concernant le transport, la piscine, l'avion et le chauffage. Ces modifications visent à rendre l'application plus claire et plus précise pour les utilisateurs.
- **Éditeur de situations :** Ajout d'un éditeur de situations avec vérification des erreurs et complétion automatique [#2740](https://github.com/incubateur-ademe/nosgestesclimat/issues/2740).
- **Partage de situations :** Possibilité de partager des situations configurées [#2740](https://github.com/incubateur-ademe/nosgestesclimat/issues/2740).
- **Mode scolaire :** Corrections et améliorations du wording et des actions disponibles en mode scolaire. Suppression des actions "café" et "JVA" en mode scolaire.
- **Calculs :** Mise à jour des chiffres relatifs à la consommation d'eau avec la version réglementaire.
- **Funfacts :** Correction des conditions d'affichage des "funfacts".
- **Suppression de marques :** Suppression de certaines marques dans les options de configuration.

### Évolutions techniques
- **Mise à jour des packages et de Node.js :** Mise à jour des dépendances et de la version de Node.js pour améliorer la sécurité et les performances.
- **Workflow CI/CD :** Correction du workflow de publication de la documentation.
- **Infrastructure :** Utilisation d'un modèle depuis Scaleway.
- **Publicodes :** Mise à jour de la base de données Publicodes ED-fr.
- **Suppression du support de l'espagnol :** Suppression de la langue espagnole des langues supportées.

### Autres changements
- **Documentation :** Amélioration de la documentation et publication de la documentation rapide (quick-doc).
- **Nettoyage du code :** Suppression de code de débogage et de lignes de sortie inutiles.
- **Sauvegarde :** Ajout d'une commande "save" dans l'éditeur pour sauvegarder les configurations.
- **Gestion des commits :** Utilisation du hash du commit pour la publication.
- **Correction de bugs :** Correction de plusieurs bugs mineurs liés à l'affichage et au fonctionnement de l'application.
