## Changelog : jeveuxaider-front (30 derniers jours, au 3 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la plateforme "Je veux aider" en se concentrant sur l'ajout de nouvelles fonctionnalités pour la gestion des ressources et des organisations, l'amélioration de la recherche et de la localisation, ainsi que des corrections de bugs et des optimisations techniques pour une meilleure expérience utilisateur. Une attention particulière a été portée à la campagne d'été et aux événements liés à la canicule.

### Évolutions fonctionnelles
- Ajout d'un lien "Canicule" dans la navigation principale pour faciliter l'accès aux missions liées à cet événement. [#348](https://github.com/betagouv/jeveuxaider-front/issues/348)
- Modification du libellé "Fermer les inscriptions" en "Mettre en pause les inscriptions" pour une meilleure clarté.
- Amélioration de la participation au tiroir pour les utilisateurs non gestionnaires. [#343](https://github.com/betagouv/jeveuxaider-front/issues/343)
- Mise à jour des options de rayon et de la logique de valeur par défaut dans le filtre de localisation. [#342](https://github.com/betagouv/jeveuxaider-front/issues/342)
- Ajout de la possibilité pour les organisations de se désabonner de manière autonome. [#322](https://github.com/betagouv/jeveuxaider-front/issues/322)
- Mise à jour des labels "rolables.fonction" pour une meilleure catégorisation. [#348](https://github.com/betagouv/jeveuxaider-front/issues/348)
- Mise à jour des informations de la mission et des composants de la section pour la campagne d'été. [#341](https://github.com/betagouv/jeveuxaider-front/issues/341)
- Suppression du filtre pour adultes dans le marché inversé, avec redirection. [#352](https://github.com/betagouv/jeveuxaider-front/issues/352)
- Ajout de Saint-Paul et Avignon aux villes multidistribuées pour une meilleure géolocalisation. [#329](https://github.com/betagouv/jeveuxaider-front/issues/329)
- Amélioration du support de la géolocalisation pour les villes multidistribuées. [#330](https://github.com/betagouv/jeveuxaider-front/issues/330)
- Ajout d'options de filtrage pour les notes autres que les mines. [#328](https://github.com/betagouv/jeveuxaider-front/issues/328)

### Évolutions techniques
- Mise à jour de l'API PlausibleStatistics pour utiliser la version 2 et correction d'un filtre de date personnalisé défectueux. [#344](https://github.com/betagouv/jeveuxaider-front/issues/344)
- Refactorisation de la logique des `queryParams` dans les statistiques pour supprimer les props inutilisés et simplifier le code. [#339](https://github.com/betagouv/jeveuxaider-front/issues/339)
- Mise à jour des attributs `aria` dans le composant `FormControl` pour une meilleure accessibilité. [#349](https://github.com/betagouv/jeveuxaider-front/issues/349)
- Optimisation de l'inclusion des dépendances dans `nuxt.config` pour éviter les messages de rechargement en développement. [#336](https://github.com/betagouv/jeveuxaider-front/issues/336)
- Suppression du composable `useAutocompleteSuggestions`. [#340](https://github.com/betagouv/jeveuxaider-front/issues/340)
- Implémentation de formulaires pour les ressources, les réseaux et les modèles de messages avec validation, gestion des soumissions et vérification des rôles utilisateurs. [#345](https://github.com/betagouv/jeveuxaider-front/issues/345), [#347](https://github.com/betagouv/jeveuxaider-front/issues/347)
- Ajout de paramètres de redirection pour la gestion dynamique des requêtes dans les composants de quiz. [#346](https://github.com/betagouv/jeveuxaider-front/issues/346)

### Autres changements
- Correction de la validation de la date de naissance pour éviter les erreurs. [#350](https://github.com/betagouv/jeveuxaider-front/issues/350)
- Correction de l'affichage du nom au lieu de la clé dans les statistiques des visites de boîtes. [#337](https://github.com/betagouv/jeveuxaider-front/issues/337)
- Correction de l'ajout des dépendances `chartjs-plugin-annotation` et `chartjs-plugin-datalabels` pour `optimizeDeps`. [#338](https://github.com/betagouv/jeveuxaider-front/issues/338)
- Mise à jour des dates des événements canicule de juin à août.
- Mise à jour de la version de l'impact de la mesure de 2023 à 2025.
- Correction de l'affichage du nom au lieu de la clé dans les statistiques des visites de boîtes.
