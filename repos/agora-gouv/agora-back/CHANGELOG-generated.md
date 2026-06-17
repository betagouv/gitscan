## Changelog : agora-back (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des thèmes hebdomadaires (thèmes "hebdo") et l'intégration avec Strapi V5. Des corrections et améliorations ont également été apportées à l'affichage des réponses QAG, à l'anonymisation des utilisateurs et à la gestion des données gouvernementales.

### Évolutions fonctionnelles
- Ajout d'une nouvelle route API publique pour consulter les thèmes de la semaine : `/theme_hebdo`
- Amélioration de l'affichage des réponses QAG en supprimant les balises HTML et en tronquant le texte.
- Correction de l'heure affichée pour la sélection des questions.
- Affichage du texte court extrait de la transcription vidéo si une réponse est au format vidéo.
- Ajout de deux nouveaux champs pour la page de détails QAG gouvernement.
- Amélioration de la gestion de la période optionnelle pour les thèmes hebdomadaires côté Strapi.
- Correction du champ "programme_du_mois" pour qu'il accepte le format rich text.
- Amélioration de l'affichage du sous-titre dynamique en fonction du type de thème (libre ou non).
- Ajout d'un indicateur booléen `estThemeLibre` pour mieux qualifier les thèmes libres.
- Correction de la sélection pour l'anonymisation des noms d'utilisateur.

### Évolutions techniques
- Migration vers Strapi V5 (en cours, avec des migrations passées en production).
- Ajout d'un header de compatibilité au client Strapi pour assurer la compatibilité avec les clients V4.
- Mise en place d'un plan de migration vers la version 5 de Strapi.
- Ajout d'un contrôleur dédié pour le traitement hebdomadaire, permettant un lancement en mode admin.
- Ajout d'un cache court pour les thèmes hebdomadaires.
- Modification du format de la photo en "media" pour les thèmes hebdomadaires.
- Ajout d'un flag pour désactiver le cache sur les thèmes hebdomadaires en environnement de recette.
- Log du remapping des fiches inventaires.
- Amélioration du filtrage des thèmes hebdomadaires pour afficher les 3 prochains.
- Correction de l'utilisation de la date de début du thème courant pour filtrer les thèmes hebdomadaires suivants.

### Autres changements
- Changements de wording divers.
- Désactivation de l'anonymisation lors de l'archivage.
- Ajout de données de test pour la tuile thème.
- Mise en majuscule de la période des thèmes hebdomadaires.
- Correction de l'introduction de la dernière question dans la requête des tendances.
- Ajout d'espaces à la place des balises `<p>`.
