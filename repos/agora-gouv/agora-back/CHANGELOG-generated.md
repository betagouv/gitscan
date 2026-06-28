## Changelog : agora-back (30 derniers jours, au 26 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées au backend d'Agora au cours des 30 derniers jours. Les principales évolutions concernent l'algorithme de tendances, la gestion des thèmes libres et l'intégration avec Strapi V5, ainsi que des corrections et optimisations diverses pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Amélioration de l'algorithme de calcul des tendances, basé sur un nombre de "likes" supérieur à 5 sur les dernières 24 heures [#issue à identifier].
- Introduction d'un indicateur booléen `estThemeLibre` pour mieux identifier les thèmes libres.
- Affichage de la transcription textuelle des réponses vidéo pour faciliter l'accessibilité et la recherche.
- Modification de l'heure de sélection des questions gagnantes, désormais fixée à 10h au lieu de 14h.
- Amélioration de l'affichage des sous-titres pour les thèmes libres.
- Ajout de la fonction de l'auteur dans les réponses preview.
- Passage de la limite de caractères pour la synthèse des réponses à 400 caractères.
- Filtrage des réponses par date minimale via les APIs.

### Évolutions techniques
- Préparation et exécution de la migration vers Strapi V5, incluant des scripts de rollback et des ajustements des migrations.
- Ajout d'un header de compatibilité pour les clients Strapi V4.
- Mise en place d'un plan de migration complet vers Strapi V5.
- Optimisation du cache pour les thèmes hebdomadaires, avec une durée de cache plus courte.
- Correction de bugs liés à la date de début des thèmes courants pour le filtrage des thèmes hebdomadaires.
- Ajout de logs pour le remapping des fiches inventaires.
- Suppression des balises HTML et troncature du texte des réponses dans certaines requêtes.

### Autres changements
- Correction de coquilles et amélioration du wording dans différentes parties de l'application.
- Ajout de points de fin de phrase manquants.
- Correction de tests suite aux modifications de la date de sélection des questions gagnantes.
- Mise en majuscule de la période des thèmes hebdomadaires.
- Proposition d'intégration ACME V2.
