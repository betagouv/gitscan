## Changelog : agora-back (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des thèmes hebdomadaires, avec l'intégration de nouvelles fonctionnalités et corrections pour une meilleure expérience utilisateur. Une migration vers la version 5 de Strapi a été préparée et partiellement déployée. Des améliorations ont également été apportées à l'affichage des réponses et à la gestion des données gouvernementales.

### Évolutions fonctionnelles
- Ajout d'une nouvelle logique pour l'onglet "Tendances" : affichage des questions ayant reçu plus de 5 "likes" au cours des dernières 24 heures.
- Amélioration de l'affichage des réponses vidéo : utilisation de la transcription pour afficher un texte court.
- Ajout de deux nouveaux champs pour la page de détails QAG gouvernement.
- Mise en place d'une nouvelle tuile pour les thèmes hebdomadaires, avec filtrage des 3 prochains thèmes.
- Correction de l'affichage de la période des thèmes hebdomadaires.
- Correction de l'affichage du champ "programme du mois" en rich text.
- Amélioration du wording pour l'heure de sélection des questions (passage à 10h).
- Correction de l'anonymisation des usernames.

### Évolutions techniques
- Préparation et début de la migration vers Strapi V5, incluant des migrations de données et des ajustements de compatibilité.  Des scripts de rollback ont été mis en place pour faciliter le processus. [#27b67e5](https://github.com/agora-gouv/agora-back/issues/27b67e5)
- Ajout d'un header de compatibilité pour les clients Strapi V4.
- Mise en place d'un contrôleur dédié pour le traitement hebdomadaire, permettant un lancement en mode admin.
- Ajout de qualificateurs de cache pour les thèmes hebdomadaires afin d'optimiser les performances.
- Utilisation de la date de début du thème courant pour filtrer les thèmes hebdomadaires suivants.
- Ajout d'un flag pour désactiver le cache sur les thèmes hebdomadaires en environnement de recette.
- Modification du format de la photo des thèmes hebdomadaires pour utiliser le format "media".
- Ajout d'un boolean `estThemeLibre` pour mieux qualifier les thèmes libres.

### Autres changements
- Ajout de logs pour le remapping des fiches inventaires.
- Suppression des balises HTML et troncature du `reponseText` dans `qags/reponses/pagenumber`.
- Mise en majuscule de la "periode" du thème hebdomadaire.
- Ajout d'espaces en remplacement des balises `<p>`.
- Correction de la sélection de la date pour les tests de sélection des questions gagnantes.
- Correction de bugs liés à la sélection des questions gagnantes.
