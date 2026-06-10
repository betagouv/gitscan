## Changelog : jeveuxaider-front (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des organisations et des missions, notamment en simplifiant les formulaires d'inscription et en ajoutant de nouvelles fonctionnalités pour la campagne d'été. Des corrections ont également été apportées pour améliorer l'expérience utilisateur sur mobile et pour la gestion des statistiques.

### Évolutions fonctionnelles
- **Gestion des organisations :** Refonte des formulaires d'inscription des organisations avec une meilleure gestion de l'adresse et des validations [#346](https://github.com/betagouv/jeveuxaider-front/issues/346).
- **Partage de missions :** Amélioration du partage de missions, notamment pour les utilisateurs non-gestionnaires [#353](https://github.com/betagouv/jeveuxaider-front/issues/353).
- **Campagne d'été :** Ajout d'un lien vers la campagne "Canicule" dans la navigation principale et mise à jour des informations relatives à la tournée d'été [#342](https://github.com/betagouv/jeveuxaider-front/issues/342).
- **Gestion des inscriptions :** Modification du libellé "Fermer les inscriptions" en "Mettre en pause les inscriptions" pour une meilleure clarté.
- **Statistiques :** Correction de l'affichage du nom dans les statistiques de visites et simplification de la logique des paramètres de requête.
- **Désinscription des organisations :** Possibilité pour les organisations de se désinscrire de manière autonome [#322](https://github.com/betagouv/jeveuxaider-front/issues/322).
- **Filtre de localisation :** Mise à jour des options de rayon dans le filtre de localisation, incluant 0 et 1000.
- **Gestion des ressources et réseaux :** Ajout de nouveaux formulaires pour la gestion des ressources et des réseaux avec validation, téléchargement de médias et gestion des rôles.
- **UTM parameters:** Ajout de paramètres UTM pour le suivi des invitations.

### Évolutions techniques
- **Refactoring :** Amélioration de la gestion de l'état des organisations et de la logique des badges.
- **Adresse :** Mise à jour de la logique de récupération de l'adresse dans le formulaire d'inscription des organisations.
- **API Plausible :** Mise à jour de l'API Plausible vers la version 2 et suppression d'un filtre de date défectueux.
- **Optimisation des dépendances :** Optimisation de l'inclusion des dépendances dans la configuration Nuxt pour éviter les rechargements en développement.
- **ARIA attributes:** Mise à jour des attributs ARIA pour éviter les erreurs liées aux attributs avec tiret.

### Autres changements
- **Documentation :** Mise à jour de la description du projet et de la pile technique dans le fichier README.
- **Labels Rolables:** Mise à jour des labels "rolables.fonction".
- **Corrections mineures :** Diverses corrections de bugs et améliorations de la qualité du code.
- **Suppression de code obsolète :** Suppression du composable `useAutocompleteSuggestions`.
- **Corrections de dates :** Mise à jour des dates de l'événement canicule de juin à août.
