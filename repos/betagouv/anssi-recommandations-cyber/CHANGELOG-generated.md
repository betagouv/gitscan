## Changelog : anssi-recommandations-cyber (30 derniers jours, au 23 juillet 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives de l'expérience utilisateur, notamment dans l'affichage des sources et des réponses, ainsi que l'ajout d'un système de feedback utilisateur. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance. La sécurité a été renforcée avec des mises à jour de dépendances.

### Évolutions fonctionnelles
- Ajout d'un bouton pour copier les sources de la réponse.
- Amélioration de l'affichage des réponses détaillées pour une meilleure lisibilité.
- Affichage du titre du document au lieu du nom du fichier.
- Ajout de la date de mise à jour du document.
- Possibilité de soumettre un avis utilisateur sur la qualité des réponses (exactitude et complétude).
- Affichage des sources dans un carrousel avec des boutons de navigation.
- Génération d'images des pages PDF pour les sources.
- Correction du comportement de défilement lors de l'utilisation de la recherche.
- Amélioration de la gestion des erreurs lors de la génération de pages PDF.
- Ajout d'une image générique pour les documents non-PDF.
- Affichage du contenu des paragraphes.

### Évolutions techniques
- Intégration de `zizmor` pour la validation de la configuration et renforcement de la sécurité.
- Désactivation des identifiants `git` dans les workflows CI/CD pour améliorer la sécurité.
- Refactorisation du code pour séparer la logique de réponse de l'API du traitement métier.
- Ajout du reclassement par LLM et injection du reclasseur dans le service Albert.
- Suppression des champs obsolètes.
- Amélioration de la gestion des erreurs lors de l'appel au reclassement.
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et bénéficier des dernières améliorations (dompurify, svelte, vite, starlette, cryptography).
- Utilisation du store `storeAvisUtilisateurBis` pour gérer le formulaire d'avis utilisateur.

### Autres changements
- Ajout d'icônes DSFR aux boutons du carrousel.
- Passage du bouton de copie en style tertiaire.
- Sécurisation du vocabulaire utilisé dans le prompt pour une portée juridique précise.
- Ajout de wording spécifique pour les tests internes de l'ANSSI.
- Nettoyage du code et des tests.
- Mise à jour de la documentation sur les interactions entre MQC et Albert.
- Correction de liens et de redirections.
- Amélioration de la gestion des logs.
- Modification du message d'accueil et de retour.
- Renforcement du prompt pour améliorer la citation des recommandations.
- Tri des sources du reclasseur LLM.
- Canonisation des questions reformulées.
- Suppression d'un feature flag obsolète.
