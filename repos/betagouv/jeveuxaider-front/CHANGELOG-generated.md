## Changelog : jeveuxaider-front (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur et la gestion des organisations. Des améliorations ont été apportées aux formulaires, à la recherche de missions et à la gestion des utilisateurs, notamment l'ajout de la possibilité pour les organisations de se désinscrire elles-mêmes. Des corrections de bugs et des optimisations techniques ont également été réalisées.

### Évolutions fonctionnelles
- Les organisations peuvent maintenant se désinscrire de la plateforme de manière autonome. [#322](https://github.com/betagouv/jeveuxaider-front/issues/322)
- Amélioration de l'affichage du nom des visiteurs dans les statistiques des visites. [#337](https://github.com/betagouv/jeveuxaider-front/issues/337)
- Amélioration du filtre de localisation avec l'ajout des options de rayon 0 et 1000. [#339](https://github.com/betagouv/jeveuxaider-front/issues/339)
- Ajout de Saint-Paul et Avignon à la liste des villes multidistribuées pour une meilleure géolocalisation. [#329](https://github.com/betagouv/jeveuxaider-front/issues/329)
- Ajout d'options de filtrage pour les notes autres que les miennes. [#328](https://github.com/betagouv/jeveuxaider-front/issues/328)
- Ajout d'un composant de pagination simple pour l'index du journal d'activité. [#323](https://github.com/betagouv/jeveuxaider-front/issues/323)
- Ajout d'un modal pour les utilisateurs n'ayant pas renseigné leur numéro de téléphone et leur code postal. [#321](https://github.com/betagouv/jeveuxaider-front/issues/321)
- Amélioration des cartes de missions avec l'ajout de détails sur l'activité et la localisation. [#318](https://github.com/betagouv/jeveuxaider-front/issues/318)
- Ajout de la possibilité de changer de rôle utilisateur. [#318](https://github.com/betagouv/jeveuxaider-front/issues/318)
- Implémentation de la gestion des formulaires avec validation, soumission et vérification des rôles utilisateurs.
- Implémentation de la gestion des formulaires avec validation et support du téléchargement de médias.

### Évolutions techniques
- Refactorisation de la gestion des statistiques pour supprimer les props inutilisés et simplifier la logique des queryParams.
- Refactorisation des composants modaux pour utiliser `useForm` pour la gestion et la validation des formulaires.
- Refactorisation des composants `CardMission` et `OrganizationBox` pour utiliser `BaseTextFormatted` pour le rendu des descriptions.
- Optimisation de l'inclusion des dépendances dans `nuxt.config` pour éviter les rechargements en mode développement. [#336](https://github.com/betagouv/jeveuxaider-front/issues/336)
- Suppression du composable `useAutocompleteSuggestions`. [#340](https://github.com/betagouv/jeveuxaider-front/issues/340)

### Autres changements
- Ajout de champs supplémentaires dans les exports. [#327](https://github.com/betagouv/jeveuxaider-front/issues/327)
- Correction de l'affichage du nom au lieu de la clé dans les statistiques des visites.
- Correction de l'optimisation des dépendances pour inclure `chartjs-plugin-annotation` et `chartjs-plugin-datalabels`.
