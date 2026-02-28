## Changelog : pitchou (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à Pitchou au cours du dernier mois. Les principales évolutions concernent l'intégration et l'amélioration des données AARRI, des corrections de bugs pour une meilleure gestion des pièces jointes et des informations de dossier, ainsi que des ajustements de l'interface utilisateur pour une expérience plus fluide. Des améliorations de la documentation et de la synchronisation avec Démarche Numérique ont également été réalisées.

### Évolutions fonctionnelles
- Correction d'un bug concernant la date de saisine dans la modale de la pièce jointe (#517).
- Ajout du champ texte "Numéro Onagre" dans l'onglet Instruction (#500).
- Les fichiers manquants de Démarche Numérique sont maintenant correctement intégrés dans Pitchou (#503).
- Affichage de l'état "Retenu" pour les dossiers AARRI (#494).
- Correction d'un message d'erreur trompeur "dossier bien mis à jour" (#490).
- Correction de la présence des espèces dans l'aire d'influence et du risque malgré les mesures ERC (#495).
- Amélioration de l'affichage CSS des pages "Mes dossiers" et "Tous les dossiers" (#504).
- Suppression du bouton "Ajouter une pièce jointe" dans l'onglet Instruction (#510).
- Correction des noms de fichiers de pièces jointes contenant des caractères Unicode (#520).
- Remplacement de "nouveau" par "expérimental" dans l'interface (#512).

### Évolutions techniques
- Outil interne développé pour extraire les données AARRI (#509).
- Amélioration de la synchronisation avec Démarche Numérique (#497).
- Suppression des données d'événements inutiles (#506).
- Ajout d'événements de contrôle pour le suivi AARRI (#486).
- Ajout d'événements de consultation des dossiers (#474).
- Préparation de tests e2e pour améliorer la qualité du code (#501).
- Correction de la page des statistiques (#507).
- Arrêt de la synchronisation des avis d'expert avec les annotations privées de Démarche Numérique (#499).
- Amélioration de la gestion des mesures d'impact AARRI (#493).
- Suppression des adresses beta.gouv.fr des métriques AARRI (#491).
- Ajustement des événements AARRI (#505).

### Autres changements
- Ajout de documentation pour ajouter une espèce manquante (#498).
- Ajout de documentation expliquant les différences entre Démarche Numérique et Pitchou (#508).
- Fin de la correspondance des colonnes du tableau de suivi pour l'import Corse (#477).
- Mises à jour de la documentation `phases-instructions.md` (plusieurs commits).
