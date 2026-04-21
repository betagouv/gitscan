## Changelog : mon-entreprise (30 derniers jours, au 19 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur une refonte majeure du modèle de calcul pour les travailleurs indépendants (régime TI), avec l'intégration des dernières mises à jour réglementaires et une amélioration significative de la précision des simulations. De nombreuses corrections et optimisations ont été apportées, notamment concernant les cotisations, les exonérations et les cas particuliers. Des améliorations de l'expérience utilisateur ont également été réalisées, avec notamment la suppression du simulateur RGCP obsolète et des ajustements de l'interface.

### Évolutions fonctionnelles
- Suppression du simulateur RGCP, désormais obsolète.
- Ajout de la prise en charge des dividendes dans les simulations pour les travailleurs indépendants.
- Amélioration du calcul des cotisations et de l'assiette sociale pour les travailleurs indépendants, incluant la prise en compte de la pension invalidité et des exonérations.
- Ajout de la prise en compte du PASS mahorais pour les DROM.
- Correction de l'affichage des informations de l'entreprise sélectionnée.
- Ajout de liens vers des services utiles (ex: service employeur).
- Amélioration de la navigation entre les différents simulateurs indépendants.
- Correction de l'affichage des informations et du fonctionnement des simulateurs en iframe.
- Mise à jour des plafonds de CA pour les simulations.
- Ajout d'un bandeau rouge d'alerte en cas de règles obsolètes détectées.
- Ajout d'un bandeau d'information pour les simulations en cours de chargement.

### Évolutions techniques
- Refonte du modèle de calcul pour les travailleurs indépendants (régime TI) avec intégration de nouvelles règles et améliorations de la précision.
- Refactorisation importante du code, notamment concernant la gestion des règles, des questions, des sélecteurs et des actions du store.
- Séparation du code en paquets plus modulaires (modele-ti, modele-as, règles communes).
- Amélioration de la performance de `useEngine`.
- Mise à jour des versions de Node.js et des actions CI/CD.
- Correction de bugs liés à la gestion des expressions Publicodes et à la restauration de l'état de la simulation.
- Amélioration des tests unitaires et des snapshots.
- Utilisation d'un modèle de règles par simulateur.

### Autres changements
- Mise à jour de la documentation et des traductions.
- Correction de typos et amélioration de la lisibilité du code.
- Suppression de code commenté et de dépendances inutilisées.
- Amélioration de la documentation interne et des commentaires.
- Mise à jour des références aux réglementations et aux taux de cotisation.
- Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
- Amélioration de la gestion des erreurs et des messages d'alerte.
- Correction de problèmes de style et d'alignement de l'interface utilisateur.
