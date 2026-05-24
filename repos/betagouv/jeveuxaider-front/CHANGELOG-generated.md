## Changelog : jeveuxaider-front (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration des formulaires d'administration pour les ressources et les réseaux, ainsi que sur l'optimisation de la recherche de lieux et des statistiques. Des corrections ont également été apportées pour améliorer l'expérience utilisateur et la stabilité de la plateforme. L'autonomie de désinscription des organisations a été implémentée.

### Évolutions fonctionnelles
- **Formulaires d'administration :** Implémentation de nouveaux formulaires pour la gestion des ressources et des réseaux, incluant la validation, le téléchargement de médias et la gestion des rôles [#343].
- **Filtre de localisation :** Mise à jour des options de rayon de recherche avec des valeurs par défaut plus pertinentes et l'ajout de 0 et 1000km comme options [#342].
- **Statistiques :** Amélioration de l'affichage des statistiques de visites, affichant désormais le nom plutôt que la clé [#337]. Simplification de la logique des paramètres de requête [#339].
- **Notes :** Ajout d'options de filtrage pour les notes, permettant de distinguer les notes relatives aux "mines" des autres [#328].
- **Désinscription des organisations :** Les organisations peuvent désormais se désinscrire de manière autonome [#322].
- **Pagination :** Ajout d'une pagination simple pour l'index du journal d'activité [#323].
- **Géolocalisation :** Amélioration du support de la géolocalisation pour les villes multidistribuées, avec l'ajout de Saint-Paul et Avignon [#329, #330].
- **Export :** Ajout de champs supplémentaires dans les exports de données [#327].

### Évolutions techniques
- **Optimisation des dépendances :** Optimisation de l'inclusion des dépendances dans `nuxt.config` pour éviter les rechargements en développement [#336].
- **Suppression de code obsolète :** Suppression du composable `useAutocompleteSuggestions` [#340].
- **Mises à jour de librairies :** Mises à jour de plusieurs dépendances, notamment `nitropack`, `axios`, `fast-uri`, `simple-git`, `fast-xml-builder`, `uuid` et `postcss`.
- **Correction de dépendances :** Ajout des dépendances manquantes `chartjs-plugin-annotation` et `chartjs-plugin-datalabels` [#338].

### Autres changements
- Correction d'un bug empêchant l'affichage correct des noms dans les statistiques de visites [#337].
- Suppression de props inutilisés dans le composant de statistiques [#339].
