## Changelog : fondation (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à la fondation au cours des 30 derniers jours. Les principales évolutions concernent l'affectation des dossiers, la gestion des fichiers, l'interface utilisateur et la correction de bugs. Des améliorations ont également été apportées à l'infrastructure et aux tests.

### Évolutions fonctionnelles
- Amélioration de l'affectation automatique des dossiers :
    - Correction du calcul de l'arrondi des affectations (#226).
    - Correction de la distribution arithmétique des affectations (#225).
    - Gestion de l'affectation unique par membre et par groupe de grade (#223).
    - Possibilité de publier une version sans affectations (#164).
- Gestion des fichiers :
    - Ajout de l'historique des fichiers avec commentaires (#194).
    - Ajout de la description des observations (#193, #219).
    - Suppression des fichiers de la modale d'observation (#172).
    - Possibilité de modifier les priorités des fichiers (#171).
    - Affichage du nombre de fichiers par statut (#68).
- Interface utilisateur :
    - Ajout d'indicateurs pour les commentaires des rapporteurs sur les observations (#198).
    - Affichage de la position actuelle (#218).
    - Affichage de la version dans le pied de page (#197).
    - Amélioration de l'affichage des badges (#187).
    - Ajout de badges dynamiques pour le calcul de l'état du tableau (#163).
    - Ajout d'un indicateur pour les suivis d'observation (#160).
    - Amélioration de la modale magistrat (#192).
    - Ajout d'un indicateur pour les positions nécessitant 2 rapporteurs (#168).
- Corrections de bugs :
    - Correction d'un bug lié au calcul de l'âge dans la carte récapitulative (#180).
    - Correction d'un bug lié à la redirection Lolfi (#155).
    - Correction de l'affichage des alertes pour les positions nécessitant un rapport (#192).
    - Correction de l'affichage des alertes pour les rapporteurs "premier président de chambre" (#168).
    - Correction de la récupération de la charge de travail sur les versions non publiées (#222).
    - Correction de l'utilisation de la fonction de connexion asynchrone (#221).
    - Correction de la recherche d'ID externe indépendamment du nom (#220).
    - Correction de l'affichage des alertes sur la position cible uniquement en back-office (#195).
    - Correction de l'affichage des alertes pour les membres sur les rapporteurs (#200).

### Évolutions techniques
- Ajout de tests full-stack de base (#187).
- Ajout de modules HTTP (#205).
- Suppression de Lodash (#202).
- Suppression des fichiers en dehors du scope de la requête (#200).
- Ajout de l'intégration Sentry pour la gestion des erreurs (#159).
- Ajout de l'authentification basique (#156).
- Ajout d'un hook SG (#157).
- Mise à jour de React Router (#183).
- Promotion de `dotenvx` vers les dépendances (#170).
- Ajout de dépendabot pour la gestion des dépendances (#203).
- Amélioration des permissions des jobs CI pour la production (#186, #184).
- Suppression des tests lors de la publication (#191).
- Ajout de validations PR (#207).

### Autres changements
- Ajout de tags aux utilisateurs sur la notification de changelog (#227).
- Ajout de la cible de grade dans la sortie Excel (#224).
- Mise en place d'une release sur staging après le tagging (#201).
- Amélioration des alertes (#224).
- Suppression des tests de la release (#191).
- Correction de typos (#183).
- Amélioration de l'affichage des badges (#187).
- Ajout de la CC Avocat PARIS (#200).
- Déplacement des rapporteurs dans l'Excel (#200).
- Masquage des LODAM observers (#200).
- Modification du message de succès lors de la publication d'une session (#200).
- Ajout d'étoiles rouges dans le formulaire d'import de session (#200).
- Ajout de commentaires pour les observations (#152).
- Suppression des tests de la release (#191).
- Ajout de la fonction de mise à jour du suivi à partir de la modale de résultat (#161).
- Correction de l'export Excel dans le domaine de l'API (#165).
- Amélioration de la modale d'observation (#192).
- Ajout de l'acronyme du poste pour les magistrats (#172).
- Suppression des tests de la release (#191).
