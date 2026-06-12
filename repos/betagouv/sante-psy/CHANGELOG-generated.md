## Changelog : sante-psy (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des rendez-vous et des informations des psychologues et des universités. Des restrictions ont été ajoutées pour empêcher la suppression de rendez-vous trop anciens, et des informations importantes comme le numéro RPPS des psychologues sont maintenant enregistrées. La liste des universités a également été mise à jour.

### Évolutions fonctionnelles
- **Rendez-vous :** Limitation du nombre de rendez-vous à 12. [#850](https://github.com/betagouv/sante-psy/issues/850)
- **Rendez-vous :**  Il n'est plus possible de supprimer les rendez-vous trop anciens. Un bouton désactivé remplace le bouton de suppression. [#844](https://github.com/betagouv/sante-psy/issues/844) et [#845](https://github.com/betagouv/sante-psy/issues/845)
- **Psychologues :** Ajout du champ RPPS pour les psychologues dans la base de données. [#849](https://github.com/betagouv/sante-psy/issues/849)
- **Universités :** Ajout d'une colonne UAI pour les universités. [#846](https://github.com/betagouv/sante-psy/issues/846)
- **Universités :** Mise à jour de la liste complète des universités françaises.
- **Interface utilisateur :** Ajout d'infobulles (Tooltips) pour les boutons de suppression de rendez-vous, améliorant l'expérience utilisateur.
- **Interface utilisateur :** Renommage du champ ADELI en ADELI/RPPS dans la section d'informations du psychologue.

### Évolutions techniques
- **Refactoring :** Création d'un composant Tooltip réutilisable pour améliorer la cohérence de l'interface utilisateur.
- **Eslint :** Autorisation des exports uniques dans le code.
- **Authentification :** Correction d'un problème d'invalidation du token de connexion. [#840](https://github.com/betagouv/sante-psy/issues/840)

### Autres changements
- Suppression d'un fichier PDF obsolète concernant les psychologues. [#847](https://github.com/betagouv/sante-psy/issues/847)
