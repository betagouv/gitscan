## Changelog : pitchou (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à Pitchou au cours des 30 derniers jours. Les principales évolutions concernent l'intégration et l'amélioration des données AARRI, des corrections de bugs et des améliorations de l'interface utilisateur, notamment pour la gestion des dossiers et des avis d'expert. La synchronisation avec l'API Démarche Numérique a également été affinée.

### Évolutions fonctionnelles
- Ajout du champ "Numéro Onagre" dans l'onglet Instruction des dossiers (#500).
- Rajout des fichiers de Démarche Numérique manquants dans Pitchou (#503).
- Affichage des acquis sur la page AARRI (#487).
- Affichage de "Retenu" dans les informations AARRI (#494).
- Possibilité de modifier les avis d’expert dans l’onglet Avis (#431).
- Suppression du bouton "Ajouter une pièce jointe" dans l'onglet Instruction (#510).
- Remplacement de "nouveau" par "expérimental" dans l'interface (#512).
- Correction d'un bug concernant un message erroné "dossier bien mis à jour" (#490).
- Correction d'un bug lié aux commentaires dans la liste "Mes dossiers" (#489).
- Amélioration de l'affichage des pages "Mes dossiers" et "Tous les dossiers" avec du CSS (#504).
- Ajout de documentation pour ajouter une espèce manquante (#498).

### Évolutions techniques
- Amélioration de la synchronisation avec l'API Démarche Numérique (#497).
- Correction de la page des statistiques (#507).
- Ajustement des événements AARRI (#505).
- Arrêt de la synchronisation des avis expert avec les annotations privées de Démarche Numérique (#499).
- Implémentation de l'API GeoMCE (#484).
- Ajout d'événements de consultation des dossiers (#474).
- Ajout d'événements de contrôle (#486).
- Calcul de l'indicateur "acquis" à partir des événements (#479).
- Correction de la logique pour `presence_especes_dans_aire_influence` et `risque_malgre_mesures_erc` (#495).
- Fin de la correspondance des colonnes du tableau de suivi pour l'import Corse (#477).
- Suppression des données d'événements (#506).
- Suppression des adresses en beta.gouv.fr des métriques AARRI (#491).
- Ajout de documentation pour l'ajout d'une espèce manquante (#498).
- Préparation de tests e2e (#501).

### Autres changements
- Ajout de documentation concernant les différences entre DN et Pitchou (#508).
- Mise à jour de la documentation `phases-instructions.md` (plusieurs commits).
- Envoi de l'événement `seConnecter` à chaque connexion (#482).
- Ajout de liens vers les nouvelles pages de listes de dossiers (#481).
