## Changelog : anssi-recommandations-cyber (30 derniers jours, au 21 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment l'affichage des sources, la gestion des avis utilisateurs et la correction de bugs liés à la navigation et à l'affichage des résultats. Des améliorations de sécurité ont également été apportées avec la mise à jour de plusieurs dépendances. Enfin, un nouveau système de reclassement des réponses basé sur un LLM a été intégré.

### Évolutions fonctionnelles
- Amélioration de l'affichage des sources : affichage sur toute la largeur de la page, carrousel pour les pages PDF, et génération d'images des pages PDF côté navigateur.
- Nouveau formulaire d'avis utilisateur : permet de soumettre des avis sur la complétude et l'exactitude des réponses, avec validation des saisies.
- Intégration d'un reclassement des réponses par LLM pour améliorer la pertinence des résultats.
- Correction du défilement : amélioration du défilement vers la question posée par l'utilisateur et navigation horizontale des sources.
- Harmonisation du nombre de résultats retournés par la recherche.
- Ajout d'une documentation sur les interactions entre MQC et Albert.
- Affichage du contenu des paragraphes.

### Évolutions techniques
- Ajout de l'outil `zizmor` pour valider la configuration de sécurité.
- Désactivation des identifiants `git` dans les workflows CI/CD pour renforcer la sécurité.
- Refactorisation du code et suppression d'éléments inutiles dans plusieurs composants.
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et améliorer la stabilité (dompurify, svelte, vite, starlette, cryptography).
- Injection du reclasseur dans le service Albert.
- Modification de l'API pour prendre en compte le nouveau modèle de pertinence et les sources adaptées.
- Utilisation du store `storeAvisUtilisateurBis` pour gérer le formulaire d'avis utilisateur.

### Autres changements
- Suppression du feature flag `reclassement`.
- Suppression de champs obsolètes.
- Ajout de raisons pour lesquelles les sources ne sont pas adaptées, affichées dans les journaux et dans l'interface utilisateur.
- Reformattage du code pour améliorer la lisibilité.
- Ajout de tests et suppression de tests inutiles.
- Mise à jour de la documentation.
- Correction de bugs mineurs liés à l'affichage et au comportement de l'interface utilisateur.
- Ajout de logs pour faciliter le débogage.
