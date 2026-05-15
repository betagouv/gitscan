## Changelog : projects (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de gestion des tableaux de bord, notamment l'exportation des données, la duplication de tableaux et la gestion des droits d'accès. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les données des tableaux de bord au format CSV.
- Amélioration de l'interface utilisateur des actions sur les tableaux de bord pour une meilleure harmonisation.
- Les filtres appliqués sont désormais inclus dans l'URL, permettant de les partager et de les conserver.
- Lors de la duplication d'une carte, le tableau de bord s'ouvre directement sur la nouvelle carte.
- Correction d'un bug empêchant l'ouverture des cartes avec la combinaison de touches Cmd+Enter sur Mac.
- Amélioration de l'affichage des activités.
- Les notifications ne sont plus automatiquement marquées comme lues lors d'un clic.
- Ajout d'une API pour les statistiques (#67).

### Évolutions techniques
- Correction d'un problème d'extraction des données lors de la duplication de tableaux de bord.
- Correction d'un problème d'ID de projet cible lors de la duplication de modèles de tableaux de bord.
- Correction de la création de tableaux de bord à partir de modèles.
- Correction d'un bug empêchant la mise à jour des tableaux de bord.
- Correction d'un bug empêchant l'affichage correct des couleurs de fond des échéances.
- Correction d'un bug empêchant l'ajout de plusieurs utilisateurs dans la modale de partage.

### Autres changements
- Correction d'un bug qui affichait le sélecteur de projet dans le mode organisation.
- Correction des droits d'accès dans l'organisation (#68).
- Correction d'un problème d'affichage des noms de tableaux de bord trop longs.
- Mise en place d'un environnement de staging (#69).
