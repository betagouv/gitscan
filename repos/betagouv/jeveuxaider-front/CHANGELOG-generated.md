## Changelog : jeveuxaider-front (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment en facilitant la gestion des organisations et des missions. Des corrections et des améliorations techniques ont également été apportées pour optimiser la performance et la robustesse de la plateforme.

### Évolutions fonctionnelles
- Les organisations peuvent maintenant se désinscrire de manière autonome. [#322](https://github.com/betagouv/jeveuxaider-front/issues/322)
- Amélioration de l'affichage du nom des établissements dans les statistiques de visites. [#337](https://github.com/betagouv/jeveuxaider-front/issues/337)
- Ajout de Saint-Paul et d'Avignon à la liste des villes multi-distribuées, améliorant la géolocalisation. [#329](https://github.com/betagouv/jeveuxaider-front/issues/329)
- Ajout d'options de filtrage pour les notes autres que les mines. [#328](https://github.com/betagouv/jeveuxaider-front/issues/328)
- Ajout d'une pagination simple pour l'index des logs d'activité. [#323](https://github.com/betagouv/jeveuxaider-front/issues/323)
- Ajout d'un modal pour les utilisateurs sans numéro de téléphone ou code postal. [#321](https://github.com/betagouv/jeveuxaider-front/issues/321)
- Amélioration de la carte de mission avec des détails sur l'activité et la localisation. [#327](https://github.com/betagouv/jeveuxaider-front/issues/327)
- Ajout de la possibilité de changer de rôle et amélioration de la gestion des erreurs liées à l'authentification. [#318](https://github.com/betagouv/jeveuxaider-front/issues/318)
- Restriction de l'accès à l'index des réseaux à l'administrateur. [#320](https://github.com/betagouv/jeveuxaider-front/issues/320)

### Évolutions techniques
- Refactorisation des composants modaux pour utiliser `useForm` pour la gestion des formulaires et la validation.
- Refactorisation des composants de prévisualisation de mission et de la boîte d'organisation pour utiliser `BaseTextFormatted` pour le rendu des descriptions.
- Mise à jour du composant `Select` pour accepter `null` comme valeur valide et nettoyage du code inutilisé dans les composants modaux.
- Ajout du rôle 'responsable' à la condition de visibilité de l'ID de mission. [#318](https://github.com/betagouv/jeveuxaider-front/issues/318)
- Optimisation de l'inclusion des dépendances dans la configuration Nuxt pour éviter les rechargements en développement. [#336](https://github.com/betagouv/jeveuxaider-front/issues/336)

### Autres changements
- Correction de l'affichage du nom au lieu de la clé dans les statistiques de visites. [#337](https://github.com/betagouv/jeveuxaider-front/issues/337)
- Ajout des dépendances `chartjs-plugin-annotation` et `chartjs-plugin-datalabels` pour corriger un problème avec les graphiques. [#336](https://github.com/betagouv/jeveuxaider-front/issues/336)
