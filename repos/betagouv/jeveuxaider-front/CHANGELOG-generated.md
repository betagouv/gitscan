## Changelog : jeveuxaider-front (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la plateforme "Je veux aider" avec un focus sur le partage de missions, la gestion des organisations, et l'expérience utilisateur globale. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application. Une nouvelle fonctionnalité pour la gestion des événements "canicule" a été ajoutée.

### Évolutions fonctionnelles
- Amélioration du partage de missions, avec une refonte complète de l'interface [#353](https://github.com/betagouv/jeveuxaider-front/issues/353).
- Suppression du filtre "adultes" de la marketplace inversée et ajout d'une redirection. [#352](https://github.com/betagouv/jeveuxaider-front/issues/352)
- Mise à jour des dates des événements "canicule" de juin à août. [#348](https://github.com/betagouv/jeveuxaider-front/issues/348)
- Modification du texte du bouton "Fermer les inscriptions" pour "Mettre en pause les inscriptions" pour une meilleure clarté. [#349](https://github.com/betagouv/jeveuxaider-front/issues/349)
- Ajout d'un lien "Canicule" dans la navigation principale, tant sur desktop que sur mobile. [#349](https://github.com/betagouv/jeveuxaider-front/issues/349)
- Amélioration de la participation à l'organisation pour les non-managers. [#343](https://github.com/betagouv/jeveuxaider-front/issues/343)
- Possibilité pour les organisations de se désinscrire de manière autonome [#322](https://github.com/betagouv/jeveuxaider-front/issues/322).
- Ajout de paramètres UTM aux invitations pour un meilleur suivi.
- Implémentation de formulaires pour les ressources, les réseaux et les modèles de messages avec validation et gestion des rôles utilisateurs.
- Mise à jour des labels des rôles "rolables.fonction".

### Évolutions techniques
- Correction d'un problème de défilement horizontal dans le Drawer.
- Mise à jour de la librairie Axios vers la version 1.16.0.
- Correction de la validation de la date de naissance.
- Refactorisation du composant `statistics` pour supprimer les props inutilisés et simplifier la logique des queryParams.
- Optimisation de l'inclusion des dépendances dans la configuration Nuxt pour éviter les rechargements en développement.
- Mise à jour de plusieurs dépendances (qs, nitropack, fast-uri, simple-git, fast-xml-builder).
- Utilisation de `v-bind` pour les attributs aria dans `FormControl` pour éviter les erreurs liées aux attributs avec tirets.
- Mise à jour de l'API PlausibleStatistics vers la version 2 et suppression du filtre `date_range` défectueux.
- Suppression du composable `useAutocompleteSuggestions`.

### Autres changements
- Correction d'un bug concernant le rendu du nom au lieu de la clé dans `BoxVisitsStatistics`.
- Ajout des dépendances `chartjs-plugin-annotation` et `chartjs-plugin-datalabels` pour corriger un problème avec `optimizeDeps`.
- Ajout de props `redirectParams` au composant `QuizStepBenefits` pour une gestion dynamique des paramètres de requête.
- Mise à jour des composants `MissionInfos` et `Section` pour la campagne d'été.
- Mise à jour des options de rayon dans le filtre de localisation pour inclure 0 et 1000.
