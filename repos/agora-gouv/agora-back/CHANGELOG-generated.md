## Changelog : agora-back (30 derniers jours, au 10 juillet 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de la gestion du cache, de l'algorithme de tendances, et de l'intégration avec Strapi (migration vers la version 5). Des outils d'administration ont été ajoutés pour faciliter la gestion du contenu et le débogage. L'automatisation du renouvellement des certificats SSL a également été implémentée.

### Évolutions fonctionnelles
- Ajout d'une route pour vider le cache REDIS via l'interface Swagger.
- Possibilité de suspendre le trafic vers Strapi pour investigation en production.
- Ajout d'une route d'administration pour changer le statut d'une question.
- Amélioration de l'algorithme de calcul des tendances avec une nouvelle formule (V3 et V4).
- Introduction d'une nouvelle logique pour l'onglet "Tendances" basée sur le nombre de "likes" reçus dans les dernières 24 heures.
- Ajout de la fonction de l'auteur dans les previews de réponses.
- Ajout d'un motif de refus pour la modération, permettant un meilleur suivi et une potentielle utilisation future.
- Intégration de la transcription vidéo pour afficher un texte court dans les réponses au format vidéo.
- Suppression des balises HTML et troncature du texte des réponses dans l'API `qags/reponses/pagenumber`.
- Ajout de clusters de mots pour la semaine libre (gestion via CMS).
- Automatisation du renouvellement des certificats SSL via ACME [#670](https://github.com/agora-gouv/agora-back/issues/670).
- Passage de l'heure de sélection des questions gagnantes à 10h.

### Évolutions techniques
- Passage de la méthode PATCH à POST pour le push du certificat sur Cloudflare.
- Migration de Strapi vers la version 5 et correction des migrations associées.
- Script de rollback fourni pour les migrations Strapi V5 des IDs de questions et de choix.
- Amélioration de la gestion du cache : flush du cache de cluster de mots lors du vidage de cache global, ajout de qualificateurs de cache pour les thèmes hebdomadaires.
- Correction de bugs et améliorations diverses dans l'algorithme de tendances.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Ajout de logs pour le remapping des fiches inventaires.
- Correction de wording pour l'heure de sélection des questions (14h -> 10h).
- Ajout de valeurs par défaut plus spécifiques pour la domaine libre.
- Correction de petites erreurs typographiques et de formatage.
- Ajout de valeurs par défaut plus spécifiques pour la domaine libre.
