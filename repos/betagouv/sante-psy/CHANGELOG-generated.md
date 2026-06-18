## Changelog : sante-psy (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des rendez-vous et des informations des professionnels de santé. Des limitations ont été ajoutées au nombre de rendez-vous, et des restrictions ont été mises en place pour empêcher la suppression de rendez-vous trop anciens. L'application a également été améliorée avec l'ajout du numéro RPPS pour les psychologues et une liste complète des universités françaises.

### Évolutions fonctionnelles
- **Rendez-vous :** Limitation du nombre de rendez-vous à 12 par étudiant [#850].
- **Rendez-vous :** Lors de l'ajout d'un nouveau rendez-vous, l'utilisateur reste sur la même page et la liste des rendez-vous est automatiquement mise à jour.
- **Rendez-vous :** Lors de la suppression d'un rendez-vous, le compteur de rendez-vous de l'étudiant est mis à jour, ce qui peut déclencher une alerte si le nombre de rendez-vous est trop élevé.
- **Rendez-vous :**  Les boutons de suppression des rendez-vous anciens sont désactivés au lieu d'être cachés [#845]. Un infobulle explicative est ajoutée pour indiquer pourquoi la suppression n'est pas possible.
- **Psychologues :** Ajout du champ RPPS (numéro d'identification des professionnels de santé) aux informations des psychologues [#849].
- **Universités :** Ajout d'une liste complète des universités françaises [#845].
- **Connexion :** Correction d'un problème empêchant l'invalidation du token de connexion [#840].
- **Informations Psychologue:** Renommage du champ ADELI en ADELI/RPPS dans la section d'informations du psychologue [#9d96541].

### Évolutions techniques
- **Node.js :** Mise à jour de Node.js [#855].
- **Axios :** Mise à jour de la librairie Axios en version 1.16.0 [#843].
- **Eslint :** Configuration de ESLint pour autoriser les exports uniques [#46602f2].
- **Composant Tooltip :** Création d'un composant Tooltip réutilisable pour afficher des informations contextuelles [#b1cb60a].

### Autres changements
- **Refactoring :** Rétractation d'une modification concernant la création d'un nouvel étudiant [#847].
- **Interface utilisateur :** Amélioration de la largeur minimale de la colonne "badge" dans la vue des rendez-vous [#94301c0].
