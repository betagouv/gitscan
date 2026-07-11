## Changelog : anssi-recommandations-cyber (30 derniers jours, au 09 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment l'affichage des sources, la gestion des PDF et l'ajout d'un nouveau formulaire pour recueillir les avis des utilisateurs. Des corrections de bugs ont également été apportées pour améliorer la navigation et la génération de PDF. Des mises à jour de sécurité ont été intégrées pour certaines dépendances.

### Évolutions fonctionnelles
- Amélioration de l'affichage des sources : les sources sont maintenant affichées sur toute la largeur de la page.
- Gestion des PDF :
  - Affichage des pages PDF dans un carrousel.
  - Génération de l'image de la page PDF directement dans le navigateur.
  - Affichage d'une image générique si le document téléchargé n'est pas un PDF.
  - La génération des pages PDF continue même en cas d'erreur.
- Nouveau formulaire d'avis utilisateur :
  - Initialisation et implémentation du formulaire pour recueillir les avis des utilisateurs.
  - Validation de la longueur des commentaires, de l'exactitude et de la complétude des avis.
  - Possibilité de compléter les avis utilisateurs.
  - Affichage des retours utilisateurs.
- Correction : Le bouton "suivant" est activé lorsque les sources sont chargées [#issue à ajouter si applicable].
- Correction : Défilement automatique vers la dernière question posée par l'utilisateur [#issue à ajouter si applicable].
- Correction : Défilement horizontal des sources cible via les boutons "suivant" et "précédent" [#issue à ajouter si applicable].

### Évolutions techniques
- Modification de l'API pour prendre en compte un nouveau modèle basé sur la pertinence et les sources adaptées.
- Refactorisation des routes relatives aux avis utilisateurs.
- Utilisation du store `storeAvisUtilisateurBis` pour gérer le formulaire d'avis utilisateur.
- Mise en place d'un feature flag pour activer le nouveau formulaire d'avis utilisateur.
- Validation de la longueur des saisies utilisateur.
- Renommage de fichiers et de constantes pour une meilleure clarté du code.

### Autres changements
- Ajout de documentation sur les interactions entre MQC et Albert.
- Ajout des raisons pour lesquelles les sources ne sont pas adaptées dans les journaux.
- Ajout de la mention "Tous les champs sont obligatoires" dans le formulaire.
- Mise à jour de la classe des boutons du bandeau utilisateur en `primary`.
- Suppression d'un `console.log` dans l'adaptateur PDF du front-end.
- Épinglage des versions des dépendances des GitHub Actions pour plus de stabilité.
- Mises à jour de sécurité pour les dépendances : `dompurify`, `svelte`, `vite`, `starlette` et `cryptography`.
