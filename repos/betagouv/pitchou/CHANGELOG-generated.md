## Changelog : pitchou (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à Pitchou au cours des 30 derniers jours. Les principales évolutions concernent l'intégration et l'amélioration des données AARRI, des corrections de bugs et des améliorations de l'interface utilisateur, notamment pour la gestion des pièces jointes et des avis d'expert. Des efforts ont également été faits pour améliorer la documentation et la synchronisation avec Démarche Numérique.

### Évolutions fonctionnelles
- Correction d'un bug affichant une date de saisine incorrecte dans la modale de la pièce jointe (#517).
- Suppression du bouton "Ajouter une pièce jointe" dans l'onglet instruction (#510).
- Ajout du champ texte "Numéro onagre" dans l'onglet Instruction (#500).
- Possibilité de modifier les avis d’expert dans l’onglet Avis (#431).
- Affichage des acquis AARRI sur la page AARRI (#487).
- Affichage de "Retenu" dans le contexte AARRI (#494).
- Correction d'un message erroné "dossier bien mis à jour" (#490).
- Amélioration de l'affichage CSS des pages "Mes dossiers" et "Tous les dossiers" (#504).
- Rajout des fichiers de Démarche Numérique manquants (#503).
- Correction de la page des statistiques (#507).

### Évolutions techniques
- Remplacement de "nouveau" par "expérimental" dans l'interface (#512).
- Suppression des données d'événements inutiles (#506).
- Ajustement des événements AARRI pour une meilleure précision (#505).
- Amélioration de la synchronisation avec Démarche Numérique (#497).
- Correction de la présence des champs `presence_especes_dans_aire_influence` et `risque_malgre_mesures_erc` (#495).
- Intégration de l'API GeoMCE (#484).
- Ajout d'événements de contrôle et de consultation des dossiers (#474, #486).
- Calcul de l'indicateur acquis à partir des événements (#479).
- Envoi d'un événement `seConnecter` à chaque connexion utilisateur (#482).
- Arrêt de la synchronisation des avis expert avec les annotations privées de Démarche Numérique (#499).
- Ajout de documentation pour ajouter une espèce manquante (#498).

### Autres changements
- Ajout d'un outil interne pour extraire les données AARRI (#509).
- Mise à jour de la documentation `phases-instructions.md` (plusieurs commits).
- Fin de la correspondance des colonnes du tableau de suivi pour l'import Corse (#477).
- Suppression des adresses en beta.gouv.fr des métriques AARRI (#491).
- Préparation de tests e2e (#501).
- Ajout de documentation pour l'ajout d'espèces manquantes (#498).
- Correction d'un bug de commentaire dans "Mes dossiers" (#489).
- Revert d'une requête pour récupérer les actifs (#517).
