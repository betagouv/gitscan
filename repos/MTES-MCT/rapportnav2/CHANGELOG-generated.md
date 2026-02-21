## Changelog : rapportnav2 (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions de rapportnav2 se concentrent sur l'amélioration de la sécurité, la correction de bugs et l'ajout de nouvelles fonctionnalités, notamment concernant la gestion des cibles, des informations générales et des rapports de mission. Des améliorations ont également été apportées à l'interface utilisateur et à l'infrastructure de construction et de déploiement.

### Évolutions fonctionnelles
- Ajout de la possibilité de trier les informations générales par ID de mission (descendant).
- Amélioration de l'affichage des coordonnées GPS.
- Ajout d'une fonctionnalité de recherche dans le panneau d'administration.
- Activation du bouton de suppression de mission en front-end.
- Ajout d'un indicateur du nombre de cibles sur le titre.
- Possibilité de ne pas utiliser les ressources lors de la création d'une mission.
- Amélioration de la gestion des ressources complétées pour les statistiques.
- Ajout d'un champ pour indiquer si une mission est complète pour les statistiques.
- Ajout de la possibilité de lier l'utilisateur actuel aux requêtes Sentry pour un meilleur suivi des erreurs.

### Évolutions techniques
- Renforcement de la sécurité en supprimant les données sensibles des logs et en protégeant contre les attaques par traversée de chemin lors de la compression de fichiers.
- Mise à jour des dépendances : `aquasecurity/trivy-action`, `lodash-es`.
- Amélioration de la gestion des erreurs avec l'implémentation des réponses RFC 7807 Problem Detail.
- Refactorisation du code pour améliorer la gestion des erreurs et les tests sur plusieurs entités (Agent, Vessel, Natinf, ControlUnitResources, Crew, General Infos).
- Amélioration de la configuration de Sentry avec l'ajout d'un fichier de configuration et l'initialisation des sessions.
- Corrections de build et de dépendances frontend.
- Amélioration du processus de construction et de déploiement avec des corrections de CI/CD.
- Mise à jour des dépendances frontend.
- Correction de problèmes liés à la validation des mots de passe.

### Autres changements
- Ajout de tests pour MonitorEnv et pour les cas d'utilisation d'authentification.
- Nettoyage du code et refactorisation de certaines parties du frontend.
- Documentation mise à jour sur la gestion des erreurs.
- Corrections de tests unitaires.
- Corrections de problèmes liés à l'affichage des établissements avec un nom nul.
- Suppression de code obsolète.
- Corrections de problèmes liés à l'audit npm.
- Corrections de problèmes liés à l'utilisation de la librairie Axios.
