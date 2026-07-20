## Changelog : agora-back (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des consultations ACME, l'optimisation de la sélection des questions et des tendances, ainsi que l'ajout de fonctionnalités d'administration pour une meilleure gestion du contenu et du cache. Plusieurs corrections et ajustements ont également été apportés pour améliorer la stabilité et la flexibilité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'une route d'administration pour modifier le statut d'une question. [#670](https://github.com/agora-gouv/agora-back/issues/670)
- Implémentation de l'automatisation Sectigo via ACME pour la gestion des certificats. [#670](https://github.com/agora-gouv/agora-back/issues/670)
- Ajout de la possibilité de filtrer les réponses par date minimale via l'API.
- Amélioration de l'affichage des previews de réponses avec la fonction de l'auteur.
- Ajout d'un flag pour suspendre le trafic vers Strapi en cas de problèmes de production.
- Possibilité de forcer le déclenchement de la sélection des questions via l'API.
- Modification du déclencheur temporel de sélection de la question gagnante, passage sur les thèmes hebdomadaires.
- Ajout d'un motif de refus pour la modération des contributions, pour une meilleure traçabilité.
- Ajout de clusters de mots pour la semaine libre (ex: 'tesla').
- Augmentation de la longueur maximale de la synthèse des réponses à 400 caractères.
- Ajout d'un mécanisme pour bloquer le partage de sa propre réponse dans les previews.

### Évolutions techniques
- Simplification du flush du cache Redis en utilisant `flushdb` pour garantir la suppression de toutes les données.
- Ajout du flush du cache de cluster de mots à la routine de vidage de cache.
- Passage de l'utilisation de `PATCH` à `POST` pour le push du certificat sur Cloudflare.
- Passage de l'URL de modification des statuts en mode query param pour une utilisation plus simple avec Swagger.
- Refonte de l'algorithme de calcul des tendances (V3 et V4).
- Amélioration de la gestion des erreurs et des fallbacks dans l'extraction des informations de l'auteur des réponses.
- Correction d'une erreur dans le sous-titre des thèmes libres.

### Autres changements
- Documentation du workflow complet ACME.
- Ajout de valeurs par défaut plus spécifiques pour la domaine libre.
- Suppression de fichiers de logs inutiles.
- Correction de petites erreurs de texte et de formatage.
- Ignorer fichier de travail.
- Correction route challenge ACME.
